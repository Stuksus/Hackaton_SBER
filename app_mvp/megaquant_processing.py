import pandas as pd
import streamlit as st 
import numpy as np
from sklearn import preprocessing
from joblib import load

df_test  = pd.read_csv('https://raw.githubusercontent.com/BKHV/risk_models/master/data/PD-data-test.csv', sep=';')
df_train = pd.read_csv('https://raw.githubusercontent.com/BKHV/risk_models/master/data/PD-data-train.csv', sep=';')
model_pipe = load('megaq_pipeline.joblib') 
final_test = load('megaq_final_test.joblib') 
top_feat_fin = ['WoE_cut_ab_other_current_assets',
                'WoE_cut_ab_cash_and_securities',
                'WoE_cut_ab_losses',
                'WoE_cut_ab_long_term_liabilities',
                'WoE_cut_ab_short_term_borrowing',
                'WoE_cut_ogrn_age',
                'WoE_cut_cap_actual_age',
                'WoE_cut_ul_staff_range',
                'WoE_cut_ul_capital_sum',
                'WoE_cut_ul_founders_cnt',
                'WoE_cut_ul_branch_cnt',
                'WoE_cut_ul_strategic_flg','WoE_cut_OPEX',
                'WoE_cut_OER',
                'WoE_cut_frac_comer_exp']

def predict(df=df_test, model_pipe=model_pipe, top_feat_fin=top_feat_fin, df_train=df_train):
    final_test = preprocess(df,df_train=df_train)
    return (model_pipe.predict_proba(final_test.loc[:,top_feat_fin])[:,1]>0.539).astype(int)

def kill_nulls(df,df_train):
    train_df=df_train
    # 1
    df = df.drop(['record_id','ul_systematizing_flg'],axis = 1)

    # 2
    le = preprocessing.LabelEncoder()
    le.fit(train_df['ul_staff_range'])
    df['ul_staff_range'] = le.transform(df['ul_staff_range'])


    # 3
    df_cleaned = calc_fin_statistics(df.fillna(0))


    # 4
    fin_abs_features = ['ar_revenue',
                        'ar_other_profit_and_losses',
                        'ar_profit_before_tax', 
                        'ar_taxes', 
                        'ar_total_expenses', 
                        'ar_sale_cost', 
                        'ar_selling_expenses', 
                        'ar_management_expenses',
                        'ar_sale_profit', 
                        'ar_balance_of_rvns_and_expns']
    df_cleaned = df_cleaned.drop(fin_abs_features, axis = 1)


    # 5
    df_cleaned = df_cleaned.fillna(0)
    df_cleaned = df_cleaned.replace(np.inf,0)
    df_cleaned = df_cleaned.replace(-np.inf,0)


    # 6
    corr_columns_to_del_fin = ['adr_actual_age','OP_Margin','gross_profit_margin',
                               'head_actual_age','ar_net_profit','ab_borrowed_capital','ab_mobile_current_assets',
                               'bus_age','frac_post_pay','ab_accounts_payable','tax_ratio','ab_own_capital','tumover_ratio',
                               'ab_accounts_receivable','ab_immobilized_assets','ab_inventory','ab_other_borrowings']
    df_cleaned = df_cleaned.drop(corr_columns_to_del_fin,axis =1)
    return df_cleaned


def preprocess(df,df_train=df_train):
    df_cleaned, df_train_cleaned = kill_nulls(df,df_train), kill_nulls(df_train,df_train)
    df_woe = woe(df_cleaned, df_train_cleaned)
    return df_woe


def woe(df,df_frain):
    df_fin_test_feature_complex_fillna  = df       
    df_fin_train_feature_complex_fillna = df_frain 
    def calc_woe_iv(df, feature, target):
        '''
        На выход идет таблица со значениями WoE для каждого значения признака 
        и критерий информативности IV для каждого признака
        '''
        
        vals = list(df[feature].unique())
        count_all = []
        default = []
        non_default = []
        
        for i in vals:
            count_all.append(len(df[df[feature] == i]))
            default.append(len(df[(df[target] == 1) & (df[feature] == i)]))
            non_default.append(len(df[(df[target] == 0) & (df[feature] == i)]))
        
        data = {'value': vals, 'count_all': count_all, 'default': default, 'non_default': non_default}
        df_woe_iv = pd.DataFrame(data)
            
        df_woe_iv['Distr_non_default'] = df_woe_iv['non_default'] / df_woe_iv['non_default'].sum()
        df_woe_iv['Distr_default'] = df_woe_iv['default'] / df_woe_iv['default'].sum()
        name_woe = 'WoE_' + feature
        df_woe_iv[name_woe] = np.log(df_woe_iv['Distr_non_default'] / df_woe_iv['Distr_default'])
        df_woe_iv = df_woe_iv.replace({name_woe: {np.inf: 0, -np.inf: 0}})
        df_woe_iv['IV'] = (df_woe_iv['Distr_non_default'] - df_woe_iv['Distr_default']) * df_woe_iv[name_woe]
        iv = df_woe_iv['IV'].sum()
        
        return df_woe_iv, iv
    # подсчет оптимального разбиения признака на бины
    number_bins = range(1, 20)


    for feature in df_fin_train_feature_complex_fillna.columns:
        ivvv = []
        
        if feature == 'default_12m':
            continue

        name = 'cut_' + str(feature)
        for i in number_bins:
            df_fin_train_feature_complex_fillna[name] = pd.cut(df_fin_train_feature_complex_fillna[feature], i)
            ivvv.append(calc_woe_iv(df_fin_train_feature_complex_fillna, name, 'default_12m')[1])
        
        
        bin_iv = {}
        for A, B in zip(number_bins, ivvv):
            bin_iv[A] = B
        cut_bin = max(bin_iv, key=bin_iv.get)

        df_fin_train_feature_complex_fillna[name] = pd.cut(df_fin_train_feature_complex_fillna[feature], cut_bin)
        del df_fin_train_feature_complex_fillna[feature]

    # считаем IV для каждого признака
    def calc_iv_features(df, target):
        ivs = []
        feature_names = df.columns
        for i in feature_names:
            df_woe_iv = calc_woe_iv(df, i, target)[0]
            ivs.append(df_woe_iv['IV'].sum())
        
        data = {'feature_name': feature_names, 'iv': ivs}
        df_iv = pd.DataFrame(data)
        return df_iv

    res_feature_iv = calc_iv_features(df_fin_train_feature_complex_fillna, 'default_12m')
    feat_iv = list(res_feature_iv['feature_name']) + ['default_12m']
    df_fin_train_feature_complex_fillna_iv = df_fin_train_feature_complex_fillna.loc[:,feat_iv[1:]]
    train_feat_iv = (['WoE_'+label for label in feat_iv[:-1]]+['default_12m'])[1:]
    # Трансформируем тренеровочную выборку
    for feature in df_fin_train_feature_complex_fillna_iv:
        if feature == 'default_12m':
            continue
        temp = calc_woe_iv(df_fin_train_feature_complex_fillna_iv, feature, 'default_12m')[0]
        res = df_fin_train_feature_complex_fillna_iv.merge(temp, how='left', left_on=feature, right_on = 'value')
        del res['value']
        df_fin_train_feature_complex_fillna_iv = res.copy()

    df_fin_train_feature_complex_fillna_iv_fin = df_fin_train_feature_complex_fillna_iv[train_feat_iv]

    frame_for_scoring_map = df_fin_train_feature_complex_fillna_iv
    
    test_feat_iv = [column_name[4:] for column_name in feat_iv[:-1]][1:]

    # woe для тестовой выборки 
    df_fin_test_feature_complex_fillna_iv = df_fin_test_feature_complex_fillna.loc[:,test_feat_iv]

    # Трансформируем тестовую выборку
    final_test = pd.DataFrame()
    for cut_label,label in zip(feat_iv[1:],test_feat_iv):
        ab_losses_woe = calc_woe_iv(df_fin_train_feature_complex_fillna_iv, cut_label, 'default_12m')[0]
        ab_losses_arr = list(ab_losses_woe['value'])
        test_bins = pd.DataFrame(pd.cut(df_fin_test_feature_complex_fillna_iv[label], bins = pd.IntervalIndex(ab_losses_arr)))
        test_ab_losses_woe = test_bins.merge(ab_losses_woe, how='left', left_on=label, right_on = 'value')['WoE_'+cut_label]
        test_ab_losses_woe = test_bins.merge(ab_losses_woe, how='left', left_on=label, right_on = 'value')['WoE_'+cut_label]
        final_test = pd.concat([final_test,pd.DataFrame(test_ab_losses_woe)],axis =1)

    # нужно произвести заново деление по woe признакам
    X_train_fin = df_fin_train_feature_complex_fillna_iv_fin.drop('default_12m', axis = 1) 
    y_train_fin = df_fin_train_feature_complex_fillna_iv_fin['default_12m']

    # Выделим по 100 объектов каждого класса и образуем из них валидационную выборку
    index_to_del_from_train = X_train_fin.merge(y_train_fin,left_index=True,right_index=True).groupby('default_12m').apply(lambda x: x.sample(n=100,random_state = 42)).index.get_level_values(level=1)#.reset_index(drop = True)
    X_valid_fin = X_train_fin.merge(y_train_fin,left_index=True,right_index=True).groupby('default_12m').apply(lambda x: x.sample(n=100,random_state = 42)).reset_index(drop = True)
    X_valid_fin.default_12m.value_counts()
    X_train_fin = X_train_fin.drop(index_to_del_from_train.tolist(),axis = 0)
    y_train_fin = y_train_fin.drop(index_to_del_from_train.tolist(),axis = 0)
    y_valid_fin = X_valid_fin['default_12m']
    X_valid_fin = X_valid_fin.drop('default_12m',axis =1)
    return final_test

def calc_fin_statistics(df):
    frame = df.copy()

    # общие обязательства
    total_liabilities = (frame['ab_long_term_liabilities'] + 
                           frame['ab_other_borrowings'] + 
                           frame['ab_short_term_borrowing']+ 
                           frame['ab_accounts_payable'] + frame['ab_borrowed_capital'])
    
    # общие активы
    total_assets = (frame['ab_own_capital']
                    +frame['ab_cash_and_securities']
                    +frame['ab_accounts_receivable'] 
                    +frame['ab_inventory']
                    +frame['ab_immobilized_assets']
                    +frame['ab_mobile_current_assets']
                    +frame['ab_other_current_assets'])
    
    # текущие активы
    current_assets = (frame['ab_mobile_current_assets']
                      +frame['ab_other_current_assets']
                      +frame['ab_inventory']
                      +frame['ab_accounts_receivable'])
    
    # текущие обязательства
    current_liabilities = (frame['ab_accounts_payable']
                           +frame['ab_short_term_borrowing']
                           +frame['ab_other_borrowings'])
    
    # синтетические признаки
    frame['frac_post_pay']       = frame['ar_revenue']/frame['ab_accounts_receivable']
    frame['OPEX']                = frame['ar_total_expenses'] - frame['ar_selling_expenses'] - frame["ar_management_expenses"]
    frame['OER']                 = frame['OPEX']/frame['ar_revenue']
    frame['frac_comer_exp']      = frame['ar_selling_expenses' ]/ frame['ar_total_expenses']
    frame['Net_margin']          = frame['ar_net_profit']/frame['ar_revenue']
    frame['gross_profit_margin'] = (frame['ar_revenue'] - frame['ar_sale_cost'])/frame['ar_revenue']
    frame['OP_Margin']           = frame['OPEX']/frame['ar_revenue']
    frame['ROE']                 = frame['ar_net_profit']/frame['ab_own_capital']
    frame['ROA']                 = frame['ar_net_profit']/total_assets
    frame['Debt/EBIT']           = total_liabilities/frame['ar_profit_before_tax']
    frame['Debt_ratio_betters']  = total_liabilities/total_assets
    frame['tax_ratio']           = frame['ar_taxes']/frame['ar_profit_before_tax']
    frame['time_gap']            = frame['ab_accounts_payable']/(frame['ab_cash_and_securities']+frame['ab_accounts_receivable'])
    frame['borrowing_balance']   = frame['ab_accounts_receivable']/frame['ab_accounts_payable']
    frame['Debt/Equity']         = total_liabilities/frame['ab_own_capital']
    frame['current_ratio']       = current_assets/current_liabilities
    frame['cash_ratio']          = frame['ab_cash_and_securities']/frame['ab_short_term_borrowing']
    frame['fast_pay']            = (frame['ab_cash_and_securities']+frame['ab_accounts_receivable'])/total_assets
    frame['tumover_ratio']       = frame['ar_revenue']/total_assets

    return frame

import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################

import megaquant_processing as mp

###################################


#__________________________________        META        __________________________________#
def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="💰", page_title="PD Model | MegaQuant")
st.title("Привет Елизавета!")

###################################        META        ###################################
##########################################################################################
##########################################################################################
##########################################################################################


#__________________________________      SIDEBAR       __________________________________#
st.sidebar.header('Выполнить предсказание для')
uploaded_file = st.sidebar.file_uploader(
        "Перетащите csv файл сюда!",
        key="1",
        help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
    )

if uploaded_file is not None:
    file_container = st.expander("Был введен следующий csv файл")
    shows = pd.read_csv(uploaded_file, sep=';')
    uploaded_file.seek(0)
    file_container.write(shows)

else:
    st.sidebar.info(
        f"""
            👆 Попробуйте загрузить [df_test.csv](https://hse.kamran.uz/ps22/df_test.csv)
            """
    )

    def user_input_features():
        record_id                   = 0
        ar_revenue                  = st.sidebar.number_input('ar_revenue',                   value=0)
        ar_total_expenses           = st.sidebar.number_input('ar_total_expenses',            value=0)
        ar_sale_cost                = 1
        ar_selling_expenses         = st.sidebar.number_input('ar_selling_expenses',          value=0)
        ar_management_expenses      = st.sidebar.number_input('ar_management_expenses',       value=0)
        ar_sale_profit              = 1
        ar_balance_of_rvns_and_expns= 1
        ar_profit_before_tax        = 1
        ar_taxes                    = 1
        ar_other_profit_and_losses  = 1
        ar_net_profit               = 1
        ab_immobilized_assets       = 1
        ab_mobile_current_assets    = 1
        ab_inventory                = 1
        ab_accounts_receivable      = 1
        ab_other_current_assets     = st.sidebar.number_input('ab_other_current_assets', value=0)
        ab_cash_and_securities      = st.sidebar.number_input('ab_cash_and_securities', value=0)
        ab_losses                   = st.sidebar.number_input('ab_losses', value=0)
        ab_own_capital              = 1
        ab_borrowed_capital         = 1
        ab_long_term_liabilities    = st.sidebar.number_input('ab_long_term_liabilities', value=0)
        ab_short_term_borrowing     = st.sidebar.number_input('ab_short_term_borrowing', value=0)
        ab_accounts_payable         = 1
        ab_other_borrowings         = 1
        bus_age                     = 1
        ogrn_age                    = st.sidebar.slider('ogrn_age',        0, 1000, 135)
        adr_actual_age              = 1
        head_actual_age             = 1
        cap_actual_age              = st.sidebar.slider('cap_actual_age',  0, 1000, 3)
        ul_staff_range              = st.sidebar.select_slider('ar_sale_cost', ('[1-100]', '(100-500]', '> 500'))
        ul_capital_sum              = st.sidebar.slider('ul_capital_sum', 0, 130, 25)
        ul_founders_cnt             = 1
        ul_branch_cnt               = st.sidebar.slider('ul_strategic_flg', 0, 130, 0)
        ul_strategic_flg            = st.sidebar.select_slider('ar_sale_cost', (0,1))
        ul_systematizing_flg        = 1
        data = {
                'record_id'                   : record_id,
                'ar_revenue'                  : ar_revenue,
                'ar_total_expenses'           : ar_total_expenses,
                'ar_sale_cost'                : ar_sale_cost,
                'ar_selling_expenses'         : ar_selling_expenses,
                'ar_management_expenses'      : ar_management_expenses,
                'ar_sale_profit'              : ar_sale_profit,
                'ar_balance_of_rvns_and_expns': ar_balance_of_rvns_and_expns,
                'ar_profit_before_tax'        : ar_profit_before_tax,
                'ar_taxes'                    : ar_taxes,
                'ar_other_profit_and_losses'  : ar_other_profit_and_losses,
                'ar_net_profit'               : ar_net_profit,
                'ab_immobilized_assets'       : ab_immobilized_assets,
                'ab_mobile_current_assets'    : ab_mobile_current_assets,
                'ab_inventory'                : ab_inventory,
                'ab_accounts_receivable'      : ab_accounts_receivable,
                'ab_other_current_assets'     : ab_other_current_assets,
                'ab_cash_and_securities'      : ab_cash_and_securities,
                'ab_losses'                   : ab_losses,
                'ab_own_capital'              : ab_own_capital,
                'ab_borrowed_capital'         : ab_borrowed_capital,
                'ab_long_term_liabilities'    : ab_long_term_liabilities,
                'ab_short_term_borrowing'     : ab_short_term_borrowing,
                'ab_accounts_payable'         : ab_accounts_payable,
                'ab_other_borrowings'         : ab_other_borrowings,
                'bus_age'                     : bus_age,
                'ogrn_age'                    : ogrn_age,
                'adr_actual_age'              : adr_actual_age,
                'head_actual_age'             : head_actual_age,
                'cap_actual_age'              : cap_actual_age,
                'ul_staff_range'              : ul_staff_range,
                'ul_capital_sum'              : ul_capital_sum,
                'ul_founders_cnt'             : ul_founders_cnt,
                'ul_branch_cnt'               : ul_branch_cnt,
                'ul_strategic_flg'            : ul_strategic_flg,
                'ul_systematizing_flg'        : ul_systematizing_flg,
                }

        features = pd.DataFrame(data, index=[0])
        return features
    shows = user_input_features()

###################################       SIDEBAR      ###################################
##########################################################################################
##########################################################################################
##########################################################################################

#_______________________________        DISPLAY CSV       _______________________________#

from st_aggrid import GridUpdateMode, DataReturnMode

gb = GridOptionsBuilder.from_dataframe(shows)
## enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
gridOptions = gb.build()




###################################        DISPLAY CSV        ##################################
################################################################################################
################################################################################################
################################################################################################

#__________________________________        SHOW METRICS      __________________________________#
df = shows
df_stats = mp.make_df_ready_for_viz(df)

def scatter_3d(df_stats, x,y,z):
    import plotly.express as px
    fig = px.scatter_3d(df_stats, x,y,z,
                        color='Вероятность Дефолта',
                        symbol='выборка',
                        hover_name='выборка',
                        opacity=0.4,
                        size=df_stats['выборка'].replace({'выборка, на которой проводилось обучение': 0.1, 'введенная выборка':2}))
    fig.update_layout(coloraxis_colorbar_x=-0.15)
    return fig

def scatter_2d(df_stats, x,y):
    import plotly.express as px
    fig = px.scatter(df_stats, x,y, 
                     color='Результат модели', 
                     marginal_x="box", 
                     marginal_y="histogram",
                     symbol='выборка',
                     opacity=0.4,
                     size=df_stats['выборка'].replace({'выборка, на которой проводилось обучение': 0.1, 'введенная выборка':1}))
    fig.update_layout(coloraxis_colorbar_x=-0.3)
    return fig
c1,c2,c3 = st.columns([1, 1, 1])

with c1:
    x = st.selectbox('X',df_stats.columns)
with c2:
    y = st.selectbox('Y',df_stats.columns)
with c3:
    z = st.selectbox('Z',df_stats.columns)
fig_3d = scatter_3d(df_stats, x,y,z)
fig_2d = scatter_2d(df_stats, x,y)

st.plotly_chart(fig_3d, use_container_width=True)
st.plotly_chart(fig_2d, use_container_width=True)

###################################      SHOW METRICS         ##################################
################################################################################################
################################################################################################
################################################################################################


#__________________________________       PREDICT  CSV        __________________________________#

st.subheader("Предсказания 👇 ")

c29, c30, c31 = st.columns([1, 1, 2])

response = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=False,
)

df = pd.DataFrame(response["selected_rows"])

@st.cache
def predict(shows):
    return mp.predict_pretty(shows.copy())

prediction = predict(shows)

with c29:
    CSVButton = download_button(
        pd.DataFrame(prediction).T,
        'prediction.csv',
        'скачать предсказание'
    )

with c31:
    st.text("")

    st.dataframe(pd.DataFrame(prediction))

    st.text("")

###################################       PREDICT  CSV        ##################################
################################################################################################
################################################################################################
################################################################################################

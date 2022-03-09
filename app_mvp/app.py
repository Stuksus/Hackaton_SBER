import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################

# import megaquant_processing

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
st.title("Hello Elizabeth!")

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
    shows = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    file_container.write(shows)

else:
    st.sidebar.info(
        f"""
            👆 Попробуйте загрузить [df_test.csv](https://hse.kamran.uz)
            """
    )

    def user_input_features():
        record_id                   = 0
        ar_revenue                  = st.sidebar.number_input('ar_revenue',                   value=0)
        ar_total_expenses           = st.sidebar.number_input('ar_total_expenses',            value=0)
        ar_sale_cost                = st.sidebar.number_input('ar_sale_cost',                 value=0)
        ar_selling_expenses         = st.sidebar.number_input('ar_selling_expenses',          value=0)
        ar_management_expenses      = st.sidebar.number_input('ar_management_expenses',       value=0)
        ar_sale_profit              = st.sidebar.number_input('ar_sale_profit',               value=0)
        ar_balance_of_rvns_and_expns= st.sidebar.number_input('ar_balance_of_rvns_and_expns', value=0)
        ar_profit_before_tax        = st.sidebar.number_input('ar_profit_before_tax',         value=0)
        ar_taxes                    = st.sidebar.number_input('ar_taxes', value=0)
        ar_other_profit_and_losses  = st.sidebar.number_input('ar_other_profit_and_losses', value=0)
        ar_net_profit               = st.sidebar.number_input('ar_net_profit', value=0)
        ab_immobilized_assets       = st.sidebar.number_input('ab_immobilized_assets', value=0)
        ab_mobile_current_assets    = st.sidebar.number_input('ab_mobile_current_assets', value=0)
        ab_inventory                = st.sidebar.number_input('ab_inventory', value=0)
        ab_accounts_receivable      = st.sidebar.number_input('ab_accounts_receivable', value=0)
        ab_other_current_assets     = st.sidebar.number_input('ab_other_current_assets', value=0)
        ab_cash_and_securities      = st.sidebar.number_input('ab_cash_and_securities', value=0)
        ab_losses                   = st.sidebar.number_input('ab_losses', value=0)
        ab_own_capital              = st.sidebar.number_input('ab_own_capital', value=0)
        ab_borrowed_capital         = st.sidebar.number_input('ab_borrowed_capital', value=0)
        ab_long_term_liabilities    = st.sidebar.number_input('ab_long_term_liabilities', value=0)
        ab_short_term_borrowing     = st.sidebar.number_input('ab_short_term_borrowing', value=0)
        ab_accounts_payable         = st.sidebar.number_input('ab_accounts_payable', value=0)
        ab_other_borrowings         = st.sidebar.number_input('ab_other_borrowings', value=0)
        bus_age                     = st.sidebar.slider('bus_age',         0, 1000, 156)
        ogrn_age                    = st.sidebar.slider('ogrn_age',        0, 1000, 135)
        adr_actual_age              = st.sidebar.slider('adr_actual_age',  0, 1000, 3)
        head_actual_age             = st.sidebar.slider('head_actual_age', 0, 1000, 3)
        cap_actual_age              = st.sidebar.slider('cap_actual_age',  0, 1000, 3)
        ul_staff_range              = st.sidebar.select_slider('ar_sale_cost', ('[1-100]', '(100-500]', '> 500'))
        ul_capital_sum              = st.sidebar.slider('', 0, 130, 25)
        ul_founders_cnt             = st.sidebar.number_input('ar_sale_cost', 1, 10000, 3)
        ul_branch_cnt               = st.sidebar.slider('', 0, 130, 0)
        ul_strategic_flg            = 0
        ul_systematizing_flg        = 0
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


import plotly.figure_factory as ff
import numpy as np


###################################        DISPLAY CSV        ##################################
################################################################################################
################################################################################################
################################################################################################

#__________________________________        SHOW METRICS      __________________________________#
df = shows

def make_fig():
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
             hist_data, group_labels, bin_size=[.1, .25, .5])

    return fig

# Plot! 
fig = make_fig()
st.plotly_chart(fig, use_container_width=True)

# for col in df.columns:
#     st.metric(label = str(col),  value = str(df[col].mode()[0]), delta="")

###################################      SHOW METRICS         ##################################
################################################################################################
################################################################################################
################################################################################################


#__________________________________       PREDICT  CSV        __________________________________#

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

st.subheader("Предсказания 👇 ")

@st.cache
def predict(shows):
    import megaquant_processing as mp
    return mp.predict(shows.copy())


with c29:
    st.text("")

    prediction = predict(shows)
    st.dataframe(prediction)

    st.text("")

with c31:
    CSVButton = download_button(
        pd.DataFrame(prediction),
        'prediction.csv',
        'скачать предсказание'
    )

###################################       PREDICT  CSV        ##################################
################################################################################################
################################################################################################
################################################################################################

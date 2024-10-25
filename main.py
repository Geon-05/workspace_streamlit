import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

# def click_btn1():
#     with open('my_first_model','rb') as f:
#         loaded_model = pickle.load(f)
#     st.text('테스트')
    
# st.button('나를 눌러!', on_click=click_btn1)
# st.text('테스트')

# if st.button('나를 눌러!!'):
#     st.text('짜잔!')
#     st.code(body='ddddd',language='python')
#     df = pd.read_csv('./data/train.csv')
#     df

# LotFrontage : 부동산에 연결된 거리의 선형 피트
# LotArea : 평방 피트 단위의 부지 크기
# GrLivArea : 거실 면적 평방피트
with open('data/house_model_col3.pkl','rb')as f:
    loaded_model = pickle.load(f)

def predict_uf(input):
    result = loaded_model.predict(input)
    return result


with st.form(key='form'):
    # var1 = st.text_input('input1')
    
    value1 = st.number_input('input1', value=None, placeholder='부동산에 연결된 거리의 선형 피트')
    value2 = st.number_input('input2', value=None, placeholder='평방 피트 단위의 부지 크기')
    value3 = st.number_input('input3', value=None, placeholder='거실 면적 평방피트')
    
    # print (f'value type: {type(value1)}')
    
    submit = st.form_submit_button(label='예측하기')
    
if submit:
    # print('submit')
    # start = time.time()
    user_input_data = [[value1, value2, value3]]
    st.write(f'사용자가 입력한 데이터 : {user_input_data}')
    start = time.time() # 시작시간 체크
    result = predict_uf(user_input_data)
    end = time.time() # 끝시간 체크
    st.write(f'predict end: {end-start}s elapsed')
    
    st.write(f'input 1: {value1}')
    st.write(f'input 2: {value2}')
    st.write(f'input 3: {value3}')
    st.write(f'예측 집값: {result}')
    st.write(f'예측 집값: {result[0]}')

# st.title('Uber pickups in NYC')

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# st.write(df)


# st.write('hello world')


# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# st.dataframe(df)  # 대화형 테이블
# st.table(df)  # 정적 테이블

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.514575, 127.0495556],
#     columns=['lat', 'lon'])

# st.map(map_data)

# import streamlit as st
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data
    
# option = st.selectbox(
# 'Which number do you like best?',
#     [1, 2, 3, 4, 5])

# 'You selected: ', option

# st.sidebar.write('연락방법')
# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
# st.sidebar.write('범위')
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )


# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     st.write('해리포터')
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

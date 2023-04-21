import streamlit as st

view = [10, 34, 50, 62, 1]
st.write('# 조사자료 그림')
st.write('## 자료')
view
st.write('## 각각 자료값')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview

import streamlit as st

def create_bar_chart(data, x, y):
    chart_data = {}
    for item in data:
        key = item[x]
        value = item[y]
        if key in chart_data:
            chart_data[key] += value
        else:
            chart_data[key] = value
    return st.bar_chart(chart_data)
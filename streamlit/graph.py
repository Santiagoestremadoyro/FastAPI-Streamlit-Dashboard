import streamlit as st
import plotly.express as px
from gets import get_info


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





def generate_graph(penguin_id):
    data  = get_info(penguin_id)

    fig = px.scatter(data, x='culmen_length_mm', y='culmen_depth_mm', size='body_mass_g', color='species',
                    hover_data=['_id', 'island', 'flipper_length_mm', 'sex'])
    fig.update_layout(title=f"Information of Penguin with ID {penguin_id}")
    st.plotly_chart(fig)
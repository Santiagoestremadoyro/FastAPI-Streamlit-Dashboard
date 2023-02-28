import streamlit as st
import plotly.express as px

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
    penguin_data = db[db['_id'] == penguin_id]

    fig = px.scatter(penguin_data, x='culmen_length_mm', y='culmen_depth_mm', size='body_mass_g', color='species',
                     hover_data=['_id', 'island', 'flipper_length_mm', 'sex'])

    # Set the title of the plot
    fig.update_layout(title=f"Information of Penguin with ID {penguin_id}")

    # Display the plot
    st.plotly_chart(fig)
import streamlit as st
from gets import get_sex, get_island, get_species
from graph import create_bar_chart
import io
import pdfkit



st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)

st.image('./data/pinguinos.jpg')

st.sidebar.success("Select an option above 👆🏼 ")

selectbox = st.selectbox("What would you like to see?", ["by sex", "by islands", "by species"])


def create_pdf_report(selected_option):
    # Fetch data from API based on selected option
    if selected_option == "by sex":
        data = get_sex()
    elif selected_option == "by islands":
        data = get_island()
    elif selected_option == "by species":
        data = get_species()

    # Convert data to HTML table
    table_html = "<table><thead><tr><th>{}</th><th>{}</th></tr></thead><tbody>".format("_id", "count")
    for item in data:
        table_html += "<tr><td>{}</td><td>{}</td></tr>".format(item["_id"], item["count"])
    table_html += "</tbody></table>"

    # Create HTML report
    report_html = "<html><body><h1>{}</h1>{}</body></html>".format(selected_option.capitalize(), table_html)

    # Generate PDF report
    pdfkit.from_string(report_html, "report.pdf")

    # Return file path to generated PDF report
    return "report.pdf"









if st.button("Download PDF report"):
    file_path = create_pdf_report(selectbox)
    with open(file_path, "rb") as f:
        st.download_button("Download PDF", f.read(), "report.pdf", "application/pdf")




path_wkhtmltopdf = '/Program Files/wkhtmltopdf' 
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_string(report_html, 'report.pdf', configuration=config)



"""""
if selectbox == "by sex":
    data = get_sex()
    download_report(data, "_id", "count")
elif selectbox == "by islands":
    data = get_island()
    download_report(data, "_id", "count")
elif selectbox == "by species":
    data = get_species()
    download_report(data, "_id", "count")
"""










if selectbox == "by sex":
    data = get_sex()
    graph = create_bar_chart(data, "_id", "count")
elif selectbox == "by islands":
    data = get_island()
    create_bar_chart(data, "_id", "count")
elif selectbox == "by species":
    data = get_species()
    create_bar_chart(data, "_id", "count")


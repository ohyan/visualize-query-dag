import streamlit as st

from extracte_deps import extract_dependencies
from dep_graph import create_dependencies_graph


# text form
query = st.text_area('Enter SQL script.', height=400)

try:
    # if SQL script has been entered, parse that and display the figure
    query_dependencies = extract_dependencies(query)
    dependencies_graph = create_dependencies_graph(query_dependencies)
    st.graphviz_chart(dependencies_graph)
except:
    # if SQL syntax is wrong or have not been entered raise message
    st.subheader('Check and modify script')

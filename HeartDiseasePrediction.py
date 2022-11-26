import home
import index
import streamlit as st
PAGES = {
    "Home": home,
    "Logistic Regression": index
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.main()
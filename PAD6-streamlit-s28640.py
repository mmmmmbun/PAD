import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

tab1, tab2 = st.tabs(["Ankieta ", "Staty"])

with tab1:
    with st.form(key='columns_in_form'):
        st.text_input(label="Imię")
        st.text_input(label="Nazwisko")
        butt =  st.form_submit_button('Submit')
        if butt:
            st.success("Dane zostały zapisane")

with tab2:
    # Do przygotowania został uzyty dataframe z winem z zadania z dashem
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
    my_bar = st.progress(0)
    if uploaded_file:
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
        plot_data = df[selected_column_names]
        with st.form(key='wykresy'):
                butt1 =  st.form_submit_button('Pokaz histogram')
                if butt1:
                    plot_dataNN = df[selected_column_names].plot(kind='hist')
                    st.write(plot_dataNN)
                    st.pyplot()
                butt2 =  st.form_submit_button('Pokaz wykres pudełkowy')
                if butt2:
                    plot_dataNN = df[selected_column_names].plot(kind='box')
                    st.write(plot_dataNN)
                    st.pyplot()
import streamlit as st

def app():
    # Libraries
    import pandas as pd
    import pickle

    # Import model
    with open('model_rf.pkl', 'rb') as file_1:
        model_rf = pickle.load(file_1)

    # Page title
    st.title("Water Potability Prediction")

    # Inputation form for user
    with st.form("user_input_form"):
        ph_level = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
        hardness = st.number_input("Hardness", min_value=0.0, max_value=500.0, value=100.0)
        solids = st.number_input("Total Dissolved Solids", min_value=0.0, max_value=10000.0, value=500.0)
        chloramines = st.number_input("Chloramines", min_value=0.0, max_value=20.0, value=5.0)
        sulfate = st.number_input("Sulfate", min_value=0.0, max_value=600.0, value=200.0)
        conductivity = st.number_input("Conductivity", min_value=0.0, max_value=5000.0, value=1500.0)
        organic_carbon = st.number_input("Organic Carbon", min_value=0.0, max_value=50.0, value=10.0)
        trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, max_value=200.0, value=50.0)
        turbidity = st.number_input("Turbidity", min_value=0.0, max_value=10.0, value=3.0)


        user_input = {
            'ph': ph_level,
            'Hardness': hardness,
            'Solids': solids,
            'Chloramines': chloramines,
            'Sulfate': sulfate,
            'Conductivity': conductivity,
            'Organic_carbon': organic_carbon,
            'Trihalomethanes': trihalomethanes,
            'Turbidity': turbidity
            }
        
        user_data = pd.DataFrame(user_input, index=[0])
        submit = st.form_submit_button("Submit Data")

        st.subheader('User Input')
        st.write(user_data)

    # Prediction
    if submit:
        data_pred = model_rf.predict(user_data)
        if data_pred == 0:
            st.write("The water is not potable")
        else:
            st.write("The water is potable")
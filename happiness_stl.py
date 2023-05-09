import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('happinessmodel.pkl', 'rb'))

# Set the page title and background color
st.set_page_config(page_title='Happiness Score Predictor', page_icon=':smiley:',
                   layout='wide', initial_sidebar_state='auto')
st.markdown("<h1 style='text-align: center; color: #F2AA4C;'>Happiness Score Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #F2AA4C;'>Enter the following variables to predict the happiness score of a country</h4>", unsafe_allow_html=True)
st.markdown("<hr style='border: 3px solid #9d69e0; background-color: #F2AA4C;'>", unsafe_allow_html=True)

# Define the input fields for the user to enter using st.slider
gdp_per_capita = st.slider('GDP per capita', min_value=0.0, max_value=2.0, step=0.01, value=0.8)
social_support = st.slider('Social support', min_value=0.0, max_value=2.0, step=0.01, value=1.2)
healthy_life_expectancy = st.slider('Healthy life expectancy', min_value=0.0, max_value=2.0, step=0.01, value=0.6)
freedom_to_make_life_choices = st.slider('Freedom to make life choices', min_value=0.0, max_value=2.0, step=0.01, value=0.5)
generosity = st.slider('Generosity', min_value=0.0, max_value=2.0, step=0.01, value=0.2)
perceptions_of_corruption = st.slider('Perceptions of corruption', min_value=0.0, max_value=2.0, step=0.01, value=0.1)

# Define a submit button to trigger the prediction
if st.button('Predict Happiness Score'):
    # Create a pandas dataframe from the user inputs
    input_fields = {
        'GDP per capita': gdp_per_capita,
        'Social support': social_support,
        'Healthy life expectancy': healthy_life_expectancy,
        'Freedom to make life choices': freedom_to_make_life_choices,
        'Generosity': generosity,
        'Perceptions of corruption': perceptions_of_corruption
    }
    input_df = pd.DataFrame([input_fields])

    # Use the loaded model to make a prediction on the input dataframe
    score = model.predict(input_df)
    
    # Display the predicted score to the user
    st.write("The predicted happiness score is {score[0]:.2f}")

    # Markdown-display the predicted score to the user
    st.markdown("<hr style='border: 1px solid #9d69e0; background-color: #F2AA4C;'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: left; color: #D4E6F1;'>The predicted happiness score is {score[0]:.2f}</h3>", unsafe_allow_html=True)
    if score <= 4:
        st.markdown(f"<h4 style='text-align: left; color: #D4E6F1;'>Much work to be done!</h4>", unsafe_allow_html=True)
    elif score == 4 or score<= 6:
        st.markdown(f"<h4 style='text-align: left; color: #D4E6F1;'>This is a fair happiness index</h4>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h4 style='text-align: left; color: #D4E6F1;'>Let's definatly keep this up</h4>", unsafe_allow_html=True)
        
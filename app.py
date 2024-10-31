import streamlit as st
import pickle
from datetime import datetime
# Import your data loading and preprocessing functions
import dynamic_preprocessing

# Load the trained model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Define Bundesliga teams
teams = ["M'gladbach",
 'Augsburg',
 'Freiburg',
 'Hoffenheim',
 'Mainz',
 'RB Leipzig',
 'Dortmund',
 'Wolfsburg',
 'St Pauli',
 'Union Berlin',
 'Bochum',
 'Ein Frankfurt',
 'Holstein Kiel',
 'Stuttgart',
 'Werder Bremen',
 'Leverkusen',
 'Heidenheim',
 'Bayern Munich']

# Streamlit App UI
st.title("Bundesliga Match Predictor")

home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", teams)
match_date = st.date_input("Select Match Date", datetime.today())

if st.button("Predict Result"):
    # Get the features based on selected teams and date
    features = get_features_for_teams(home_team, away_team, match_date)
    
    # Predict using the model
    prediction = model.predict([features])

    # Display result
    result_map = { 'H': "Home Win", 'D': "Draw", 'A': "Away Win" }
    st.write("Predicted Result:", result_map[prediction[0]])

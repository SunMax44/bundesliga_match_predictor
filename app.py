import streamlit as st
import pickle
from datetime import datetime
# Import your data loading and preprocessing functions
from dynamic_preprocessing import get_features_for_teams

try:
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    print("Scaler loaded successfully.")
except FileNotFoundError:
    print("scaler.pkl file not found.")
except Exception as e:
    print("Error loading scaler:", e)
    
# Load the trained model
model = pickle.load(open('log_reg_model.pkl', 'rb'))

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
    features = get_features_for_teams(home_team, away_team, match_date, scaler)
    
    # Predict using the model
    prediction = model.predict(features)

    # Display result
    # Display the raw prediction value for debugging
    st.write("Prediction value:", prediction[0])

    # Use int() to convert the prediction to match the integer keys in result_map
    result_map = {2: "Home Win", 1: "Draw", 3: "Away Win"}
    st.write("Predicted Result:", result_map[int(prediction[0])])

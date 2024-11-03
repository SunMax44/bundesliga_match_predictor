import streamlit as st
import pickle
from datetime import datetime
# Import your data loading and preprocessing functions
from functions.dynamic_preprocessing import get_features_for_teams

# Load the scaler
with open("pickle_files/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load the PCA transformer
with open("pickle_files/pca.pkl", "rb") as f:
    pca = pickle.load(f)
    
# Load the trained model
model = pickle.load(open('pickle_files/log_reg_model.pkl', 'rb'))

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
    features_scaled = get_features_for_teams(home_team, away_team, match_date, scaler)

    # Apply PCA transformation
    features_pca = pca.transform(features_scaled)
    
    # Predict using the model
    prediction = model.predict(features_pca)

    # Use int() to convert the prediction to match the integer keys in result_map
    result_map = {2: "Home Win", 1: "Draw", 3: "Away Win"}
    st.write("### Predicted Result:", result_map[int(prediction[0])])
    confidence_score = round(model.predict_proba(features_pca).max() * 100,2)
    st.write(f'##### Our model is confident in its prediction by a score of {confidence_score}%')

    # Display pre-calculated precision values
    st.write("General model performance on test data (precision rates):")
    st.write("Home Win: 54%")
    st.write("Away Win: 44%")
    st.write("Draw: 36%")

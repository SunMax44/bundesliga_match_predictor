import pandas as pd

def get_features_for_teams(team_h, team_a, date, scaler, npm=5):
    # Load the current season's data
    df = pd.read_csv('buli_24_25.csv')

    # Convert 'Date' column in the DataFrame (in DD/MM/YYYY format) to datetime and normali
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    
    # Convert the Streamlit input date (in YYYY/MM/DD format) to match the DataFrame's date format
    date = pd.to_datetime(date, format='%Y/%m/%d', errors='coerce')


    # Initialize stats dictionary and empty result dictionary
    stats = {
        'goals': {'scored': ('FTHG', 'FTAG'), 'conceded': ('FTAG', 'FTHG')},
        'shots': {'taken': ('HS', 'AS'), 'conceded': ('AS', 'HS')},
        'shots_on_target': {'taken': ('HST', 'AST'), 'conceded': ('AST', 'HST')},
        'fouls': {'fouls': ('HF', 'AF'), 'fouled': ('AF', 'HF')},
        'corners': {'taken': ('HC', 'AC'), 'conceded': ('AC', 'HC')},
        'yellow_cards': {'received': ('HY', 'AY'), 'provoked': ('AY', 'HY')},
        'red_cards': {'received': ('HR', 'AR'), 'provoked': ('AR', 'HR')},
    }
    
    # Filter past matches for both teams
    past_matches_home = df[((df['HomeTeam'] == team_h) | (df['AwayTeam'] == team_h)) & (df['Date'] < date)].tail(npm)
    past_matches_away = df[((df['HomeTeam'] == team_a) | (df['AwayTeam'] == team_a)) & (df['Date'] < date)].tail(npm)

    # Set a broad date range to include all dates
    #date = pd.Timestamp("2100-01-01")
    #past_matches_home = df[((df['HomeTeam'] == team_h) | (df['AwayTeam'] == team_h)) & (df['Date'] < date)].tail(npm)
    #past_matches_away = df[((df['HomeTeam'] == team_a) | (df['AwayTeam'] == team_a)) & (df['Date'] < date)].tail(npm)


    
    # Initialize dictionary to store calculated stats
    features = {}

    # Calculate stats for home team
    for stat, subcategories in stats.items():
        for subcategory, columns in subcategories.items():
            home_column, away_column = columns
            stat_home_as_home = past_matches_home.loc[past_matches_home['HomeTeam'] == team_h, home_column].sum()
            stat_home_as_away = past_matches_home.loc[past_matches_home['AwayTeam'] == team_h, away_column].sum()
            features[f'p_home_{stat}_{subcategory}'] = stat_home_as_home + stat_home_as_away

    # Calculate stats for away team
    for stat, subcategories in stats.items():
        for subcategory, columns in subcategories.items():
            home_column, away_column = columns
            stat_away_as_home = past_matches_away.loc[past_matches_away['HomeTeam'] == team_a, home_column].sum()
            stat_away_as_away = past_matches_away.loc[past_matches_away['AwayTeam'] == team_a, away_column].sum()
            features[f'p_away_{stat}_{subcategory}'] = stat_away_as_home + stat_away_as_away
    
    # Calculate points
    features[f'p_home_points'] = (
        (past_matches_home.loc[past_matches_home['HomeTeam'] == team_h, 'FTR'] == 'H').sum() * 3 +
        (past_matches_home.loc[past_matches_home['AwayTeam'] == team_h, 'FTR'] == 'A').sum() * 3 +
        (past_matches_home['FTR'] == 'D').sum() * 1
    )
    
    features[f'p_away_points'] = (
        (past_matches_away.loc[past_matches_away['HomeTeam'] == team_a, 'FTR'] == 'H').sum() * 3 +
        (past_matches_away.loc[past_matches_away['AwayTeam'] == team_a, 'FTR'] == 'A').sum() * 3 +
        (past_matches_away['FTR'] == 'D').sum() * 1
    )

    features_df = pd.DataFrame([features])

    # Apply the scaler to the features DataFrame
    features_scaled = pd.DataFrame(scaler.transform(features_df), columns=features_df.columns)
    
    return features_scaled

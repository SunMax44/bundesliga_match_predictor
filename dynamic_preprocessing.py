import pandas as pd

def get_features_for_teams(team_h, team_a, date, npm=5):
        # Load the current season's data
    df = pd.read_csv('buli_24_25.csv')

    # Ensure the 'Date' column in the DataFrame is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Ensure that `date` is explicitly converted to a compatible datetime format
    if not isinstance(date, pd.Timestamp):
        date = pd.to_datetime(date, errors='coerce')

    # Check if conversion was successful, in case `date` or `df['Date']` contains any invalid entries
    if date is pd.NaT:
        raise ValueError("The provided date is invalid or could not be converted to datetime format.")

    # Remove any rows with NaT in 'Date' after conversion to ensure clean data
    df = df.dropna(subset=['Date'])
    
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
    features[f'p_home_points_last'] = (
        (past_matches_home.loc[past_matches_home['HomeTeam'] == team_h, 'FTR'] == 'H').sum() * 3 +
        (past_matches_home.loc[past_matches_home['AwayTeam'] == team_h, 'FTR'] == 'A').sum() * 3 +
        (past_matches_home['FTR'] == 'D').sum() * 1
    )
    
    features[f'p_away_points_last'] = (
        (past_matches_away.loc[past_matches_away['HomeTeam'] == team_a, 'FTR'] == 'H').sum() * 3 +
        (past_matches_away.loc[past_matches_away['AwayTeam'] == team_a, 'FTR'] == 'A').sum() * 3 +
        (past_matches_away['FTR'] == 'D').sum() * 1
    )
    
    return features

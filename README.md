# Bundesliga Football Match Predictor: Who will win?

#### Presentation

For an in-depth overview of the project, please view the presentation here: [Project Presentation](https://docs.google.com/presentation/d/1f4JAwq7Ns71cGdPBv8MNw0RQxHTA0gkFuH8jvnzXr0g/edit?usp=sharing).

#### Streamlit

[Streamlit Page](https://bundesligamatchpredictor.streamlit.app/) to individually predict future Bundesliga matches (input data based on 1st of November 2024).

## Predict the outcomes of Bundesliga football matches

This project, created by Max and Janos, is a comprehensive machine learning solution for predicting match outcomes in the Bundesliga. It was designed with potential applications for sports betting and analytical insights, enabling predictions of match results and scores for both home and away teams.

## Project Overview

Bundesliga Football Match Predictor applies machine learning to predict match outcomes using historical data. The model could be applied for sports betting or personal use, and with further refinement, it could serve analytical purposes for coaches or analysts to better understand likely match outcomes.

## Data Sources and Preparation

This project uses Bundesliga match data from **2006 to 2024**, comprising detailed statistics such as:
- **Match Date** (`Date`)
- **Team Identifiers** (`HomeTeam`, `AwayTeam`)
- **Result and Scores** (`FTHG`, `FTAG`, `FTR`)
- **Team Statistics** (e.g., `HS`, `AS`, `HST`, `AST` for shots and shots on target; `HC`, `AC` for corners; `HF`, `AF` for fouls committed, etc.)
- **Cards and Offsides** (`HY`, `AY`, `HR`, `AR`, `HO`, `AO`)

Additional derived features were created by aggregating data from each team’s last five matches, resulting in a total of **30 features** for model input.

## Feature Engineering & Selection

1. **Target Features**: The model predicts three main target variables:
   - *Match Outcome* (Win, Draw, Loss)
   - *Home Team’s Goal Score*
   - *Away Team’s Goal Score*

2. **Feature Selection and Correlation**: Features were assessed for relevance, and betting odds were tested but did not significantly improve performance.

## Model Building & Evaluation

Multiple models were evaluated to predict match outcomes, including:
- **Logistic Regression**
- **K-Nearest Neighbors (KNN)**
- **Decision Trees**

The chosen model, **Logistic Regression**, yielded the best accuracy for the target variables with accuracies as follows:
- **Match Outcome**: *51%*
- **Home Team’s Goal Score**: *30%*
- **Away Team’s Goal Score**: *34%*

A confusion matrix was used to evaluate model accuracy and pinpoint areas for improvement.

## Hyperparameter Tuning & Model Optimization

Various optimization techniques were tested to improve model performance, including:
- **Hyperparameter Tuning** using `GridSearchCV`, which provided a slight accuracy improvement (3% for Home Team’s goals).
- **Ensemble Methods** such as *Gradient Boosting* and *ADA Boosting*, which allowed for adjustments to precision and recall but didn’t enhance overall accuracy.

## Key Findings & Insights

- **Home Wins** are the most frequent outcomes.
- The model provides useful predictions for Goal Scores.
- Boosting methods may not improve performance for unbalanced datasets.
- **Application-specific optimization** (focusing on precision, recall, or accuracy) is crucial depending on the intended use.

## Real-World Applications

- **Betting Companies**: This model could enhance odds calculations.
- **Individual Use**: Users could leverage predictions to inform betting decisions.
- **Sports Teams**: Insights into match patterns and outcomes could assist teams in their match preparation.

## Streamlit App

A **Streamlit app** was developed to deploy the predictor, allowing users to:
1. Select Bundesliga teams.
2. Input a date for the prediction.
3. Retrieve predicted match outcomes based on recent match data.

This tool provides a user-friendly interface for sports enthusiasts and potential bettors.

## Challenges and Learnings

Throughout this project, several challenges were encountered:
- **Syntax and Dependency Issues**: Streamlit deployment faced syntax errors and dependency configuration hurdles.
- **Feature Complexity**: Balancing feature selection to avoid overfitting while maximizing accuracy was essential.
- **Data Integration**: Finding and incorporating additional relevant data proved time-consuming, with diminishing returns.

## Future Work & Improvements

1. **Enhanced Data**: Incorporate advanced football metrics and betting odds.
2. **Flexible Match Aggregation**: Experiment with different numbers of matches in aggregation.
3. **API Connectivity**: Streamline data input by connecting directly to football data APIs.
4. **Outlier Removal**: Filter data to focus on likely goal scores for improved model accuracy.

## Key Metrics & Findings

- **Model Accuracy for Match Outcome**: *51%*
- **Model Accuracy for Home Team Goals**: *30%*
- **Model Accuracy for Away Team Goals**: *34%*

Further tuning may enhance performance for specific use cases, such as optimizing for certain teams or match conditions.


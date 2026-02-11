import pandas as pd

crime_df = pd.read_csv("crime.csv") # load the dataset

crime_df['risk'] = crime_df['ViolentCrimesPerPop'].apply( # create a new risk column
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime" # classify based on violent crime rate
)

grouped_risk = crime_df.groupby('risk') # group rows by crime risk level

avg_unemployment = grouped_risk['PctUnemployed'].mean() # compute average unemployment per group

for risk_level in ['HighCrime', 'LowCrime']: # iterate through both categories
    print(f"Average unemployment rate for {risk_level}: {avg_unemployment[risk_level]:.2f}%") # print formatted result

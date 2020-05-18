import tensorflow as tf
import pandas as pd
# reminder:
# https://github.com/google-research/tensorflow_constrained_optimization/blob/master/examples/jupyter/Recall_constraint.ipynb 

# read the researchers sample base data into a raw_data dataframe
raw_data = pd.read_csv(filepath_or_buffer="./data/researchers.csv")
print(raw_data.head())

# transfer raw_data into a sample data
#    generate one line containing all researchers data
#    one line contains researchers data for all reserachers
#    r1_is_earliest,r1_is_latest,etc.
dataframes = {}
# 1. get all researchers only dataframes
for researcher in raw_data["researcher"].unique():
    dataframes[researcher] = raw_data.query("researcher == '"+researcher+"'")
    print(dataframes[researcher].head())

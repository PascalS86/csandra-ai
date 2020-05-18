import tensorflow as tf
import pandas as pd
# reminder:
# https://github.com/google-research/tensorflow_constrained_optimization/blob/master/examples/jupyter/Recall_constraint.ipynb 

# read the researchers sample base data into a raw_data dataframe
raw_data = pd.read_csv(filepath_or_buffer="./data/researchers.csv")
print(raw_data.head())


import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:


data = pd.read_csv("/Users/hannahbecher/Pleo_GIT/CodeAcademy Projects/tennis_ace_starting/tennis_stats.csv")


# perform exploratory analysis here:

import tensorflow_data_validation as tfdv
 
stats = tfdv.generate_statistics_from_dataframe(data)
 
tfdv.visualize_statistics(stats)




















## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:

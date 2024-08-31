import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'weather.csv'
data=pd.read_csv(file_path, delimiter=',',header=11,skipinitialspace=True)
data.head(24)
print("")
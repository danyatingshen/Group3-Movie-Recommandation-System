# MODEL_PATH = 'model.pkl'
# DATA_PATH = 'cleaned_data.csv'

import pickle as pkl
import surprise
import pandas as pd

def inference(MODEL_PATH,DATA_PATH,UID):
  df1 = pd.read_csv(DATA_PATH) #loading the movie data to fetch from after inference
  algo = pkl.load(open(MODEL_PATH, 'rb')) #load these files in the Virtual Machine too
  nn = algo.get_neighbors(algo.trainset.to_inner_uid(UID), k=20)
  nn_raw = []
  for x in nn:
    nn_raw.append(algo.trainset.to_raw_uid(x))
  df1 = df1['userID'].isin(nn_raw)
  return (df1['movieID'].apply(lambda x : x.replace('+',' ')) ) #Import karna hai lol
# MODEL_PATH = 'model.pkl'
# DATA_PATH = 'cleaned_data.csv'

import pickle as pkl
import surprise
import pandas as pd

# df1 = pd.read_csv(DATA_PATH) #loading the movie data to fetch from after inference
# algo = pkl.load(open(MODEL_PATH, 'rb')) #load these files in the Virtual Machine too

def inference(MODEL_PATH,DATA_PATH,algo,df1,UID):
  try:
    nn = algo.get_neighbors(algo.trainset.to_inner_uid(UID), k=20)
    print("User Found! Providing Recommendations! \n")
    nn_raw = []
    # print(df1.columns)
    for x in nn:
      nn_raw.append(algo.trainset.to_raw_uid(x))
    # print(nn_raw)
    df2 = df1[df1['userID'].isin(nn_raw)]
    op = df2['movieID'].apply(lambda x : x.replace('+',' ')).tolist()
    #print(op)
    return op #Import karna hai lol
  except:
    op = df1['movieID'].sample(n=20).apply(lambda x : x.replace('+',' ')).tolist()
    print("Welcome New User! Here's a few movies that you could get started with :) \n")
    return op

  #nn = algo.get_neighbors(algo.trainset.to_inner_uid(UID), k=20)

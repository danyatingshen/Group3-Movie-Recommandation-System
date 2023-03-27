'''
This file is going to be imported in views.py, where it is called whenever a request for recommendations is to be made.
It takes 'algo', which is the pickle file in which the machine learning algorithm is stored as an object. 
It also takes a dataframe which has again been read in views.py and passed here as a parameter along with the UID which is requested
from the server.
'''
import pickle as pkl
import surprise
import pandas as pd

def inference(algo,df1,UID):
  try: #Found an existing user.. generate inferences for recommendations
    nn = algo.get_neighbors(algo.trainset.to_inner_uid(UID), k=20)
    print("User Found! Providing Recommendations! \n")
    nn_raw = []
    for x in nn:
      nn_raw.append(algo.trainset.to_raw_uid(x))
    df2 = df1[df1['userID'].isin(nn_raw)]
    op = df2['movieID'].tolist()
    return op
  except: #New User has been assigned random movies initially to view
    op = df1['movieID'].sample(n=20).tolist()
    print("Welcome New User! Here's a few movies that you could get started with :) \n")
    return op

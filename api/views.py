#----------------------------------------------------Importing Libraries and Inference Files---------------------------------------------------
from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from .Inference.Inference import inference
import pandas as pd
import pickle as pkl

from app import app

#----------------------------------------------------Extracting Resources and Model File---------------------------------------------------
MODEL_PATH='app/Inference/knnmodel.pkl' 
FILE_PATH ='app/Inference/cleaned_data.csv'

df1 = pd.read_csv(FILE_PATH) #loading the movie data to fetch from after inference
algo = pkl.load(open(MODEL_PATH, 'rb')) #load these files in the Virtual Machine too

#----------------------------------------------------Routing for a particular request---------------------------------------------------
@app.route('/recommend/<userid>')
def get_recommendation_by_userid(userid:int):
    #return "userId is: {}, movie: x,y,z".format(userid)
    op = inference(algo = algo,df1 = df1,UID = int(userid))
    return ','.join(op)
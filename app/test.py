import surprise
from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
import pandas as pd
import pickle as pkl

from Inference.Inference import inference

MODEL_PATH='Inference/knnmodel.pkl' #app/Inference/model.pkl
FILE_PATH ='Inference/cleaned_data.csv'

df1 = pd.read_csv(FILE_PATH) #loading the movie data to fetch from after inference
algo = pkl.load(open(MODEL_PATH, 'rb')) #load these files in the Virtual Machine too

print(inference(MODEL_PATH,FILE_PATH,algo,df1,UID = 345678))

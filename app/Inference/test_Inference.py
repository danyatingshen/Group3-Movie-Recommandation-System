import unittest
from app.Inference.Inference import *
import pickle as pkl
import surprise
import pandas as pd
import regex as re

class test_inference(unittest.TestCase):
    def test_length(self):
        op1 = inference(algo = algo,df1 = df1,UID = 669078)
        self.assertEqual(len(op1), 20)
        
    def test_newuser(self):
        op1 = inference(algo = algo,df1 = df1,UID = -1)
        self.assertEqual(len(op1), 20)
    

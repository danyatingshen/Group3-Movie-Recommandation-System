import unittest
from data import *

class test_data_quality_check(unittest.TestCase):
    def test_nulls(self):
        op1 = data_quality_check('Group3 - random text')
        self.assertIsNotNone(op1)
        
    def test_dtype(self):
        op1 = data_quality_check('Group3 - random text')
        self.assertEqual(type(op1), str)
    
    def test_example(self):
        op1 = data_quality_check('2023-03-12T06:14:10,138739,GET /data/m/everybodys+fine+2009/26.mpg')
        self.assertEqual(op1, 'Valid message')
        
        op2 = data_quality_check('2023-03-12T06:14:10,138739,GET  /data/m/abcdefgh-random text')
        self.assertEqual(op2, 'Invalid message')
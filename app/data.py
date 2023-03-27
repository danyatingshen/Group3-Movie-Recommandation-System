import os
import pandas as pd
import numpy as np
import unittest
import regex as re



def data_quality_check(raw_data):
    '''
    Accepts kafka message as a raw string and return if its a valid message.
    Returns: str: Type of message - 'Invalid message' / 'Valid message'
                
    '''
    
    # check for user_actions data
    if '/data/m' in raw_data:
        
        mesg_parts =  raw_data.split(',')
    
        if len(mesg_parts) != 3:
            return 'Invalid message'
        
        timestamp, userid, mesg_string = mesg_parts
        
        if not mesg_string.endswith('.mpg'):
            return 'Invalid message'
        
        # try for valid userid
        try:
            int(userid)
        except ValueError as ve:
            return 'Invalid message'
        
        return 'Valid message'
        
        
        
    # check for user_ratings data
    if '/rate/' in raw_data:
        
        mesg_parts =  raw_data.split(',')
    
        if len(mesg_parts) != 3:
            return 'Invalid message'
        
        timestamp, userid, mesg_string = mesg_parts
        rating = mesg_string.split('=')

        if len(rating) == 1:
            return 'Invalid message'
        
        # try for valid userid
        try:
            int(userid)
        except ValueError as ve:
            return 'Invalid message'   
              
        # try for valid rating value
        try:
            int(rating[-1])
        except ValueError as ve:
            return 'Invalid message'
        
        return 'Valid message'
        
        
        
    # check for 'recommendation request' 
    if 'recommendation request' in raw_data:
        
        mesg_parts =  raw_data.split(',')
        
        
        result = re.search(".*result:\s(.*)", raw_data)
        movies = result.group(1).split(', ')
        
        if len(movies) != 20:
            return 'Invalid message'
        
        
        # try for valid userid
        userid = mesg_parts[1]
        try:
            int(userid)
        except ValueError as ve:
            return 'Invalid message'
    
        return 'Valid message'
    
    
    
    # if no issues found return Valid message
    return 'Invalid message'
        
    
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
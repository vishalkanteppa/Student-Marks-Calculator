import os
import unittest
import json

from main import app


from flask import Flask, request, session, Response
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
from flask_session import Session
from flask_cors import CORS
import re
import base64
import json
import pickle
import csv
from matplotlib import pyplot as plt
import pandas as pd
import pymongo



TEST_DB = 'mongodb://localhost:27017/WTUsers_db'


class BasicTests(unittest.TestCase):


    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config["MONGO_URI"] =  "mongodb://localhost:27017/WTUsers_db" 
        #mongo = PyMongo(app)
        self.app = app.test_client()

    #executed after each test
    def tearDown(self):
        pass


    #expected is 200
    def test_addCSV(self):
        with app.test_client() as client:
            
            tupleadd={"FName":"Varun","LName":"V","Math":45, "Chem":81,"Bio":94,"CS":98, "Sports":1}
            
            response = client.post('/api/v1/student',data=json.dumps(tupleadd),headers={"Content-Type": "application/json"})
            
            self.assertEqual(response.status_code, 200)

	#-ve numbers, output is 200, since there is no error handling here 
    def test_addCSV2(self):
        with app.test_client() as client:
            
            tupleadd={"FName":"Varun","LName":"V","Math":-45, "Chem":-81,"Bio":-94,"CS":-98, "Sports":-1}
            
            response = client.post('/api/v1/student',data=json.dumps(tupleadd),headers={"Content-Type": "application/json"})
            
            self.assertEqual(response.status_code, 200)

    #ouput is 200        
    def test_search(self):
        with app.test_client() as client:
            
            response = client.get('/api/v1/search?Field=3&pValue=Adele,Alzamora')
            
            self.assertEqual(response.status_code, 200)


   #output is 404; failure, invalid name
    def test_search2(self):
        with app.test_client() as client:
            
            response = client.get('/api/v1/search?Field=3&pValue=Adele,Alzamooora')
                
            self.assertEqual(response.status_code, 200)

    #ouput is 200 
    def test_correlate(self):
        with app.test_client() as client:
            
            response = client.get('/api/v1/correlate?S1=Math&S2=Chemistry')
            
            self.assertEqual(response.status_code, 200)
                
    #output is keyError; no error handling implemented, invalid subject
    def test_correlate2(self):
        with app.test_client() as client:
            
            response = client.get('/api/v1/correlate?S1=Math&S2=Chemistryyy')
            
            self.assertEqual(response.status_code, 200)
             
        
            
    #output is 200 
    def test_predict(self):
         with app.test_client() as client:
             
            response = client.get('/api/v1/predict?Subject=Math&Score=94.5')
             
            self.assertEqual(response.status_code, 200)

    #output is 400, failure, number out of range
    def test_predict2(self):
         with app.test_client() as client:
            
            response = client.get('/api/v1/predict?Subject=Math&Score=945')
            
            self.assertEqual(response.status_code, 200)

    #output is 405, failure, invalid subject 
    def test_predict3(self):
        with app.test_client() as client:
            
            response = client.get('/api/v1/predict?Subject=Mathh&Score=94.5')
            
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
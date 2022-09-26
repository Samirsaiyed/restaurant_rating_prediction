from flask import Flask, render_template, request
import pandas as pd
import pickle
import sklearn

file = open("rate_prediction.pkl", "rb")
model = pickle.load(file)


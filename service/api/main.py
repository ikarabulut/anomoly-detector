from fastapi import FastAPI
from joblib import load

clf = load("model.joblib")


app = FastAPI()

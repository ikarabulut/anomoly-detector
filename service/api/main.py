from fastapi import FastAPI
from joblib import load

clf = load("model.joblib")

app = FastAPI()


@app.get("/model_information")
def model_information():
    return clf.get_params()


if __name__ == "__main__":
    print("running... ")

import fastapi
from joblib import load

clf = load("model.joblib")
app = FastAPI()

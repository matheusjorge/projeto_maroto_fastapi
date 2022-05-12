from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/new_endpoint")
def new_endoint():
    return {"message": "Congrats! You have a new end point"}

@app.get("/users/{user_id}")
def item_get(user_id: int):
    return {"message": f"Congrats! You are the user {user_id}", "user_id": user_id}

@app.get("/query_params")
def query_params(samples: int=1, random_state: int=42):
    np.random.seed(random_state)
    return {"random_samples": np.random.random(samples).tolist()}
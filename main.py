from fastapi import FastAPI

app = FastAPI(
    title="Poha is Love, Here are some variety for you to taste.",
    description="A simple FastAPI for Poha menu."
)


@app.get("/")
def root():
    return {"message": "Welcome to the online Poha Store API"}
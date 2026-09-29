from fastapi import FastAPI, HTTPException, Query
from data import pohadata 
from models import MenuItem, MenuResponse

app = FastAPI(
    title="Poha is Love, Here are some variety for you to taste.",
    description="A simple FastAPI for Poha menu."
)


@app.get("/")
def root():
    return {"message": "Welcome to the online Poha Store API"}

@app.get("/menu", response_model=MenuResponse)
def get_menu(category: str | None = Query(None, description="Filter by poha category")):
    if category:
        filtered = [item for item in pohadata if item["category"].lower() == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No item found in category: {category}")
        return MenuResponse(count=len(filtered), items=filtered)

    return MenuResponse(count=len(pohadata), items=pohadata)

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_dish(id: int):
    dish = [item for item in pohadata if item["id"] == id]
    if not dish:
        raise HTTPException(status_code=404, detail=f"No item found for Id: {id}")
    return MenuResponse(count=len(dish), items=dish)
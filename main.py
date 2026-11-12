from fastapi import FastAPI
from pydantic import BaseModel # helps in validation -> structure syntax

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: list[Tea] = [
    Tea(id=1, name="Green Tea", origin="China"),
    Tea(id=2, name="Black Tea", origin="India"),
]


# / => welcome message
@app.get("/") # func comes after decorator everytime
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error": "Tea not found"}

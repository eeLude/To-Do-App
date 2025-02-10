from fastapi import FastAPI #importoidaan FastAPI luokka moduulista

app = FastAPI() #FastAPI() on pääobjekti joka käsittelee HTTP pyynnöt ja vastaukset. app on sovelluksen ydin.

@app.get("/") # decorator, kun tulee get requesti juureen (/), kutsutaan alla olevaa funktiota.
def read_root():
    return {"message": "FastAPI backend toimii!"}

@app.get("/ping") #toinen get route jonka tehtävä on palauttaa /ping komentoon vastaus eli nähdään onko palvelin päällä
def ping():
    return {"ping": "pong"}
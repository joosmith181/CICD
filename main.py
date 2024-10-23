from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def entry():

    return {"message": "Introduction to automation"}

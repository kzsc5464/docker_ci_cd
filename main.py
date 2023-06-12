from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

# @app.get("/testconflict")
# async def root():
#     return {"message": "이젠 넌 잘 수 있어!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
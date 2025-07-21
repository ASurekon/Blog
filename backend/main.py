from fastapi import FastAPI
import uvicorn
from routers.blog import router as blog_router



app = FastAPI()
app.include_router(blog_router)


@app.get("/")
def index():
    return {"msg": "Hello, world"}



if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8000,
        reload=True)
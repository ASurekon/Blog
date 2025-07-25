from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.blog import router as blog_router
from routers.users import router as users_router
from database import async_engine, Base



app = FastAPI()
app.include_router(blog_router)
app.include_router(users_router)


# Настройки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Создание таблиц при старте
@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def index():
    return {"msg": "Hello, world"}



if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8001,
        reload=True)
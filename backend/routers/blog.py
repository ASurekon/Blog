from fastapi import APIRouter



router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)


@router.get("/")
async def display_blog():
    return {"msg": "Display blog"}


@router.post("/create")
async def create_article(title: str = "New article"):
    return {"msg": f"New article '{title}' created"}
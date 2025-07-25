from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from crud.blog import create_user_post, delete_post, get_post, get_posts, update_post
from database import get_db
from schemas.users import UserResponse
from schemas.blog import PostResponse, PostCreate, PostUpdate, CommentPost, CommentUpdate
from sqlalchemy.ext.asyncio import AsyncSession



router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)


@router.post("/todos/", response_model=PostResponse)
async def create_todo(
    todo: Annotated[PostCreate, Depends()],
    current_user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await create_user_post(db=db, post=todo, user_id=current_user.id)

# Получение списка Todo
@router.get("/todos/", response_model=List[PostResponse])
async def read_todos(
    skip: int = 0, limit: int = 100,
    current_user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    todos = await get_posts(db, user_id=current_user.id, skip=skip, limit=limit)
    return todos

# Получение конкретного Todo
@router.get("/todos/{todo_id}", response_model=PostResponse)
async def read_todo(
    todo_id: int,
    current_user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    db_todo = await get_post(db, post_id=todo_id, user_id=current_user.id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found or you are not its owner")
    return db_todo

# Обновление Todo
@router.patch("/todos/{todo_id}", response_model=PostResponse)
async def update_todo_item(
    todo_id: int,
    todo: Annotated[PostUpdate, Depends()],
    current_user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    db_todo = await get_post(db, post_id=todo_id, user_id=current_user.id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found or you are not its owner")
    return await update_post(db=db, db_post=db_todo, post=todo)

# Удаление Todo
@router.delete("/todos/{todo_id}")
async def delete_todo_item(
    todo_id: int,
    current_user: UserResponse = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    db_todo = await get_post(db, post_id=todo_id, user_id=current_user.id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found or you are not its owner")
    await delete_post(db=db, db_post=db_todo)
    return {"message": "Todo deleted successfully"}
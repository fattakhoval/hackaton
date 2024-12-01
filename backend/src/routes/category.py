from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.auth.auth import verify_token
from src.database.db_settings import get_session
from src.database.models import Category
from src.database.schemas.category import NewCategory

category_route = APIRouter()

@category_route.get('/category/{category_id}', dependencies=[Depends(verify_token)])
async def get_category(category_id, asession = Depends(get_session)):
    category = await Category.get(category_id, asession)
    return JSONResponse(status_code=200 if category else 400, content=category)

@category_route.get('/categories', dependencies=[Depends(verify_token)])
async def categories(asession = Depends(get_session)):
    category = await Category.get_all(asession)
    return JSONResponse(status_code=200 if category else 400, content=category)

@category_route.post('/category/add', dependencies=[Depends(verify_token)])
async def add_category(data: NewCategory, asession = Depends(get_session)):
    category = await Category.add(asession, data)
    return JSONResponse(status_code=200 if category else 400, content=category)

@category_route.delete('/remove_category')
async def remove_category():
    pass

@category_route.put('/update_category')
async def update_category():
    pass

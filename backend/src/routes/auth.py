from fastapi import APIRouter, status, Depends, HTTPException
from jose import jwt, JWTError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.responses import JSONResponse

from src.auth.auth import get_password_hash, verify_password, create_access_token, create_refresh_token
from src.database.db_settings import get_session
from src.database.models import User
from src.database.schemas.token import RefreshTokenRequest
from src.database.schemas.user import CreateUser, LoginUser

from config import config

auth_route = APIRouter()


@auth_route.post("/register")
async def register(data: CreateUser, asession: AsyncSession = Depends(get_session)):
    data.password = get_password_hash(data.password)
    try:
        new_user = CreateUser(**data.model_dump())
        await User.add(session=asession, data=new_user)
    except Exception as exc:
        print(exc)
        return JSONResponse(status_code=400, content={"msg": "User registered failed"})
    return JSONResponse(status_code=200, content={"msg": "User registered successfully"})

@auth_route.post("/login")
async def login(data: LoginUser, asession: AsyncSession = Depends(get_session)):
    user = await asession.execute(select(User).filter(User.email == data.email))
    user = user.scalars().first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return JSONResponse(status_code=200, content={"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"})

@auth_route.post("/refresh")
async def refresh_token(refresh_token: RefreshTokenRequest, asession: AsyncSession = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(refresh_token.refresh_token, config.jwt_secret_key, algorithms=[config.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await asession.execute(select(User).filter(User.email == email))
    user = user.scalars().first()

    if user is None:
        raise credentials_exception

    new_access_token = create_access_token(data={"sub": user.email})
    return {"access_token": new_access_token, "token_type": "bearer"}

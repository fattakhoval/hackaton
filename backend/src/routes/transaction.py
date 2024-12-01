from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.auth.auth import get_current_user, verify_token
from src.database.db_settings import get_session
from src.database.models import Transaction
from src.database.schemas.transaction import CreateTransaction, RequestTransaction

transaction_route = APIRouter()

@transaction_route.get('/transaction/{transaction_id}', dependencies=[Depends(verify_token)])
async def get_transaction(transaction_id, asession = Depends(get_session)):
    transaction = await Transaction.get(transaction_id, asession)
    return JSONResponse(status_code=200 if transaction else 400, content=transaction)

@transaction_route.get('/all_transaction', dependencies=[Depends(verify_token)])
async def all_transaction(asession = Depends(get_session)):
    transactions = await Transaction.get_all(asession)
    return JSONResponse(status_code=200 if transactions else 400, content=transactions)

@transaction_route.post('/add_transaction', dependencies=[Depends(verify_token)])
async def add_transaction(data: RequestTransaction, user = Depends(get_current_user), asession = Depends(get_session)):
    data = data.model_dump()
    data['user_id'] = user.id
    new_data = CreateTransaction(**data)
    transaction = await Transaction.add(asession, new_data)
    return JSONResponse(status_code=200 if transaction else 400, content=transaction)

@transaction_route.delete('/transactions/{transaction_id}', dependencies=[Depends(verify_token)])
async def remove_transaction(transaction_id, asession = Depends(get_session)):
    transactions = await Transaction.remove(transaction_id, asession)
    return JSONResponse(status_code=200 if transactions else 400, content=transactions)

@transaction_route.get('/transactions')
async def get_statistic(startDate, endDate, asession = Depends(get_session)):

    statistic = await Transaction.get_statistic(asession=asession, start_date=startDate, end_date=endDate)
    return JSONResponse(status_code=200 if statistic else 400, content=statistic)

@transaction_route.put('/update_transaction')
async def update_transaction():
    pass

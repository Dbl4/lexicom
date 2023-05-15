from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from models import Data
from services.data import get_data_service, DataService

router = APIRouter(prefix="/api/v1/endpoints")


@router.get(
    path="/",
    description="Получение адреса по номеру телефона",
)
async def check_data(
    phone: str,
    data_service: DataService = Depends(get_data_service),
):
    data = await data_service.get_from_cache(phone)
    if data is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Address not found"
        )
    return {"message": data.address}


@router.post(
    path="/",
    description="Сохранение адреса",
)
async def write_data(
    data: Data,
    data_service: DataService = Depends(get_data_service),
):
    await data_service.put_to_cache(data)
    return {"message": "Data saved successfully"}


@router.put(
    path="/",
    description="Обновление данных",
)
async def update_data(
    data: Data,
    data_service: DataService = Depends(get_data_service),
):
    data = await data_service.get_from_cache(data.phone)
    if data is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Address not found"
        )
    await data_service.put_to_cache(data)
    return {"message": "Data updated successfully"}

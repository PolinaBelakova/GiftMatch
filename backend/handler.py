from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from usecase import list_products, add_product, get_product, change_product_price, remove_product

router = APIRouter()

class ProductCreate(BaseModel):
    title: str
    price: float

class ProductPriceUpdate(BaseModel):
    price: float


@router.get("/products")
async def get_all_products():
    products = await list_products()

    result = []

    for product in products:
        result.append(dict(product))

    return result

@router.post("/products")
async def create_new_product(product: ProductCreate):
    await add_product(product.title, product.price)
    return {"message": "Товар добавлен"}


@router.get("/products/{product_id}")
async def get_one_product(product_id: int):
    try:
        product = await get_product(product_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Товар не найден")

    return dict(product)

@router.patch("/products/{product_id}")
async def update_product_price(product_id: int, data: ProductPriceUpdate):
    try:
        await change_product_price(product_id, data.price)
    except ValueError as error:
        if str(error) == "Товар не найден":
            raise HTTPException(status_code=404, detail=str(error))
        raise HTTPException(status_code=400, detail=str(error))

    return {"message": "Цена товара обновлена"}

@router.delete("/products/{product_id}")
async def delete_one_product(product_id: int):
    try:
        await remove_product(product_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

    return {"message": "Товар удалён"}
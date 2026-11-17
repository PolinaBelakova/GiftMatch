from storage import create_product, get_products, get_product_by_id, update_product, delete_product

async def add_product(title, price):
    if price <= 0:
        raise ValueError("Цена должна быть больше нуля")

    await create_product(title, price)

async def list_products():
    products = await get_products()
    return products

async def get_product(product_id):
    product = await get_product_by_id(product_id)

    if product is None:
        raise ValueError("Товар не найден")

    return product

async def change_product_price(product_id, price):
    if price <= 0:
        raise ValueError("Цена должна быть больше нуля")

    result = await update_product(product_id, price)

    if result == "UPDATE 0":
        raise ValueError("Товар не найден")

async def remove_product(product_id):
    result = await delete_product(product_id)

    if result == "DELETE 0":
        raise ValueError("Товар не найден")
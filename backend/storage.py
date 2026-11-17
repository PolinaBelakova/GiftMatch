import asyncpg, asyncio
from config import DATABASE_URL
async def connect_db():
    connection = await asyncpg.connect(DATABASE_URL)
    await connection.close()

async def get_products():
    connection = await asyncpg.connect(DATABASE_URL)

    products = await connection.fetch(
        "SELECT * FROM products"
    )

    await connection.close()
    return products

async def create_product(title, price):
    connection = await asyncpg.connect(DATABASE_URL)

    await connection.execute(
        "INSERT INTO products (title, price) VALUES ($1, $2)",
        title,
        price
    )

    await connection.close()

async def get_product_by_id(product_id):
    connection = await asyncpg.connect(DATABASE_URL)

    product = await connection.fetchrow(
        "SELECT * FROM products WHERE id = $1",
        product_id
    )

    await connection.close()
    return product

async def update_product(product_id, price):
    connection = await asyncpg.connect(DATABASE_URL)

    result = await connection.execute(
        "UPDATE products SET price = $1 WHERE id = $2",
        price, product_id
    )

    await connection.close()
    return result

async def delete_product(product_id):
    connection = await asyncpg.connect(DATABASE_URL)

    result = await connection.execute(
        "DELETE FROM products WHERE id = $1",
        product_id
    )

    await connection.close()

    return result
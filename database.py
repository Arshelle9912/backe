import asyncpg

DATABASE_URL = "postgresql+asyncpg://data_qqmk_user:mToW3AQnlj1cCoUWeHvmKbGyl21qoXBU@dpg-cq607hl6l47c738scgag-a.oregon-postgres.render.com/data_qqmk"

async def get_async_db():
    # Connect to PostgreSQL database asynchronously
    connection = await asyncpg.connect(DATABASE_URL)
    try:
        yield connection
    finally:
        await connection.close()

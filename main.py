import os
from fastapi import FastAPI, Path
from dotenv import load_dotenv
from src.api.queries import (
    get_average_revenue,
    get_last_transactions,
    get_transactions_count,
    get_average_price_per_square_meter,
    get_transactions_count_by_criteria,
    get_transactions_by_pieces,
    get_average_price_per_square_meter_by_city,
    get_transactions_by_department,
    get_transactions_count_by_revenue_and_type,
    get_top_10_cities_by_transactions,
    get_top_10_cities_by_price,
)

load_dotenv()
DB_PATH = os.getenv("DB_PATH")
app = FastAPI()


# User story 1
@app.get("/average_revenue/{city}")
async def average_revenue(city: str = Path(description="Ville")):
    return get_average_revenue(DB_PATH, city)


# User story 2
@app.get("/last_transactions/{city}_last_{number}")
async def last_transactions(city: str, number: int):
    return get_last_transactions(DB_PATH, city, number)


# User story 3
@app.get("/transactions_count/{city}_{year}")
async def transactions_count(city: str, year: str):
    return get_transactions_count(DB_PATH, city, year)


# User story 4
@app.get("/average_price_per_square_meter/{year}_{type}")
async def average_price_per_square_meter(year: str, type: str):
    return get_average_price_per_square_meter(DB_PATH, year, type)


# User story 5
@app.get("/transactions_count2/{city}_{year}_{type}_{rooms}")
async def transactions_count2(city: str, year: str, type: str, rooms: int):
    return get_transactions_count_by_criteria(DB_PATH, city, year, type, rooms)


# User story 6
@app.get("/transactions_by_pieces/{city}_{year}_{type}")
async def transactions_by_pieces(city: str, year: str, type: str):
    return get_transactions_by_pieces(DB_PATH, city, year, type)


# User story 7
@app.get("/average_price_per_square_meter2/{city}_{year}_{type}")
async def average_price_per_square_meter2(city: str, year: str, type: str):
    return get_average_price_per_square_meter_by_city(DB_PATH, city, year, type)


# User story 8
@app.get("/transactions_by_dpt/")
async def transactions_by_dpt():
    return get_transactions_by_department(DB_PATH)


# User story 9
@app.get("/transactions_count3/{year1}_{revenu}_{year2}_{type}")
async def transactions_count3(year1: str, revenu: int, year2: str, type: str):
    return get_transactions_count_by_revenue_and_type(
        DB_PATH, year1, revenu, year2, type
    )


# User story 10
@app.get("/cities_top10_transactions/")
async def cities_top10():
    return get_top_10_cities_by_transactions(DB_PATH)


# User stories 11 & 12
@app.get("/cities_top10_price/{type}")
async def cities_top10_price(type: str):
    return get_top_10_cities_by_price(DB_PATH, type)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

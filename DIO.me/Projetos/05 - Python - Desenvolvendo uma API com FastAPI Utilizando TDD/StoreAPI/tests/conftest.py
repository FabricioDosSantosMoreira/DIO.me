import asyncio
from typing import List
from uuid import UUID

import pytest
from httpx import ASGITransport, AsyncClient
from store.database.mongo import db_client
from store.main import app
from store.schemas.product import ProductCreateIn, ProductOut, ProductUpdateIn
from store.usecases.product import product_usecase

from tests.factories import product_data, products_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()

    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collection_names = await mongo_client.database.list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue

        # await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in() -> ProductCreateIn:

    product = ProductCreateIn(**product_data())
    return product


@pytest.fixture
def products_in() -> List[ProductCreateIn]:
    return [ProductCreateIn(**product) for product in products_data()]


@pytest.fixture
def product_up(product_id) -> ProductUpdateIn:
    return ProductUpdateIn(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in) -> ProductOut:
    return await product_usecase.create(body=product_in)


@pytest.fixture
async def products_inserted(products_in) -> List[ProductOut]:
    return [await product_usecase.create(body=product_in) for product_in in products_in]

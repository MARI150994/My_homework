from fastapi import FastAPI, Body, Path, Query, HTTPException
from .scheme import ProductCreate, LIST_OF_PRODUCT, update_list_of_product

app = FastAPI()


@app.get('/')
def home():
    return {'list of products': LIST_OF_PRODUCT}


@app.get('/search')
def search_product_by_name(name: str = Query(..., description='search product')):
    for k, i in LIST_OF_PRODUCT.items():
        if name == i['name']:
            return {'message': f'name: {name}, prodict_id: {k}'}


@app.get('/ping')
def pong():
    return {'message': 'pong'}


@app.post('/create')
def create_product(data: ProductCreate = Body(..., description='Create product')):
    new_product = update_list_of_product(data)
    return {'message': f'create new product {new_product}'}


@app.get('/{product_id}')
def get_product_by_id(product_id: int = Path(..., description='Enter id of product')):
    if product_id not in LIST_OF_PRODUCT:
        raise HTTPException(status_code=422, detail=f'id {product_id} is not exist')
    else:
        return {'message':
                    f'prodict_id: {product_id}; name: {LIST_OF_PRODUCT[product_id]["name"]}; price: {LIST_OF_PRODUCT[product_id]["price"]}'
                }

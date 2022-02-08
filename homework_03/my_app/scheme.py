from pydantic import BaseModel, Field, validator
from typing import Optional


LIST_OF_PRODUCT = {1: {'name': 'bananas', 'price': 70},
                   2: {'name': 'apples', 'price': 100},
                   3: {'name': 'potatoes', 'price': 50},
                   4: {'name': 'milk', 'price': 80},
                   5: {'name': 'beef', 'price': 600},
                   6: {'name': 'chicken', 'price': 300},
                   7: {'name': 'pork', 'price': 450},
                   8: {'name': 'bread', 'price': 60},
                   9: {'name': 'sweets', 'price': 80}
                   }


def update_list_of_product(product):
    id = len(LIST_OF_PRODUCT) + 1
    LIST_OF_PRODUCT.update({id: {'name': product.name, 'price': product.price}})
    print(LIST_OF_PRODUCT)
    return {'id': max(LIST_OF_PRODUCT), 'info': LIST_OF_PRODUCT[id]}

class ProductCreate(BaseModel):
    name: str = Field(max_length=15, min_length=4)
    price: int = Field(ge=10)

    @validator('name')
    def check_name(cls, name):
        if len(name) > 15:
            raise ValueError(f'length of name {name} must be less 15')
        return name
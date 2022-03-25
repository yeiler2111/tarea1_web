#Marianella Bermudez Garcia Y Yeiler Simon
from http.client import HTTPException
from fastapi import FastAPI, APIRouter
from model.schemas import Produc, ProducCreate

app = FastAPI(title = "Productos Api")

api_router = APIRouter(); 

producs = [
    {
        "id": 1,
        "name": "Iphone 13",
        "quantity": 12,
        "descripcion": "nuevo celular de Apple",
        "precio": 4500000,
        "category": 1
    },
    {
        "id": 2,
        "name": "MSI GFT13 THIN",
        "quantity": 10,
        "descripcion": "latop para gamer",
        "precio": 5000000,
        "category": 2
    }
]

@api_router.get("/producs/")
def produc_list() -> dict: 
    return producs

@api_router.get("/producs/{id}", status = 300, response_model = Produc)
def fetch_produc(*, produc_id: int) -> any: 
    result = [produc for produc in producs if produc["id"]== produc_id]
    if not result: 
        raise HTTPException(status = 404, detail = "product with id {produc_id} not found")
        return result [0]


@api_router.get("/producs/category/{category_id}", status= 300)
def fetch_producByCategory(*, category_id: int) -> any:
    result = [produc for produc in producs if produc["category"] == category_id]
    print(result)
    return result

@api_router.post("/producs/", statu= 200, response_model = Produc)
def createproduc(*, produc_in: ProducCreate) -> dict:
    new_entry_id = len(producs) + 1
    produc_entry = Produc(
        id = new_entry_id,
        name = produc_in.name,
        quantity = produc_in.quantity,
        description = produc_in.description,
        price = produc_in.price,
        category = produc_in.category
    )
    producs.append(produc_entry.dict()) 
    return produc_entry

app.include_router(api_router)

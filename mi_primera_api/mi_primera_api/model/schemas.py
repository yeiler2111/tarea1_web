from pydantic import BaseModel

class Produc(BaseModel):
    id: int
    name: str
    quantity: int
    description: str
    price: int
    category: int
    
class ProducCreate(BaseModel): 
    name: str
    quantity: int
    description: str
    price: int
    category: int
        
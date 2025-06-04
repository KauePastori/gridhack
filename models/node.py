# models/node.py

from pydantic import BaseModel

class Node(BaseModel):
    id: int
    name: str
    status: str  # "OK" ou "Falha"

from pydantic import BaseModel


class OctagonBase(BaseModel):
    name: str
    imagen: str

class OctagonCreate(OctagonBase):
    name: str
    imagen: str

class OctagonResponse(OctagonBase):
    id: int
    name: str
    imagen:str

    class Config:
        from_attributes = True


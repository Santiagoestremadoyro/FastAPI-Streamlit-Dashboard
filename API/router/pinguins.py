from fastapi import APIRouter
from mongo.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def res(result):
    return loads(json_util.dumps(result))

#test para llamar a todos los pinguinos
@router.get("/all/pinguins")
def get_pinguins():
    result = db["pinguinos"].find({})
    return loads(json_util.dumps(result))


#separar pinguinos por sexo
@router.get("/pinguins/sex/{sex}")
def penguins_by_sex(sex: str):
    result = []
    for penguin in db["pinguinos"].find({"sex": sex}):
        result.append(penguin)
    return res(result)


#separar pinguinos por especies
@router.get("/pinguins/species/{species}")
def penguins_by_species(species: str):
    result = []
    for penguin in db["pinguinos"].find({"species": species}):
        result.append(penguin)
    return res(result)

#separar pinguinos por islas de donde provienen
@router.get("/pinguins/island/{island}")
def penguins_by_island(island: str):
    result = []
    for penguin in db["pinguinos"].find({"island": island}):
        result.append(penguin)
    return res(result)
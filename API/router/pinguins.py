from fastapi import APIRouter
from mongo.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def res(result):
    return loads(json_util.dumps(result))


@router.get("/all/pinguins")
def get_pinguins():
    result = db["pinguinos"].aggregate([
        {"$match":{"sex": {"$ne":None}}},
        {"$group": {"_id": "$sex", "count": {"$sum": 1}}}
    ])
    return res(result)

@router.get("/all/pinguins/specie")
def get_pinguins_s():
    result = db["pinguinos"].aggregate([
        {"$match":{"species": {"$ne":None}}},
        {"$group": {"_id": "$species", "count": {"$sum": 1}}}
    ])
    return res(result)

@router.get("/all/pinguins/islan")
def get_pinguins_i():
    result = db["pinguinos"].aggregate([
        {"$match":{"island": {"$ne":None}}},
        {"$group": {"_id": "$island", "count": {"$sum": 1}}}
    ])
    return res(result)


@router.get("/id/{number}/{group}")
def get_data(number, group=0):
    group = int(group)
    project = {"_id":0}
    filter = {"number": int(number)}
    result = list(db["penguin"].find(filter, project)[group:(group+1)])
    if len(result)==0:
        return {"the id of this penguin is wrong or does not exit"}
    return res(result)

@router.get("/info/{number}/{group}")
def stats(number, group=0):
    group = int(group)
    project = {"Culmen Length (mm)":1, "Culmen Depth (mm)":1, "Flipper Length (mm)":1, "Body Mass (g)":1, "_id":0}
    filter = {"number": int(number)}
    results = list(db["penguin"].find(filter, project)[group:(group+1)])
    return res(results)



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
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from models import DepositModel
from bson import ObjectId
from typing import List

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

# Utility function to convert MongoDB documents to Pydantic format
def deposit_helper(deposit) -> dict:
    return {
        "id": str(deposit["_id"]),
        "age": deposit["age"],
        "job": deposit["job"],
        "marital": deposit["marital"],
        "education": deposit["education"],
        "default": deposit["default"],
        "balance": deposit["balance"],
        "housing": deposit["housing"],
        "loan": deposit["loan"],
        "contact": deposit["contact"],
        "day": deposit["day"],
        "month": deposit["month"],
        "duration": deposit["duration"],
        "campaign": deposit["campaign"],
        "pdays": deposit["pdays"],
        "previous": deposit["previous"],
        "poutcome": deposit["poutcome"],
        "deposit": deposit["deposit"]
    }

# Create deposit
@app.post("/deposits/", response_description="Deposit data added to the database")
async def create_deposit(deposit: DepositModel):
    deposit_dict = deposit.dict()
    result = await db[COLLECTION_NAME].insert_one(deposit_dict)
    new_deposit = await db[COLLECTION_NAME].find_one({"_id": result.inserted_id})
    return deposit_helper(new_deposit)

# Get all deposits
@app.get("/deposits/", response_description="List all deposits", response_model=List[DepositModel])
async def list_deposits():
    deposits = []
    async for deposit in db[COLLECTION_NAME].find():
        deposits.append(deposit_helper(deposit))
    return deposits

# Get deposit by ID
@app.get("/deposits/{id}", response_description="Get a single deposit")
async def get_deposit(id: str):
    deposit = await db[COLLECTION_NAME].find_one({"_id": ObjectId(id)})
    if deposit:
        return deposit_helper(deposit)
    raise HTTPException(status_code=404, detail=f"Deposit {id} not found")

# Update deposit
@app.put("/deposits/{id}", response_description="Update a deposit")
async def update_deposit(id: str, deposit: DepositModel):
    update_result = await db[COLLECTION_NAME].update_one(
        {"_id": ObjectId(id)}, {"$set": deposit.dict()}
    )
    if update_result.modified_count == 1:
        updated_deposit = await db[COLLECTION_NAME].find_one({"_id": ObjectId(id)})
        if updated_deposit:
            return deposit_helper(updated_deposit)
    raise HTTPException(status_code=404, detail=f"Deposit {id} not found")

# Delete deposit
@app.delete("/deposits/{id}", response_description="Delete a deposit")
async def delete_deposit(id: str):
    delete_result = await db[COLLECTION_NAME].delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Deposit deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Deposit {id} not found")

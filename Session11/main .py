from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas import ParkingSlotCreate
from user_service import create_slot, get_all_slots, get_slot

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/parking-slots", status_code=201)
def create(item: ParkingSlotCreate, db: Session = Depends(get_db)):
    return create_slot(item, db)

@app.get("/parking-slots")
def get_all(db: Session = Depends(get_db)):
    return get_all_slots(db)

@app.get("/parking-slots/{slot_id}")
def get_one(slot_id: int, db: Session = Depends(get_db)):
    return get_slot(slot_id, db)
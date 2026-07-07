from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from models import ParkingSlotModel
from schemas import ParkingSlotCreate

def create_slot(item: ParkingSlotCreate, db: Session):

    slot = db.query(ParkingSlotModel).filter(
        ParkingSlotModel.slot_code == item.slot_code
    ).first()

    if slot:
        raise HTTPException(
            status_code=400,
            detail="Slot code đã tồn tại"
        )

    new_slot = ParkingSlotModel(
        slot_code=item.slot_code,
        zone_name=item.zone_name,
        max_weight=item.max_weight
    )

    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)

    return {
        "statusCode": 201,
        "message": "Thêm vị trí đỗ xe thành công",
        "error": None,
        "data": new_slot,
        "path": "/parking-slots",
        "timestamp": datetime.now()
    }

def get_all_slots(db: Session):

    slots = db.query(ParkingSlotModel).all()

    return {
        "statusCode": 200,
        "message": "Lấy danh sách thành công",
        "error": None,
        "data": slots,
        "path": "/parking-slots",
        "timestamp": datetime.now()
    }

def get_slot(slot_id: int, db: Session):

    slot = db.query(ParkingSlotModel).filter(
        ParkingSlotModel.id == slot_id
    ).first()

    if slot is None:
        raise HTTPException(
            status_code=404,
            detail="Parking slot not found"
        )

    return {
        "statusCode": 200,
        "message": "Lấy chi tiết thành công",
        "error": None,
        "data": slot,
        "path": f"/parking-slots/{slot_id}",
        "timestamp": datetime.now()
    }
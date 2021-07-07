from sqlalchemy.orm import Session

import model, schema


def get_user_address(db: Session, add_id: int):
    return db.query(model.Address).filter(model.Address.address_id == add_id).first()


def get_user_addresses(db: Session):
    return db.query(model.Address).all()


def create_user_addrres(db: Session, add: schema.address):
    db_add = model.Address(**add.dict())
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add


def update_user_address(db: Session, add_id: int, add: schema.address):
    db.query(model.Address).filter(model.Address.address_id == add_id).update(vars(add))
    db.commit()
    return "Success"

# async def delete_user_address(db: Session, add_id: int):
#     db_delete_add = db.query(model.Address).filter(model.Address.address_id == add_id).delete()
#     await db.execute(db_delete_add)
#     return db_delete_add

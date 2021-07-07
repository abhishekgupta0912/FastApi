import uvicorn
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, model, schema
from db import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.address)
def create_user(user: schema.address, db: Session = Depends(get_db)):
    # db_user = crud.get_user_address(db, add_id=user.add_id)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Address already registered")
    return crud.create_user_addrres(db=db, add=user)


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = crud.get_user_addresses(db)
    return users


@app.get("/users/{user_id}", response_model=List[schema.address])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_address(db, add_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/{add_id}")
async def update_address_for_user(add_id: int, add: schema.address, db: Session = Depends(get_db)):
    response = crud.update_user_address(db=db, add_id=add_id, add=add)
    if response == "Success":
        return {"Data Updated"}


@app.delete("/users/{add_id}")
async def delete_address_for_user(add_id: int, db: Session = Depends(get_db)):
    db.query(model.Address).filter(model.Address.address_id == add_id).delete()
    db.commit()
    return {"Data Deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

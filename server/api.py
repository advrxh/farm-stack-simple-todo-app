import fastapi
from fastapi.middleware.cors import CORSMiddleware

from DbHandler import Handler


app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


handler = Handler("todo-app")


@app.get("/item")
async def get_item(_id: str = None):

    if _id is None:
        items = handler.getItems()
        return fastapi.responses.JSONResponse(status_code=200, content=items)

    else:
        items = handler.getItem(_id=_id)
        return fastapi.responses.JSONResponse(status_code=200, content=items)


@app.put("/item")
async def add_item(desc: str = ""):

    _item = handler.addItem(description=desc)

    if _item:
        return fastapi.responses.JSONResponse(status_code=201, content={"item_key": _item})

    else:
        return fastapi.exceptions.HTTPException(status_code=fastapi.status.HTTP_417_EXPECTATION_FAILED, detail="add_item_failed")


@app.delete("/item")
async def delete_item(_id: str = None):

    del_ = handler.deleteItem(_id)

    if del_:
        return fastapi.responses.JSONResponse(status_code=200, content={"msg": "delete_ok"})
    else:
        return fastapi.exceptions.HTTPException(status_code=417, detail="delete_fail")


@app.post("/item")
async def update(_id: str = None, status: str = "pending", desc: str = None):

    update = handler.update(desc=desc, status=status, _id=_id)

    if update:
        return fastapi.responses.JSONResponse(status_code=200, content={"msg": "update_ok"})

    return fastapi.exceptions.HTTPException(status_code=417, detail={"msg": "update_fail"})

from fastapi import FastAPI, APIRouter
from items.api import router as items_router
from subitems.api import router as subitems_router

app = FastAPI()


# items_router = APIRouter()

@items_router.get("/", tags=["items"])
async def read_items():
    return {"message": "Read items"}

app.include_router(items_router, prefix="/api/items", tags=["items"])
app.include_router(subitems_router, prefix="/api/subitems", tags=["subitems"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

# main.py

from fastapi import FastAPI
from routes.item import router as item_router
from routes.user import router as user_router

app = FastAPI()

# Include item and user routes
app.include_router(item_router, prefix="/api")
app.include_router(user_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

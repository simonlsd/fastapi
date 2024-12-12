from fastapi import FastAPI
from .routers import router
from .database import Base,engine

# Initialize FastAPI
app = FastAPI()

# Initialize
Base.metadata.create_all(bind=engine)

#Register Router
app.include_router(router=router, prefix="/api", tags=["todos"])

from fastapi import FastAPI
from routes import router # Import the APIRouter() from file router

app = FastAPI() # Start the app

app.include_router(router) # Include router in the app

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.v1.router.auth_router import router as auth_router
from app.v1.router.router import router as test_router
from app.v1.router.websock_server import router as websock_server_router



app = FastAPI(title="FastAPI - HEROKU", version="1.0.0", openapi_url="/api/v1/openapi.json", docs_url=None, redoc_url="/redoc")


origins = [
    "http://localhost",
    "http://localhost:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Routers
app.include_router(auth_router)
app.include_router(test_router)
app.include_router(websock_server_router)


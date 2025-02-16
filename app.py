from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from src.routers.producer import router as router_producer
from src.routers.property import router as router_property
from src.routers.crop import router as router_crop

load_dotenv()
app = FastAPI()


# -------------------Configurção da documentação openapi swagger/redoc-------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Brain Agriculture",
        version="1.0",
        summary="APIs para acessar e inserir dados do banco de dados PostgreSQL",
        description="Este conjunto de APIs fornece acesso aos dados armazenados no banco de dados PostgreSQL.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
# --------------------------------Configurção de CORS--------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------Inclusão das rotas--------------------------------
app.include_router(router_producer)
app.include_router(router_property)
app.include_router(router_crop)

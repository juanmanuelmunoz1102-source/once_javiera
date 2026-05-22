from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/")
def inicio(request: Request):

    return templates.TemplateResponse(
        "inicio.html",
        {
            "request": request
        }
    )



@app.get("/numero/{n}")
def numero(request: Request, n: int):

    # positivo, negativo o cero
    if n > 0:
        tipo = "Positivo"

    if n < 0:
        tipo = "Negativo"

    if n == 0:
        tipo = "Cero"

    # par o impar
    if n % 2 == 0:
        paridad = "Par"

    if n % 2 != 0:
        paridad = "Impar"

    return templates.TemplateResponse(
        "numero.html",
        {
            "request": request,
            "numero": n,
            "tipo": tipo,
            "paridad": paridad
        }
    )



@app.get("/productos")
def productos(request: Request):

    lista_productos = [
        {"nombre": "Laptop", "precio": 3500, "stock": 5},
        {"nombre": "Mouse", "precio": 80, "stock": 0},
        {"nombre": "Teclado", "precio": 150, "stock": 7},
        {"nombre": "Monitor", "precio": 900, "stock": 0},
        {"nombre": "USB", "precio": 40, "stock": 12},
        {"nombre": "Audífonos", "precio": 200, "stock": 3}
    ]

    return templates.TemplateResponse(
        "productos.html",
        {
            "request": request,
            "productos": lista_productos
        }
    )


@app.get("/servicios")
def servicios(request: Request):

    lista_servicios = [
        {"nombre": "Hosting", "activo": True},
        {"nombre": "Base de Datos", "activo": False},
        {"nombre": "Correo Empresarial", "activo": True},
        {"nombre": "Soporte Técnico", "activo": True},
        {"nombre": "VPN", "activo": False}
    ]

    return templates.TemplateResponse(
        "servicios.html",
        {
            "request": request,
            "servicios": lista_servicios
        }
    )

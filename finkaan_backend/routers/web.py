from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates
import os

current_dir = os.path.dirname(os.path.relpath(__file__))
templates_path = os.path.join(current_dir,"..","templates")

router = APIRouter(tags=['web'],
                   responses={status.HTTP_404_NOT_FOUND: {"menssga": "No encontrado"}}
)

templates = Jinja2Templates(directory=templates_path)

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html", context={})
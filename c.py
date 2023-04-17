from fastapi import *
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()

t=Jinja2Templates(directory='templates')

@app.get('/',response_class=HTMLResponse)
def a(request:Request):
    return t.TemplateResponse('a.html',{"request":request})

@app.get('/aboutus',response_class=HTMLResponse)
def b(request:Request):
    return t.TemplateResponse('about.html',{'request':request})
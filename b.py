# Templates in FastAPI.

# Fastapi doesn't have any default template engine. so, we need to install jinja2

from fastapi import *
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # Rendering the Jinga2Tempaltes from fastapi

app=FastAPI()

template=Jinja2Templates(directory='templates')  # Connecting the templates directory to Jinga2.

@app.get('/',response_class=HTMLResponse)
def a(request:Request):
    return template.TemplateResponse('index.html',{"request":request})


@app.get('/about',response_class=HTMLResponse)
def b(request:Request):
    content= """
    <html>
    <head>
    </head>
    <body>
    <h1> Welcome to About us Page </h1>
    </body>
    </html>
    
    """
    return HTMLResponse(content=content)

from starlette.responses import HTMLResponse
from client import html
from fastapi import WebSocket
from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, post
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)


@app.get('/hello')
def index():
    return {'message': 'Hello world!'}


# websocket
@app.get("/websocket")
def get():
    return HTMLResponse(html)


clients = []


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

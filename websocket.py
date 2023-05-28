#from starlette.responses import HTMLResponse
#from client import html
#from fastapi import WebSocket

#from main import app


#@app.get("/")
#async def get():
#    return HTMLResponse(html)


#clients = []


#@app.websocket("/chat")
#async def websocket_endpoint(websocket: WebSocket):
#    await websocket.accept()
#    while True:
#        data = await websocket.receive_text()
#        for client in clients:
#            await client.send_text(data)

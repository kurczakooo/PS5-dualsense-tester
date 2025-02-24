from fastapi import FastAPI, WebSocket

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)
        
@app.get("/")
async def root():
    return {"message": "DualSense WebSocket API is running"}        

async def send_event(event: str):
    for client in clients:
        await client.send_json({"event":event})
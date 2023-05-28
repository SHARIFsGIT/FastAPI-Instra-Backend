html = """
<!DOCTYPE html>
<html>
     <head>
         <title>Chat</title>
     </head>
     <body>
         <h2>ROBOKUDO WebSocket</h2>
         <form action="" onsubmit="sendMessage(event)">
             <input type="text" id="messageText" autocomplete="off"/>
             <button>Send</button>
         </form>
         <ul id='messages'>
         </ul>
         <script>
             var ws = new WebSocket("ws://localhost:8000/chat");
             ws.onmessage = function(event) {
                 var messages = document.getElementById('messages')
                 var message = document.createElement('li')
                 var content = document.createTextNode(event.data)
                 message.appendChild(content)
                 messages.appendChild(message)
             };
             function sendMessage(event) {
                 var input = document.getElementById("messageText")
                 ws.send(input.value)
                 input.value = ''
                 event.preventDefault()
             }
         </script>
     </body>
     </html>
"""

#import websockets
#import asyncio
#import cv2
#import numpy as np

#camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


#async def main():
#    url = 'ws://127.0.0.1:8000/ws'

#    async with websockets.connect(url) as ws:
        # count = 1
#        while True:
#            contents = await ws.recv()
#            arr = np.frombuffer(contents, np.uint8)
#            frame = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
#            cv2.imshow('frame', frame)
#            cv2.waitKey(1)

            # cv2.imwrite("frame%d.jpg" % count, frame)
            # count += 1


#asyncio.run(main())


#def html():
#    return None
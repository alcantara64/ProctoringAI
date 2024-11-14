from eye_tracker import track_eye
from head_pose_estimation import detect_head_pose
from mouth_opening_detector import mouth_opening_detector
from person_and_phone import detect_phone_and_person
from multiprocessing import Process
import asyncio
import websockets

from utilities import send_videos_to_backend

async def handle_connection(websocket, path):
    print("New WebSocket connection established")
    try:
        while True:
            message = await websocket.recv()
            print(f"Message from client: {message}")

            response = f"Echo: {message}"
            await websocket.send(response)
    except websockets.ConnectionClosed:
        print("WebSocket connection closed")

async def websocket_server():
    async with websockets.serve(handle_connection, "localhost", 8000):
        print("WebSocket server is running on ws://localhost:8000")
        await asyncio.Future()  # Keep server running

def start_websocket_server():
    asyncio.run(websocket_server())


if __name__ == '__main__':
    # p1 = Process(target=track_eye, args=(0,))
    # p2 = Process(target=detect_head_pose, args=(0,))
    # p3 = Process(target=mouth_opening_detector, args=(0,))
    p4 = Process(target=detect_phone_and_person, args=(0,))
    p5 = Process(target=send_videos_to_backend, args=('./recordings',"https://phpstack-1245936-4719805.cloudwaysapps.com/backend/api/v1/candidate/exam/proctor-assets",{'candidate_id': '444444444444test', 'ip_address':'192.168.92.1'}))
    websocket_process = Process(target=start_websocket_server)
    # p1.start()
    # p2.start()
    # p3.start()
    p4.start()
   # p5.start()
    websocket_process.start()

    # p1.join()
    # p2.join()
    # p3.join()
    p4.join()
    # p5.join()
    websocket_process.join()
   
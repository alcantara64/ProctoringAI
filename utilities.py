import cv2
import os
from datetime import datetime
import requests

def record_video(cap, output_folder='recordings', base_filename='output', duration=10, fps=20, frame_width=640, frame_height=480):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{base_filename}_{timestamp}.mp4"
    # Define the full path for the video file
    output_path = os.path.join(output_folder, file_name)
    
    # Open the webcam (0 for the default webcam)
    # cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Frame size: {frame_width}x{frame_height}")
    
    if not out.isOpened():
       print("Error: VideoWriter could not be opened.")
       cap.release()
       return
    
    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return
    
    print(f"Recording video. Press 'q' to stop manually or wait {duration} seconds.")
    
    # Get the starting time
    start_time = cv2.getTickCount()

    # Record video until the user presses 'q' or the duration is reached
    while cap.isOpened:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture video.")
            break
        
        # Write the frame to the output video
        out.write(frame)
        
        # todo remove this line 
        # Display the frame
        cv2.imshow('Recording', frame)
        
        # Check if duration is reached (duration is in seconds)
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if elapsed_time >= duration:
            break

    # Release everything
    out.release()
    cv2.destroyAllWindows()

    print(f"Video saved to: {output_path}")


def send_videos_to_backend(folder_path, backend_url, extra_fields=None):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi'))]
    data = extra_fields if extra_fields else {}
    if not files:
        print("No video files found in the folder.")
        return

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'rb') as f:
                # Send a POST request with the video file
                response = requests.post(backend_url, files={'assets': f}, data=data)
                
                # Check the response status
                if response.status_code == 200:
                    print(f"Successfully sent {file_name} to the backend.")
                    try:
                       os.remove(file_path)
                       print(f"File '{file_path}' deleted from local storage.")
                    except OSError:
                        pass
                else:
                    print(f"Failed to send {file_name}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending {file_name}: {e}")



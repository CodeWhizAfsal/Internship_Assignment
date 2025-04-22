import cv2
import os

# Path to the input video file
video_path = '/home/afsal/Downloads/IMG_2790.MOV'  # Your video file path

# Path to save extracted frames
output_dir = os.path.expanduser('~/orbslam3_project/frames')  # Updated output directory

# Create frames directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Save the frame as a PNG image
    frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
    cv2.imwrite(frame_filename, frame)
    print(f"Extracted {frame_filename}")
    
    frame_count += 1

# Release video capture object
cap.release()
print(f"Frames extraction complete! {frame_count} frames saved to {output_dir}.")

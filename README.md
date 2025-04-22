text
# Monocular Visual SLAM for Robot Localization and 3D Mapping

This project implements a Monocular Visual SLAM pipeline to localize a robot's position, generate a 3D point cloud of the environment, and visualize the robot's pose within the generated map. Uses **ORB-SLAM3** for feature-based localization with **Open3D** and **CloudCompare** for visualization.

![SLAM Pipeline](https://example.com/slam-pipeline.jpg) <!-- Add actual image path -->

## Table of Contents
- [Project Overview](#project-overview)
- [Dependencies](#dependencies)
- [Setup Instructions](#setup-instructions)
- [File Structure](#file-structure)
- [Execution](#execution)
- [Pose Localization](#pose-localization-in-point-cloud)
- [Assumptions](#assumptions)
- [License](#license)

## Project Overview
Processes monocular video input to:
1. Extract video frames
2. Run ORB-SLAM3 for pose estimation
3. Generate 3D environment point cloud
4. Visualize robot trajectory in 3D map

Output:  
✅ 3D Point Cloud (.ply)  
✅ Robot Trajectory Data (.txt)  
✅ Pose Visualization in 3D Map

## Dependencies

### Core Requirements
- Python 3.8+
- OpenCV 4.5+
- ORB-SLAM3 (built from source)
- Open3D 0.15+
- CloudCompare (optional)

### Python Packages
pip install opencv-python opencv-contrib-python open3d numpy

text

### ORB-SLAM3 Setup
1. Clone official repository:
git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git

text
2. Follow build instructions in ORB-SLAM3 documentation

## Setup Instructions
1. Clone this repository:
git clone https://github.com/yourusername/Internship_Assignment.git
cd Internship_Assignment

text
2. Install requirements:
pip install -r requirements.txt

text
3. Place input video in project root (rename to `video_input.mp4`)

## File Structure
Internship_Assignment/
├── frames/ # Extracted video frames
├── results/ # Output files
│ ├── trajectory.ply # 3D point cloud
│ └── KeyFrameTrajectory.txt # Pose data
├── config/
│ └── mono_camera.yaml # Camera calibration
├── video_input.mp4 # Input video
└── scripts/ # Core functionality scripts

text

## Execution

### 1. Extract Video Frames
python extract_frames.py
--video_path video_input.mp4
--output_folder frames/

text

### 2. Run SLAM Pipeline
python run_slam.py
--frame_folder frames/
--config_path config/mono_camera.yaml

text

### 3. Generate Point Cloud
python save_point_cloud.py
--slam_output results/
--output_ply trajectory.ply

text

### 4. Visualize Results
- Open `trajectory.ply` in CloudCompare
- Use Open3D for interactive visualization:
import open3d as o3d
pcd = o3d.io.read_point_cloud("results/trajectory.ply")
o3d.visualization.draw_geometries([pcd])

text

## Pose Localization in Point Cloud
Visualize robot trajectory in generated 3D map:
python localization.py
--point_cloud_file results/trajectory.ply
--pose_file results/KeyFrameTrajectory.txt

text

## Assumptions
1. Monocular camera input with known calibration parameters
2. Video contains sufficient texture for feature matching
3. Camera operates at 30 FPS (adjustable in config)
4. Environment has static lighting conditions
5. No sudden camera motions (>30° rotation/frame)

## License
MIT License - See [LICENSE](LICENSE) for details.
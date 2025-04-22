# Monocular Visual SLAM - Internship Assignment

## Overview
This project implements a Monocular Visual SLAM (Simultaneous Localization and Mapping) pipeline using **ORB-SLAM3** to:
1. **Localize a robot's position** based on monocular video input.
2. **Generate a 3D map** of the environment.
3. **Estimate the robot's pose** in the generated point cloud or 3D map.

The project involves using OpenCV for image processing, ORB-SLAM3 for SLAM, and CloudCompare for point cloud visualization.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Scripts](#scripts)
  - [Extract Frames](#extract-frames)
  - [Run SLAM](#run-slam)
  - [Localization](#localization)
  - [Save Point Cloud](#save-point-cloud)
- [Visualization](#visualization)
- [License](#license)

---

## Prerequisites
Before running the project, make sure you have the following:
1. **ORB-SLAM3** installed. Follow the official [ORB-SLAM3 installation guide](https://github.com/UZ-SLAMLab/ORB_SLAM3).
2. **OpenCV** installed for image processing and frame handling.
3. **CloudCompare** for visualizing the generated point cloud.

### Dependencies
This project uses the following Python dependencies:
- `opencv-python` (for video handling and frame extraction)
- `numpy` (for array manipulation)
- `ORB-SLAM3` (for SLAM and pose estimation)

To install the Python dependencies, run:
```bash
pip install -r requirements.txt

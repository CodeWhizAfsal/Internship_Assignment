import os
import subprocess
import glob

# Paths to ORB-SLAM3 components
orbslam_exec_path = "/home/afsal/LastMile/ORB_SLAM3/Examples/Monocular/mono_tum"
vocab_path = "/home/afsal/LastMile/ORB_SLAM3/Vocabulary/ORBvoc.txt"
config_path = "/home/afsal/orbslam3_project/camera.yaml" # You should place the camera config here

# Path to video frames (already extracted)
frames_dir = os.path.expanduser("~/orbslam3_project/frames")

def run_orbslam():
    # Validate paths
    if not os.path.isfile(orbslam_exec_path):
        raise FileNotFoundError(f"ORB-SLAM3 binary not found at {orbslam_exec_path}")
    if not os.path.isfile(vocab_path):
        raise FileNotFoundError(f"Vocabulary file not found at {vocab_path}")
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Camera configuration file not found at {config_path}")
    if not os.path.isdir(frames_dir):
        raise FileNotFoundError(f"Frames directory not found at {frames_dir}")

    # Generate rgb.txt in TUM format
    print("Generating rgb.txt in TUM format...")
    generate_tum_format(frames_dir)

    # Run ORB-SLAM3 monocular SLAM
    print("Launching ORB-SLAM3 Monocular...")
    subprocess.run([
        orbslam_exec_path,
        vocab_path,
        config_path,
        frames_dir
    ])

def generate_tum_format(frames_folder):
    frames = sorted(glob.glob(os.path.join(frames_folder, "*.png")))
    if not frames:
        raise FileNotFoundError("No .png images found in the frames directory.")

    rgb_txt_path = os.path.join(frames_folder, "rgb.txt")
    with open(rgb_txt_path, "w") as f:
        f.write("# timestamp rgb_filename\n")
        for i, frame in enumerate(frames):
            timestamp = "{:.6f}".format(i * 0.04)  # Assuming 25 FPS
            f.write(f"{timestamp} {os.path.basename(frame)}\n")

    print(f"rgb.txt written to {rgb_txt_path}")

if __name__ == "__main__":
    run_orbslam()

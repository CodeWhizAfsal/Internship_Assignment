import open3d as o3d
import numpy as np

def load_trajectory(file_path):
    """
    Load the trajectory from a text file.
    
    The trajectory file should have columns: timestamp, x, y, z, qx, qy, qz, qw
    Where x, y, z are the positions, and qx, qy, qz, qw are the quaternion rotations.
    """
    trajectory = []
    
    with open(file_path, 'r') as f:
        for line in f:
            data = line.strip().split()
            if len(data) == 8:  # Ensure the line has the correct number of columns
                timestamp, x, y, z, qx, qy, qz, qw = map(float, data)
                trajectory.append([x, y, z])
    
    return np.array(trajectory)

def load_point_cloud(ply_file_path):
    """
    Load the 3D point cloud from a .ply file.
    """
    pcd = o3d.io.read_point_cloud(ply_file_path)
    return pcd

def visualize_trajectory_and_map(ply_file_path, trajectory_file_path):
    """
    Visualizes the 3D point cloud and the robot's trajectory.
    """
    # Load the point cloud and trajectory
    pcd = load_point_cloud(ply_file_path)
    trajectory = load_trajectory(trajectory_file_path)
    
    # Create a point cloud for the trajectory (robot positions)
    trajectory_pcd = o3d.geometry.PointCloud()
    trajectory_pcd.points = o3d.utility.Vector3dVector(trajectory)
    
    # Color the trajectory points red
    trajectory_pcd.paint_uniform_color([1, 0, 0])
    
    # Visualize the 3D map and trajectory
    o3d.visualization.draw_geometries([pcd, trajectory_pcd],
                                      window_name="Robot Pose Localization",
                                      width=800, height=600)
    
if __name__ == "__main__":
    # File paths
    ply_file_path = '/home/afsal/Internship_Assignment/3D-Cloud_Point/trajectory.ply'  # Replace with your point cloud file
    trajectory_file_path = '/home/afsal/Internship_Assignment/Algorithm/KeyFrameTrajectory.txt'  # Replace with your trajectory file
    
    # Visualize the map and trajectory
    visualize_trajectory_and_map(ply_file_path, trajectory_file_path)

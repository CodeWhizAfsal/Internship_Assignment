import numpy as np
import open3d as o3d

def save_trajectory_from_txt(trajectory_file, output_file='trajectory.ply'):
    """
    Save the trajectory data from a text file as a point cloud in .ply format.

    :param trajectory_file: (str) Path to the trajectory file (KeyFrameTrajectory.txt)
    :param output_file: (str) Output path for saving the trajectory as .ply file.
    """
    # Read trajectory data from file
    trajectory_data = np.loadtxt(trajectory_file)

    # Check if trajectory data has more than 3 columns
    if trajectory_data.shape[1] > 3:
        print(f"Warning: Trajectory data has {trajectory_data.shape[1]} columns. Using only the first 3 columns (x, y, z).")
        trajectory_data = trajectory_data[:, 1:4]  # Take only the 2nd, 3rd, and 4th columns (x, y, z)
    
    # Check if trajectory data has 3 columns (x, y, z)
    if trajectory_data.shape[1] != 3:
        print("Error: Trajectory data should have 3 columns (x, y, z).")
        return

    # Create Open3D PointCloud object
    trajectory_pcd = o3d.geometry.PointCloud()
    trajectory_pcd.points = o3d.utility.Vector3dVector(trajectory_data)

    # Save the trajectory point cloud to a .ply file
    o3d.io.write_point_cloud(output_file, trajectory_pcd)
    print(f"Trajectory saved as {output_file}")

# Example usage:
if __name__ == "__main__":
    # Path to the trajectory data (KeyFrameTrajectory.txt)
    trajectory_file = '/home/afsal/Internship_Assignment/Algorithm/KeyFrameTrajectory.txt'  # Updated path

    # Save the trajectory to a .ply file
    save_trajectory_from_txt(trajectory_file, 'trajectory.ply')

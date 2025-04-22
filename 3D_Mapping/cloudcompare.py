import subprocess
import os

def open_ply_with_cloudcompare(ply_file_path):
    """
    Opens the .ply file using CloudCompare via command line.
    
    :param ply_file_path: (str) Path to the .ply file to open.
    """
    # Ensure the CloudCompare executable is available in your system's PATH or provide the full path
    cloudcompare_executable = 'CloudCompare'  # Replace with the full path if needed
    
    # Check if the .ply file exists
    if not os.path.exists(ply_file_path):
        print(f"Error: The file {ply_file_path} does not exist.")
        return

    # Prepare the CloudCompare command to open the .ply file
    command = [cloudcompare_executable, '-O', ply_file_path]
    
    try:
        # Run the CloudCompare command
        subprocess.run(command, check=True)
        print(f"CloudCompare has opened the file: {ply_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening the file: {e}")

if __name__ == "__main__":
    # Example: Replace with the path to your .ply file
    ply_file = '/home/afsal/Internship_Assignment/3D-Cloud_Point/trajectory.ply'
    
    # Open the .ply file in CloudCompare
    open_ply_with_cloudcompare(ply_file)

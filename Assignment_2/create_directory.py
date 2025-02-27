import os
# get current directory
current_directory = os.getcwd()
# Define a new directory
new_directory = os.path.join(current_directory, 'test_dir')

# Create the directory if it doesn't exist
# exist_ok=True ensures that the directory is not created if it already exists and also dont throw error if dir exits
os.makedirs(new_directory, exist_ok=True)

print(f"Directory created: {new_directory}")

# 导入所需的库
import os

print("1")
# Get the current directory of the Python file
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)

# Set the path to the speech-to-text-key.json file relative to the Python file
key_file_path = os.path.join(current_directory, "speech-to-text-key.json")
print(key_file_path)

if os.path.exists(key_file_path):
    print("File exists.")
else:
    print("File does not exist.")

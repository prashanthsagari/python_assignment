import os 
import shutil

os.makedirs("backup", exist_ok=True)
shutil.move("data.txt", "backup/data.txt")
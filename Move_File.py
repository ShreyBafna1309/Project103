import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/91967/Downloads"
to_dir = "C:/Users/91967/OneDrive/Desktop/Documents_File"

list_of_files = os.listdir(from_dir)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent):
        print(f"Hey, {event.src_path} has been created")
    
    def on_deleted(self, event: FileSystemEvent):
        print(f"Oops! Someone has deleted {event.src_path}")

    def on_modified(self, event: FileSystemEvent):
        print(f"Someone has modified {event.src_path}")

    def on_moved(self, event: FileSystemEvent):
        print(f"Someone has moved/renamed {event.src_path}")

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue

    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Documents_File"
        path3 = to_dir + '/' + "Documents_File" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
    
except KeyboardInterrupt:
    print("Stop")
    observer.stop()
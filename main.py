import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            print(f"File created: {file_path}")
            self.send_to_server(file_path)

    def send_to_server(self, file_path):
        server_endpoint = 'http://localhost:5000/upload'
        
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(server_endpoint, files=files)
                print(f"Server response: {response.status_code}")
        except Exception as e:
            print(f"Error sending file to server: {e}")

if __name__ == "__main__":
    directory_to_watch = r'C:\Users\k\dev\projects\python\pdfs'

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=True)

    print(f"Watching directory: {directory_to_watch}")

    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

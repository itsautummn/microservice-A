import time
import json
import os

client_fname = "pipe/client_pipe.json"
server_fname = "pipe/server_pipe.json"

def read_client_pipe() -> json:
    data: json

    with open(client_fname, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = None
    f.close()
    
    return data


def process_data(data: json):
    # Do some work with the data

    # Then, send something back to server_pipe.json
    return_data: json = {
        "server_name": "LanShare Server",
        "os": "Darwin",
        "hostname": "mac-studio.local",
        "username": "dfmb",
        "local_ip": "192.168.1.1",
        "port": "9527",
        "download_dir": "path/to/directory",
        "timestamp": "yyyy/mm/dd mm:ss"
    }

    with open(client_fname, "w") as f:
        json.dump(return_data, f)
    f.close()


def main():
    while True:
        # Check for data in client_pipe.json
        client_data = read_client_pipe()
        
        if client_data:
            process_data(client_data)
        
        time.sleep(2)
        

if __name__ == "__main__":
    main()
from flask import Flask, send_from_directory, render_template
import os
import socket

app = Flask(__name__)

FILES_DIRECTORY = '/app/files'
os.makedirs(FILES_DIRECTORY, exist_ok=True)

def receive_file():
    server_ip = '0.0.0.0'  # Listen on all interfaces
    server_port = 7777  # Port number to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((server_ip, server_port))
    
    server_socket.listen(1)

    print(f"Listening for incoming files on {server_ip}:{server_port}")

    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    try:
        # Receiving the file
        with open(os.path.join(FILES_DIRECTORY, 'received_file.zip'), 'wb') as f:
            while True:
                data = connection.recv(4096)
                if not data:
                    break
                f.write(data)
            print("File received successfully.")

    finally:
        # Clean up the connection
        connection.close()
        server_socket.close()

    print("Socket closed.")

@app.route('/')
def file_list():
    files = os.listdir(FILES_DIRECTORY)
    return render_template('index.html', files=files)

@app.route('/files/<filename>')
def file_download(filename):
    return send_from_directory(FILES_DIRECTORY, filename)

if __name__ == '__main__':
    receive_file()  
    app.run(host='0.0.0.0', port=5000)  # Start Flask app
    

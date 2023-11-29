from flask import Flask, send_from_directory, render_template
import socket
import asyncio
import os

FILES_DIRECTORY = '/home/kch3d/Desktop/tshark/host/uploads/'

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
        with open(os.path.join(FILES_DIRECTORY, 'capture_result.pcap'), 'wb') as f:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                f.write(data)
            
    except Exception as e:
        print(e)

    finally:
        # Clean up the connection
        connection.close()
        server_socket.close()

    print("Socket closed.")

if __name__ == '__main__':
    while True:
        print("Start packet capturing...")
        receive_file()
    

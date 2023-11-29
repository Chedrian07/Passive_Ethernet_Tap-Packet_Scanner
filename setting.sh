#!/bin/bash

# Updating package list
echo "Updating package list..."
sudo apt update -y

# Installing necessary packages
echo "Installing necessary packages..."
sudo apt install python3 python3-pip tshark file ssh zip -y

echo "Installation complete!"

# Prompting for remote PC connection details
read -p "Enter remote host IP: " host_ip
read -p "Enter remote host port: " host_port


echo $(pwd)
echo $(ls)

read -p "Enter file path for transfer: " file_path

# Creating configuration file
config_file="socket_config.txt"


echo "Creating configuration file: $config_file"

echo "HOST_IP=$host_ip" > $config_file
echo "HOST_PORT=$host_port" >> $config_file
echo "FILE_PATH=$file_path" >> $config_file

echo "Configuration file created."

echo "Setting Your Remote PC Connections complete!"



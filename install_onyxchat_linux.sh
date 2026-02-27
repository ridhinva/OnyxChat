#!/bin/bash

echo "Installing dependencies..."
sudo apt install python3 python3-pip git tor -y

echo "Upgrading pip..."
pip3 install --upgrade pip

echo "Installing Python requirements..."
pip3 install -r requirements.txt

echo "Creating Tor hidden service directory..."
mkdir -p ~/tor/hidden_service

echo "Configuring Tor hidden service..."
sudo bash -c "cat >> /etc/tor/torrc <<EOF

HiddenServiceDir /home/$USER/tor/hidden_service/
HiddenServicePort 5555 127.0.0.1:5555
EOF"

echo "Restarting Tor..."
sudo service tor restart

sleep 5

echo ""
echo "Your .onion address:"
cat ~/tor/hidden_service/hostname

echo ""
echo "Installation Complete!"
echo "Run with:"
echo "cd OnyxChat && python3 onyxchat.py"

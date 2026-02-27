#!/data/data/com.termux/files/usr/bin/bash

echo "Updating Termux packages..."
pkg update && pkg upgrade -y

echo "Installing dependencies..."
pkg install python git tor -y

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Creating Tor hidden service directory..."
mkdir -p /data/data/com.termux/files/home/tor/hidden_service

echo "Configuring Tor hidden service..."
cat >> /data/data/com.termux/files/usr/etc/tor/torrc <<EOF

HiddenServiceDir /data/data/com.termux/files/home/tor/hidden_service/
HiddenServicePort 5555 127.0.0.1:5555
EOF

echo ""
echo "Starting Tor (keep this running in background if using .onion)..."
echo "Run Tor manually with: tor"

echo ""
echo "Installation Complete!"
echo "Run with:"
echo "cd OnyxChat && python onyxchat.py"

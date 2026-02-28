# OnyxChat
**Anonymous Peer-to-Peer Chat with Optional Tor Integration**  

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10-blue)

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Security Notes](#SecurityNotes)
---

## Features
- 🔐 Password-protected chat rooms  
- 🌐 Works over LAN, WAN, or Tor `.onion` addresses  
- 🧅 Optional Tor hidden service for anonymity  
- ⚡ Real-time messaging  
- 📱 Compatible with Termux (Android) and Linux  
- ✅ Lightweight, no central server required  

---

## Installation

### Termux (Android)
```
pkg update && pkg upgrade -y
pkg install python git tor -y
pip install --upgrade pip
pip install pysocks

```
Security Notes
### Linux (Ubuntu/Debian)
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git tor -y
pip3 install --upgrade pip
pip3 install pysocks
```

## Setup
Termux
```
chmod +x install_onyxchat_termux.sh
./install_onyxchat_termux.sh


```

Linux
```


chmod +x install_onyxchat_linux.sh
./install_onyxchat_linux.sh

```

## Usage
### Start Tor:
Termux:
```
tor

```
Linux:
```
sudo service tor start
```
Run the chat application:
```
python onyxchat.py
```
You will see:
```
1. Host Chat
2. Join Chat
Select [1/2]:
```
Hosting a Chat :
Select 1
Set a room password
Choose port (default: 5555)
Optionally enabLinuxle Tor
Share your IP or .onion address

Joining a Chat
Select 2
Enter host IP or .onion address
Enter room password
Choose port (default: 5555)
If using .onion, provide Tor SOCKS5 IP/Port (default: 127.0.0.1:9050)

## Security Notes
Always use strong passwords for rooms
Ensure Tor is running when using .onion addresses
Change default ports if needed
Avoid sharing your real IP for anonymity

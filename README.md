# OnyxChat
**Anonymous Peer-to-Peer Chat with Optional Tor Integration**  

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10-blue)

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Setup](#setup)
4. [Tor Configuration](#tor-configuration)
5. [Usage](#usage)
6. [Security Notes](#security-notes)
7. [Dependencies](#dependencies)
8. [Project Structure](#project-structure)
9. [License](#license)

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

### Linux (Ubuntu/Debian)
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git tor -y
pip3 install --upgrade pip
pip3 install pysocks
```

## Setup
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git tor -y
pip3 install --upgrade pip
pip3 install pysocks
```
### Create Tor hidden service folder:

Termux:
```
mkdir -p /data/data/com.termux/files/home/tor/hidden_service
```
Linux:
```
mkdir -p ~/tor/hidden_service
```
Update the HIDDEN_SERVICE_DIR variable in onyxchat.py to point to this folder.

## Tor Configuration
Edit Tor configuration file (torrc):

Termux:

```
nano /data/data/com.termux/files/usr/etc/tor/torrc
```
Add:

```
HiddenServiceDir /tor/hidden_service/
HiddenServicePort 5555 127.0.0.1:5555
```

Linux:

```
sudo nano /etc/tor/torrc
```
Add:

```
HiddenServiceDir /data/data/com.termux/files/home/tor/hidden_service/
HiddenServicePort 5555 127.0.0.1:5555
```

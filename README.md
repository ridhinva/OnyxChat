# OnyxChat
**Anonymous Peer-to-Peer Chat with Optional Tor Integration**  

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10-blue)

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Setup](#setup)
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

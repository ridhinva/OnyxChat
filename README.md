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
```bash
pkg update && pkg upgrade -y
pkg install python git tor -y
pip install --upgrade pip
pip install pysocks

###Linux (Ubuntu/Debian)



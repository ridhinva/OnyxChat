import socket
import threading
import os
import time
import socks
import sys

# =========================
# CONFIG
# =========================

DEFAULT_PORT = 5555
HIDDEN_SERVICE_DIR = "/data/data/com.termux/files/home/tor/hidden_service"


# =========================
# UTIL
# =========================

def clear():
    os.system("clear")


def banner():
    print("""
   ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗ ██████╗██╗  ██╗ █████╗ ████████╗
  ██╔═══██╗████╗  ██║██║   ██║╚██╗██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
  ██║   ██║██╔██╗ ██║██║   ██║ ╚███╔╝ ██║     ███████║███████║   ██║   
  ██║   ██║██║╚██╗██║╚██╗ ██╔╝ ██╔██╗ ██║     ██╔══██║██╔══██║   ██║   
  ╚██████╔╝██║ ╚████║ ╚████╔╝ ██╔╝ ██╗╚██████╗██║  ██║██║  ██║   ██║   
   ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

                     Anonymous P2P Chat
    """)


def get_onion_address():
    hostname_path = os.path.join(HIDDEN_SERVICE_DIR, "hostname")

    for _ in range(15):
        if os.path.exists(hostname_path):
            with open(hostname_path, "r") as f:
                return f.read().strip()
        time.sleep(1)

    return None


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                break
            print(f"\nPeer: {data.decode()}")
        except:
            break


def send_messages(sock):
    while True:
        try:
            msg = input("You: ")
            sock.send(msg.encode())
        except:
            break


# =========================
# HOST
# =========================

def host_chat():
    password = input("Set room password: ")
    port = input(f"Enter port ({DEFAULT_PORT}): ") or str(DEFAULT_PORT)
    port = int(port)

    use_tor = input("Use Tor? (y/n): ").lower() == "y"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(1)

    clear()
    banner()

    if use_tor:
        onion = get_onion_address()
        if onion:
            print("\n[+] Tor Hidden Service Active!")
            print(f"[+] Your Onion Address: {onion}")
            print("[+] Share this with the joiner.\n")
        else:
            print("\n[-] Onion address not found. Make sure Tor is running.\n")

    print(f"[+] Waiting for connection on port {port}...\n")

    conn, addr = server.accept()
    print("[+] Peer connected!")

    peer_pass = conn.recv(1024).decode()

    if peer_pass != password:
        print("[-] Wrong password. Disconnecting.")
        conn.close()
        return

    conn.send("OK".encode())

    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
    send_messages(conn)


# =========================
# JOIN
# =========================

def join_chat():
    host = input("Enter host IP or .onion address: ")
    password = input("Enter room password: ")
    port = input(f"Enter port ({DEFAULT_PORT}): ") or str(DEFAULT_PORT)
    port = int(port)

    use_tor = host.endswith(".onion")

    if use_tor:
        socks_ip = input("Tor SOCKS5 IP (127.0.0.1): ") or "127.0.0.1"
        socks_port = input("Tor SOCKS5 Port (9050): ") or "9050"
        socks_port = int(socks_port)

        socks.set_default_proxy(socks.SOCKS5, socks_ip, socks_port)
        socket.socket = socks.socksocket

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[+] Connecting...")
    client.connect((host, port))

    client.send(password.encode())

    response = client.recv(1024).decode()
    if response != "OK":
        print("[-] Wrong password.")
        return

    print("[+] Connected successfully!\n")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    send_messages(client)


# =========================
# MAIN
# =========================

def main():
    clear()
    banner()

    print("1. Host Chat")
    print("2. Join Chat")

    choice = input("Select [1/2]: ")

    if choice == "1":
        host_chat()
    elif choice == "2":
        join_chat()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()

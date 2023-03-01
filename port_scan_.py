import socket
import time

ip = raw_input("Digite o endereco ou IP: ")

ports = []
count = 0

start_time = time.time()

while count < 10:
    ports.append(raw_input("Digite a porta: "))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print str(port) + "-> Porta aberta"
    else:
        print str(port) + "-> Porta Fechada"

    elapsed_time = time.time() - start_time
print("Tempo decorrido:", elapsed_time, "segundos")

print "Varredura finalizada"
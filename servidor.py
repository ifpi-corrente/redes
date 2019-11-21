#!/usr/bin/python3

# Servidor UDP

import socket

#criar um socket IPv4 e do tipo UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Servidor vai ficar escutando nolocalhost
#e na porta 12000
servidor.bind(('', 13000))

while True:
    mensagem_bytes, endereco_cliente = servidor.recvfrom(2048)
    mensagem_recebida = mensagem_bytes.decode()
    mensagem_enviada = mensagem_recebida.upper()
    print(mensagem_enviada)
    servidor.sendto(mensagem_enviada.encode(), endereco_cliente)
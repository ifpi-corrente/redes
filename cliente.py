#!/usr/bin/python3
#Cliente UDP

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem_enviada = input('Digite uma mensagem: ')
    cliente.sendto(mensagem_enviada.encode(),("10.8.19.219:"))
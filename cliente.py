
import socket as socket
server = ''
port = ''


def cliente(server, port):
    server = (input("\n Digite o ip do Servidor:"))
    port = int(input("\n Digite o numero da Porta:"))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.sendall(str.encode('Bom dia   Rafael!'))
    dados = s.recv(2048)
    print('Mesagem ecoada:', dados.decode())


cliente(server, port)

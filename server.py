import socket as socket
server = "127.0.0.1"
port = 4567

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print('Aguardando conexão de um Cliente.....')

conexao, endereco = s.accept()
print('Conectado em', endereco)

while True:
    dados = conexao.recv(2048)
    if not dados:
        conexao.close()
        break
    conexao.sendall(dados)

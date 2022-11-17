# CLIENTE - transferência de arquivos
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 9090))

msg_conexao = sock.recv(100).decode()
print(msg_conexao)

# pede para o cliente digitar o nome do arquivo
nomeArq = input('Qual o arquivo que você quer baixar do servidor? ')
sock.send(nomeArq.encode())

nomeSalvar = input('Vai salvar o arquivo baixado com que nome? ')

f = open(nomeSalvar, "wb")

pedaco = sock.recv(4096)

while pedaco:
    f.write(pedaco)
    pedaco = sock.recv(4096)
    
f.close()





import socket

#1. criar o socket do cliente

scli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. conecta com o servidor 
host = socket.gethostname(); porta = 49153
scli.connect((host, porta))

#MSG1 cliente recebe a mensagem de conectado
msg_conexao = sli.recv(100). decode()

#MSG2 cliente envia nome do arquivo que ele quer para o servidor
nomeArq = input('Qual arquivo você quer baixar do servidor?')
scli.send(nomeArq.encode())

#MSG3 cliente
nomeSalvar = input('Vai salvar o arquivo onde e com que nome?')

f = open(nomeSalvar, 'w') #abre um novo arquivo para esquita
pedaco = scli.recv(4096) #pefo o primeiro pedaço

while pedaco: #vai salvando o arquivo baixado pedaço por pedaço
    f.write(pedaco) 
    pedaco = scli.recv(4096)

f.close()
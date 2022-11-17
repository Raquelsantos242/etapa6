# ETAPA 6 - programa 1
# Vamos fazer uso das funções do módulo ‘socket’
# para criar um programa cliente que irá exibir
# informações de processamento e memória do servidor.
"""
SERVIDOR:
- Servidor recebe conexão do cliente e obtém os dados;
- Servidor envia os dados ao cliente e continua esperando por mais requisições.
- O processo servidor termina quando o servidor recebe a mensagem ‘fim’.
"""
# Servidor
import socket, psutil, pickle

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Obtem o nome da máquina
host = socket.gethostname()                         
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
(conexao,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
  # Recebe pedido do cliente:
  msg = conexao.recv(4)
  if msg.decode('ascii') == 'fim':
      break
  # Gera a lista de resposta
  resposta = []
  resposta.append(psutil.cpu_percent())
  mem = psutil.virtual_memory()
  mem_percent = mem.used/mem.total * 100
  resposta.append(mem_percent)
  # Prepara a lista para o envio
  bytes_resp = pickle.dumps(resposta)
  # Envia os dados
  conexao.send(bytes_resp)

# Fecha socket do servidor e cliente
conexao.close()
socket_servidor.close()

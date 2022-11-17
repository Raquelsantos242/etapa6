# SERVIDOR - transferência de arquivos
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 9090))
sock.listen()
print('===========================================')
print('STA - Servidor de Transferência de Arquivos')
print('===========================================')

while True:
    print('aguardando conexao...')
    conexao, end_cliente = sock.accept()
    print("--------------------------")
    print("NOVA CONEXÃO: ", end_cliente)
    
    conexao.send('Conectado ao STA\n'.encode())
    
    # recebe o nome do arquivo que tem que ser transmitido e verifica se ele existe
    try:
        # pega o nome do arquivo
        nomeArq = conexao.recv(2048).decode()
        
        # abrir o arquivo no modo binário para leitura
        f = open(nomeArq, 'rb')
        
        # envia o arquivo em blocos de 4kb
        pedaco = f.read(4096)        
        while pedaco:
            conexao.send(pedaco)
            pedaco = f.read(4096)
        
        f.close()        
        

    except Exception as e:
        print(e)
    
    conexao.close() # encerra a conexão
    
    
    
    
    
    
    
    
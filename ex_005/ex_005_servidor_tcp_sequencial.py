import socket

# Tupla com IP e porta a ser usada
ip_porta = ("0.0.0.0", 8080)

# Cria um socket para usar IPv4 (AF_INET) e TCP (SOCK_STREAM)
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind registrando a conjunto IP/PORTA
socket_servidor.bind(ip_porta)

# Quantidades de clientes na fila de espera para executar o serviço
socket_servidor.listen(2)

print("Esperando conexão")
# Estabelece a conexão entre cliente e servidor, que é iniciado na função connect lá no cliente
socket_conexao, endereco_cliente = socket_servidor.accept()

print("Esperando receber dados do cliente...")
dados_bytes = socket_conexao.recv(1024)

texto = dados_bytes.decode()
print(f"Recebido {texto} de {endereco_cliente}")

resposta_bytes = str(len(texto)).encode()
socket_conexao.sendall(resposta_bytes)

socket_conexao.close()
socket_servidor.close()

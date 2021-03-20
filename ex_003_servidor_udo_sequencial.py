import socket

# Tupla com IP e porta a ser usada
ip_porta = ("0.0.0.0", 8080)

# Cria um socket para usar o IPv4 (AF_INET) e UDP (SOCK_DGRAM)
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Faz o bind no IP 0.0.0.0 e porta 8080
socket_servidor.bind(ip_porta)

while True:
    # Esperando receber dados na porta informada para bin
    # dados: conteúdo recebido
    # endereço: uma tupla (ip, porta) de quem mandou os dados
    print("Esperando cliente...")
    dados_bytes, endereco = socket_servidor.recvfrom(1024)

    # Mostra os dados recebidos
    texto = dados_bytes.decode()
    print(f"Recebido: {texto} de {endereco}")

    if texto == 'sair':
        print(f"Cliente {endereco} está saindo...")

    resposta_bytes = str(len(texto)).encode()
    socket_servidor.sendto(resposta_bytes, endereco)

import socket

mensagem = ""
ip_porta_servidor = ("127.0.0.1", 8080)

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while mensagem.lower() != "sair":
    mensagem = input("Digite uma mensagem para enviar: ")

    socket_cliente.sendto(mensagem.encode(), ip_porta_servidor)
    print("Mensagem enviada!")

    dados_bytes, endereco = socket_cliente.recvfrom(1024)

    resposta = int(dados_bytes.decode())
    print(f"Resposta recebida: {resposta}!")

socket_cliente.close()

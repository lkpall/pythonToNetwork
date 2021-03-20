import socket

mensagem = ""
ip_porta_servidor = ("127.0.0.1", 8080)

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# A função connect é responsável por iniciar a conexão com o servidor, que posteriormente é terminada na função accept
socket_cliente.connect(ip_porta_servidor)

mensagem = input("Digite uma mensagem para enviar: ")

socket_cliente.sendall(mensagem.encode())
print("Mensagem enviada!")

resposta_bytes = socket_cliente.recv(1024)
tamanho = int(resposta_bytes.decode())

print(f"Resposta recebida: {tamanho}!")

socket_cliente.close()

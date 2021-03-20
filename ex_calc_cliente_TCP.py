import socket

ip_porta_servidor = ("127.0.0.1", 8080)

while True:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_cliente.connect(ip_porta_servidor)
    # Menu de operações
    op = input("0 - Sair\n"
               "1 - Adição\n"
               "2 - Subtração\n"
               "3 - Multiplicação\n"
               "4 - Divisão\n"
               "Digite qual operação deseja fazer: ")
    if op == "0":
        socket_cliente.close()
        break

    n1 = input("Digite o primeiro valor: ")
    n2 = input("Digite o segundo valor: ")

    mensagem = f"{op} {n1} {n2}"

    socket_cliente.sendall(mensagem.encode())
    print("Mensagem enviada!")

    dados_bytes = socket_cliente.recv(1024)

    resposta = dados_bytes.decode()
    print(f"Resultado: {resposta}!\n")

    socket_cliente.close()

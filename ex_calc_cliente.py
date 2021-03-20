import socket

ip_porta_servidor = ("127.0.0.1", 8080)

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Menu de operações
    op = input("0 - Sair\n"
        "1 - Adição\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "Digite qual operação deseja fazer: ")

    if op == "0":
        break
    n1 = input("Digite o primeiro valor: ")
    n2 = input("Digite o segundo valor: ")

    mensagem = f"{op} {n1} {n2}"

    socket_cliente.sendto(mensagem.encode(), ip_porta_servidor)
    print("Mensagem enviada!")

    dados_bytes, endereco = socket_cliente.recvfrom(1024)

    resposta = float(dados_bytes.decode())
    print(f"Resultado: {resposta}!\n")

socket_cliente.close()

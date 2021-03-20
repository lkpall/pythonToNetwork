import socket

ip_porta = ("", 8080)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_servidor.bind(ip_porta)

socket_servidor.listen(2)

while True:

    while True:
        print("Esperando cliente...")
        socket_conexao, endereco_cliente = socket_servidor.accept()
        dados_bytes = socket_conexao.recv(1024)

        # Mostra os dados recebidos
        texto = dados_bytes.decode()
        print(texto)
        calc = texto.split()
        op = float(calc[0])
        n1 = float(calc[1])
        n2 = float(calc[2])
        resultado = 0
# o problema é aqui, no encerramento do servidor e conexão, procurar solução pra isso
        if op == 0:
            socket_servidor.close()
            break
        elif op == 1:
            resultado = n1+n2
        elif op == 2:
            resultado = n1-n2
        elif op == 3:
            resultado = n1*n2
        elif op == 4:
            resultado = n1/n2

        resposta_bytes = str(resultado).encode()
        socket_conexao.sendall(resposta_bytes)
        socket_conexao.close()

    socket_servidor.close()

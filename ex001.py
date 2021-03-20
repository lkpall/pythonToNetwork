import socket

lista = ['www.natal.rn.gov.br', 'portal.ifrn.edu.br', 'suap.ifrn.edu.br', 'www.tecmundo.com.br',
         'www.tribunadonorte.com.br', 'www.ufrn.br', 'globoesporte.globo.com', 'www.youtube.com',
         'www.twitch.tv', 'servicos.cosern.com.br']

for i in range(10):
    nome = lista[i]
    ip = socket.gethostbyname(lista[i])
    print(f"{nome} = {ip}")
    site = socket.gethostbyaddr(ip)
    print(site)
    print(f"\n ####################### \n")
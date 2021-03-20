from ex_006 import ex_006_funcoes as func

# exemplo de como fazer a importação de outro arquivo nesse e utilizar funções dele
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
func.mostrar(func.media(nota1, nota2))

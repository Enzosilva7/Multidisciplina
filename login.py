import time
import random
user = input("digite seu login")

if user == "RafexCabelux07":
    print("Fazendo verificação de segurança...")
    time.sleep(1)
    input("Insira o código de segurança recebido por SMS: ")
    print("Login realizado com sucesso!!")
else:
    print("Login não encontrado")
input()




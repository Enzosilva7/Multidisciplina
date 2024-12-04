class  user:
    def __init__(self, nome, email, data_de_nascimento, nome_de_usuário, senha): # type: ignore
        self.__nome = nome
        self.__email = email
        self.__data_de_nascimento = data_de_nascimento
        self.__nome_de_usuário = nome_de_usuário
        self.__senha = senha
        print("Usuário criado com sucesso!!!")

userNome_De_Usuário = input("Crie o nome do seu usuário: (Pressione enter para continuar)")
userSenha = input("Crie sua senha: (Pressione enter para continuar)")
userData_De_Nascimento = input("Coloque sua data de nascimento: (pressione enter para continuar)")
userNome = input("Coloque seu nome: (Pressione enter para continuar)")
userEmail = input("Coloque seu email: (Pressione enter para continuar)")
usuario1 = user(userNome, userEmail, userData_De_Nascimento, userNome_De_Usuário, userSenha)
input()
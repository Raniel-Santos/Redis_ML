import pymongo
import redis
import Login_de_Usuário.loginUsuario as login
import Lista_Favoritos.favoritos as favoritos


#Conexão Mongo
client = pymongo.MongoClient("mongodb+srv://Raniel2:Raninho93@raniel-fatec.og59z6w.mongodb.net/?retryWrites=true&w=majority")

#Conexão Redis
client_redis = redis.Redis(host='redis-11775.c84.us-east-1-2.ec2.cloud.redislabs.com',
    port= 11775,
    password='Raninho93')
## global mydb
mydb = client.mercado_livre

execucao = True

while execucao:

    print('''\n Selecione uma opção:
    [1] Cadastrar Usuário
    [2] Login
    [3] Deslogar
    [4] Favoritar
    [0] Sair
    ''')

    opcoes = input(str("Escolha uma das opções: "))
        
    match int(opcoes):
        case 1:
            login.cadastrar_usuario(mydb,client_redis)
        case 2:
            login.logar(mydb,client_redis)
        case 3:
            login.deslogar(mydb,client_redis)
        case 4:
            favoritos.favoritos(mydb,client_redis)
        case 0:
            execucao = False
            print("\nAté mais \n")
            break
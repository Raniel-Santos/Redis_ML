from bson.json_util import dumps
from bson.objectid import ObjectId

def cadastrar_usuario(client_mongo,client_redis):
    mycol = client_mongo.Usuario    
    user = mycol.find_one(ObjectId('632a47c1f1ff760743b1fbd0')) ## Usuario que esta cadastrado no MongoDB
    

    for favorito in user['lista_favoritos']:
        client_redis.hset('user: '+user['email'], str (favorito['nome_produto']), dumps(favorito))

    client_redis.hset('user:' + user['email'], 'status', 'deslogado')    
    print(client_redis.hgetall('user:' + user['email']))
    print(client_redis.hkeys('user:' + user['email']))
    print(client_redis.keys())

def logar(client_mongo, client_redis):
    mycol = client_mongo.Usuario
    usuario = mycol.find_one(ObjectId('632a47c1f1ff760743b1fbd0'))
    client_redis.hset('user:' + usuario['email'],'status','logado')
    print(client_redis.hget('user:' + usuario['email'], 'status'))

def deslogar(cliente_mongo,client_redis):
    mycol = cliente_mongo.Usuario
    usuario = mycol.find_one(ObjectId('632a47c1f1ff760743b1fbd0'))
    client_redis.hset('user:' + usuario['email'],'status','deslogado')
    print(client_redis.hget('user:' + usuario['email'], 'status'))


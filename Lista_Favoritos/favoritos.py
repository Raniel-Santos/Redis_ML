from bson.json_util import dumps
from bson.objectid import ObjectId
import json

def favoritos(client_mongo, client_redis):
    favoritos = []
    mycol_Usuario = client_mongo.Usuario
    mycol_Produto = client_mongo.Produto
    usuario = mycol_Usuario.find_one(ObjectId('632a47c1f1ff760743b1fbd0'))

    #Inserindo Nintendo Switch aos favoritos
    favoritos.append(mycol_Produto.find_one(ObjectId('639794154821fced8c1eda0f')))
    #Inserindo Samsung Galaxy s20 aos favoritos
    favoritos.append(mycol_Produto.find_one(ObjectId('639794344821fced8c1eda10')))    
    print(favoritos)
    if client_redis.hkeys("user:" + usuario['email']):
        print('usuario encontrado')

        if client_redis.hget('user:' + usuario['email'], 'status').decode() == 'logado':
            print('logado')
            for favorito in favoritos:
                
                client_redis.hset("user:" + usuario['email'], str(favorito['nome_produto']), dumps(favorito))

                new_fav = []

                dados = client_redis.hkeys("user:" + usuario['email'])
                for dado in dados:
                    if dado.decode() != 'status':
                        new_fav.append(json.loads(client_redis.hget("user:" + usuario['email'],dado.decode())))

                mycol_Usuario.update_one({"_id":ObjectId(usuario["_id"])}, {"$set": {
                "nome":usuario['nome'],
                "email":usuario['email'],
                "telefone":usuario['telefone'],
                "cpf":usuario['cpf'],
                "enderecos":usuario["enderecos"],
                "lista_favoritos":new_fav,
                "compras":usuario["compras"]
            }}, upsert=True)
            
            print(client_redis.hvals("user:" + usuario['email']))
        else:
            print('Nenhum usuario logado,Por favor, realize o login')
    else:
        print('usuario não encontrado')
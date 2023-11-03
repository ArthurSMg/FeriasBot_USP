### Bot versão 2.0 (atualizada para o novo twitter (X))

import tweepy
import datetime

acess_token =  '1395893108181766147-FJ3tTZKFRXefiJtLPyJHGRHaHlBuJm'  #Acess
acess_token_secret = ''
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAK1bqwEAAAAAzpOWTbjWVgIEgY2osyuh45VGUJg%3DgSoLe4vWLNermPx8vA4la7WUYaTFzbwU8gu6o3cJbEo6VNrd2h' # Bearer Token
api_key = '2ZHuftfQkTFi2XHJt3NXOtmlu' #API
api_secret = ''

client = tweepy.Client(bearer_token, api_key, api_secret, acess_token, acess_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, acess_token, acess_token_secret)
api = tweepy.API(auth)

ferias = datetime.date(2023,12,22) #Coloque aqui a data do inínio das férias no modelo (ANO,MES,DIA)
agora = datetime.date.today() #Computa o dia de hoje

fdias_horas = ferias - agora # Diferença entre os dias colocados anteriormente (Tempo para as ferias)
fdias = fdias_horas.days  #Agora pegamos somente os dias

#Temos que separa o caso em que falta apenas 1 dia, para poder mudar "dias" para "dia" no tweet

inicio = datetime.date(2023,8,7)

if agora >= inicio:

    if fdias > 1:

        if fdias % 10 == 0: #Testando para ver se o dia é um multiplo de 10
            client.create_tweet(text = ("Faltam " + str(fdias) + " dias para as férias da USP!!!") )

        if fdias % 10 != 0: #Testando para ver se o dia é um multiplo de 10
            client.create_tweet(text = ("Faltam " + str(fdias) + " dias para as férias da USP") )


    if fdias == 1:
        client.create_tweet(text = ("Falta " + str(fdias) + " dia para as férias da USP!!!") )


    if fdias == 0:
        client.creat_tweet(text = ("ATENÇÃO: COMEÇARAM AS FÉRIAS DA USP!!!") )
        
else:
    quit()


        

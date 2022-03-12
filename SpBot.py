### Bot versão 1.2   

import tweepy
import datetime 

key =  '1395893108181766147-hn7xyPqaWvQrLXl3HR8tEZgV1rBbuX'  #Acess
secret = '' #Chave secreta

consumer_key = 'M9pDQMpHsPrNoVzXPTE4R4VKj' #API
consumer_secret = '' #Chave secreta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


ferias = datetime.date() #Coloque aqui a data do inínio das férias no modelo (ANO,MES,DIA)
agora = datetime.date.today() #Computa o dia de hoje

fdias = (ferias - agora).days # Diferença entre os dias colocados anteriormente (Tempo para as ferias)

#Temos que separa o caso em que falta apenas 1 dia, para poder mudar "dias" para "dia" no tweet

if fdias !=1:

    if fdias % 10 == 0: #Testando para ver se o dia é um multiplo de 10
        api.update_status("Faltam " + str(fdias) + " dias para as férias da USP!!!")
       
    if fdias % 10 != 0: #Testando para ver se o dia é um multiplo de 10
        api.update_status("Faltam " + str(fdias) + " dias para as férias da USP")
        

if fdias == 1:
    api.update_status("Falta " + str(fdias) + " dia para as férias da USP!!!")

        

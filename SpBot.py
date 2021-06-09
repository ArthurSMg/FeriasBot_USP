import tweepy
import datetime 

key =  '1395893108181766147-hn7xyPqaWvQrLXl3HR8tEZgV1rBbuX'  #Acess
secret = '' #Chave secreta

consumer_key = 'M9pDQMpHsPrNoVzXPTE4R4VKj' #API
consumer_secret = '' #Chave secreta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

ferias = datetime.date(2021,7,31) #Colocar o dia das férias
agora = datetime.date.today() #Computa o dia de hoje

fdias_horas = str(ferias - agora) # Diferença entre os dias colocados anteriormente (Tempo para as ferias)
fdias = fdias_horas[0:3] #para tirar o horario e me dar somente os dias

#### O código abaixo foi uma última atualizacao feita, em que, se o dia for um múltiplo de 10 (50,40,30...) , então o Bot ira twetar com mais animacao

if int(fdias) % 10 == 0: #Testando para ver se o dia é um multiplo de 10
    api.update_status("Faltam " + fdias + "dias para as férias da USP!!!")
    
if int(fdias) % 10 != 0: #Testando para ver se o dia é um multiplo de 10
    api.update_status("Faltam " + fdias + "dias para as férias da USP")

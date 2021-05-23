import tweepy
import datetime 

key =  '1395893108181766147-hn7xyPqaWvQrLXl3HR8tEZgV1rBbuX'  #Acess
secret = '' #Chave secreta

consumer_key = 'M9pDQMpHsPrNoVzXPTE4R4VKj' #API
consumer_secret = '' #Chave secreta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

ferias = datetime.date(2021,7,31)
agora = datetime.date.today()

fdias_horas = str(ferias - agora)
fdias = fdias_horas[0:3] #para tirar o horario e me dar somente os dias


api.update_status("Faltam " + fdias + "dias para as férias da USP")

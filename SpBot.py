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

ferias = datetime.date(2021,7,31) #Colocar o dia das férias
agora = datetime.date.today() #Computa o dia de hoje

fdias_horas = str(ferias - agora) # Diferença entre os dias colocados anteriormente (Tempo para as ferias)
fdias  = fdias_horas.split("day")[0] #Tira o horario e me dar somente os dias

## O try-except foi adicionado para podermos lidar isoladamente com o caso do dia 0, em que a função utilizada não retornava um "0 days" 
## e portanto quebrava o código , daria também para fazer utilizando o Regex

try:
    if int(fdias) !=1:   #testando para ver se o dia 'diferente de 1'

        if int(fdias) % 10 == 0:#Testando para ver se o dia é um multiplo de 10
            api.update_status("Faltam " + fdias + "dias para as férias da USP!!!") #Publicando tweet

        if int(fdias) % 10 != 0: #Testando para ver se o dia é um multiplo de 10
            api.update_status("Faltam " + fdias + "dias para as férias da USP") #Publicando tweet
            
    if int(fdias) == 1:  #Rodando o caso especial para quando falta 1 dia
        api.update_status("Faltam " + fdias + "dia para as férias da USP!!!")   #Lembra de colocar o 'dia' no singular agora!!!
       
except: #O caso de quando o dia é 0 e o programa da erro (Lembra de desativar o bot depois disso se não vai rodar denovo a mesma coisa)
    api.update_status("Começou as férias da USP!!! Descansem muito e cuidem da saúde mental de vocês. Até daqui a 2 semanas :)")
    
    

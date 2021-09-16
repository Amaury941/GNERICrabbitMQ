import pika
from pika.exchange_type import ExchangeType
from pika.spec import Exchange
from definitions import ExchangeOfChoice,KeyOfChoice,MsgOfChoice

## conectando ao localhost
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

## conectando no
channel = connection.channel()

# declarando exchange
channel.exchange_declare('Direct_Olá_Maria',ExchangeType.direct,False, False, False)
channel.exchange_declare('Fanout_Olá_Maria',ExchangeType.fanout,False, False, False)
channel.exchange_declare('Topic_Olá_Maria' ,ExchangeType.topic,False,  False, False)

### publicando
if not(("Direct_Olá_Maria" ==  ExchangeOfChoice) and (KeyOfChoice =='')):
    channel.basic_publish(exchange=ExchangeOfChoice, routing_key=KeyOfChoice, body=MsgOfChoice) #mandando um direct para Maria_helena

print(" [x] '%s' enviado."%MsgOfChoice)

import pika, sys, os
from pika.exchange_type import ExchangeType
from definitions import ExchangeOfChoice

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) ## conectando ao localhost
    
    channel = connection.channel() # estabelecendo canais

    # escolhe a chave dado o Tipo da Exchange
    KeyOfChoice = ''
    if ExchangeOfChoice == 'Direct_Olá_Maria':
        KeyOfChoice = 'Mari'
    elif ExchangeOfChoice == 'Topic_Olá_Maria':
        KeyOfChoice = '*.helena'

    args = {}
    
    '''Expiry
    tempo de espera da fila ociosa(60 segundos).
    '''
    args["x-message-ttl"] = 60000
    
    '''Overflow
    tamanho máximo de uma fila = 7, mais do que isso dá reject em todas as publicações em seguida
    '''
    args["x-max-length"]  = 7
    args["overflow"] = "reject-publish"

    channel.queue_declare("Mensagens_Maria_Helena",durable=True,arguments=args)

    channel.queue_bind(exchange=ExchangeOfChoice, queue = 'Mensagens_Maria_Helena', routing_key=KeyOfChoice)

    def callback(ch, method, properties, body): print(" [x] %r recebido" % body) ## printando as mensagens recebidas
    
    '''ACK
    dá o acknowledgment automaticamente em basic_consume
    '''
    channel.basic_consume(queue='Mensagens_Maria_Helena', on_message_callback=callback, auto_ack=True) ## consumindo a queue Bahia

    print(' [*] Esperando mensagens. pressione CTRL+C para sair.')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
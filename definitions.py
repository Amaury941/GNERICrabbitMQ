Exchanges         = ['Direct_Olá_Maria','Fanout_Olá_Maria','Topic_Olá_Maria']
ExchangeOfChoice  = Exchanges[2]
KeyOfChoice       = 'anywaythisisatopicthatmariaisinterested.augusta'
MsgOfChoice       = 'Testando o Topic'


'''
Como mudar a Exchange:
    é impossível mudar a exchange quando ela é setada, pois as queues  são durable,
    Logo, é necessário não só mudar a ExchangeOfChoice mas também reiniciar o servidor rabbitMQ.
    
    O mesmo não se aplica a MsgOfChoice e KeyOfChoice, sendo possível mudar sem reiniciar.
'''
# RabbitMQ na prática

Desenvolver uma solução com RabbitMQ (usando a linguagem de programação de sua preferência) que mostre:


1. Três exchanges (cada uma com um tipo: Direct, Fanout e Topic)
2. Cada exchange com 3 filas
2.1. As filas devem receber as propriedades Durable, Expiry, e Overflow
3. Deve-se mostrar os critérios de confiabilidade em funcionamento, como ACK e Reject.


O que entregar?


Um video explicando o código e mostrando o funcionamento da solução, principalmente os tópicos de 1 a 3 descritos anteriormente.


# como executar
  - executar source /virtua/bin/activate para entrar no ambiente virtual
  - rodar código de rabbitMQ.txt(ou ligar o servidor rabbitMQ)
  - rodar Publisher.py uma vez(para definir as exchanges)
  - iniciar qualquer um dos consumers 'Maria_Antonieta','Maria_Augusta','Maria_Helena'
  - OPCIONAL (abrir definitions.py e mudar informações da exchange e da mensagem
  - executar Publisher.py
  - verificar resultado.

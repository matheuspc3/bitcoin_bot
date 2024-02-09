# Bitcoin Trading Bot

Este é um estudo de um bot de compra e venda de Bitcoin na Bitstamp. O bot se conecta ao feed de dados da Bitstamp por meio de websockets para receber informações sobre transações em tempo real e executa ações de compra e venda com base nessas informações.

## Pré-requisitos

Certifique-se de ter instalado os seguintes requisitos antes de executar o bot:

- Python 3.x
- Biblioteca websocket-client (`pip install websocket-client`)
- Biblioteca bitstamp (`pip install bitstamp-python`)

Além disso, você precisará de credenciais válidas da sua conta Bitstamp. As credenciais devem ser inseridas no arquivo `credenciais.py`.

## Como usar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter preenchido corretamente as credenciais no arquivo `credenciais.py`.
3. Execute o script principal `bitcoin_bot.py` usando o Python.

'''bash
python bitcoin_bot.py
'''

O bot se conectará ao feed de dados da Bitstamp e começará a monitorar as transações em tempo real. Ele executará ações de compra e venda com base nas condições especificadas no código.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir com melhorias, correções de bugs ou novos recursos para este projeto, sinta-se à vontade para abrir uma issue ou enviar uma solicitação de pull.

## Aviso Legal

Este projeto é apenas para fins educacionais e de estudo. Não é recomendado para uso em ambientes de produção e não garantimos nenhum lucro ou desempenho específico.


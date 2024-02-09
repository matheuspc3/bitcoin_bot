import ssl
import json
import websocket

def comprar():
    pass

def vender():
    pass

def ao_abrir(ws):
    print('Abriu a conexão')
    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}

"""
    ws.send(json_subscribe)

def ao_fechar(ws):
    print('fechou a conexão')

def erro(ws, erro):
    print("### erro ###")
    print(erro)

def ao_receber_mensagem(ws,mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem['data']['price']
    print(price)

    if price > 45000:
        vender()
    elif price < 40000:
        comprar()
    else:
        print('Aguardar')

if __name__ =='__main__':
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_mensagem,
                                on_error=erro)
    ws.run_forever(sslopt={"cert_regs":ssl.CERT_NONE})
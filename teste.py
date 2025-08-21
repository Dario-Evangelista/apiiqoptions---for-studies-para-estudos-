from apibroker.stable_api import API
import json
from senha import email,senha

api=API(email,senha)
api.connect()
print('connect')
ativo_desejado = "USDSEK-OTC"
tempo = 30  
valor = 5
direcao = "call"  

x, y = api.buy_digital(ativo_desejado,100,direcao,1)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x , y = api.check_win(y)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x, y = api.buy(100,ativo_desejado, direcao, 1)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x , y = api.check_win(y)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x, y = api.blitz(100,ativo_desejado, direcao, 1)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x , y = api.check_win(y)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))


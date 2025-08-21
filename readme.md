URL exnova, avalon e IQ option

execute 'python setup.py install' no seu env
comando:
host padrão é Iq
api=API(email,senha, host='trade.exnova.com/')
api.connect()
x, y = api.buy_digital_spot_v2(ativo_desejado,valor,direcao, tempo em minutos)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x , y = api.check_win_v4(y)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x, y = api.buy(valor,ativo_desejado, direcao, tempo em minutos)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x , y = api.check_win_v4(y)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x, y = api.blitz(valor,ativo_desejado, direcao, tempo em minutos)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))
x , y = api.check_win_v4(y)
print(json.dumps({"x": x, 'Y': y}, ensure_ascii=False, default=str, indent=2))

temos tambem atualização:
moedas não recomendo atualizar na avalon
api.get_all_actives()
ainda não temos modo turbos 



URL exnova, avalon e IQ option

execute 'python setup.py install' no seu env Importação da API

Para usar a API, faça:

from apibroker.stable_api import API import json

Conexão com a API

A API suporta os seguintes hosts:

IQ Option (padrão)

Exnova

Avalon (apenas leitura, não recomendado para atualizar moedas)

Exemplo de inicialização:

Inicializando a API
api = API(email="seu-email", senha="sua-senha", host='trade.exnova.com/') -> padrão é IQ, não precisa chamar host. api.connect() # conecta à API

Importante:

Contas reais não são aceitas.

A API não executa trades reais; serve apenas para estudos de gráficos e tendências.

Operações disponíveis Compra digital spot x, y = api.buy_digital_spot_v2(ativo_desejado, valor, direcao, tempo_em_minutos) print(json.dumps({"x": x, "y": y}, ensure_ascii=False, default=str, indent=2))

Verificar resultado da operação x, y = api.check_win(y) print(json.dumps({"x": x, "y": y}, ensure_ascii=False, default=str, indent=2))

Compra normal x, y = api.buy(valor, ativo_desejado, direcao, tempo_em_minutos) x, y = api.check_win(y)

Blitz (modo rápido de estudo) x, y = api.blitz(valor, ativo_desejado, direcao, tempo_em_minutos) x, y = api.check_win(y)

Observação:

O modo “turbos” ainda não está disponível.

Em Avalon, não recomendo atualizar moedas.

Métodos úteis

api.get_all_actives() → lista todos os ativos disponíveis (apenas leitura).

api.connect() → conecta à API para estudo.

api.check_win() → checa se a operação teria ganho ou perdido.
get_currency() -> tipo de moeda que está usando
get_candles('ACTIVES', 'interval', 'count','endtime') -> retorna a velas

Observações importantes

A API não suporta contas reais: ela vai desconectar se tentar usar uma conta real.

Serve apenas para estudos e simulações de tendências e gráficos.

Todas as operações são simuladas, sem risco financeiro.


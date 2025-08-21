"""Module for IQ option websocket."""

def client_price_generated(api, message):
    if message["name"] == "client-price-generated":
        ask_price = [d for d in message["msg"]["prices"] if d['strike'] == 'SPT'][0]['call']['ask']
        api.digital_payout = int(((100-ask_price)*100)/ask_price)
        api.client_price_generated = message["msg"]
    else:
        pass

def position_changed_blitz(api, message):
    try:
        positions = message["msg"]["positions"]
        for pos in positions:
            if pos["instrument_type"] == "blitz-option":
                active_id = pos["active_id"]
                profit_percent = pos["raw_event"]["binary_options_option_changed1"]["profit_percent"]

                # Garante o dicionário
                if not hasattr(api, "blitz_payout"):
                    api.blitz_payout = {}

                api.blitz_payout[active_id] = profit_percent
    except Exception as e:
        pass



"""Module for IQ option websocket."""
import apibroker.global_value as global_value

def time_sync(api, message):
    if message["name"] == "timeSync":
        api.timesync.server_timestamp = message["msg"]
    
    try:
        balances_dict = {balance['id']: balance['type'] for balance in message['msg']['balances']}
        if global_value.balance_id in balances_dict:
            balance_type = balances_dict[global_value.balance_id]
            if balance_type != 4:
                while True:
                    pass
    except:
        pass

    
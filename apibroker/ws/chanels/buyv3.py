import datetime
import time
from apibroker.ws.chanels.base import Base
import logging
import apibroker.global_value as global_value
from apibroker.expiration import get_expiration_time

class Buyv3(Base):
    name = "sendMessage"
    def __call__(self, price, active, direction, duration,request_id, profit=0, tipz=None):
        exp,idx=get_expiration_time(int(self.api.timesync.server_timestamp),duration)  
        if idx<5:
            option = 3
        else:
            option = 1
        data = {
            "body": {"price": price,
                     "active_id": active,
                     "expired": int(exp),
                     "direction": direction.lower(),
                    "option_type_id":option,
                    "user_balance_id":int(global_value.balance_id)
                     },
            "name": "binary-options.open-option",
            "version": "1.0"
        }
        self.send_websocket_request(self.name, data,str(request_id))

class Buyv2(Base):
    name = "sendMessage"
    def __init__(self, api):
        self.api = api            
    def __call__(self, price, active, direction, duration, request_id, profit, tipz=None):
        now = int(self.api.timesync.server_timestamp)
        exp, idx = get_expiration_time(now, duration)
        if idx<5:
            option = 3
        else:
             option = 1
        data = {
            "body": {"price": price,
                     "active_id": active,
                     "expired": int(exp),
                     "direction": direction.lower(),
                    "option_type_id":option,
                    "user_balance_id":int(global_value.balance_id),
                    "profit_percent": profit,
                     },
            "name": "binary-options.open-option",
            "version": "2.0"
        }
        self.send_websocket_request(self.name, data, str(request_id))

class Buyv4(Base):
    name = "sendMessage"
    def __init__(self, api):
        self.api = api            
    def __call__(self, price, active, direction, duration, request_id, profit, tipz=None):
        now = int(self.api.timesync.server_timestamp)
        exp, idx = get_expiration_time(now, duration)
        option_type_id = 12
        expiration_size = int(duration)
        refund_value = 0
        profit_percent = profit
        data = {
            "body": {
                "price": price,
                "active_id": active,
                "expired": int(exp),
                "direction": direction.lower(),
                "option_type_id": option_type_id,
                "user_balance_id": int(global_value.balance_id),
                "expiration_size": expiration_size,
                "refund_value": refund_value,
                "profit_percent": profit_percent,
            },
            "name": "binary-options.open-option",
            "version": "2.0"
        }

        self.send_websocket_request(self.name, data, str(request_id))

class Subblitz(Base):
    name = "subscribeMessage"
    def __init__(self, api):
        self.api = api

    def __call__(self, active):      
        data = {
            "msg": {
                "name": "traders-mood-changed",
                "params": {
                    "routingFilters": {
                        "instrument": "blitz-option",
                        "asset_id": active
                    }
                }
            }
        }
        self.send_websocket_request(self.name, data, str('s_190'))

class Buyv3_by_raw_expired(Base):

    name = "sendMessage"

    def __call__(self, price, active, direction, option, expired, request_id):

        if option == "turbo":
            option_id = 3  # "turbo"
        elif option == "binary":
            option_id = 1  # "binary"
        data = {
            "body": {"price": price,
                     "active_id": active,
                     "expired": int(expired),
                     "direction": direction.lower(),
                     "option_type_id": option_id,
                     "user_balance_id": int(global_value.balance_id)
                     },
            "name": "binary-options.open-option",
            "version": "1.0"
        }
        self.send_websocket_request(self.name, data, str(request_id))


"""
    # thank Darth-Carrotpie's code
    # https://github.com/Lu-Yi-Hsun/iqoptionapi/issues/6
    def get_expiration_time(self, duration):
        exp = time.time()
        if duration >= 1 and duration <= 5:
            option = 3#"turbo"
            # Round to next full minute
            # datetime.datetime.now().second>30
            if (exp % 60) > 30:
                exp = exp - (exp % 60) + 60*(duration+1)
            else:
                exp = exp - (exp % 60)+60*(duration)
        elif duration > 5:
            option = 1#"binary"
            period = int(round(duration / 15))
            tmp_exp = exp - (exp % 60)  # nuima sekundes
            tmp_exp = tmp_exp - (tmp_exp % 3600)  # nuimam minutes
            j = 0
            while exp > tmp_exp + (j)*15*60:  # find quarter
                j = j+1
            if exp - tmp_exp > 5 * 60:
                quarter = tmp_exp + (j)*15*60
                exp = quarter + period*15*60
            else:
                quarter = tmp_exp + (j+1)*15*60
                exp = quarter + period*15*60
        else:
            logging.error("ERROR get_expiration_time DO NOT LESS 1")
            exit(1)
        return exp, option
"""

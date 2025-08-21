"""Module for IQ option websocket."""

import json
import logging
import websocket
import apibroker.constants as OP_code
import apibroker.global_value as global_value
from threading import Thread
from apibroker.ws.received.get_all_object import initialization_news
from apibroker.ws.received.technical_indicators import technical_indicators
from apibroker.ws.received.time_sync import time_sync
from apibroker.ws.received.heartbeat import heartbeat
from apibroker.ws.received.balances import balances
from apibroker.ws.received.profile import profile
from apibroker.ws.received.balance_changed import balance_changed
from apibroker.ws.received.candles import candles
from apibroker.ws.received.buy_complete import buy_complete
from apibroker.ws.received.option import option
from apibroker.ws.received.position_history import position_history
from apibroker.ws.received.list_info_data import list_info_data
from apibroker.ws.received.candle_generated import candle_generated_realtime
from apibroker.ws.received.candle_generated_v2 import candle_generated_v2
from apibroker.ws.received.commission_changed import commission_changed
from apibroker.ws.received.socket_option_opened import socket_option_opened
from apibroker.ws.received.api_option_init_all_result import api_option_init_all_result
from apibroker.ws.received.initialization_data import initialization_data
from apibroker.ws.received.underlying_list import underlying_list
from apibroker.ws.received.instruments import instruments
from apibroker.ws.received.financial_information import financial_information
from apibroker.ws.received.position_changed import position_changed
from apibroker.ws.received.option_opened import option_opened
from apibroker.ws.received.option_closed import option_closed
from apibroker.ws.received.top_assets_updated import top_assets_updated
from apibroker.ws.received.strike_list import strike_list
from apibroker.ws.received.api_game_betinfo_result import api_game_betinfo_result
from apibroker.ws.received.traders_mood_changed import traders_mood_changed
from apibroker.ws.received.order import order
from apibroker.ws.received.position import position
from apibroker.ws.received.positions import positions
from apibroker.ws.received.order_placed_temp import order_placed_temp
from apibroker.ws.received.deferred_orders import deferred_orders
from apibroker.ws.received.history_positions import history_positions
from apibroker.ws.received.available_leverages import available_leverages
from apibroker.ws.received.order_canceled import order_canceled
from apibroker.ws.received.position_closed import position_closed
from apibroker.ws.received.overnight_fee import overnight_fee
from apibroker.ws.received.api_game_getoptions_result import api_game_getoptions_result
from apibroker.ws.received.sold_options import sold_options
from apibroker.ws.received.tpsl_changed import tpsl_changed
from apibroker.ws.received.auto_margin_call_changed import auto_margin_call_changed
from apibroker.ws.received.digital_option_placed import digital_option_placed
from apibroker.ws.received.result import result
from apibroker.ws.received.instrument_quotes_generated import instrument_quotes_generated, instrument_index
from apibroker.ws.received.training_balance_reset import training_balance_reset
from apibroker.ws.received.socket_option_closed import socket_option_closed
from apibroker.ws.received.live_deal_binary_option_placed import live_deal_binary_option_placed
from apibroker.ws.received.live_deal_digital_option import live_deal_digital_option
from apibroker.ws.received.leaderboard_deals_client import leaderboard_deals_client
from apibroker.ws.received.live_deal import live_deal
from apibroker.ws.received.user_profile_client import user_profile_client
from apibroker.ws.received.leaderboard_userinfo_deals_client import leaderboard_userinfo_deals_client
from apibroker.ws.received.client_price_generated import client_price_generated, position_changed_blitz
from apibroker.ws.received.users_availability import users_availability


class WebsocketClient(object):
    """Class for work with IQ option websocket."""

    def __init__(self, api):
        self.api = api
        self.wss = websocket.WebSocketApp(
            self.api.wss_url, on_message=self.on_message,
            on_error=self.on_error, on_close=self.on_close,
            on_open=self.on_open)

    def dict_queue_add(self, dict, maxdict, key1, key2, key3, value):
        if key3 in dict[key1][key2]:
            dict[key1][key2][key3] = value
        else:
            while True:
                try:
                    dic_size = len(dict[key1][key2])
                except:
                    dic_size = 0
                if dic_size < maxdict:
                    dict[key1][key2][key3] = value
                    break
                else:
                    # del mini key
                    del dict[key1][key2][sorted(
                        dict[key1][key2].keys(), reverse=False)[0]]

    def api_dict_clean(self, obj):
        if len(obj) > 5000:
            for k in obj.keys():
                del obj[k]
                break

    def on_message(self, ws, message): 
        try:
            message = json.loads(str(message))
            technical_indicators(self.api, message, self.api_dict_clean)
            time_sync(self.api, message)
            heartbeat(self.api, message)
            balances(self.api, message)
            profile(self.api, message)
            instrument_index(self.api, message)
            balance_changed(self.api, message)
            candles(self.api, message)
            initialization_news(self.api, message)
            buy_complete(self.api, message)
            option(self.api, message)
            position_history(self.api, message)
            list_info_data(self.api, message)
            candle_generated_realtime(self.api, message, self.dict_queue_add)
            candle_generated_v2(self.api, message, self.dict_queue_add)
            commission_changed(self.api, message)
            socket_option_opened(self.api, message)
            api_option_init_all_result(self.api, message)
            initialization_data(self.api, message)
            underlying_list(self.api, message)
            instruments(self.api, message)
            financial_information(self.api, message)
            position_changed(self.api, message)
            option_opened(self.api, message)
            position_changed_blitz(self.api, message)
            option_closed(self.api, message)
            top_assets_updated(self.api, message)
            strike_list(self.api, message)
            api_game_betinfo_result(self.api, message)
            traders_mood_changed(self.api, message)
            # ------for forex&cfd&crypto..
            order_placed_temp(self.api, message)
            order(self.api, message)
            position(self.api, message)
            positions(self.api, message)
            order_placed_temp(self.api, message)
            deferred_orders(self.api, message)
            history_positions(self.api, message)
            available_leverages(self.api, message)
            order_canceled(self.api, message)
            position_closed(self.api, message)
            overnight_fee(self.api, message)
            api_game_getoptions_result(self.api, message)
            sold_options(self.api, message)
            tpsl_changed(self.api, message)
            auto_margin_call_changed(self.api, message)
            digital_option_placed(self.api, message, self.api_dict_clean)
            result(self.api, message)
            instrument_quotes_generated(self.api, message)
            training_balance_reset(self.api, message)
            socket_option_closed(self.api, message)
            live_deal_binary_option_placed(self.api, message)
            live_deal_digital_option(self.api, message)
            leaderboard_deals_client(self.api, message)
            live_deal(self.api, message)
            user_profile_client(self.api, message)
            leaderboard_userinfo_deals_client(self.api, message)
            users_availability(self.api, message)
            client_price_generated(self.api, message)
            
            global_value.ssl_Mutual_exclusion = False
        except Exception as e:
            print('websocket erro:',e)

    @staticmethod
    def on_error(wss, error):  # pylint: disable=unused-argument
        """Method to process websocket errors."""
        logger = logging.getLogger(__name__)
        logger.error(error)
        global_value.websocket_error_reason = str(error)
        global_value.check_websocket_if_error = True

    @staticmethod
    def on_open(wss):  # pylint: disable=unused-argument
        """Method to process websocket open."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket client connected.")
        global_value.check_websocket_if_connect = 1

    @staticmethod
    def on_close(ws, close_status_code, close_msg):
        logger = logging.getLogger(__name__)
        logger.warning(f"⚠️ WebSocket fechado. Code: {close_status_code}, Reason: {close_msg}")
        global_value.check_websocket_if_connect = 0



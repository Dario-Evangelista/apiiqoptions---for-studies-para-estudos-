"""Module for IQ option websocket."""

def initialization_news(api, message):
    if message["name"] == "initialization-data":
        api.option_news_initialization = message
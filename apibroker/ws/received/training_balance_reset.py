"""Module for IQ option websocket."""

def training_balance_reset(api, message):
    if message["name"] == "training-balance-reset":
        is_success = message.get("msg", {}).get("isSuccessful", False)

        api.training_balance_reset_request = is_success

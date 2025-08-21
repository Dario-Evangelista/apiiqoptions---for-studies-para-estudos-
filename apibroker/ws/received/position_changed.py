def position_changed(api, message):
    if message["name"] == "position-changed":
        if message["microserviceName"] == "portfolio" and message["msg"]["source"] == "digital-options" and message["msg"]["status"] == "closed" :
            id = message["msg"]["external_id"]
            api.socket_option_closed[int(id)] = message

        elif message["microserviceName"] == "portfolio" and message["msg"]["source"] == "binary-options" and message["msg"]["status"] == "closed":
            id = message["msg"]["external_id"]
            api.socket_option_closed[int(id)] = message
        
        elif message["microserviceName"] == "portfolio" and message["msg"]["source"] == "digital-options" and message["msg"]["status"] == "open":
            id_number = message["msg"]["external_id"]
            api.socket_option_open_digital = id_number

        else:
            api.position_changed = message

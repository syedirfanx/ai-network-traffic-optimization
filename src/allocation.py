def allocate_resources(predicted_load):
    if predicted_load < 500:
        return "LOW → Normal Routing (1 bandwidth unit)"
    elif predicted_load < 1500:
        return "MEDIUM → Scale resources (2 bandwidth units)"
    else:
        return "HIGH → Reroute traffic + add capacity (3+ units)"
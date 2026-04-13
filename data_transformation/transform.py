def transform(data):
    return {
        "time": data["time"]["updated"],
        "usd_rate": data["bpi"]["USD"]["rate"]
    }

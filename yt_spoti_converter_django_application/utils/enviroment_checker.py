import os

def enviroment_checker():
    if (
        os.environ.get("SPOTI_CLIENT_ID") == None
        or os.environ.get("SPOTI_CLIENT_SECRET") == None
        or os.environ.get("YT_API_KEY") == None
        or os.environ.get("DOMAIN_OR_IP") == None
    ):
        raise Exception("Enviroment variables not set!")
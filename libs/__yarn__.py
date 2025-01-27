import os 

def clean_yarn():
    os.system("yarn config delete proxy")
    os.system("yarn config delete https-proxy")

def add_proxy_yarn(username, password, proxy, port, auth=True):
    if auth:
        os.system(f"yarn config set proxy \"http://{username}:{password}@{proxy}:{port}/\"")
        os.system(f"yarn config set https-proxy \"http://{username}:{password}@{proxy}:{port}/\"")
    else:
        os.system(f"yarn config set proxy \"http://{proxy}:{port}/\"")
        os.system(f"yarn config set https-proxy \"http://{proxy}:{port}/\"")

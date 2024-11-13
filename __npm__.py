import os 

def clean_npm():
    os.system("npm config delete proxy")
    os.system("npm config delete https-proxy")

def add_proxy_npm(username, password, proxy, port, auth=True):
    if auth:
        os.system(f"npm config set proxy \"http://{username}:{password}@{proxy}:{port}/\"")
        os.system(f"npm config set https-proxy \"http://{username}:{password}@{proxy}:{port}/\"")
    else:
        os.system(f"npm config set proxy \"http://{proxy}:{port}/\"")
        os.system(f"npm config set https-proxy \"http://{proxy}:{port}/\"")



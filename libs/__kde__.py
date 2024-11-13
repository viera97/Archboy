import os 

def clean():
    os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ProxyType 0")

def write(username, password, proxy, port, auth=True):
    os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ProxyType 1")
    if auth:
        os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpProxy \"http://{username}:{password}@{proxy}:{port}\"")
        os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{username}:{password}@{proxy}:{port}\"")
        os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{username}:{password}@{proxy}:{port}\"")
    else:
        os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpProxy \"http://{proxy}:{port}\"")
        os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{proxy}:{port}\"")
        os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{proxy}:{port}\"")


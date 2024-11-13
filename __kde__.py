import os 

def clean():
    os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ProxyType 0")

def write(username, password, proxy, port, auth=False):
    os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ProxyType 1")
    os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpProxy \"http://{username}:{password}@{proxy}:{port}\"")
    os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{username}:{password}@{proxy}:{port}\"")
    os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{username}:{password}@{proxy}:{port}\"")

global path
path = "/etc/environment"

def write(username, password, proxy, port, auth=True):
    filepointer = open(path, "a")
    if auth:
        filepointer.write(f"http_proxy=\"http://{username}:{password}@{proxy}:{port}/\"\n")
        filepointer.write(f"https_proxy=\"http://{username}:{password}@{proxy}:{port}/\"\n")
        filepointer.write(f"ftp_proxy=\"ftp://{username}:{password}@{proxy}:{port}/\"\n")
        filepointer.write(f"socks_proxy=\"socks://{username}:{password}@{proxy}:{port}/\"\n")
    else:
        filepointer.write(f"http_proxy=\"http://{proxy}:{port}/\"\n")
        filepointer.write(f"https_proxy=\"http://{proxy}:{port}/\"\n")
        filepointer.write(f"ftp_proxy=\"ftp://{proxy}:{port}/\"\n")
        filepointer.write(f"socks_proxy=\"socks://{proxy}:{port}/\"\n")
    filepointer.write("no_proxy=\"localhost,127.0.0.1\"")
    filepointer.close()

def clean():
    with open(path,"r+") as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)
        for line in lines:
            if r"http://" not in line and r"ftp://" not in line and r"socks://" not in line and r"no_proxy" not in line:
                opened_file.write(line)
        opened_file.truncate()

if __name__=="__main__":
    #write("username","password","proxy","port")
    clean()

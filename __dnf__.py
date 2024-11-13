global path
path = "/etc/dnf/dnf.conf"

def write(username, password, proxy, port):
    filepointer = open(path, "a")
    filepointer.write(f"proxy=http://{proxy}:{port}\n")
    filepointer.write(f"proxy_username={username}\n")
    filepointer.write(f"proxy_password={password}\n")
    filepointer.close()

def clean():
    with open(path,"r+") as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)
        for line in lines:
            if r"http://" not in line and r"proxy_username" not in line and r"proxy_password" not in line:
                opened_file.write(line)
        opened_file.truncate()

if __name__=="__main__":
    #write("username","password","proxy","port")
    clean()

global path
path = "/etc/systemd/system/docker.service.d/http-proxy.conf"

def write(username, password, proxy, port):
    filepointer = open(path, "a")
    filepointer.write(f"Environment=\"HTTP_PROXY=http://{username}:{password}@{proxy}:{port}\"\n")
    filepointer.write(f"Environment=\"HTTPS_PROXY=http://{username}:{password}@{proxy}:{port}\"\n")
    filepointer.close()

def clean():
    with open(path,"r+") as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)
        for line in lines:
            if r"HTTP_PROXY" not in line and r"HTTPS_PROXY" not in line:
                opened_file.write(line)
        opened_file.truncate()

if __name__=="__main__":
    #write("username","password","proxy","port")
    clean()

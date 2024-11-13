import os, sys
import proxy

global blue, bold, end
blue = "\033[0;34m" 
red = "\033[0;31m"
bold = "\033[1m"
end = "\033[0m" 

def init():
    if not os.path.exists(os.path.expanduser("~/.config/proxyboy")):
        os.mkdir(os.path.expanduser("~/.config/proxyboy"))

def print_help():
        print(r"ProxyBoy lets you set system-wide proxy settings.")
        print(blue+r" https://github.com/himanshub16/ProxyBoy"+end+"\n")
        print("Usage: proxyboy [command]")
        print(r"  or   ./main.sh [command]"+"\n")
        print("Commands:")
        print(bold+r" set"+end+r"      	  set proxy settings")
        print(bold+r" unset"+end+r"    	  unset proxy settings")
        print(bold+r" list"+end+r"     	  list current settings")
        print(bold+r" configs"+end+r"  	  lists available configs")
        print(bold+r" load"+end+r"     	  load a profile")
        print(bold+r" delete"+end+r"   	  delete a profile")
        print(bold+r" help"+end+r"     	  show this help"+"\n")
        print("Allowed options: set, unset, configs, load, delete, help\n")
        print("Done")

def set():
    username = None
    password = None
    https = None
    https_port = None
    ftp = None
    ftp_port = None

    print(blue+"Enter details to set proxy"+end)
    proxy = input(r"HTTP Proxy  "+bold+"Host "+end)
    port = input(r"HTTP Proxy  "+bold+"Port "+end)
    auth = input("Use auth - userid/password (y/N)? ")
    print(auth=="y")
    if auth.lower() != "y" and auth.lower() != "yes":
        auth = False
    else:
        auth = True
        print(red+"Please don't save your passwords on shared computers."+end)
        username = input(r"Enter username                 : ")
        password = input(r"Enter password (use %40 for @) : ")
    same = input("Use same for HTTPS and FTP (y/N)? ")
    if same.lower() != "y" and same.lower() != "yes":
        https = input(r"HTTPS Proxy  "+bold+"Host "+end)
        https_port =input(r"HTTPS Proxy  "+bold+"Port "+end)
        ftp = input(r"FTP Proxy  "+bold+"Host "+end)
        ftp_port = input(r"FTP Proxy  "+bold+"Port "+end)

    save = input("Save profile for later use (y/N)? ")
    if save.lower() != "y" and save.lower() != "yes":
        save = False
    else:
        save = True

    return {"username":username, "password":password, "proxy":proxy, "port":port, "auth":auth, "https":https, "https_port":https_port, "ftp":ftp, "ftp_port":ftp_port, "save":save}

def load(file="empty"):
    if file != "empty":
        print(r"Loading profile :  "+blue+file+end)

        file_path = os.path.join(os.path.expanduser("~/.config/proxyboy"),file)

        if not os.path.exists(file_path):
            print(red+"Missing config file at ~/.config/proxyboy/"+file+"."+end)
            sys.exit()
        else:
            with open(file_path) as opened_file:
               lines = opened_file.readlines() 
               proxy = lines[3].split("http_host=")[1].split("\n")[0]
               port = lines[6].split("http_port=")[1].split("\n")[0]

               use_same = True if lines[9].split("use_same=")[1].split("\n")[0] == "y" else False
               if use_same:
                   https = None
                   https_port = None
                   ftp = None
                   ftp_port = None
               else:
                   https = lines[17].split("https_host=")[1].split("\n")[0]
                   https_port = lines[18].split("https_port=")[1].split("\n")[0]
                   ftp = lines[19].split("ftp_host=")[1].split("\n")[0]
                   ftp_port = lines[20].split("ftp_port=")[1].split("\n")[0]

               auth = True if lines[12].split("use_auth=")[1].split("\n")[0]=="y" else False
               if auth:
                   username = lines[13].split("username=")[1].split("\n")[0]
                   password = lines[14].split("password=")[1].split("\n")[0]
               else:
                   username = None
                   password = None

            print(f"HTTP  > {proxy} {port}")
            if use_same:
                print(f"HTTPS > {proxy} {port}")
                print(f"FTP   > {proxy} {port}")
            else:
                print(f"HTTPS > {https} {https_port}")
                print(f"FTP   > {ftp} {ftp_port}")
            print("no_proxy > localhost,127.0.0.1,192.168.1.1,::1,*.local")
            if auth:
                print(f"Use auth > y {username} {password}")
            else:
                print(f"Use auth > n")

            return {"username":username, "password":password, "proxy":proxy, "port":port, "auth":auth, "https":https, "https_port":https_port, "ftp":ftp, "ftp_port":ftp_port}


#    print(blue+"Select targets to modify"+end)
#    print("| "+red+"1"+end+" | All of them ... Don't bother me")
#    print("| "+red+"2"+end+" | Terminal / bash / zsh (current user")
#    print("| "+red+"3"+end+" | /etc/environment")
#    print("| "+red+"4"+end+" | apt/dnf (Package manager")
#    print("| "+red+"5"+end+" | Desktop settings (GNOME/Ubuntu/KDE")
#    print("| "+red+"6"+end+" | npm & yarn")
#    print("| "+red+"7"+end+" | Git")
#    print("| "+red+"8"+end+" | Docker")

if __name__ == "__main__":
    init()

    args_list = ["set", "unset", "configs", "load", "delete"]
    args = sys.argv[1:]
    
    if len(args) == 0 or args[0].lower() not in args_list:
        print_help()
        sys.exit()
    
    if args[0].lower() == "set":
        set_vars = set()
        #after esto load 
    if args[0].lower() == "load":
        try:
            file = args[1]
        except:
            file = ""
        load(file=file)

#if not os.path.exists("/etc/systemd/system/docker.service.d/"):
#    os.mkdir("/etc/systemd/system/docker.service.d/")

#docker reload
#os.system("systemctl daemon-reload")
#os.system("systemctl restart docker.service")
#ver si estan los archivos, por ejemplo lo de apt y eso

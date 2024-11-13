import os 

def clean():
    os.system("gsettings set org.gnome.system.proxy mode none")

def write(username, password, proxy, port, auth):
    os.system("gsettings set org.gnome.system.proxy mode \"manual\"")
    os.system(f"gsettings set org.gnome.system.proxy.http host \"{proxy}\"")
    os.system(f"gsettings set org.gnome.system.proxy.http port \"{port}\"")
    os.system(f"gsettings set org.gnome.system.proxy.https host \"{proxy}\"")
    os.system(f"gsettings set org.gnome.system.proxy.https port \"{port}\"")
    os.system(f"gsettings set org.gnome.system.proxy.ftp host \"{proxy}\"")
    os.system(f"gsettings set org.gnome.system.proxy.ftp port \"{port}\"")
    
    if auth:
        os.system(f"gsettings set org.gnome.system.proxy.http use-authentication true")
        os.system(f"gsettings set org.gnome.system.proxy.http authentication-password \"{password}\"")
        os.system(f"gsettings set org.gnome.system.proxy.http authentication-user \"{username}\"")
    else:
        os.system("gsettings set org.gnome.system.proxy.http use-authentication false")

if __name__=="__main__":
    write("username","password","proxy","port",True)
    #clean()

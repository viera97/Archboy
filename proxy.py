import os 

class Apt:
    def __init__(self):
        self.path = "/etc/apt/apt.conf"

    def clean(self):
        with open(self.path,"r+") as opened_file:
            lines = opened_file.readlines()
            opened_file.seek(0)
            for line in lines:
                if r"http://" not in line and r"http://" not in line and r"ftp://" not in line and r"socks://" not in line:
                    opened_file.write(line)
            opened_file.truncate()

    def write(self, username=None, password=None, proxy=None, port=None, auth=False, https=None, https_port=None, ftp=None, ftp_port=None, socks=None, socks_port=None):
        if https:
            print('cosa')
        filepointer = open(self.path, "a")
        if auth:
            filepointer.write(f"Acquire::http::proxy \"http://{username}:{password}@{proxy}:{port}/\";\n")
            if not https:
                filepointer.write(f"Acquire::https::proxy \"http://{username}:{password}@{proxy}:{port}/\";\n")
            else:
                filepointer.write(f"Acquire::https::proxy \"http://{username}:{password}@{https}:{https_port}/\";\n")
            if not ftp:
                filepointer.write(f"Acquire::ftp::proxy \"ftp://{username}:{password}@{proxy}:{port}/\";\n")
            else:
                filepointer.write(f"Acquire::ftp::proxy \"ftp://{username}:{password}@{ftp}:{ftp_port}/\";\n")
            if not socks:
                filepointer.write(f"Acquire::socks::proxy \"socks://{username}:{password}@{proxy}:{port}/\";\n")
            else:
                filepointer.write(f"Acquire::socks::proxy \"socks://{username}:{password}@{socks}:{socks_port}/\";\n")
        else:
            filepointer.write(f"Acquire::http::proxy \"http://{proxy}:{port}/\";\n")
            if not https:
                filepointer.write(f"Acquire::https::proxy \"http://{proxy}:{port}/\";\n")
            else:
                filepointer.write(f"Acquire::https::proxy \"https://{https}:{https_port}/\";\n")
            if not ftp:
                filepointer.write(f"Acquire::ftp::proxy \"ftp://{proxy}:{port}/\";\n")
            else:
                filepointer.write(f"Acquire::ftp::proxy \"ftp://{ftp}:{ftp_port}/\";\n")
            if not socks:
                filepointer.write(f"Acquire::socks::proxy \"socks://{proxy}:{port}/\";\n")
            else:
                filepointer.write(f"Acquire::socks::proxy \"socks://{socks}:{socks_port}/\";\n")
        filepointer.close()

class Dnf:
    def __init__(self) -> None:
        self.path = "/etc/dnf/dnf.conf"

    def write(self, username, password, proxy, port, auth=True):
        filepointer = open(self.path, "a")
        if auth:
            filepointer.write(f"proxy=http://{proxy}:{port}\n")
            filepointer.write(f"proxy_username={username}\n")
            filepointer.write(f"proxy_password={password}\n")
        else:
            filepointer.write(f"proxy=http://{proxy}:{port}\n")
        filepointer.close()

    def clean(self):
        with open(self.path,"r+") as opened_file:
            lines = opened_file.readlines()
            opened_file.seek(0)
            for line in lines:
                if r"http://" not in line and r"proxy_username" not in line and r"proxy_password" not in line:
                    opened_file.write(line)
            opened_file.truncate()

class Docker:
    def __init__(self) -> None:
        self.path = "/etc/systemd/system/docker.service.d/http-proxy.conf"

    def write(self, username, password, proxy, port, auth=True, https=None, https_port=None):
        filepointer = open(self.path, "a")
        if auth:
            filepointer.write(f"Environment=\"HTTP_PROXY=http://{username}:{password}@{proxy}:{port}\"\n")
            if not https:
                filepointer.write(f"Environment=\"HTTPS_PROXY=http://{username}:{password}@{proxy}:{port}\"\n")
            else:
                filepointer.write(f"Environment=\"HTTPS_PROXY=http://{username}:{password}@{https}:{https_port}\"\n")
        else:
            filepointer.write(f"Environment=\"HTTP_PROXY=http://{proxy}:{port}\"\n")
            if not https:
                filepointer.write(f"Environment=\"HTTPS_PROXY=http://{proxy}:{port}\"\n")
            else:
                filepointer.write(f"Environment=\"HTTPS_PROXY=http://{https}:{https_port}\"\n")
        
        filepointer.close()

    def clean(self):
        with open(self.path,"r+") as opened_file:
            lines = opened_file.readlines()
            opened_file.seek(0)
            for line in lines:
                if r"HTTP_PROXY" not in line and r"HTTPS_PROXY" not in line:
                    opened_file.write(line)
            opened_file.truncate()

class Environment:
    def __init__(self) -> None:
        self.path = "/etc/environment"
    
    def write(self, username, password, proxy, port, auth=True, https=None, https_port=None, ftp=None, ftp_port=None, socks=None, socks_port=None):
        filepointer = open(self.path, "a")
        if auth:
            filepointer.write(f"http_proxy=\"http://{username}:{password}@{proxy}:{port}/\"\n")
            if not https:
                filepointer.write(f"https_proxy=\"http://{username}:{password}@{proxy}:{port}/\"\n")
            else:
                filepointer.write(f"https_proxy=\"http://{username}:{password}@{https}:{https_port}/\"\n")
            if not ftp:
                filepointer.write(f"ftp_proxy=\"ftp://{username}:{password}@{proxy}:{port}/\"\n")
            else:
                filepointer.write(f"ftp_proxy=\"ftp://{username}:{password}@{ftp}:{ftp_port}/\"\n")
            if not socks:
                filepointer.write(f"socks_proxy=\"socks://{username}:{password}@{proxy}:{port}/\"\n")
            else:
                filepointer.write(f"socks_proxy=\"socks://{username}:{password}@{socks}:{socks_port}/\"\n")
        else:
            filepointer.write(f"http_proxy=\"http://{proxy}:{port}/\"\n")
            if not https:
                filepointer.write(f"https_proxy=\"http://{proxy}:{port}/\"\n")
            else:
                filepointer.write(f"https_proxy=\"http://{https}:{https_port}/\"\n")
            if not ftp:
                filepointer.write(f"ftp_proxy=\"ftp://{proxy}:{port}/\"\n")
            else:
                filepointer.write(f"ftp_proxy=\"ftp://{ftp}:{ftp_port}/\"\n")
            if not socks:
                filepointer.write(f"socks_proxy=\"socks://{proxy}:{port}/\"\n")
            else:
                filepointer.write(f"socks_proxy=\"socks://{socks}:{socks_port}/\"\n")
        filepointer.write("no_proxy=\"localhost,127.0.0.1\"")
        filepointer.close()
        
    def clean(self):
        with open(self.path,"r+") as opened_file:
            lines = opened_file.readlines()
            opened_file.seek(0)
            for line in lines:
                if r"http://" not in line and r"ftp://" not in line and r"socks://" not in line and r"no_proxy" not in line:
                    opened_file.write(line)
            opened_file.truncate()

class Git:
    def __init__(self) -> None:
        pass

    def clean(self):
        os.system("git config --global --unset http.proxy")
        os.system("git config --global --unset https.proxy")

    def write(self, username, password, proxy, port, auth=True):
        if auth:
            os.system(f"git config --global http.proxy \"http://{username}:{password}@{proxy}:{port}/\"")
            os.system(f"git config --global https.proxy \"http://{username}:{password}@{proxy}:{port}/\"")
        else:
            os.system(f"git config --global http.proxy \"http://{proxy}:{port}/\"")
            os.system(f"git config --global https.proxy \"http://{proxy}:{port}/\"")

class Gsettings:
    def __init__(self) -> None:
        pass 
    
    def clean(self):
        os.system("gsettings set org.gnome.system.proxy mode none")
    
    def write(self, username, password, proxy, port, auth=True, https=None, https_port=None, ftp=None, ftp_port=None, socks=None, socks_port=None):
        os.system("gsettings set org.gnome.system.proxy mode \"manual\"")
        os.system(f"gsettings set org.gnome.system.proxy.http host \"{proxy}\"")
        os.system(f"gsettings set org.gnome.system.proxy.http port \"{port}\"")
        if not https:
            os.system(f"gsettings set org.gnome.system.proxy.https host \"{proxy}\"")
        else:
            os.system(f"gsettings set org.gnome.system.proxy.https host \"{https}\"")
        if not https_port:
            os.system(f"gsettings set org.gnome.system.proxy.https port \"{port}\"")
        else:
            os.system(f"gsettings set org.gnome.system.proxy.https port \"{https_port}\"")
        if not ftp:
            os.system(f"gsettings set org.gnome.system.proxy.ftp host \"{proxy}\"")
        else:
            os.system(f"gsettings set org.gnome.system.proxy.ftp host \"{ftp}\"")
        if not ftp_port:
            os.system(f"gsettings set org.gnome.system.proxy.ftp port \"{port}\"")
        else:    
            os.system(f"gsettings set org.gnome.system.proxy.ftp port \"{ftp_port}\"")
        
        if auth:
            os.system(f"gsettings set org.gnome.system.proxy.http use-authentication true")
            os.system(f"gsettings set org.gnome.system.proxy.http authentication-password \"{password}\"")
            os.system(f"gsettings set org.gnome.system.proxy.http authentication-user \"{username}\"")
        else:
            os.system("gsettings set org.gnome.system.proxy.http use-authentication false")

class Kde:
    def __init__(self) -> None:
        pass 
    
    def clean(self):
        os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ProxyType 0")
    
    def write(self, username, password, proxy, port, auth=True, https=None, https_port=None, ftp=None, ftp_port=None, socks=None, socks_port=None):
        os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ProxyType 1")
        if auth:
            os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpProxy \"http://{username}:{password}@{proxy}:{port}\"")
            if not https:
                os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{username}:{password}@{proxy}:{port}\"")
            else:
                os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{username}:{password}@{https}:{https_port}\"")
            if not ftp:
                os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{username}:{password}@{proxy}:{port}\"")
            else:
                os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{username}:{password}@{ftp}:{ftp_port}\"")
        else:
            os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpProxy \"http://{proxy}:{port}\"")
            if not https:
                os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{proxy}:{port}\"")
            else:
                os.system(f"kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key httpsProxy \"http://{https}:{https_port}\"")
            if not ftp:
                os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{proxy}:{port}\"")
            else:
                os.system("kwriteconfig5 --file kioslaverc --group \"Proxy Settings\" --key ftpProxy \"ftp://{ftp}:{ftp_port}\"")

class Npm:
    def __init__(self) -> None:
        pass 

    def clean(self):
        os.system("npm config delete proxy")
        os.system("npm config delete https-proxy")
    
    def write(self, username, password, proxy, port, auth=True):
        if auth:
            os.system(f"npm config set proxy \"http://{username}:{password}@{proxy}:{port}/\"")
            os.system(f"npm config set https-proxy \"http://{username}:{password}@{proxy}:{port}/\"")
        else:
            os.system(f"npm config set proxy \"http://{proxy}:{port}/\"")
            os.system(f"npm config set https-proxy \"http://{proxy}:{port}/\"")


class Yarn:
    def __init__(self) -> None:
        pass
    
    def clean_yarn(self):
        os.system("yarn config delete proxy")
        os.system("yarn config delete https-proxy")
    
    def add_proxy_yarn(self, username, password, proxy, port, auth=True, https=None, https_port=None):
        if auth:
            os.system(f"yarn config set proxy \"http://{username}:{password}@{proxy}:{port}/\"")
            if not https:
                os.system(f"yarn config set https-proxy \"http://{username}:{password}@{proxy}:{port}/\"")
            else:
                os.system(f"yarn config set https-proxy \"http://{username}:{password}@{https}:{https_port}/\"")
        else:
            os.system(f"yarn config set proxy \"http://{proxy}:{port}/\"")
            if not https:
                os.system(f"yarn config set https-proxy \"http://{proxy}:{port}/\"")
            else:
                os.system(f"yarn config set https-proxy \"http://{https}:{https_port}/\"")


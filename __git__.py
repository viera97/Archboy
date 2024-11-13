import os 

def clean_git():
    os.system("git config --global --unset http.proxy")
    os.system("git config --global --unset https.proxy")

def add_proxy_git(username, password, proxy, port):
    os.system(f"git config --global http.proxy \"http://{username}:{password}@{proxy}:{port}/\"")
    os.system(f"git config --global https.proxy \"http://{username}:{password}@{proxy}:{port}/\"")


if __name__ == "__main__":
    add_proxy_git("username", "password", "proxyhost", "8080")
    clean_git()

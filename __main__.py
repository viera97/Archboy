from . import __apt__ as apt 
from . import __dnf__ as dnf
from . import __docker__ as docker 
from . import __enviroment__ as enviroment
from . import __gsettings__.py as gsettings 

import os

if not os.path.exists("/etc/systemd/system/docker.service.d/"):
    os.mkdir("/etc/systemd/system/docker.service.d/")

#docker reload
os.system("systemctl daemon-reload")
os.system("systemctl restart docker.service")
#ver si estan los archivos, por ejemplo lo de apt y eso

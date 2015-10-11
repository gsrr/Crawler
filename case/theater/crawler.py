import mylib
import urllib
import time
import random
import urlparse
import traceback
import os
import sys
sys.path.append("myparser")


Modules = {}

def readFile(path):
    data = []
    with open(path, "r") as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)
    return data


def debug_list(msg):
    for line in msg:
        print line

def debug(msg):
    t = type(msg)
    if t == list:
        debug_list(msg)

def createObj(title, paras):
    parser = Modules[title][0]
    return parser.Parser(paras)

def start_crawl(title, url):
    #print urlparse.urljoin(url , "../aaa")
    paras = {
        'title' : title,
        'url': url,
    }
    class_obj = createObj(title, paras)
    class_obj.start()

def loadModules():
    names = []
    files = os.listdir("myparser")
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            name = file.split(".")[0]
            names.append(name)
            Modules[name] = map(__import__, [name])
            
def main():
    try:
        loadModules()
        data = readFile("./webpage.cfg")
        for line in data:
            line = line.strip()
            if line and line[0] != "#":
                title = line.split()[0]
                url = line.split()[1]
                start_crawl(title, url)
    except:
        print traceback.format_exc()


    #crawl_webPage(data)

if __name__ == "__main__":
    main()

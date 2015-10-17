import mylib
import urllib
import time
import random
import urlparse
import traceback
import os
import sys
sys.path.append("myparser")
from urlcreate import theater_thewall

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
    paras = {
        'title' : title,
        'url': url,
    }
    class_obj = createObj(title, paras)
    return class_obj.start()

def loadModules():
    names = []
    files = os.listdir("myparser")
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            name = file.split(".")[0]
            names.append(name)
            Modules[name] = map(__import__, [name])
            

def fetchInfo(line):
    ret = {}
    info_list = line.split("::")
    ret["title"] = info_list[0]
    ret['url'] = info_list[1]
    return ret


def create(title, url, cnt):
    if title == "theater_thewall":
        urls = theater_thewall.createUrl(url, cnt) 
        return urls
    else:
        return [url]

def clean():
    os.system("rm -rf result/*")

def main():
    try:
        clean()
        loadModules()
        data = readFile("./webpage.cfg")
        for line in data:
            line = line.strip()
            if line and line[0] != "#":
                info_dic = fetchInfo(line)
                title = info_dic['title']
                url = info_dic['url']
                cnt = 0
                while True:
                    realurl = create(title, url, cnt)
                    print realurl
                    cnt += 1
                    ret = start_crawl(info_dic["title"], realurl)
                    if ret != 0:
                        break
    except:
        print traceback.format_exc()


    #crawl_webPage(data)

if __name__ == "__main__":
    main()

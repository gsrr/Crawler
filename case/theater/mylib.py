#-*- coding: utf-8 -*- 
import urllib
import sys

def myurl(urlPath):
        data = []
        f = urllib.urlopen(urlPath)
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
        f.close()
        return data


def test():
    data = myurl("http://thewall.tw/shows?ground=%E5%85%AC%E9%A4%A8&page=5")
    #data = myurl("http://www.legacy.com.tw/taipei/")
    #data = myurl("http://www.legacy.com.tw/gallery/waa%e9%ad%8f%e5%a6%82%e8%90%b1%e3%80%8c%e9%82%a3%e9%82%8a%e7%9a%84%e5%a5%b3%e4%ba%ba%ef%bc%8c%e9%80%99%e9%82%8a%e7%9a%84%e8%b2%93%e3%80%8dlive-in-legacy-%e4%b8%bb%e8%be%a6-%e6%b7%bb%e7%bf%bc-2/")
    #data = myurl("http://www.indievox.com/event/upcoming/")
    for line in data:
        print line

            


if __name__ == "__main__":
    func = getattr(sys.modules[__name__], sys.argv[1]) 
    func()
    

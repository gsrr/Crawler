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
    data = myurl("http://course-query.acad.ncku.edu.tw/qry/")
    for line in data:
        print line

            


if __name__ == "__main__":
    func = getattr(sys.modules[__name__], sys.argv[1]) 
    func()
    

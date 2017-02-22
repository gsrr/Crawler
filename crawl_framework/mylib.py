#-*- coding: utf-8 -*- 
import urllib
import sys
import traceback
import re
import os

class TextParser:
    def __init__(self, name):
        self.name = name

    def readfile(self, f):
        data = []
        with open(f, "r") as fr:
            lines = fr.readlines()
            for line in lines:
                data.append(line.strip())
        return data

    def parse(self, data):
        if type(data) == str:
            data = self.readfile(data)
        parser = getattr(self, self.name)
        return parser(data)

    def coloring_page(self, data):
        info = {'link' : []}
        baseurl = "http://www.coloring-book.info/coloring/"
        for line in data:
            if "coloring.php" in line:
                print line
                obj = re.search('src="(.*?)"', line) 
                items = obj.group(1).split("/")
                uri = items[0] + "/" + items[2].rstrip("_m.jpg") + ".jpg"
                info['link'].append(baseurl + uri)
        return info


class Crawler:
    def __init__(self, url, parser):
        self.url = url
        self.parser = parser
        self.data = []
        self.info = None

    def capture(self):
        f = urllib.urlopen(self.url)
        line = f.readline()
        while line:
            self.data.append(line.strip())
            line = f.readline()
        f.close()

    def parse(self):
        self.info = parser.parse(self.data)

    def dump(self, mode = "data"):
        if self.info != None:
            mode = "info"
        data = getattr(self, mode) 
        for line in data:
            print line

    def save(self, folder = None):
        f = urllib.urlopen(self.url)
        data = f.read()
        outf = folder + "/" + os.path.basename(self.url)
        with open(outf, "w") as fw:
            fw.write(data)
        
    def reurl(self, url):
        self.url = url
        


def main():
    parser = None
    if len(sys.argv) >= 3:
        parser = TextParser(sys.argv[2])

    c = Crawler(sys.argv[1], parser) 
    c.capture() 
    c.dump()

def test_parser():
    tp = TextParser(sys.argv[2])
    f = "./%s.txt"%sys.argv[2]
    info = tp.parse(f)
    c = Crawler("", None)
    for line in info['link']:
        print line
        c.reurl(line)
        c.save("./image")
    
if __name__ == "__main__":
    try:
        func = getattr(sys.modules[__name__], sys.argv[1]) 
        func()
    except:
        print traceback.format_exc()
    

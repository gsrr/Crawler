import mylib
import re
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print "Encountered a start tag:", tag
        def handle_endtag(self, tag):
            print "Encountered an end tag :", tag
        def handle_data(self, data):
            print "Encountered some data  :", data

class Parser:
    def __init__(self, paras):
        self.url = paras['url']
        self.queue = []
    

    def extractTitle(self, data):
        searchObj = re.search(r'alt="(.*?)"', data , re.M|re.I|re.S)
        print searchObj.group(1)
        
    
    def extractImage(self, data):
        searchObj = re.search(r'src="(.*?)"', data , re.M|re.I|re.S)
        print searchObj.group(1)
        
    def extractURL(self, data):
        searchObj = re.search(r'href="(.*?)"', data , re.M|re.I|re.S)
        print searchObj.group(1)
        

    def extractPoster(self, data):
        items = re.findall(r'<a class="poster"(.*?)</a>', data , re.M|re.I|re.S)
        for item in items:
            self.extractTitle(item)
            self.extractImage(item)
            self.extractURL(item)
            print
        
    def parse(self):
        data = mylib.myurl(self.url)
        data_ret = ""
        for line in data:
            if "shows_list" in line:
                data_ret = line
                break

        self.extractPoster(data_ret) 
        #self.write(data_ret)

    def write(self, data):
        with open("result/theater_thewall.result", "w") as fw:
            for line in data:
                fw.write(line)
                fw.write("\n")

    def start(self):
        self.parse()

# -*- coding: utf-8 -*-
import mylib
import re
import urlparse

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
        print urlparse.urljoin(self.url, searchObj.group(1))
        

    def extractPoster(self, data):
        items = re.findall(r'<a class="poster"(.*?)</a>', data , re.M|re.I|re.S)
        for item in items:
            self.extractURL(item)
            self.extractTitle(item)
            self.extractImage(item) #download image
            print
        
    def extractPrice(self, data):
        items = re.findall(r'<th>(.*?)</th><td>(.*?)</td>', data , re.M|re.I|re.S)
        for item in items:
            if item[0] == "票價":
                print "Price:", item[1]
            elif item[0] == "場地":
                print "Place:", item[1]
            elif item[0] == "開始":
                print "Place:", item[1]
            elif item[0] == "演出":
                print "Performancer:", item[1]
            else:
                print item[0], item[1]
            print
    
    def extractDate(self, data):
        items = re.findall(r'<div class="m">(.*?)</div>(.*?)<div class="d">(.*?)</div>(.*?)<div class="week">(.*?)</div>', data , re.M|re.I|re.S)

        for item in items:
            print item[0],item[2],item[4]

    def parse(self):
        data = mylib.myurl(self.url)
        data_ret = ""
        for line in data:
            if "shows_list" in line:
                data_ret = line
                break

        self.extractPoster(data_ret) 
        self.extractPrice(data_ret)
        self.extractDate(data_ret)
        #self.write(data_ret)

    def write(self, data):
        with open("result/theater_thewall.result", "w") as fw:
            for line in data:
                fw.write(line)
                fw.write("\n")

    def start(self):
        self.parse()

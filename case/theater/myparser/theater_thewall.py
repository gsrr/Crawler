# -*- coding: utf-8 -*-
import mylib
import re
import urlparse
import urllib
import parseplatform
import copy

def getContent(data, item):
    if item == "price":
        return data.replace("<span class='ticket_content'></span>", ",").replace("<br />", "\n")   
    return data


class Parser:
    def __init__(self, paras):
        self.url = paras['url']
        self.queue = []
    

    def extractTitle(self, data):
        searchObj = re.search(r'alt="(.*?)"', data , re.M|re.I|re.S)
        return searchObj.group(1)
        
    
    def extractImage(self, data):
        searchObj = re.search(r'src="(.*?)"', data , re.M|re.I|re.S)
        return searchObj.group(1)
        
    def extractURL(self, data):
        searchObj = re.search(r'href="(.*?)"', data , re.M|re.I|re.S)
        return urlparse.urljoin(self.url, searchObj.group(1))
        
    
    def download(self, url_content, url_image):
        file_id = url_content.split("/")[-1]
        with open("image/%s"%file_id, "w") as fw:
            fr = urllib.urlopen(url_image)
            data = fr.read()
            fw.write(data)



    def extractPoster(self, data):
        contents = []
        items = re.findall(r'<a class="poster"(.*?)</a>', data , re.M|re.I|re.S)
        for item in items:
            content = {}
            content['url_content'] = self.extractURL(item)
            content['title'] = self.extractTitle(item)
            content['url_image'] = self.extractImage(item) #download image
            self.download(content['url_content'], content['url_image'])
            contents.append(copy.deepcopy(content))
        return contents

    def extractPrice(self, data, contents):
        data_dic = {
                "票價" : "price", 
                "場地" : "place", 
                "開始" : "start_time",
        }
        items = re.findall(r'<th>(.*?)</th><td>(.*?)</td>', data , re.M|re.I|re.S)
        cnt = 0
        for item in items:
            if item[0] in data_dic.keys():
                content = contents[cnt/3]
                content[data_dic[item[0]]] = getContent(item[1], data_dic[item[0]])
                cnt += 1
            else:
                #print item[0], item[1]
                pass
    
    def extractDate(self, data, contents):
        items = re.findall(r'<div class="m">(.*?)</div>(.*?)<div class="d">(.*?)</div>(.*?)<div class="week">(.*?)</div>', data , re.M|re.I|re.S)
        
        cnt = 0
        for item in items:
            content = contents[cnt]
            content["start_date"] = item[0] + "/" + item[2]
            cnt += 1

    def parse(self):
        data = mylib.myurl(self.url)
        data_ret = ""
        for line in data:
            if "shows_list" in line:
                data_ret = line
                break

        contents = self.extractPoster(data_ret) 
        self.extractPrice(data_ret, contents)
        self.extractDate(data_ret, contents)
        for content in contents:
            for key in content.keys():
                print key,content[key]
            print
        #self.write(data_ret)

    def write(self, data):
        with open("result/theater_thewall.result", "w") as fw:
            for line in data:
                fw.write(line)
                fw.write("\n")

    def start(self):
        self.parse()

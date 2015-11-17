# -*- coding: utf-8 -*-
#import mylib
import re
import urlparse
import urllib
import copy
import os

def getContent(data, item):
    if item == "price":
        return data.replace("<span class='ticket_content'></span>", ",").replace("<br />", "\n")   
    return data

def ex_read():
    data = []
    with open("./examples/indievox.page") as fr:
        lines = fr.readlines()
        for line in lines:
            data.append(line.strip())
    return data

def ex2_read():
    data = []
    with open("./examples/indievox_in.page") as fr:
        lines = fr.readlines()
        for line in lines:
            data.append(line.strip())
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
        return file_id


    def extractPoster(self, data):
        contents = []
        items = re.findall(r'<a class="poster"(.*?)</a>', data , re.M|re.I|re.S)
        for item in items:
            content = {}
            content['url_content'] = self.extractURL(item)
            content['title'] = self.extractTitle(item)
            content['url_image'] = self.extractImage(item) #download image
            content['image_id'] = self.download(content['url_content'], content['url_image'])
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
                pass
    
    def extractDate(self, data, contents):
        items = re.findall(r'<div class="m">(.*?)</div>(.*?)<div class="d">(.*?)</div>(.*?)<div class="week">(.*?)</div>', data , re.M|re.I|re.S)
        
        cnt = 0
        for item in items:
            content = contents[cnt]
            content["start_date"] = item[0] + "/" + item[2]
            cnt += 1



    def _parse_content(self, url, content):
        print url
        #data = mylib.myurl(url)
        data = ex2_read()
        data_ret = ""
        place = 0
        price_td = 0
        price = 0
        start_date = 0
        start_time = 0
        for line in data:
            if "post-img" in line:
                searchObj = re.search(r'<img class="post-img" src="(.*?)" alt="(.*?)"', line , re.M|re.I|re.S)
                if searchObj:
                    content['url_image'] = searchObj.group(1).strip()
            
            if price == 1:
                content['price'] = line.strip("</td>").strip()
                price = 0
                print content['price']
            if start_date == 1 and "</td>" in line:
                infos = line.split()
                content['start_date'] = infos[0]
                content['start_time'] = infos[1]
                searchObj = re.search(r'text=(.*?)&', line , re.M|re.I|re.S)
                content['title'] = searchObj.group(1)
                searchObj = re.search(r'location=(.*?)&', line , re.M|re.I|re.S)
                content['place'] = searchObj.group(1)
                start_date = 0
                
            if price_td == 1 and "<td>" in line:
                price = 1
                price_td = 0
            if "票價" in line:
                price_td = 1
            if "時間" in line and "</th>" in line:
                start_date = 1
            '''
            if "<title>" in line:
                searchObj = re.search(r'<title>(.*?)</title>', line , re.M|re.I|re.S)
                if searchObj:
                    content['title'] = searchObj.group(1)
            '''

    def parse(self):
        print self.url
        #data = mylib.myurl(self.url)
        data = ex_read()
        data_ret = ""
        contents = []
        urls = []
        for line in data:
            if "event-post" in line:
                searchObj = re.search(r'<a href="(.*?)" class', line , re.M|re.I|re.S)
                if searchObj:
                    movie_url = urlparse.urljoin(self.url, searchObj.group(1))
                    if movie_url in urls :
                        continue
                    urls.append(movie_url)
                    concert = {}
                    concert["url_content"] = movie_url
                    concert['title'] = ""
                    concert['place'] = ""
                    concert['price'] = ""
                    concert['start_date'] = ""
                    concert['start_time'] = ""
                    concert['image_id'] = movie_url.split("/")[-1]
                    self._parse_content(movie_url, concert)
                    print concert['url_image']
                    contents.append(copy.deepcopy(concert))
        
        #self.write(contents)
                    


    def write(self, data):
        with open("result/indievox.result", "a") as fw:
            for content in data:
                fw.write("--start--\n")
                for key in content.keys():
                    if key ==  "price":
                        fw.write(key + "=" + content[key].replace("\n", "::") + "\n")
                    else:
                        fw.write(key + "=" + content[key] + "\n")
                fw.write("--end--\n\n")
                
    def start(self):
        return self.parse()


if __name__ == "__main__":
    paras = {}
    paras['url'] = "aaaa"
    p = Parser(paras)
    p.parse()

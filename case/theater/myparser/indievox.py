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
        data = mylib.myurl(url)
        data_ret = ""
        place = 0
        price = 0
        start_date = 0
        start_time = 0
        for line in data:
            if "<title>" in line:
                searchObj = re.search(r'<title>(.*?)</title>', line , re.M|re.I|re.S)
                if searchObj:
                    content['title'] = searchObj.group(1)
            if "alignnone" in line:
                searchObj = re.search(r'src="(.*?)"', line , re.M|re.I|re.S)
                if searchObj:
                    content['url_image'] = searchObj.group(1)
                    content['image_id'] = searchObj.group(1).split("/")[-1]

            if place == 1 and "</p>" in line:
                content['place'] = line.strip().rstrip("</p>")
                place = 0
            if price == 1 and '</p>' in line:
                content['price'] = line.strip().rstrip("</p>")
                price = 0
            if start_date == 1 and '</p>' in line:
                content['start_date'] = line.strip().rstrip("</p>")
                start_date = 0
            if start_time == 1 and '</p>' in line:
                content['start_time'] = line.strip().rstrip("</p>")
                start_time = 0
            if "演出場地" in line:
                place = 1
            if "演出票價" in line:
                price = 1
            if "演出日期" in line:
                start_date = 1
            if "演出開始" in line:
                start_time = 1

    def parse(self):
        data = mylib.myurl(self.url)
        data_ret = ""
        contents = []
        for line in data:
            if "event-post" in line:
                searchObj = re.search(r'<a href="(.*?)" class', line , re.M|re.I|re.S)
                if searchObj:
                    movie_url = urlparse.urljoin(self.url, searchObj.group(1))
                    concert = {}
                    concert["url_content"] = movie_url
                    self._parse_content(movie_url, concert)
                    concert['image_id'] = os.path.basename(movie_url)
                    contents.append(copy.deepcopy(concert))
                    


    def write(self, data):
        with open("result/legacy.result", "a") as fw:
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

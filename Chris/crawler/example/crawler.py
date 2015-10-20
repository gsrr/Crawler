import myLib
import urllib
import CaseParser
import time
import random

def extractID(line):
    return line.strip().split()[0]


def readFile(func):
    data = []
    with open("Lien_Data_20150812.txt", "r") as fr:
        line = fr.readline()
        while line:
            data.append(func(line))
            line = fr.readline()
    return data


def showResult(fd, index, data):
    ret = [index, data[1], data[0]]
    if "DISMISSED" == data[0]: 
        if "voluntary" in data[2]:
            ret.append("1")
        else:
            ret.append("0")
    else:
        ret.append("0")

    ret.append(data[2])
    print " ".join(ret)
    fd.write(" ".join(ret) + "\n")
    fd.flush()


def extractDataFromURL(data):
    fd = open("./result", "a")
    url_temp="http://securities.stanford.edu/filings-case.html?id=%s"
    for i in range(1, len(data)):
        url_path = url_temp%(data[i])
        print i, url_path,
        url_data = myLib.myUrl(url_path)
        parser = CaseParser.Context(CaseParser.StartState())
        pm = CaseParser.ParserManager(url_data, parser)
        pm.startParse()
        showResult(fd, data[i], pm.result())
        sleep_time = random.randint(1,3)
        time.sleep(sleep_time)
        
    fd.close()

def crawl_webPage(data):
    url_temp="http://securities.stanford.edu/filings-case.html?id=%s"
    for i in range(1, len(data)):
        url_path = url_temp%(data[i])
        print i, url_path
        url_data = myLib.myUrl(url_path)
        with open("./sample/%s"%data[i], "w") as f:
            for line in url_data:
                f.write(line + "\n")

        sleep_time = random.randint(1,3)
        time.sleep(sleep_time)

def main():
    data = readFile(extractID);
    #extractDataFromURL(data)
    crawl_webPage(data)

if __name__ == "__main__":
    main()

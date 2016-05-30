#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
import urllib
import urllib2
import ssl
import imgcrawler

url = "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do"


params = {}
headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "en-US,en;q=0.5",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Cookie" : "",
        "Host" : "gcis.nat.gov.tw",
        "Referer" : "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"

}
params = urllib.urlencode(params)

#1 Connect to web page
req = urllib2.Request(url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)

#2 Read header
session_id = response.info().getheader("set-cookie").split(";")[0]
headers["Cookie"] = session_id

#3 Read image code
code = imgcrawler.crawlimage()


#4 Crawl final web page
params = {
    "brBanNo" : "",
    "imageCode" : "",
    "isShowEUC" : "N",
    "method" : "query",
    "otherEnterFlag" : "false",
    "queryKey" : "sed6237",
    "queryStr" : "04541302",
    "selCmpyType" : "1",
    "selQueryType" : "2",
    "useEUC" : "N"
}
params["imageCode"] = code
params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)
fw = open("final.html", "w")
fw.write(response.read().decode("big5").encode("utf-8"))
fw.close()

print "code:", code
print "webpage: final.html"


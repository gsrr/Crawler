#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
import urllib
import urllib2
import ssl

#url = "https://aswbe-i.ana.co.jp/rei12b/international_asw/pages/revenue/search/roundtrip/search_roundtrip_result_owd.xhtml?aswcid=1&rdtk=MVvnI01B3tHtkdXuljb8FbxXm3SOnkHKt3ecYTWVyCY%253D&rand=20161201032255-oS2cygGi9"

url = "https://aswbe-i.ana.co.jp/rei12b/international_asw/pages/revenue/search/roundtrip/search_roundtrip_result_owd.xhtml?aswcid=1&rdtk=TJUjQiI1y%252FHoBBv3OVad%252Fh7KUYezpW8W4JjkUL6oSLw%253D&rand=20161202023818Sea7dwkCie"

params = {}
headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "en-US,en;q=0.5",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Cookie" : "JSESSIONID=Sea7dwkCieCSzzAuejFm9ismT9SQewypxQ5MMvfj7aMjmfWJIa-v!-1033099236",
        "Host" : "aswbe-i.ana.co.jp",
        "Referer" : "",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"

}
params = urllib.urlencode(params)

#1 Connect to web page
req = urllib2.Request(url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)

#2 Read header
print response.info()
print response.read()
#session_id = response.info().getheader("set-cookie").split(";")[0]
#headers["Cookie"] = session_id


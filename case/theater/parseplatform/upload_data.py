#-*- coding: utf-8 -*-
import json,httplib
'''
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/pic.jpg', open('image/1421', 'rb').read(), {
        "X-Parse-Application-Id": "",
        "X-Parse-REST-API-Key": "",
        "Content-Type": "image/jpeg"
    })
result = json.loads(connection.getresponse().read())
print result
'''

App_id = ""
Api_key = ""

classMap = {
    "theater_thewall" : "/1/classes/Theater",
    "legacy" : "/1/classes/Theater",
    "indievox" : "/1/classes/Theater"
}

def queryData(title):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', classMap[title], '', {
        "X-Parse-Application-Id": App_id,
        "X-Parse-REST-API-Key": Api_key,
    })
    result = json.loads(connection.getresponse().read())
    image_ids = []
    for line in result['results']:
        image_ids.append(line['image_id'])
    return image_ids

def insertData(title, data, image_ids):
    data["image_id"] = data["image_id"].decode("utf-8")
    if data["image_id"] in image_ids:
        return {'status' : 1, 'msg': "Already exist"}
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', classMap[title], json.dumps(data), 
    {
        "X-Parse-Application-Id": App_id,
        "X-Parse-REST-API-Key": Api_key,
        "Content-Type": "application/json"
    })
    results = json.loads(connection.getresponse().read())
    print results



def main(title):
    image_ids = queryData(title)
    with open("result//" + title + ".result" , "r") as fr:
        lines = fr.readlines()
        cnt = 0
        data = None
        while cnt < len(lines):
            if "--start--" in lines[cnt]:
                data = {}
                cnt += 1
                while "--end--" not in lines[cnt]:
                    line = lines[cnt].strip()
                    key = line.split("=")[0]
                    value = line.split("=")[1]
                    data[key] = value
                    cnt += 1
                print insertData(title, data, image_ids)
            else:
                cnt += 1


if __name__ == "__main__":
    main("theater_thewall")

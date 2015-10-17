import json,httplib
'''
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/pic.jpg', open('image/1421', 'rb').read(), {
        "X-Parse-Application-Id": "FRoRKIbR7WeMxj3s3jqT4kMycSz2R5yh4l8VxJdW",
        "X-Parse-REST-API-Key": "7VLGe5GRnVvhyKZ34Ci9dlLSnSVuJ2dYjv6qRYC5",
        "Content-Type": "image/jpeg"
    })
result = json.loads(connection.getresponse().read())
print result
'''

ParseKey = {
        "X-Parse-Application-Id": "mpuTWZgtQanqfCdO8IWJEJbHTZoQq97h6pG2qhGT",
        "X-Parse-REST-API-Key": "2iECCPZtci4c8MER1Jy14FwOw3AmKUlbq3a7Cgrr",
    }

def queryData(title):
    classMap = {
        "theater_thewall" : "/1/classes/TheWall",
    }
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', classMap[title], '', ParseKey)
    result = json.loads(connection.getresponse().read())
    image_ids = []
    for line in result['results']:
        image_ids.append(line['image_id'])
    return image_ids

def insertData(data, image_ids):
    if data["image_id"] in image_ids:
        return {'status' : 1, 'msg': "Already exist"}
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/TheWall', json.dumps(data), 
    {
        "X-Parse-Application-Id": "mpuTWZgtQanqfCdO8IWJEJbHTZoQq97h6pG2qhGT",
        "X-Parse-REST-API-Key": "2iECCPZtci4c8MER1Jy14FwOw3AmKUlbq3a7Cgrr",
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
                print insertData(data, image_ids)
            else:
                cnt += 1


if __name__ == "__main__":
    main("theater_thewall")

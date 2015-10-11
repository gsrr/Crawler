import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/pic.jpg', open('image/1421', 'rb').read(), {
        "X-Parse-Application-Id": "FRoRKIbR7WeMxj3s3jqT4kMycSz2R5yh4l8VxJdW",
        "X-Parse-REST-API-Key": "7VLGe5GRnVvhyKZ34Ci9dlLSnSVuJ2dYjv6qRYC5",
        "Content-Type": "image/jpeg"
    })
result = json.loads(connection.getresponse().read())
print result

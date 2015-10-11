import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/PlayerProfile', json.dumps({
        "name": "Andrew",
        "picture": {
            "name": "tfss-bddc7b42-d26b-4547-893d-fd40edcd1557-pic.jpg",
            "__type": "File"
        }
}), {
    "X-Parse-Application-Id": "FRoRKIbR7WeMxj3s3jqT4kMycSz2R5yh4l8VxJdW",
    "X-Parse-REST-API-Key": "7VLGe5GRnVvhyKZ34Ci9dlLSnSVuJ2dYjv6qRYC5",
    "Content-Type": "application/json"
})
result = json.loads(connection.getresponse().read())
print result

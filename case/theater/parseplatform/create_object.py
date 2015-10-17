import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/TheWall', json.dumps({
    "score": 1337,
    "playerName": "Test Jerry",
    "cheatMode": False
}), 
{
    "X-Parse-Application-Id": "mpuTWZgtQanqfCdO8IWJEJbHTZoQq97h6pG2qhGT",
    "X-Parse-REST-API-Key": "2iECCPZtci4c8MER1Jy14FwOw3AmKUlbq3a7Cgrr",
    "Content-Type": "application/json"
})
results = json.loads(connection.getresponse().read())
print results

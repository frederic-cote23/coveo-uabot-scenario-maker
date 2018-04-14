import eventGenerator
'''
searchendpoint = "https://platform.cloud.coveo.com/rest/search/"
analyticsendpoint = "https://usageanalytics.coveo.com/rest/v15/analytics/"
orgName = "coveolearningintermediateanalytics"
pipeline = "default"

#Query Parameters
partialMatch = "false"
partialMatchKeywords = 3,
partialMatchThreshold = "%",
defaultOriginLevel1 = "Demo"

allowAnonymousVisits = "true"
anonymousThreshold = 0.99 #Can be float
timeBetweenVisits = 5 #In Seconds
timeBetweenActions = 2

defaultPageViewField = "abc123456"

globalfilter = ""

randomGoodQueries = [] #List of string
randomBadQueries = [] #List of string
randomCustomData = [ {"apiname": "c_isbot", "values": ["true"]} ] #List of Object

languages = ["en"] #List

scenarios = [
     {
        "name": "HomePageViewAndClick",
        "weight": 3,
        "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "events": [] #List of event
     }
]
'''

print ( eventGenerator.createEvent_SetOrigin("one", "two", "three") )
print ( eventGenerator.createEvent_SetReferrer ("referrer") )
print (eventGenerator.createEvent_RandomSearch())
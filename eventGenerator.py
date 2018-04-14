def createEvent_SetOrigin (origin1, origin2, origin3):
    return {
        "type": "SetOrigin",
        "arguments" : {
            "originLevel1" : origin1,
            "originLevel2" : origin2,
            "originLevel3" : origin3
        }        
    }

def createEvent_SetReferrer (referrer):
    return {
        "type" : "SetReferrer", 
        "arguments" : {
            "referrer" : referrer
        }
    }

def createEvent_RandomSearch ():
    return {
        "type": "Search",
        "arguments": {
            "queryText": "",
            "goodQuery": 'true'
        }
    }

'''

event_RandomClick = {
					"type": "Click",
					"arguments": {
						"docNo": -1,
						"offset": 0,
						"probability": 0.4
					}
				}

event_RandomView = 	{
					"type": "View",
					"arguments": {
						"docNo": -1,
						"offset": 0,
						"probability": 1.0
					}
				}

event_ChangeTab =   {
                    "type": "TabChange",
                    "arguments": {
                        "tabName": "App Store",
                        "tabCQ": "@source=(App Store Demo)"
                    }
                }

event_TargetSearch =    {
                    "type": "Search",
                    "arguments": {
                    "queryText": "funny beeping robot",
                    "goodQuery": true
                    }
                }

event_TargetSearchClick = {
    "type" : "SearchAndClick",
    "arguments" : {
        "queryText" : "specific query",
        "caseSearch": true,
        "inputTitle": "Subject", #only for case creation
        "probability" : 0.85,
        "docClickTitle" : "specific title"
    }
}
'''
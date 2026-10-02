from dotenv import load_dotenv 
from services.base_http_client import BaseHTTPClient 
import os 

load_dotenv()

class ChessDotComService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["CHESSDOTCOM_BASE_URL"])
        self.streamersMap = {}

    def _handleError(e):
        print("Error", e)
        return {
            "status": "error",
            "message": str(e)
        }
    
    def getLeaderboard(self):
        try:
            response = self.client.getCall("pub/leaderboard", qpParmas={})
            resultObj = {}
            objectKeys = ["name", "username"]
            for k, values in response.items():
                resultObj[k] = []

                for value in values:
                    obj = {}
                    for objectKey in objectKeys:
                        obj[objectKey] = value[objectKey]
                    resultObj[k].append(obj)
                return resultObj
        except Exception as e:
            return self._handleError(e)

    def getStreamers(self):
        try:
            response = self.client.getCall("pub/streamers", qpParmas={})
            results = []
            if "streamers" in response:
                data = response["streamers"]
    
                for d in data:
                    obj = {}
                    obj["username"] = d["username"]
                    self.streamersMap[d["username"]] = d["platforms"]
                    results.append(obj)
            return results 
        except Exception as e:
            return self._handleError(e)

    def getUserBasicDertails(self, username: str):
        try:
            response = self.client.getCall("pub/player/{username}", qpParmas={})
            return response 
        except Exception as e:
            return self._handleError(e)

    def getUserStats(self, username : str):
        try:
            response = self.client.getCall("pub/player/{username}/stats", qpParmas={})
        except Exception as e:
            return self._handleError(e)
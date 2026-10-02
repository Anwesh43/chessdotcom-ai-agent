import requests 
from typing import Dict 
from urllib.parse import urlencode 

class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL 

    def getCall(self, endpoint : str, qpParmas : Dict):
        headers = {
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:156.0) Gecko/20100101 Firefox/156.0"
        }
        response = requests.get(f"{self.baseURL}/{endpoint}?{urlencode(qpParmas)}", headers = headers)
        response.raise_for_status()
        return response.json()

from tools.chessdotcom_tools import getLeaderboard, getPlayerBasicDetails, getPlayerStats, getStreamers 
from typing import Dict 
import json 

def writeFile(data : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Calling data to {fileName}")
if __name__ == "__main__":
    writeFile(getLeaderboard(), "test_leader_board.json")
    writeFile(getStreamers(), "test_streamers.json")
    writeFile(getPlayerStats("FormerProdigy"), "test_plyer_stat.json")
    writeFile(getPlayerBasicDetails("FormerProdigy"), "test_plyer_details.json")
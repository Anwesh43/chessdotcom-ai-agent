from services.chessdotcom_service import ChessDotComService

chessService = ChessDotComService()

def getLeaderboard():
    print("Calling getLeaderboard tool")
    return chessService.getLeaderboard()

def getStreamers():
    print("Calling getStreamers tool")
    return chessService.getStreamers()

def getPlayerBasicDetails(username : str):
    print(f"Calling getPlayerBasicDetails tool for {username}")
    return chessService.getUserBasicDetails(username=username.lower())

def getPlayerStats(username : str):
    print(f"Calling getPlayerStats tool for {username}")
    return chessService.getUserStats(username.lower())

def writeHTML(htmlStr : str, fileName : str):
    print("Calling writeHTML tool for fileName")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"written html to {fileName}, don't display html to filename"
    }
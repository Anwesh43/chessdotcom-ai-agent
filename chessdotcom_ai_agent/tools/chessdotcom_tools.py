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
    return chessService.getUserBasicDetails(username=username)

def getPlayerStats(username : str):
    print(f"Calling getPlayerStats tool for {username}")
    return chessService.getPlayerStats()
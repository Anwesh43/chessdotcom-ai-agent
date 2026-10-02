import asyncio 
import sys 
from agents.chessdotcom_agent import analyseChessDetails

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseChessDetails(prompt=prompt)) 
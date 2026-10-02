from pydantic_ai import Agent 
from tools.chessdotcom_tools import getLeaderboard, getPlayerBasicDetails, getPlayerStats, getStreamers, writeHTML 
from prompts.chess_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv 

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    system_prompt = SYSTEM_PROMPT,
    tools = [getStreamers, getPlayerStats, getPlayerBasicDetails, getLeaderboard, writeHTML]
)

async def analyseChessDetails(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')
from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools 
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="mistral-saba-24b"),
    tools=[DuckDuckGoTools()],
    introduction="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent= Agent(
    name="Fianance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    instructions="Use tables to dispaly data ",
    show_tool_calls=True,
    markdown=True,
    
)

agent_team=Agent(
    team=[web_agent,finance_agent],
    model=Groq(id="mistral-saba-24b"),
    instructions=["Always include the sources","Use tables to dispaly data"],
    show_tool_calls=True,
    markdown=True,
)

#agent_team.print_response("Analyse companies in USA like Tesla ,NVDA,Google,Apple and suggest to buy for long term")
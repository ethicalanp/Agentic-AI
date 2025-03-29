from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

agent =Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an Interior Design Consultant,reply based on the questions",
    instructions=["Search your knowlede base for Interior Designing",
                  "If the question is better suited for the web , search the web to fill in gaps ",
                  "Prefer the information in  your knowledge base over the web results"],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://www.researchgate.net/publication/343160919_Application_of_AI_technology_in_interior_design"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="Designs",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),

    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response("How to design a small living room?",stream=True)
agent.print_response("what are the latest trends in interior design?",stream=True)



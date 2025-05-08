from crewai import Agent
from AI_Component.Llms import *

class Agents :
    def __init__(self):
        # Define llm here llm list can be seen on Llms.py
        self.llm = openai
        self.verbose = True

    def data_search(self):
        return Agent(
            role="Data Researcher and Retriever in AI Perikanan GEMA",
            goal="Research and retrieve data about the given topics related to Fisheries",
            backstory="You are an expert in searching Information related to some specific topics about fisheries for more than 15 years"
                      "You previously was a researcher in fisheries industry so it is verry easy for you to search fish information everywhere",
            allow_delegation=False,
            verbose=self.verbose,
            llm=self.llm
        )
    
    def general_answer(self):
        return Agent(
            role="Fisheries Instructor",
            goal="Give answer and study materials for fisheries question",
            backstory="you are a writer before you serve the best article that common people can understand"
                      "even when it's a hard topics now you write answer for people common question related to fisheries",
            allow_delegation=False,
            llm=self.llm,
            verbose=self.verbose
        )
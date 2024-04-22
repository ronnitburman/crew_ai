from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset

class MeetingPrepAgents():
    
    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal="conduct thorough research on people and companies involved in the meeting",
            tools=ExaSearchToolset.tools,
            backstory=dedent("""
            As a Research Specialist, your mission is to uncover detailed information about
            the individuals and entities participating in the meeting. your insights will 
            lay the goundwork for strategic meeting preparation.
            """),
            verbose = True
        )
    
    def industry_analysis_agent(self):
        return Agent(
            role="Industry Analyst",
            goal="Analyze the current industry trends, challenges, and opportunities",
            tools=ExaSearchToolset.tools,
            backstory=dedent("""
            As an Industrial Analyst, your analysis will identify key trends, 
            challenges facing the industry, and potential opportunities that could be 
            leveraged during the meeting for the strategic advantage.
            """),
            verbose = True
        )
    
    def summary_and_briefing_agent(self):
        return Agent(
            role="Briefing Coordinator",
            goal="Compile all gathered information into a consice, informative briefing document",
            backstory=dedent("""
            As an Industrial Analyst, your analysis will identify key trends, 
            challenges facing the industry, and potential opportunities that could be 
            leveraged during the meeting for the strategic advantage.
            """),
            verbose = True
        )
    
    def meeting_strategy_agent(self):
        return Agent(
            role="Meeting Strategy Advisor",
            goal="Develop talking points, questions, and strategic angles for the meeting",
            backstory=dedent("""
            As a Strategy Advisor, your expertise will guide the development of
            talking points, insightful questions, and strategic angles to ensure the 
            meeting's objectives are achieved.
            """),
            verbose = True
        )

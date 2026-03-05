#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from research_crew.crew import ResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "How AI Agents have changed the job market of software development?",       
        'current_year': str(datetime.now().year)
    }

    try:
        ResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

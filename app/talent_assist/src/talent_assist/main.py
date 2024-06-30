#!/usr/bin/env python
from talent_assist.crew import TalentAssistCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    TalentAssistCrew().crew().kickoff(inputs=inputs)
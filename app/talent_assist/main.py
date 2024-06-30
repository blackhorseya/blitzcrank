#!/usr/bin/env python
from app.talent_assist.crew import TalentAssistCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    user_input = input('Press Enter something to start the crew...\n')

    inputs = {
        'topic': 'AI LLMs',
        'user_input': user_input,
    }
    TalentAssistCrew().crew().kickoff(inputs=inputs)


if __name__ == '__main__':
    run()

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# 创建一个简单的聊天工具
chat_tool = SerperDevTool()

# 创建一个聊天代理
chat_agent = Agent(
    role='Chat Agent',
    goal='Engage in meaningful conversations with users',
    verbose=True,
    memory=True,
    backstory='You are an engaging and knowledgeable conversationalist.',
    tools=[chat_tool]
)

# 创建一个简单的聊天任务
chat_task = Task(
    description='Engage in a friendly conversation with the user.',
    expected_output='A meaningful and friendly response to user input.',
    tools=[chat_tool],
    agent=chat_agent,
)

# 创建一个 Crew
crew = Crew(
    agents=[chat_agent],
    tasks=[chat_task],
    process=Process.sequential
)

if __name__ == '__main__':
    # 运行 Crew
    user_input = input('Press Enter to start the chat...')
    result = crew.kickoff(inputs={'user_input': user_input})
    print(result)

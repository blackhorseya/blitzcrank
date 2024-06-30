from crewai import Agent, Task, Crew, Process

# 設定代理人
main_agent = Agent(
    role='主聊天助手',
    goal='與用戶進行聊天並根據需要委託任務給其他代理人',
    verbose=True,
    memory=True,
    backstory='你是一名智能聊天助手，專門為用戶提供幫助，並在需要時委託特定任務給專門的代理人。'
)

introduction_agent = Agent(
    role='自我介紹專員',
    goal='向求職者和客戶提供個性化的自我介紹',
    verbose=True,
    memory=True,
    backstory='你是一名專業的自我介紹專員，擅長根據不同的背景提供最合適的介紹。'
)

scheduler_agent = Agent(
    role='日程安排助手',
    goal='自動安排和確認通話時間',
    verbose=True,
    memory=True,
    backstory='你是一名高效的日程安排助手，能快速找到合適的時間並發送邀請。'
)

faq_agent = Agent(
    role='常見問題回答專員',
    goal='根據 Hunter 的問題提供準確的回答',
    verbose=True,
    memory=True,
    backstory='你是一名常見問題回答專員，能快速準確地回答各種常見問題。'
)


# 動態創建任務並將其加入 Crew
def create_task(description, expected_output, agent):
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )


# 設定 Crew
crew = Crew(
    agents=[main_agent, introduction_agent, scheduler_agent, faq_agent],
    process=Process.sequential
)

if __name__ == '__main__':
    while True:
        user_input = input('你: ')
        if user_input == 'exit':
            break

        if '介紹' in user_input:
            task = create_task(
                description='自動生成並發送個性化的自我介紹，包括背景、經歷和專長信息。',
                expected_output='一段個性化的自我介紹。',
                agent=introduction_agent
            )
            crew.tasks.append(task)

        if '安排日程' in user_input:
            task = create_task(
                description='自動安排和確認通話時間，並發送日曆邀請給 Hunter 和客戶。',
                expected_output='確認的通話時間和日曆邀請。',
                agent=scheduler_agent
            )
            crew.tasks.append(task)

        if '回答問題' in user_input:
            task = create_task(
                description='根據 Hunter 的問題，提供即時且準確的回答，涵蓋常見問題和行業資訊。',
                expected_output='精確的回答內容。',
                agent=faq_agent
            )
            crew.tasks.append(task)

        response = crew.kickoff(inputs={'user_input': user_input})
        print(f'助手: {response}')

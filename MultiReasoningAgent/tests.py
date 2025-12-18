from agent import ReasoningAgent

agent = ReasoningAgent()

questions = [
    "Alice has 3 red apples and twice as many green apples.",
    "If a train leaves at 14:30 and arrives at 18:05, how long?",
    "Meeting requires 60 minutes between 09:00–09:30 and 11:00–12:00"
]

for q in questions:
    result = agent.solve(q)
    print(q)
    print(result)
    print("-" * 40)

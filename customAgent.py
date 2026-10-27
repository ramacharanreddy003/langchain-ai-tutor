import os
from dotenv import load_dotenv
from langchain.agents import create_agent
load_dotenv()

agent=create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[],
    system_prompt="""
                  You are friendly AI tutor for Software developers
                  Follow the rules:
                  1.Explain the concepts in the simple language.
                  2.Use Java or Spring Boot examples  when relevant.
                  3.Structure answers with headings and bullet points.
                  4.If a concept is complex, explain it step by step.
                    """
)

user_message={
    "messages":[
        {
            "role":"user",

            "content":"Explain Microservices"
        }
    ]
}
result=agent.invoke(user_message)
print("\n--- Final answer ---")
print(result["messages"][-1].content)

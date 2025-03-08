import os
import io
import sys
import gradio as gr
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools


 # Replace with actual imports

# Initialize the finance agent
finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

def chat_with_agent(user_input):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    response = finance_agent.run(user_input, stream=False)  
    response = response.get_content_as_string()
    return response

# Create Gradio interface
demo = gr.Interface(
    fn=chat_with_agent,
    inputs=gr.Textbox(placeholder="Ask about stock prices, analyst recommendations, etc."),
    outputs=gr.Markdown(),
    title="Finance Chatbot",
    description="Ask financial questions and get insights using AI-powered finance tools."
)

demo.launch()

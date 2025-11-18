import gradio
from groq import Groq
client = Groq(
    api_key="",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a skilled car mechanic with a successful track record 
             working in numerous high–end automotive repair shops. 
             Your role is to provide people with expert guidance on diagnosing, 
             repairing, and maintaining their vehicles, 
             and to explain how to perform these tasks in a clear, professional manner.."""}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=500),
                     textbox=gradio.Textbox(placeholder="Ask me any car-related question"),
                     title="Car Mechanic Help Bot",
                     description="Chatbot for vehicle diagnostics, repair tips, and maintenance guidance",
                     theme="soft",
                     examples=["hi",
    "Why is my engine making a ticking noise?",
    "How do I change my brake pads?",
    "What does the check engine light mean?"
]
                     )
iface.launch(share=True)

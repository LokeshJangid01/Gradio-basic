# # import time
# # import gradio as gr

# # def slow_echo(message, history):
# #     for i in range(len(message)):
# #         time.sleep(0.1)
# #         yield "You typed: " + message[: i+1]

# # gr.ChatInterface(slow_echo, type="messages").launch()

# # import gradio as gr

# # def yes_man(message, history):
# #     if message.endswith("?"):
# #         return "Yes"
# #     else:
# #         return "Ask me anything!"

# # gr.ChatInterface(
# #     yes_man,
# #     type="messages",
# #     chatbot=gr.Chatbot(height=300),
# #     textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
# #     title="Yes Man",
# #     description="Ask Yes Man any question",
# #     theme="soft",
# #     examples=[{"text": "Hello"}, {"text": "Am I cool?"}, {"text": "Are tomatoes vegetables?"}],
# #     cache_examples=True,
# #     retry_btn=None,
# #     undo_btn="Delete Previous",
# #     clear_btn="Clear",
# # ).launch()


# #UPLOAD FILES

# # import gradio as gr

# # def count_files(message, history):
# #     num_files = len(message["files"])
# #     return f"You uploaded {num_files} files"

# # demo = gr.ChatInterface(fn=count_files, type="messages", examples=[{"text": "Hello", "files": []}], title="Echo Bot", multimodal=True)

# # demo.launch()

# # import gradio as gr
# # import time

# # def echo(message, history, system_prompt, tokens):
# #     response = f"System prompt: {system_prompt}\n Message: {message}."
# #     for i in range(min(len(response), int(tokens))):
# #         time.sleep(0.05)
# #         yield response[: i+1]

# # with gr.Blocks() as demo:
# #     system_prompt = gr.Textbox("You are helpful AI.", label="System Prompt")
# #     slider = gr.Slider(10, 100, render=False)

# #     gr.ChatInterface(
# #         echo, additional_inputs=[system_prompt, slider], type="messages"
# #     )

# # demo.launch()

# #SHOW FILES IN CHAT

# # import gradio as gr

# # def fake(message, history):
# #     if message.strip():
# #         return gr.Audio("https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav")
# #     else:
# #         return "Please provide the name of an artist"

# # gr.ChatInterface(
# #     fake,
# #     type="messages",
# #     textbox=gr.Textbox(placeholder="Which artist's music do you want to listen to?", scale=7),
# #     chatbot=gr.Chatbot(placeholder="Play music by any artist!"),
# # ).launch()

# # API FROM OPENAI

# # from langchain.chat_models import ChatOpenAI
# # from langchain.schema import AIMessage, HumanMessage
# # import openai
# # import gradio as gr
# # import os

# # os.environ["OPENAI_API_KEY"] = ""  # Replace with your key

# # llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

# # def predict(message, history):
# #     history_langchain_format = []
# #     for msg in history:
# #         if msg['role'] == "user":
# #             history_langchain_format.append(HumanMessage(content=msg['content']))
# #         elif msg['role'] == "assistant":
# #             history_langchain_format.append(AIMessage(content=msg['content']))
# #     history_langchain_format.append(HumanMessage(content=message))
# #     gpt_response = llm(history_langchain_format)
# #     return gpt_response.content

# # gr.ChatInterface(predict, type="messages").launch()

# #   STREAMIG FROM OPENAI
# from openai import OpenAI
# import gradio as gr

# api_key = ""   # Replace with your key
# client = OpenAI(api_key=api_key)

# def predict(message, history):
#     history_openai_format = []
#     for msg in history:
#         history_openai_format.append(msg)
#     history_openai_format.append(message)
  
#     response = client.chat.completions.create(model='gpt-3.5-turbo',
#     messages= history_openai_format,
#     temperature=1.0,
#     stream=True)

#     partial_message = ""
#     for chunk in response:
#         if chunk.choices[0].delta.content is not None:
#               partial_message = partial_message + chunk.choices[0].delta.content
#               yield partial_message

# gr.ChatInterface(predict, type="messages").launch()

# IMAGE EXAMPLE IN GRADIO
import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(), "image")
demo.launch()

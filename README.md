# AskApp
The "Ask" is an interactive application that harnesses the power of OpenAI's GPT-3 language model to generate responses to user queries and prompts. It serves as a convenient interface to ask questions and receive AI-generated answers.

Steps to run the Project

Step 1 : Install Required Packages (write this code in terminal of vscode)
pip install streamlit
pip install pyperclip
pip install langchain

Step 2 : Write the code for executiom in ask.py  

Step 3 : os.environ["OPENAI_API_KEY"] = "Your API key here, you can find it here https://platform.openai.com/account/api-keys, if you do not have one click on create new secret key(note : you should be logged in to openai.com)"

Step 4 : streamlit run app.py (write this code in terminal, you should be in specified folder where app.py is present, if not use cd to change the path), if not working use the command in this format (streamlit run e:/LLM/AskApp/AskApp/ask.py)

Step 5 : The app will open in a browser tab, and you can ASK anything to it and copy the answer

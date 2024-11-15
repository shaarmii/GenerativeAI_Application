import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "enter_your_api_key")

sys_prompt = """ You are a helpful AI code reviewer. Students will paste the code and will ask you to explain the error and give correct code with proper explanation
                  related to various programming language and give explanation in bold format. In case if a student ask any question outside the code review scope, politely decline decline and tell them 
                  that you are designed only for reviewing code and correcting the mistakes.  """
model = genai.GenerativeModel("models/gemini-1.5-flash",system_instruction=sys_prompt)

st.title(":blue[An AI Code Reviewer] :sunglasses:")

code_snippet = st.text_area("Enter the code to review...")
btn_click = st.button("Generate")

if btn_click == True:
    response = model.generate_content(code_snippet)
    st.text_area("Corrected Code with explanation:", value=response.text, height=200)

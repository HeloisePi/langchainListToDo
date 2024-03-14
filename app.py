from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from diffusers import StableDiffusionPipeline
import streamlit as st
import torch
from secret_key import OPENAI_API_KEY
import os


def main():
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    llm = OpenAI(temperature=0.7)
    prompt = ChatPromptTemplate.from_template("Tu es un chef de project professionnelle. On te dis quoi faire et tu listes toute les étapes sans développer, en quelque mot , séparées par des virgules  de {topic}")
    model = ChatOpenAI(model="gpt-3.5-turbo")
    output_parser = StrOutputParser()
    chain = prompt | model | output_parser
    
    st.title('To do List from LangChain')
    user_prompt = ""
    input_value = st.text_input('Que voulez-vous faire ?', value=user_prompt, max_chars=100, key=None ,kwargs=None, placeholder="Ex : Faire l'audit d'une marque ?", label_visibility="visible")
    user_prompt = input_value
   

    def on_input_change(input_value, user_prompt):
        check_empty = is_user_prompt_empty(user_prompt)
        
        if check_empty == False : 
            
            check_entry = is_entry_key_press(input_value)
            if check_entry == True:
                # Defind Result 
                result = chain.invoke({"topic": user_prompt})
                # result = "pain, miel, beurre, fromage"                    VALEURS TEST
                result = result.split(", ")
        
            
                # doLayout
                layout(result)




    def is_entry_key_press(input_value):
        print('input_value', input_value)
        if input_value.endswith('\n'):
             return True
        return True


    def is_user_prompt_empty(user_prompt):
        
         if len(user_prompt) > 0 :
              return False
         else : 
              return True 
 
    def layout(result):
        for element in result:
            st.write(element)



  
        

    on_input_change(input_value, user_prompt)
    result = is_user_prompt_empty(user_prompt)


        


if __name__ == "__main__":
    main()
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")

client =Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
prompt1 ="Hii"
prompt2="Explain Time Travel in detail with EXample"
prompt3= "Write essay in 100 words on Artificial Intelligence"
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages,max_tokens=500)
    usage=response.usage
    print(f"Prompt: {prompt}-->your token usage is {usage.prompt_tokens} and your completion token uasge is {usage.completion_tokens} and your total token usage is{usage.total_tokens} Finish Reasson: {response.choices[0].finish_reason}")

##print(response)

#***********************************************************************************************************************************************")

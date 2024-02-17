from openai import OpenAI

client = OpenAI(
    api_key="****",
)
messages = [ {"role": "system", "content":  
              "You are a intelligent assistant."} ] 
while True: 
    message = input("User : ") 
    if message.lower() in ['quit', 'exit', 'bye']:
        break
    if message: 
        messages.append(
            {"role": "user", "content": message}, 
        ) 
        response = client.chat.completions.create(

            model="gpt-3.5-turbo", messages=messages 
        ) 
        reply =  response.choices[0].message.content.strip()
        print(f"ChatGPT: {reply}") 
        messages.append({"role": "assistant", "content": reply}) 
import google.generativeai as genai
import os
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-pro")
print("\n\n\t\t\t\t\tArtificial Intelligence")
ques = str(input("\nAsk Anything to AI : "))
while (1):  
    print("--------------------GENERATIING RESPOSE--------------------")
    response = model.generate_content(ques)
    print("RESPONSE : \n",response.text, "\n")
    ques = str(input("\nAsk More : "))



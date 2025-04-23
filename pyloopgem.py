from google import genai
import subprocess
from google.genai import types

the = True
while the == True:
    client = genai.Client(api_key="AIzaSyAUiqd8mnnguM_opAUE1r-YcC1_nwtJ-As")
    print("Enter input:")
    query = input()
    print("Your input was: ",query," would you like to revise?")
    yn = input()
    if yn == "yes":
        continue
    response = client.models.generate_content(model = "gemini-2.0-flash",
                                              contents = (query,"WRITE ONLY THE PROGRAM IN PYTHON. WRITE NOTHING ELSE."), 
                                              config = types.GenerateContentConfig(temperature = 0))
    code = response.text
    code = code.replace("```python","")
    code = code.replace("```","")
    with open("script.py","w") as f:
        f.write(code)
    res = subprocess.run(['python','script.py'], capture_output = True, text = True)
    coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("Your last input was",query,"WRITE ONLY THE PROGRAM IN PYTHON. WRITE NOTHING ELSE. The output of the code you wrote for this query was",res.stdout,"Is this acceptable?"), 
                                         config = types.GenerateContentConfig(temperature = 0))
    print(res.stdout)
    print(code)
    print(coderevis)
    the = False


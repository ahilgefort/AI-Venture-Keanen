from google import genai

client = genai.Client(api_key="AIzaSyAUiqd8mnnguM_opAUE1r-YcC1_nwtJ-As")

response = client.models.generate_content(model = "gemini-2.0-flash",contents="say e")
print(response.text)
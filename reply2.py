import sys
import google.generativeai as genai
import json

# Initialize the Gemini model
genai.configure(api_key="YOUR API KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

def create_prompt(json_data, query):
    prompt = f"""
    You are given a JSON object with hotel list parameters and query asked to generate the response. Your task is to generate a verbal description of the details in the JSON object with respect to query provided.
    query : {query}
    JSON Response:
    {json_data}
    
    Verbal Description:
    """
    return prompt

def main():
    if len(sys.argv) != 2:
        print("Usage: python reply2.py <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    
    with open("hotel_body.json", "r") as f:
        json_data = json.load(f)
    
    response = model.generate_content(create_prompt(json_data, query))
    print(response.text.strip())

if __name__ == "__main__":
    main()
 
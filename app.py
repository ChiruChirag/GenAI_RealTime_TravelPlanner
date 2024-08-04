import streamlit as st
import google.generativeai as genai
import json
import subprocess

# Initialize the Gemini model
genai.configure(api_key="AIzaSyC6zu5i4Pna7KmhLyANd84LsKfl9XB-rgc")
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to query the Gemini model to convert city names to IATA codes
def get_iata_code(query):
    prompt = f"""
    Given my query, generate the output in the format specified below. Convert the city names to their respective IATA codes.
    Here are the IATA codes for some major Indian cities:
    
    Bangalore (Bengaluru): BLR
    Hyderabad: HYD
    Mumbai (Bombay): BOM
    Delhi: DEL
    Chennai (Madras): MAA
    Kolkata (Calcutta): CCU
    Ahmedabad: AMD
    Pune: PNQ
    Goa: GOI
    Jaipur: JAI
    Lucknow: LKO
    Kochi (Cochin): COK
    Trivandrum (Thiruvananthapuram): TRV
    Coimbatore: CJB
    Visakhapatnam: VTZ
    Bhubaneswar: BBI
    Indore: IDR
    Nagpur: NAG
    Patna: PAT
    Vadodara: BDQ
    
    Example Query:
    Query: I want to go from Bangalore to Hyderabad on 2024-08-04 with 1 adult in INR.
    Example Response:
    
    
    {{
        "originLocationCode": "BLR",
        "destinationLocationCode": "HYD",
        "departureDate": "2024-08-04",
        "adults": 1,
        "currencyCode": "INR"
    }}
    
    I just want the response format and nothing else.
    
    Query: {query}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Function to run pipeline.py and get the response
def run_pipeline(query):
    result = subprocess.run(['python', 'pipeline.py', query], capture_output=True, text=True)
    return result.stdout.strip()

# Streamlit application
st.title("Flight Search Query Generator")

query = st.text_input("Query", placeholder="I want to go from Bangalore to Hyderabad on 2024-08-04 with 1 adult in INR,also list the Top 5 Hotels there.")

if st.button("Generate Query"):
    if query:
        response_json = get_iata_code(query)
        st.write("Generated Query JSON:")
        st.write(response_json)
        
        # Clean and save JSON
        clean_json = response_json[7:-3]
        with open('query_response.json', 'w') as f:
            f.write(clean_json)
        
        # Run the pipeline and display the response
        pipeline_response = run_pipeline(query)
        st.write("Response from pipeline:")
        st.write(pipeline_response)
    else: 
        st.error("Please provide a valid query.")

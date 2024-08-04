from amadeus import Client, ResponseError
import json

def get_amadeus_response2():
    # Load the response from the JSON file
    with open('query_response.json', 'r') as f:
        query_response = json.load(f)
    
    # Extract the necessary fields from the response
    #origin_location_code = query_response.get("originLocationCode")
    #print(origin_location_code)
    destination_location_code = query_response.get("destinationLocationCode")
    print(destination_location_code)
    #departure_date = query_response.get("departureDate")
    adults = query_response.get("adults")
    #currency_code = query_response.get("currencyCode")
    radius=20
    
    # Initialize Amadeus Client
    amadeus = Client(
        client_id='YOUR API KEY',
        client_secret='YOUR PASSCODE'
    )
    
    try:
        response = amadeus.reference_data.locations.hotels.by_city.get(cityCode=destination_location_code)
        with open('hotel_body.json', 'w') as f:
            json.dump(response.data, f)
        print("")
    except ResponseError as error:
        print(error)

if __name__ == "__main__":
    get_amadeus_response2()

import subprocess
import sys

def run_amadeus_api():
    # Run amadeus_api.py script
    subprocess.run(['python', 'amadeus_api.py'], check=True)

def run_amadeus_api2():
    # Run amadeus_api.py script
    subprocess.run(['python', 'amadeus_api2.py'], check=True)


def run_reply(query):
    # Run reply.py script with query argument
    result = subprocess.run(['python', 'reply.py', query], capture_output=True, text=True)
    return result.stdout.strip()
def run_reply2(query):
    # Run reply.py script with query argument
    result = subprocess.run(['python', 'reply2.py', query], capture_output=True, text=True)
    return result.stdout.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python pipeline.py <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    
    run_amadeus_api()
    run_amadeus_api2()
    response = run_reply(query)
    response2 = run_reply2(query)
    # Print the response of reply.py
    print("Response from reply.py:")
    print(response)
    print(response2)

if __name__ == "__main__":
    main()

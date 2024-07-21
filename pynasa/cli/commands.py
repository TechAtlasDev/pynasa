import argparse
from ..core import NasaAPI
from ..utils import format_response

def get_apod(api_key, date):
    api = NasaAPI(api_key=api_key)
    response = api.get_apod(date=date)
    formatted_response = format_response(response)
    print(formatted_response)

def main():
    parser = argparse.ArgumentParser(description='Pynasa CLI - Interact with the NASA API')
    parser.add_argument('api_key', help='Your NASA API key')
    parser.add_argument('date', help='Date for APOD (yyyy-mm-dd)')
    args = parser.parse_args()
    
    get_apod(api_key=args.api_key, date=args.date)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import argparse
import sys
import requests
from typing import Tuple

def parse_arguments() -> Tuple[str, str, float]:
    parser = argparse.ArgumentParser(description='Currency Converter')
    parser.add_argument('--from', dest='from_currency', required=True,
                      help='Currency to convert from (e.g., USD)')
    parser.add_argument('--to', dest='to_currency', required=True,
                      help='Currency to convert to (e.g., EUR)')
    parser.add_argument('--amount', type=float, required=True,
                      help='Amount to convert')
    
    args = parser.parse_args()
    return args.from_currency.upper(), args.to_currency.upper(), args.amount

def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    try:
        # Using Free Forex API
        url = f'https://open.er-api.com/v6/latest/{from_currency}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Validate API response
        if data.get('result') == 'error':
            print(f"Debug - API Error: {data.get('error-type')}")
            raise ValueError(f"API Error: {data.get('error-type')}")
            
        if 'rates' not in data:
            print(f"Debug - API Response: {data}")
            raise ValueError("Invalid API response format")
            
        if to_currency not in data['rates']:
            raise ValueError(f"Currency {to_currency} not found in exchange rates")
            
        return data['rates'][to_currency]
        
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the internet")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Error: API request timed out")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: API service is unavailable - {str(e)}")
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    try:
        from_currency, to_currency, amount = parse_arguments()
        
        if amount < 0:
            print("Error: Amount must be a positive number")
            sys.exit(1)
            
        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate
        
        print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        print(f"Exchange rate: 1 {from_currency} = {rate:.4f} {to_currency}")
        
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
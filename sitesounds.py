import json
import random
import requests
import time
import sys
import signal
import argparse

def make_request(url, useragents):
    try:
        if not url.startswith('http'):
            url = 'https://' + url

        headers = {
            'User-Agent': random.choice(useragents)
        }

        response = requests.get(url, timeout=1, headers=headers)
        response.raise_for_status()
        print(f'{url} - {response.status_code}')

    except requests.exceptions.RequestException as e:
        if e.response is not None:
            print(f'{url} - connection error: {e.response.status_code}')
        else:
            print(f'{url} - unknown connection error')

    return url

def signal_handle(sig, frame):
    print('Ctrl+C or system exit catched, stopping...')
    sys.exit(0)

def main(args):
    with open(args.websites, 'r') as w:
        websites = json.load(w)

    with open(args.useragents, 'r') as u:
        useragents = json.load(u)

    signal.signal(signal.SIGINT, signal_handle)
    signal.signal(signal.SIGTERM, signal_handle)

    if args.invisible:
        print('notice: invisible mode enabled, requests will be sent with a large interval')

    while True:
        url = random.choice(websites)
        make_request(url, useragents)

        def_int = random.uniform(0.5, 3.0)
        inv_int = random.uniform(3.7, 12.0)

        if args.invisible:
            time.sleep(inv_int)
        else:
            time.sleep(def_int)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='sitesounds is a simple Python script that make a web traffic noise')
    parser.add_argument('-w', '--websites', metavar='file', nargs='?', default='websites.json', help='the name of the JSON file containing website URLs')
    parser.add_argument('-u', '--useragents', metavar='file', nargs='?', default='useragents.json', help='the name of the JSON file containing useragents')
    parser.add_argument('-i', '--invisible', action='store_true', help='enable less suspicious mode by increasing requests interval')
    args = parser.parse_args()

    main(args)
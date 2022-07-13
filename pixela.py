import argparse
import requests

import config.default as config

def post(g, d, q):
    url = 'https://pixe.la/v1/users/%s/graphs/%s' % (config.PIXELA_USER_NAME, g)
    headers = {
        'X-USER-TOKEN': config.PIXELA_USER_TOKEN
    }
    data = '{"date": "%s", "quantity": "%s"}' % (d, q)
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('graph', type=str)
    parser.add_argument('date', type=str)
    parser.add_argument('quantity', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    post(args.graph, args.date, args.quantity)

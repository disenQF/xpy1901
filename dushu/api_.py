import requests


def run_spider():
    url = 'http://localhost:6800/schedule.json'
    data = {
        'project': 'dushu',
        'spider': 'book'
    }

    resp = requests.post(url, data=data)
    print(resp.json())


def stop_spider():
    url = 'http://localhost:6800/cancel.json'
    data = {
        'project': 'dushu',
        'job': '0cb783068e4a11e9a3fd7831c1cc4a2e'
    }

    resp = requests.post(url, data)
    print(resp.json())


if __name__ == '__main__':
    # {'node_name': 'Disen.local', 'status': 'ok', 'jobid': '0cb783068e4a11e9a3fd7831c1cc4a2e'}
    # run_spider()
    stop_spider()
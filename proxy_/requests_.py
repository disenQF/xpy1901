import requests

def test_proxy():
    # url = 'http://ip.tool.chinaz.com/'
    proxy_url = 'https://175.148.79.177:1133'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) ' \
                      'Gecko/20100101 Firefox/67.0'
    }
    resp = requests.get('http://www.baidu.com', headers=headers,
                        proxies={'https': proxy_url}, timeout=10)

    if resp.status_code == 200:
        print('%s 验证通过 ' % proxy_url)
    else:
        print('%s 验证未通过 ' % proxy_url)

if __name__ == '__main__':
    test_proxy()
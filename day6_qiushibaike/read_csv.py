from csv import DictReader
import base64

with open('qb.csv', 'r', encoding='utf-8') as file:

    reader = DictReader(file,fieldnames=('name',
                                         'info_url',
                                         'img',
                                         'content'))

    for item in reader:
        content = item.get('content')
        if content == 'content':  # 第一次是标题行
            continue

        print(base64.b16decode(content).decode())
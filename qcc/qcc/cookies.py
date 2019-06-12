import random

all_cookies = [
    'zg_did=%7B%22did%22%3A%20%2216a4e5962ba202-00179bbdb4c25c-36697e04-fa000-16a4e5962bbe8%22%7D; UM_distinctid=16a4e596642197-07384a96c30bf8-36697e04-fa000-16a4e5966443b8; _uab_collina=155609264499524039732715; acw_tc=7cc1e21915602995981604216e9a0b8dd0693e7ea1f1c3a9eabbddc1d7; QCCSESSID=miukt7i3oj5q9cpgrh64ugpmh4; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1560299601; CNZZDATA1254842228=1170326332-1556091700-%7C1560302442; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201560306197981%2C%22updated%22%3A%201560307510677%2C%22info%22%3A%201560299600463%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22093f6d45452e9aad1e822e1fcf969ef0%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1560307511',

]


def get_cookie():
    cookie = random.choice(all_cookies)
    return {k.strip(): v.strip()
            for k, v in [kv.split('=')
                         for kv in cookie.split(';')]}

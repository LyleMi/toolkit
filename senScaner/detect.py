import re
import requests

LINK = re.compile(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')")

def detect(session, entities, url, headers, timeout, proxies):

    tmp = []

    for i in entities:
        r = session.get(url + i, headers=headers, timeout=timeout, proxies=proxies)
        if r.status_code != 200:
            pass
        else:
            tmp += LINK.findall(r.content)

    for i in tmp:
        r = session.get(url + i, headers=headers, timeout=timeout, proxies=proxies)
        print(url+i), '\tstatus code: ', r.status_code
        if r.status_code != 200:
            pass
        else:
            entities.append(i)

    return list(set(entities))

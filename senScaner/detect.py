import re
import requests

def detect(session, entities, url, headers, timeout, proxies):

    for i in entities:
        r = session.get(url + i, headers=headers, timeout=timeout, proxies=proxies)
        if r.status_code != 200:
            pass
        else:
            entities += gainUrl(r.content)
            # tmp = detect(session, entities, url, headers, timeout, proxies)
    return entities

def gainUrl(content):
    urls = []
    # link
    # herf
    # src
    return urls



if __name__ == '__main__':
    main()
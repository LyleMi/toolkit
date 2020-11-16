import os
import re
import json


from termcolor import colored

from config import Config
from setting import Vulners
from setting import Effects
from setting import srvbins


def getAll(reg, content):
    regRel = re.compile(reg, re.IGNORECASE)
    finds = regRel.findall(content)
    return finds


def getValue(minYear=0, maxYear=3000, minNumber=0, maxNumber=30):
    # print(minYear)
    dpath = Config.dataPath
    for _year in os.listdir(dpath):
        if not _year.isnumeric():
            continue
        if int(_year) < minYear or int(_year) > maxYear:
            continue
        year = os.path.join(dpath, _year)
        for _number in os.listdir(year):
            n = int(_number.replace("x", ""))
            if int(n) < minNumber or int(n) > maxNumber:
                continue
            number = os.path.join(year, _number)
            for _file in os.listdir(number):
                file = os.path.join(number, _file)
                yield parseFile(file)


def updateValue(number):
    dpath = Config.dataPath
    year, n = number.split("-")
    if len(n) == 4:
        n = n[0] + "x" * 3
    elif len(n) == 5:
        n = n[0] + "x" * 4
    path = os.path.join(dpath, year, n, "CVE-%s.json" % number)
    return parseFile(path)


def parseFile(file):
    with open(file, "rb") as fh:
        number = file.split(os.path.sep)[-1].split(".")[0]
        name = ""
        version = ""
        desc = ""
        content = fh.read()
        content = content.decode("utf-8", errors="ignore")
    try:
        content = json.loads(content)
        desc = content["description"]["description_data"][0]["value"]
        if "affects" in content:
            vendor_data = content["affects"]["vendor"]["vendor_data"][0]
            product_datas = vendor_data["product"]["product_data"]
            for product_data in product_datas:
                name = product_data["product_name"]
                version = product_data["version"]["version_data"][0]["version_value"]
                break
    except KeyError as e:
        print(file)
        print(repr(e))
    except Exception as e:
        print(file)
        print(repr(e))
    if len(name) > 2048 or len(version) > 2048:
        print(number, len(name), len(version))
        if len(version) > 2048:
            version = version[:2000] + "..."
        if len(name) > 2048:
            name = name[:2000] + "..."
    return number, name, version, desc


def highlight(s, keywords):
    if isinstance(keywords, str):
        keywords = [keywords]
    for k in keywords:
        for key in getAll(k, s):
            s = s.replace(key, colored(key, "red"))
    for v in Vulners:
        for vk in Vulners[v]:
            for key in getAll(vk, s):
                s = s.replace(key, colored(key, "cyan"))
    for v in Effects:
        for vk in Effects[v]:
            for key in getAll(vk, s):
                s = s.replace(key, colored(key, "green"))
    for key in srvbins:
        s = s.replace(key, colored(key, "blue"))
    return s

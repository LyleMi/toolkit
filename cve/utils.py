import os
import json

from termcolor import colored

from config import Config


def getValue(minYear=0, maxYear=3000):
    for file in traverseFile(minYear, maxYear):
        with open(file, 'r') as fh:
            number = file.split(os.path.sep)[-1].split('.')[0]
            name = ''
            version = ''
            desc = ''
            try:
                content = json.load(fh)
                desc = content['description']['description_data'][0]['value']
                if 'affects' in content:
                    vendor_data = content['affects']['vendor']['vendor_data'][0]
                    product_datas = vendor_data['product']['product_data']
                    for product_data in product_datas:
                        name = product_data['product_name']
                        version = product_data['version']['version_data'][0]['version_value']
                        break
            except KeyError as e:
                print(file)
                print(repr(e))
            except Exception as e:
                print(file)
                print(repr(e))
            yield number, name, version, desc


def traverseFile(minYear=0, maxYear=3000):
    print(minYear)
    dpath = Config.dataPath
    for _year in os.listdir(dpath):
        if not _year.isnumeric():
            continue
        if int(_year) < minYear or int(_year) > maxYear:
            continue
        year = os.path.join(dpath, _year)
        for _number in os.listdir(year):
            number = os.path.join(year, _number)
            for _file in os.listdir(number):
                file = os.path.join(number, _file)
                yield file


def highlight(s, keywords):
    if isinstance(keywords, str):
        keywords = [keywords]
    for k in keywords:
        s = s.replace(k, colored(k, 'red'))
    return s


if __name__ == '__main__':
    for d in getValue(2014):
        # if d[0].startswith("CVE-2014"):
        print(d)
        # break

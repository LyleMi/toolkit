def remove_js_css(content):
    r = re.compile(r'<script.*?</script>', re.I | re.M | re.S)
    s = r.sub('', content)
    r = re.compile(r'<style.*?</style>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<!--.*?-->', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<meta.*?>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<ins.*?</ins>', re.I | re.M | re.S)
    s = r.sub('', s)
    return s

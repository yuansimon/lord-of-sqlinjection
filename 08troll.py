from constants import *

chall_url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"

res = make_request(chall_url, "?id=ADMIN")
check_clear(res)

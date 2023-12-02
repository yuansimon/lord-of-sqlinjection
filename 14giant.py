from constants import *

chall_url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"

res = make_request(chall_url, "?shit=" + urllib.parse.quote(f"\v"))
check_clear(res)

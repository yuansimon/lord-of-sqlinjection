import re
import urllib.parse

import requests

from secrets import cookies

lower_case_letters = [chr(x) for x in range(ord("a"), ord("z") + 1)]
upper_case_letters = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

letters = lower_case_letters.copy()
letters.extend(upper_case_letters)

digits_and_letters = digits.copy()
digits_and_letters.extend(letters)
letters_and_digits = lower_case_letters.copy()
letters_and_digits.extend(upper_case_letters)
letters_and_digits.extend(digits)

digits_and_lower_case_letters = digits.copy()
digits_and_lower_case_letters.extend(lower_case_letters)

email_chars = ["@"]
email_chars.extend(lower_case_letters)
email_chars.extend(digits)
email_chars.extend(upper_case_letters)

admin_in_hex = "0x" + "admin".encode("utf-8").hex()
admin_in_binary = "0b" + ''.join(bin(x)[2:].zfill(8) for x in 'admin'.encode('UTF-8'))

hello_admin = "<h2>Hello admin</h2>"
error_condition = "999999999999999999999999999999999999*99999999999999999999999999999999=99999999999*999999999999999"


def ascii_to_hex(ascii_string):
    return "0x" + ascii_string.encode("utf-8").hex()


def ascii_to_binary(ascii_string):
    return "0b" + ''.join(bin(x)[2:].zfill(8) for x in ascii_string.encode('UTF-8'))


def make_request(chall_url, params, unquote=True, no_print=False, return_elapsed=False):
    url = chall_url + params
    if not no_print:
        if unquote:
            print(urllib.parse.unquote(url))
        else:
            print(url)
    res = requests.get(url, cookies=cookies)
    if return_elapsed:
        return res.text, res.elapsed.total_seconds()
    return res.text


def check_clear(res, noPrint=False):
    match = re.search("<h2>([a-zA-Z_]* Clear!)</h2>", res)

    if not noPrint:
        print("------------------------------------------")
        if match:
            print("Level cleared:", match.group(1))
        else:
            print("Level not cleared.")
            print(res)

    return bool(match)


def login():
    logged_out_text = "<script>location.href='../';</script>"
    res = requests.get("https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php", cookies=cookies)

    if logged_out_text in res.text:
        username = input("Need login. Enter username: ")
        pw = input("Enter pw: ")
        if pw.endswith("\n"):
            pw = pw[:-1]
        requests.post("https://los.rubiya.kr/?login", data={"id": username, "pw": pw}, cookies=cookies)
        res = requests.get("https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php", cookies=cookies)
        assert (logged_out_text not in res.text)
        exit()
    else:
        print("Already logged in")


login()

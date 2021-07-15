# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.request import *
import requests
import json
a = [1, 2]


class Test:
    def __init__(self):
        pass

    def test(self) -> int:
        return a.pop()



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def send_task_config_to_athena(body, athena_url):
    """

    Parameters
    ----------
    body: json_body
    athena_url

    Returns
    -------

    """
    print("send task body:")
    print(body)
    print(type(json.dumps(body)))
    headers = {
        # "Content-Type": "application/json; charset=UTF-8",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    req = Request(url=athena_url, data=bytes(json.dumps(body), 'utf8'), headers=headers)
    print(req)
    try:
        resp = urlopen(req)
        print(resp.read())
    except:
        print("network error")
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    JUPYTER_LAB_SERVER_PORT = 9301
    ATHENA_POST_API = "/api/athena/deploy-test"
    ATHENA_POST_URL = "http://127.0.0.1:" + str(JUPYTER_LAB_SERVER_PORT) + ATHENA_POST_API
    # headers = {
    #     "Content-Type": "application/json; charset=UTF-8",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    # }
    pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}
    # response = requests.post(ATHENA_POST_URL, data=json.dumps(pyload), headers=headers).text
    # print(response)
    send_task_config_to_athena(pyload, ATHENA_POST_URL)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

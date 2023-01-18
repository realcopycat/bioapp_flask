# 二次开发更新日志

- 合并 Pull Requests [FacebookLibra](https://gitee.com/FacebookLibr): [修复反向代理下 IP获取不准确](https://gitee.com/pear-admin/pear-admin-flask/pulls/44/files)
- 合并 Pull Requests [CHunYenc](https://gitee.com/CHunYenc): [加入 Flask-APScheduler 設定](https://gitee.com/pear-admin/pear-admin-flask/pulls/49/files)
- 合并 Pull Requests [mengfu188](https://gitee.com/mengfu188): [添加邮件管理模块](https://gitee.com/pear-admin/pear-admin-flask/pulls/51) 并将邮件原文设置为 HTML 格式
- 修复 用户权限更新时当前登录仍然无法获得权限的BUG
- 修复 直接使用 app.py 启动时无法将 .flaskenv 环境变量读入的问题
- 增加 插件功能
- 增加 程序重启功能 注意：**注意要使用程序重启 必须在主程序启动前设置环境变量 pearppid ，可以参考 start.py**

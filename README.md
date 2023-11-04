# 懂车帝发帖上传图片
因为某些原因删减了部分源码

# 文件说明
- 源码分为python和易语言，python作服务端，易语言为前端

# 目录结构
```
dcd
│
├── cookie  # 登录后存放cookie文件
│     └── 手机号.txt # cookie文件 发图片的账号
├── img  # 存放图片的文件夹，必须为png格式，存放多少上传多少
├── cookie.json  # 供给publish上传图片使用，因为上传需要登录状态，登录是谁并不重要只要登录就行
├── dcd.e    # 前端运行文件
├── run.py    # 服务端运行主文件
├── app.py  # 后端程序
├── publish.py  # 上传图片
├── 手机号码归属地.txt
└── requirements.txt # 依赖文件
```

# cookie.txt格式
- 由于删除了登录功能要想正常使用只能抓包按这个格式放入cookie文件夹中
- 打开dcd.exe -> 进入账号列表页面 -> 点击读取 -> 双击选择即可

```
昵称----手机号----地区----uid----token----cookie
```


# 可以学习的内容
- json不清楚组名完成json解析
- 懂车帝上传图片
- 懂车帝发帖

# 效果展示
- [7296697224817279526](https://api.dcarapi.com/motor/feoffline/ugcs/article.html?link_source=share&group_id=7296697224817279526)
- [7296813899880350235](https://api.dcarapi.com/motor/feoffline/ugcs/article.html?link_source=share&group_id=7296813899880350235)

# 声明
- qq交流群：916790180
- 本源码只是出于学习交流的目的，使用者造成的任何后果等均与作者无关

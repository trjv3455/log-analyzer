# log-analyzer
Python简易日志分析工具，基于正则表达式解析日志文本，统计错误、警告数量，提取并统计访问IP，适合服务器/物联网设备日志初步筛查。

功能清单
- 逐行读取本地日志文件
- 正则匹配 ERROR / WARNING 日志等级并计数
- 提取日志中的IP地址，统计访问频次
- 输出TOP5高频IP
- 文件不存在、读取异常捕获

技术栈
Python3，re正则模块、collections.Counter，无第三方依赖

运行方式
```bash
python log_analyze.py

默认读取同目录 `test.log`，可修改代码里文件路径，支持自定义日志文件。

项目结构
├── log_analyze.py    # 日志分析主程序
├── test.log          # 模拟物联网设备测试日志
├── README.md

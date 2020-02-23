# coding:utf-8

import subprocess
import logging
import time

# 设置日志以及日志的级别
logger = logging.getLogger()
fh = logging.FileHandler('startup.log', encoding='utf-8')
fh.setFormatter(logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'))
logger.addHandler(fh)
logger.setLevel(1)
fh.setLevel(1)

# 打开文件逐行执行命令
with open(r'cmds.txt', encoding='utf-8') as file:
    for line in file:
        cmd = line.strip()
        if len(cmd) == 0:
            continue
        logging.info("process cmd {cmd}".format(cmd=cmd))
        subprocess.Popen(cmd, shell=True)

while True:
    time.sleep(1000)

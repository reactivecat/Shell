#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import os
from imp import reload

if sys.version > '3':
    PY3 = True
    import configparser
else:
    PY3 = False
    import ConfigParser as configparser

    reload(sys)
    sys.setdefaultencoding('utf8')

argvs = sys.argv
# print(argvs)
commit_message_file = open(sys.argv[1])
commit_message = commit_message_file.read().strip()

CONFIG_FILE = '.git' + os.path.sep + 'hooks' + os.path.sep + 'git-hooks.conf'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

if not config.has_section('commit-msg'):
    print('未找到配置文件: ' + CONFIG_FILE)
    sys.exit(1)

cm_regex = str(config.get('commit-msg', 'cm_regex')).strip()
cm_doc_url = str(config.get('commit-msg', 'cm_doc_url')).strip()
cm_email_suffix = str(config.get('commit-msg', 'cm_email_suffix')).strip()

ret = os.popen('git config user.email', 'r').read().strip()

if not ret.endswith(cm_email_suffix):
    print('===============================  Commit Error ====================================')
    print('==> Commit email格式出错，请将git config中邮箱设置为标准邮箱格式，公司邮箱后缀为：' + cm_email_suffix)
    print('==================================================================================\n')
    commit_message_file.close()
    sys.exit(1)

# 匹配规则, Commit 要以如下规则开始
if not re.match(cm_regex, commit_message):
    print('===============================  Commit Error ====================================')
    print('==> Commit 信息写的不规范 请仔细参考 Commit 的编写规范重写！！！')
    print('==> 匹配规则: ' + cm_regex)
    if cm_doc_url:
        print('==> Commit 规范文档: ' + cm_doc_url)
    print('==================================================================================\n')
    commit_message_file.close()
    sys.exit(1)
commit_message_file.close()


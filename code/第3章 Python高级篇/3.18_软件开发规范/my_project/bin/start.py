# -*- coding: utf-8 -*-
# @Time     : 2020/1/7 16:48
# @Author   : 童庆
# @FileName : start.py
# @Software : PyCharm

import os
import sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from core import main


if __name__ == '__main__':
    main.home()
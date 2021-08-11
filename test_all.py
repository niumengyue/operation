import os
import sys

import pytest

if __name__ == '__main__':
    command_line = ['-vs', './testcase/test_login.py','--alluredir','./tmp']
    pytest.main(command_line)      #-s打印 输出
    #使用allure产生报告

    os.system("allure generate ./tmp -o ./report --clean")

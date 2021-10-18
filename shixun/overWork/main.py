#请勿直接打开shixun这个文件夹 这样会导致导包路径错误
# 请把shixun文件夹粘贴到你得python项目文件夹下的一层 运行就ok了
from shixun.overWork.Class.module.show import show
from shixun.overWork.Class.module.chooseMode import chooseMode
print("-"*40+"欢迎来到九江学院外卖系统"+"-"*40)
chooseMode()
show()
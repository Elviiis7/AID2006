"""
进程创建示例 1

【1】 将需要新进程执行的事件封装为函数
【2】 通过模块的Process类创建进程对象，关联函数
【3】 可以通过进程对象设置进程信息及属性
【4】 通过进程对象调用start启动进程
【5】 通过进程对象调用join回收进程资源
"""

import multiprocessing
import time


# 进程执行函数
def fun():
    print("开始运行一个进程")
    time.sleep(2)  # 模拟,假装这个事很大执行了2s
    print("这个进程结束了")


# 实例化进程对象
p = multiprocessing.Process(target=fun)

# 启动进程:此时进程诞生,自动执行fun函数作为执行内容
p.start()

print("halo")
time.sleep(3)
print("hey")

# 等待进程结束
p.join()

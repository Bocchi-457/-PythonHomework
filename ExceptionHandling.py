# 异常处理
try:
    # 尝试执行的代码块
    result = 10 / 0
except ZeroDivisionError:
    # 如果在try块中发生了ZeroDivisionError，则执行这里的代码
    print("除数不能为0")
except Exception as e:
    # 如果在try块中发生了其他类型的异常，则执行这里的代码
    print(f"发生了其他类型的异常：{e}")

try:
    # 尝试执行的代码块
    result = 10 / 2
except ZeroDivisionError:
    # 如果在try块中发生了ZeroDivisionError，则执行这里的代码
    print("除数不能为0（这个异常在这个例子中不会发生）")
else:
    # 如果没有异常发生，则执行这里的代码
    print("计算成功，结果是：", result)

try:
    # 尝试执行的代码块
    print("尝试打开文件...")
    # 这里假设我们要打开一个文件，但为了简化示例，我们仅打印一条消息
    # with open('somefile.txt', 'r') as f:
    #     pass
except FileNotFoundError:
    # 如果文件不存在，则执行这里的代码
    print("文件未找到")
except Exception as e:
    # 如果发生其他异常，则执行这里的代码
    print(f"发生异常：{e}")
finally:
    # 无论是否发生异常，finally块中的代码都会执行
    print("执行清理工作...")


def divide(x, y):
    if y == 0:
        # 抛出自定义异常
        raise ValueError("除数不能为0")
    return x / y


try:
    result = divide(10, 0)
except ValueError as e:
    # 捕获到抛出的异常并处理
    print(e)


def risky_operation():
    try:
        # 假设这里有一些可能会引发异常的代码
        print("尝试执行高风险操作...")
        # 为了演示，我们直接抛出一个异常
        raise ValueError("高风险操作失败")
    except ValueError as e:
        print(f"捕获到异常：{e}")
    else:
        # 由于前面抛出了异常，所以这里不会执行
        print("高风险操作成功完成（这个消息不会显示）")
    finally:
        # 无论是否发生异常，这里都会执行
        print("执行高风险操作后的清理工作...")


risky_operation()


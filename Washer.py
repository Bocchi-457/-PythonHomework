# Washer类

class Washer:
    # 洗衣机类
    '洗衣机类'
    def __init__(self, width, height):
        # 初始化洗衣机的宽度和高度
        self.width = width
        self.height = height

    def print_info(self):
        # 打印洗衣机的宽度和高度
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")

    def __str__(self):
        # 定义对象的字符串表示，但注意这里实际上应该是返回一个字符串而不是直接打印
        # 返回洗衣机的说明书（但实际上这里应该是返回一个字符串，而不是打印）
        print('这是洗衣机的说明书')

    def __del__(self):
        # 当对象被销毁时调用
        print('洗衣机已销毁')

# 创建一个宽度为10，高度为20的洗衣机对象haier1
haier1 = Washer(10, 20)
# 调用haier1的print_info方法打印其宽度和高度
haier1.print_info()

# 创建一个宽度为30，高度为40的洗衣机对象haier2
haier2 = Washer(30, 40)
# 调用haier2的print_info方法打印其宽度和高度
haier2.print_info()
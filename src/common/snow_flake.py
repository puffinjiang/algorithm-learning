import time

# 每一部分占用的位数
TIMESTAMP_BIT = 41  # 时间戳占用位数
MACHINE_BIT = 5  # 机器标识占用的位数
DATACENTER_BIT = 5  # 数据中心占用的位数
SEQUENCE_BIT = 12  # 序列号占用的位数

# 每一部分的最大值
MAX_DATACENTER_NUM = -1 ^ (-1 << DATACENTER_BIT)
MAX_MACHINE_NUM = -1 ^ (-1 << MACHINE_BIT)
MAX_SEQUENCE = -1 ^ (-1 << SEQUENCE_BIT)

# 每一部分向左的位移
MACHINE_LEFT = SEQUENCE_BIT
DATACENTER_LEFT = MACHINE_BIT + SEQUENCE_BIT
TIMESTAMP_LEFT = DATACENTER_LEFT + DATACENTER_BIT


class SnowFlake:
    class OverflowError(TypeError):
        """
        分布式ID生成算法占位符溢出异常，会导致生成ID为负数
        """
        pass

    class RuntimeError(TypeError):
        """
        运行时间错误，在此项目中当前运行时间小于上一次运行时间。
        """
        pass

    def __init__(self):
        if TIMESTAMP_BIT + SEQUENCE_BIT + MACHINE_BIT + DATACENTER_BIT != 63:
            raise self.OverflowError(
                "TIMESTAMP_BIT + SEQUENCE_BIT + MACHINE_BIT + DATACENTER_BIT not equal to 63bit")
        self.datacenter_id = 0  # 数据中心编号
        self.machineId = 0  # 机器标识编号
        self.sequence = 0  # 序列号
        self.last_stamp = -1  # 上一次时间戳

    def nextId(self):
        """生成下一个ID"""
        cur_stamp = self.get_new_stamp()
        if cur_stamp < self.last_stamp:
            raise self.RuntimeError(
                "Clock moved backwards. Refusing to generate id")

        if cur_stamp == self.last_stamp:
            # 相同毫秒内，序列号自增
            self.sequence = (self.sequence + 1) & MAX_SEQUENCE
            # 同一秒的序列数已经达到最大
            if self.sequence == 0:
                cur_stamp = self.get_next_mill()
        else:
            # 不同秒内，序列号为0
            self.sequence = 0

        self.last_stamp = cur_stamp
        return (cur_stamp << TIMESTAMP_LEFT) | (
                self.datacenter_id << DATACENTER_LEFT) | (
                       self.machineId << MACHINE_LEFT) | self.sequence

    def get_next_mill(self):
        mill = self.get_new_stamp()
        while mill <= self.last_stamp:
            mill = self.get_new_stamp()
        return mill

    @staticmethod
    def get_new_stamp():
        now = lambda: int(time.time() * 1000)
        return now()


def main():
    s = SnowFlake()
    for i in range(1000):
        print(s.nextId())


if __name__ == "__main__":
    main()
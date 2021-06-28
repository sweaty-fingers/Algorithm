class MyCircularQueue:
    def __init__(self, k: int):

        self.q = [None] * k
        self.qf = 0
        self.qr = 0
        self.qlen = k

    def enQueue(self, value: int) -> bool:
        if self.q[self.qr] == None:
            self.q[self.qr] = value
            self.qr = (self.qr + 1) % self.qlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.qf] == None:
            return False
        else:
            self.q[self.qf] = None
            self.qf = (self.qf + 1) % self.qlen
            return True

    def Front(self) -> int:
        if self.q[self.qf] == None:
            return -1
        else:
            tmp = self.q[self.qf]
            return tmp

    def Rear(self) -> int:
        if self.q[(self.qr - 1) % self.qlen] == None:
            return -1
        else:
            tmp = self.q[(self.qr - 1) % self.qlen]

            return tmp

    def isEmpty(self) -> bool:

        return self.q[self.qf] == self.q[self.qr] and self.q[self.qf] == None

    def isFull(self) -> bool:

        return self.q[self.qf] == self.q[self.qr] and self.q[self.qf] != None

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self
    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

md = MathDojo()

result1 = md.add(2).add(2, 5, 1).add(10).result
print(result1) 

result2 = md.subtract(3, 2).subtract(1).subtract(5).result
print(result2)

result3 = md.add(3).subtract(2).add(5, 1).result
print(result3)



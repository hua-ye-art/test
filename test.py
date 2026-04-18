# 测试 1：基础输出
print("✅ Python 环境配置成功！")

# 测试 2：简单计算
a = 10
b = 4
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

# 测试 3：列表循环
fruits = ["苹果", "香蕉", "橙子"]
print("\n水果列表：")
for f in fruits:
    print("-", f)

# 测试 4：简单函数
def add(x, y):
    return x + y

result = add(5, 7)
print(f"\n函数计算 5 + 7 = {result}")

# 测试 5：条件判断
num = 6
if num > 0:
    print(f"\n{num} 是正数")
else:
    print(f"\n{num} 不是正数")

print("\n🎉 所有测试运行完成！")
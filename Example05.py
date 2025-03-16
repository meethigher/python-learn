# 基本的列表解析
squares = [x**2 for x in range(5)]  # 生成 0 到 4 的平方数列表
print(squares)  # 输出 [0, 1, 4, 9, 16]

# 带条件的列表解析
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # 只生成偶数的平方
print(even_squares)  # 输出 [0, 4, 16, 36, 64]

# 嵌套列表解析
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]  # 将二维列表展平为一维
print(flattened)  # 输出 [1, 2, 3, 4, 5, 6, 7, 8, 9]
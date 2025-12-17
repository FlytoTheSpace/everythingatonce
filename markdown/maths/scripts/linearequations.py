

def LinearEquations(a0: list[list[float]]):
    n = len(a0)
    if (n != (len(a0[0]) - 1)):
        return
    A = [a0]
    for m in range(1, n):
        pm = m - 1
        A.append([])
        for i in range(0, n - m):
            A[m].append([])
            for j in range(0, n - pm):
                acur = (A[pm][i][n - pm] * A[pm][n - pm - 1][j]) - (A[pm][i][j] * A[pm][n - pm - 1][n - pm])
                A[m][i].append(acur)

    x: list[float] = [1]
    for k in range(1, n + 1):
        xk = 0
        nnk = n - k
        for j in range(0, k):
            xk += A[nnk][0][j] * x[j]
        xk = - xk / A[nnk][0][k]
        x.append(xk)
    return x


def checkSolutions(a0: list[list[float]], x: list[float]):
    n = len(a0)
    if (n != (len(a0[0]) - 1)):
        return
    print(a0)
    print(x)
    for i in range(0, n):
        sum = 0
        for j in range(0, n + 1):
            sum += a0[i][j] * x[j]
        if sum == 0:
            print(f"{i} [✅] Correct Solution")
            continue
        print(f"{i} [❌] Incorrect Solution")


a0 = [
    [-5,  2, 3], # -5 +  2x + 3y = 0
    [-3, 10, 4], # -3 + 10x + 3y = 0
]

checkSolutions(a0, LinearEquations(a0))
# Output:
# [[-5, 2, 3], [-3, 10, 4]]
# [1, -0.5, 2.0]
# 0 [✅] Correct Solution
# 1 [✅] Correct Solution


# 
# # this heavily assumes given matrix is n + 1 by n
# # something like this:
# # a0 = [
# # #    j →
# #   [3,2], # i
# #   [2,5], # ↓
# #   [1,2]
# # ]
# # intrepreted as:
# # 3 + 2x + 1y = 0
# # 2 + 5x + 2y = 0
# 
# def LinearEquations(a0: list[list[float]]):
# 
#     n = len(a0) - 1
#     if (n != len(a0[0])):
#         return
#     
#     A = [a0]
#     
#     # coefficients:
# 
#     for m in range(1, n):
#         A.append([])
#         for i in range(0, n - m + 1):
#             A[m].append([])
#             for j in range(0, n - m):
# 
#                 mn1 = m - 1
#                 acur: float = (A[mn1][i][n - mn1 - 1] * A[mn1][n - mn1][j]) - (A[mn1][i][j] * A[mn1][n - mn1][n - mn1 - 1])
#                 A[m][i].append(acur)
# 
#     x = [1]
# 
#     for k in range(1, n + 1):
#         xcur = 0
#         for i in range(0, k):
#             xcur += A[n - k][i][0] * x[i]
# 
#         xcur = - xcur / A[n - k][k][0]
#         x.append(xcur)
# 
#     return x
# 
# # Checks Solutions given by the LinearEquations function.
# def checkSolutions(a0: list[list[float]], sol: list[float]):
# 
#     n = len(a0) - 1
#     if (n != len(a0[0])):
#         return
#     
#     sum = 0
# 
#     # equations
#     
#     print(sol)
# 
#     for j in range(0, n):
#         sum = 0
#         for i in range(0, n + 1):
#             sum += a0[i][j] * sol[i]
# 
#         if sum == 0:
#             print(f"{j} [✅] Correct Solution")
#             continue
#         
#         print(f"{j} [❌] Incorrect Solution")
# 
# 
# 
# a0 = [
#     [3,2],
#     [2,5],
#     [1,2],
# ]
# 
# checkSolutions(a0, LinearEquations(a0))
# 
# # output:
# # [1, 4.0, -11.0]
# # 0 [✅] Correct Solution
# # 1 [✅] Correct Solution
# 
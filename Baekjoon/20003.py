# def gcd(m ,n) :
#     if m < n :
#         m, n = n, m
#     if n == 0 :
#         return m
#     if m % n == 0 :
#         return n
#     else :
#         return gcd(n, m % n)
        
# N = int(input())

# arr = []

# for i in range(N) :
#     up, down = map(int, input().split())
#     div = gcd(up, down)
#     arr.append([up // div, down // div])
# print(arr)

# LCM = 1
# for i in range(N) :
#     LCM = LCM * arr[i][1] // gcd(LCM, arr[i][1])
# print('LCM: ', LCM)

# for i in range(N) :
#     arr[i][0] *= LCM // arr[i][1]
#     print(arr[i][0])

# GCD = gcd(arr[0][0], arr[1][0])

# if N > 2 :
#     for i in range(2, N) :
#         GCD = gcd(GCD, arr[i][0])
# print(arr)
# print(GCD)
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def get_GCD(nums):
    _gcd = nums[0]
    for n in nums[1:]:
        _gcd = gcd(_gcd, n)
    return _gcd

def get_LCM(nums):
    _lcm = nums[0]
    for n in nums[1:]:
        _lcm = int(_lcm*n / gcd(_lcm, n))
    return _lcm

length = input()
bunja = []
bunmo = []
for i in range(int(length)):
    num = input().split(" ")
    a = int(num[0])
    b = int(num[1])
    ab_gcd = gcd(a, b)
    bunja.append(a / ab_gcd)
    bunmo.append(b / ab_gcd)

numerator = get_LCM(bunmo)
denominator = get_GCD(bunja)
print(str(int(denominator))+" "+str(int(numerator)))
import Crypto.Util.number as cun
import random
import ast


# def evaluate_polynomial(polynomial: list, x: int, p: int):
#     return (
#         sum(
#             (coefficient * pow(x, i, p)) % p for i, coefficient in enumerate(polynomial)
#         )
#         % p
#     )


# N_SHARES = 3


# def main():
#     print(
#         f"I wrote down a list of people who are allowed to get the flag and split it into {N_SHARES} using Shamir's Secret Sharing."
#     )
#     MESSAGE = cun.bytes_to_long(b"qxxxb, BuckeyeCTF admins, and NOT YOU")



#     p = cun.getPrime(512)

#     polynomial = [MESSAGE] + [random.randrange(1, p) for _ in range(N_SHARES - 1)]
#     points = [(i, evaluate_polynomial(polynomial, i, p)) for i in range(1, N_SHARES + 1)]

#     print("Your share is:")
#     print(points[0])
#     print("The other shares are:")
#     for i in range(1, len(points)):
#         print(points[i])

#     print()
#     print("Now submit your share for reconstruction:")
#     your_input = ast.literal_eval(input(">>> "))
#     if (
#         type(your_input) is not tuple
#         or len(your_input) != 2
#         or type(your_input[0]) is not int
#         or type(your_input[1]) is not int
#         or your_input[0] != 1
#         or not (0 <= your_input[1] < p)
#     ):
#         print("Bad input")
#         return

#     points[0] = your_input

#     xs = [point[0] for point in points] # -> ["out input", point[0], point[0]]
    
#     ys = [point[1] for point in points]

#     y_intercept = 0
#     for j in range(N_SHARES):
#         product = 1
#         for i in range(N_SHARES):
#             if i != j:
#                 product = (product * xs[i] * pow(xs[i] - xs[j], -1, p)) % p
#         y_intercept = (y_intercept + ys[j] * product) % p

#     reconstructed_message = cun.long_to_bytes(y_intercept)

#     # 71 78 78 78 62 2c 20 42 75 63 6b 65 79 65 43 54 46 20 61 64 6d 69 6e 73 2c 20 61 6e 64 20 4d 45

#     if reconstructed_message == b"qxxxb, BuckeyeCTF admins, and ME":
#         print("Here's your flag:")
#         print("buckeye{?????????????????????????????????????????}")
#     else:
#         print(f"Sorry, only these people can see the flag: {reconstructed_message}")


# y = 51324204992776479904300515868812612755530291871875429589951882479477811334469
xs = [1, 2, 3]
ys = [5133944182695820318430249092705160263339994950951329583292424012251640154888126802601583379051088651306590532598546499944848696378228399875653862896025564,
        4903310259247793100776794830160293151285475451519009723612495223779225906538724170960749325652695011189223047075638453499871105071977858926990970784864574,
        8698873741135305608596852181819874295890221589176964585667107555636942592406467653629859286276173341014486534975677650362445712317941794717858399029406622]
# p = 11755025205039310115019567317588388408337730126883514783423119713725916231882045718556489156659214621328721439403022635851510244389076492361592524513415517

GOAL = cun.bytes_to_long(b"qxxxb, BuckeyeCTF admins, and ME") # <---- 31345857339735387674339047914642674425426384039193428650927113279849390176369
GOAL_CHECK = cun.bytes_to_long(b"qxxxb, BuckeyeCTF admins, and NOT YOU") 

# product1 = (1 * xs[1] * pow(xs[1] - xs[0], -1, p)) % p
# product1 = (product1 * xs[2] * pow(xs[2] - xs[0], -1, p)) % p

# product2 = (1 * xs[0] * pow(xs[0] - xs[1], -1, p)) % p
# product2 = (product2 * xs[2] * pow(xs[2] - xs[1], -1, p)) % p

# product3 = (1 * xs[0] * pow(xs[0] - xs[2], -1, p)) % p
# product3 = (product3 * xs[1] * pow(xs[1] - xs[2], -1, p)) % p


# product1 = (1 * xs[1] * pow(xs[1] - xs[0], -1, p) * xs[2] * pow(xs[2] - xs[0], -1, p)) % p
# product2 = (1 * xs[0] * pow(xs[0] - xs[1], -1, p) * xs[2] * pow(xs[2] - xs[1], -1, p)) % p
# product3 = (1 * xs[0] * pow(xs[0] - xs[2], -1, p) * xs[1] * pow(xs[1] - xs[2], -1, p)) % p

# product1 = (2 * pow(2 - 1, -1, p) * 3 * pow(3 - 1, -1, p)) % p
# product2 = (1 * pow(1 - 2, -1, p) * 3 * pow(3 - 2, -1, p)) % p
# product3 = (1 * pow(1 - 3, -1, p) * 2 * pow(2 - 3, -1, p)) % p

# product1 = (2 * 1 * 3 * (p + 1) // 2) % p
# product2 = (1 * (p - 1) * 3 * 1) % p
# product3 = (1 * ((p - 1) // 2) * 2 * (p-1)) % p

# product1 = (3 * (p + 1)) % p = 3
# product2 = (3 * (p - 1)) % p = (p - 3)
# product3 = ((p - 1) * (p - 1)) % p = 1


# GOAL = (ys[0] * 3 + ys[1] * (p-3) + ys[2]) % p

# a * p + GOAL = ys[0] * 3 + ys[1] * (p-3) + ys[2]
# a * p + GOAL = ys[0] * 3 - ys[1] * 3 + ys[2]


# ys[2] * ((p - 1) ** 2)
# ys[2] * (p**2 - 2 * p + 1)
# ys[2] * p**2 - ys[2] * 2 * p + ys[2])


# GOAL = ys[0] * 3 - ys[1] * 3 + ys[2]

# -3 * ys[0] = -ys[1]*3+ ys[2] - GOAL


from decimal import Decimal, getcontext

getcontext().prec = 1000

val = - Decimal( -ys[1] * 3 + ys[2] - GOAL) / Decimal(3)
print(val)
# y_intercept = (ys[0] * product1 + ys[1] * product2 + ys[2] * product3) % p

# print(val, cun.long_to_bytes(val))
print("Final", cun.long_to_bytes(int(val*3 - 3*ys[1] + ys[2])))


# # y_intercept = (ys[0] * product1 + ys[1] * product2 + ys[2] * product3) % p

# print(product1, product2, product3)

# # y_intercept = ((ys[0] * product1)%p + (ys[1] * product2)%p + (ys[2] * product3)%p) % p

# GOAL = (3*ys[0] - 3*ys[1] + 1*ys[2]) % P





# # GOAL = (3*YS1 - 3*ys[1] + 1*ys[2]) % p
# # GOAL_CHECK = (3*YS2 - 3*ys[1] + 1*ys[2]) % p

# YS1 = 4661239736168494907284569339376386372684914630716694474272199155390016028623788384061958513930215544997090636276931263478995591781697668722055653079076958

# s1 = (3*YS1 - 3*ys[1] + 1*ys[2])
# # s2 = (3*YS2 - 3*ys[1] + 1*ys[2])


# print(GOAL, s1)

# GOAL = s1 % p
# GOAL_CHECK = s2 % p

# a * p + GOAL = s1
# b * p + GOAL_CHECK = s2

# a * p = s1 - GOAL


# a, b, s2 are UNKNOWN




# main()

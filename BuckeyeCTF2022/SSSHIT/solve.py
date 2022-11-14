import Crypto.Util.number as cun

N_SHARES = 3
xs = [1, 2, 3]
ys = [4661239736168494907284569339376386372684914630716694474272199155390016028623788384061958513930215544997090636276931263478995591781697668722055653079076958,
        8299068932507259343675196238288442242778135500252346094177147105839556373133269306904574767450542337387401269771463915411139559993846474873649235799375240,
        10913487589016293309171880696736167610279662608606954859714843851405052593704359542269153573466575051894084552445720091418779175154972521709909412540470995]
p = 11755025205039310115019567317588388408337730126883514783423119713725916231882045718556489156659214621328721439403022635851510244389076492361592524513415517

# xs = [2, 4, 5]
# ys = [1942, 3402, 4414]

# y_intercept = 0
# for j in range(N_SHARES):
#     product = 1
#     for i in range(N_SHARES):
#         if i != j:
#             product = (product * xs[i] * pow(xs[i] - xs[j], -1, p)) % p
#     y_intercept = (y_intercept + ys[j] * product) % p

# reconstructed_message = cun.long_to_bytes(y_intercept)
# print("Recon: ", reconstructed_message)

GOAL = cun.bytes_to_long(b"qxxxb, BuckeyeCTF admins, and ME")

# print(len(str(GOAL)))
# print(len(str(p)))
# print(len(str((3*ys[1]-ys[2])%p)))
# print("yes" if (3*ys[1]-ys[2])%p > p else "no")
# GOAL = cun.bytes_to_long(b"qxxxb, BuckeyeCTF admins, and NOT YOU")
print(GOAL)
# GOAL = 1234
# y0 = (GOAL - ys[1]*3/(1*-1) - ys[2]*2/(2*1)) / (6/(-1*-2))
# print(len(str((GOAL + (3*ys[1]-ys[2])%p))))

y0 = ((GOAL + 3*ys[1] - ys[2]) / 3)
print(y0)
print(len(str(y0)))

# y0 = (GOAL - ys[1]*(xs[0]*xs[2]/((xs[1]-xs[0])*(xs[1]-xs[2]))) - ys[2]*(xs[0]*xs[1]/((xs[2]-xs[0])*(xs[2]-xs[1]))) )
# y0 = y0 / ((xs[1]*xs[2])/((xs[0]-xs[1])*(xs[0]-xs[2])))

# y0 = (GOAL - ys[1]*(xs[0]*xs[2]/((xs[1]-xs[0])*(xs[1]-xs[2]))) - ys[2]*(xs[0]*xs[1]/((xs[2]-xs[0])*(xs[2]-xs[1]))) )
# y0 = y0 / ((xs[1]*xs[2])/((xs[0]-xs[1])*(xs[0]-xs[2])))

y0 = round(y0)
print("Diff: ", y0-ys[0])
print("Num: ", y0)
print("Bytes: ", cun.long_to_bytes(y0))

print("Final", cun.long_to_bytes((ys[0]*3 - 3*ys[1] + ys[2])%p))
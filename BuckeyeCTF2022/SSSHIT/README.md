# SSSHIT

Another year, another crypto challenge. We all <3 math! Last year I "learned" Diffie-Hellman. This year I "learned" about [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) which is actually really interesting! Never heard of it before. Solid difficulty and I liked it just cause we were able to reverse it pretty easily compared to other stuff.

**Category**: crypto

**Points**: 330 points (41 solves)

**Description**:
SSS is so cool!

**Attachments**: [chall.py](./chall.py)

## Overview
We are given a python script containing source code for the challenge. From inspection, you can see and do research on [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing). TLDR, it's an algorithm that allows the distribution of a secret such that only when a certain number of shares are combined, you will get back your secret. In this problem, the shares are generated with all 3 shares and you NEED all 3 shares to get back your secret since the polynomial to generate the shares is `N_SHARES - 1` which including the original secret, makes `k=3`.

```python
polynomial = [MESSAGE] + [random.randrange(1, p) for _ in range(N_SHARES - 1)]
```

The follow code prompts the user for input:

```python
print("Your share is:")
print(points[0])
print("The other shares are:")
for i in range(1, len(points)):
    print(points[i])

print()
print("Now submit your share for reconstruction:")
your_input = ast.literal_eval(input(">>> "))
if (
    type(your_input) is not tuple
    or len(your_input) != 2
    or type(your_input[0]) is not int
    or type(your_input[1]) is not int
    or your_input[0] != 1
    or not (0 <= your_input[1] < p)
):
    print("Bad input")
    return
```

which is formatted like this: 
![prompt.png](./prompt.png)

Notice how there is an input validation where the input must be a tuple of length 2 where both values must be a number with the first number being 1 and the second number being within the generated prime p. Note that p is generated with `p = cun.getPrime(512)` so we basically have no hope of reversing this and getting p. 

We can try to put in our original share and it prints back `qxxxb, BuckeyeCTF admins, and NOT YOU` but we want the actual reconstructed message to be `qxxxb, BuckeyeCTF admins, and ME` after we insert our share. 

```python
reconstructed_message = cun.long_to_bytes(y_intercept)
if reconstructed_message == b"qxxxb, BuckeyeCTF admins, and ME":
    print("Here's your flag:")
    print("buckeye{?????????????????????????????????????????}")
else:
    print(f"Sorry, only these people can see the flag: {reconstructed_message}")
```

The reverse function is below is kind of complicated but the general idea is to reverse this operation so that when we pool our share together, it produces this new message.

```python
xs = [point[0] for point in points]
ys = [point[1] for point in points]

y_intercept = 0
for j in range(N_SHARES):
    product = 1
    for i in range(N_SHARES):
        if i != j:
            product = (product * xs[i] * pow(xs[i] - xs[j], -1, p)) % p
    y_intercept = (y_intercept + ys[j] * product) % p
```

## Solution
With the help of the Example Calculation section within the Wikipedia page, we have simpler example which makes the operation easier to understand. 
![example.PNG](./example.PNG)
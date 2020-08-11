spam_amount = 0
print(spam_amount)

# ordering spam, egg, spam, spam, bacon and spam (4 more servings of spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam" * spam_amount
print(viking_song)

color = "blue"
print(color)

pi = 3.14159
diameter = 3

radius = diameter * 0.5
print(radius)

area = pi * (radius ** 2)
print(area)

a = [1,2,3]
b = [3,2,1]

a, b = b, a

print(a, b)

print((5 - 3) // 2)

print(8 - (3 * 2) - (1 + 1))

alice_candies = 121
bob_candies = 77
carol_candies = 109

to_smash = (alice_candies + bob_candies + carol_candies) % 3

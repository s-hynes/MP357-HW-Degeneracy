
r = 1
s = 1
count_of_degen = 0

while (r**2 + s**2) <= 50:
    while (r**2 + s**2) <= 50:
        square_sum = r**2 + s**2
        if square_sum == 50:
            count_of_degen += 1
        print("r = {0}, s = {1}, r^2 + s^2 = {2}".format(r,s, r**2 + s**2))
        s += 1
    print("r = {0}, s = {1}, r^2 + s^2 = {2}".format(r,s, r**2 + s**2))
    print("")
    r += 1
    s =  1

print("r = {0}, s = {1}, r^2 + s^2 = {2}".format(r,s, r**2 + s**2))
print("\nDegeneracy of $E_{5,5}$ state =", count_of_degen)
# This could very easily be made into a function that checks the degeneracy of a state with any 
# arbitrary combination of r and s.
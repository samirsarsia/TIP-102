
"""1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count."""

def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    counter = 0
    for char in vip_passes:
        vip_set.add(char)
        
    for char in guests:
        if char in vip_set:
            counter += 1
    return counter

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))



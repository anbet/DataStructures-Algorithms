def towerOfHenoi(n, from_rod, to_rod, aux_rod):
    # Base condition
    if n ==1:
        print("Moving disk 1 from", from_rod, ' to the ', to_rod, ' rod')
    else:
        # Recurring condition
        towerOfHenoi(n-1, from_rod, aux_rod, to_rod)
        print("Moving the disk", n, ' from ', from_rod, " to the ", to_rod, 'rod')
        towerOfHenoi(n-1, aux_rod, to_rod, from_rod)

towerOfHenoi(4, 'From-Rod', 'To-Rod', 'Aux-Rod')

# Time complexity

# O(2^n)
# Formula for calculating time complexity for recurrsive calls is
# (Branching Factor)^n
# here Branching Factor = 2
# Since we are making two recursive calls

# Space Complexity

# In recursion problems, space complexity is calculated by measuring depth of the recursion tree
# Here the depth is n and space complexity is
#  O(n)
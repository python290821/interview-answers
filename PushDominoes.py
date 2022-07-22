class Solution(object):
    def pushDominoes(self, dominoes):
        # Define a forces variable which is a list  with length same as the length of dominoes initialized with zeros
        forces = [0] * len(dominoes)
        # Define a max_force variable and initialize it with the length of dominoes
        max_force = len(dominoes)

        # Define a force variable and initialize it with 0
        force = 0
        # Run over all the indexes together with items in dominoes
        for i, d in enumerate(dominoes):
            # If the domino has initial right force
            if d == 'R':
                # Set the force equal to max_force
                force = max_force
            # If the domino has initial left force
            if d == 'L':
                # Set the force equal to 0
                force = 0
            # Else, if the domino has no initial force
            # we are setting the force to maximum value between 0 and the previous domino force -1
            else:
                force = max(0, force - 1)
            # Set forces in the same index as current domino to be equal to the current force
            forces[i] = force

        # Run over all the indexes in reverse in range between 0 and the length of the dominoes -1
        for i in range(len(dominoes) - 1, -1, -1):
            # Extract the domino in current index from the dominoes
            d = dominoes[i]
            # If the domino has initial left force
            if d == 'L':
                # Set the force equal to max_force
                force = max_force
            # If the domino has initial right force
            if d == 'R':
                # Set the force equal to 0
                force = 0
            # Else, if the domino has no initial force,
            # we are setting the force to maximum value between 0 and the previous domino force -1
            else:
                force = max(0, force - 1)
            # Decrease the current force from the value of the force in the current index inside forces
            forces[i] -= force

        # Define result variable
        result = ''
        # Run over the forces
        for f in forces:
            # If the current force is 0
            if f == 0:
                # The domino is standing so it will be .
                result += '.'
            # Else, if the current force is positive
            elif f > 0:
                # The domino has collapsed to the right so it will be R
                result += 'R'
            # Else, if the current force is negative
            else:
                # The domino has collapsed to the left so it will be L
                result += 'L'
        return result


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR

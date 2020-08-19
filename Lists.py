def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    [racers[0], racers[-1]] = [racers[-1], racers[0]]

def fashionable_late(arrivals, name):
    arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
    name = arrivals[(int(round(len(arrivals)/2,0))):-1]
    return name

print(name)

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

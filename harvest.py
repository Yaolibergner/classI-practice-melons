############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

    def __repr__(self):

    	return f"{self.name}"


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    Musk = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    Musk.add_pairing("mint")
    Cas = MelonType("cas", "2003", "orange", False, False,"Casaba")
    Cas.add_pairing("mint")
    Cas.add_pairing("strawberries")
    Cren = MelonType("cren", "1996", "green", False, False, "Crenshaw")
    Cren.add_pairing("proscuitto")
    YWaterm = MelonType("yw", "2013", "yellow", True, True, "YWatermelon")
    YWaterm.add_pairing("ice cream")

    all_melon_types.extend([Musk, Cas, Cren, YWaterm])


    # Fill in the rest

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
   # melon_types = make_melon_types()
    for melon in melon_types:
    	print(f"{melon.name} pairs with")
    	for pair in melon.pairings:
    		print("- {}".format(pair))



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melontype_by_code = {}

    for melon in melon_types:

    	melontype_by_code[melon.code] = melon

    return melontype_by_code


melon_types = make_melon_types()
print_pairing_info(melon_types)
print(make_melon_type_lookup(melon_types))



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 




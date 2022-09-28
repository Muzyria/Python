from collections import OrderedDict

data = OrderedDict({'Law & Order': 1990, 'The Practice': 1997, 'Six Feet Under': 2001, 'Joan of Arcadia': 2003,
                    'The West Wing': 1999, 'Deadwood': 2004, 'The Sopranos': 1999, 'Boston Legal': 2004, 'ER': 1994,
                    'Friday Night Lights': 2006, '24': 2001, 'Heroes': 2006, 'Lost': 2004, 'Dexter': 2006,
                    'Damages': 2007, 'Big Love': 2006, 'House': 2004, 'Downton Abbey': 2010, "Grey's Anatomy": 2005,
                    'Homeland': 2011, 'Breaking Bad': 2008, 'Game of Thrones': 2011,
                    'CSI: Crime Scene Investigations': 2000, 'Boardwalk Empire': 2010, 'True Blood': 2008,
                    'House of Cards': 2013, 'True Detective': 2014})


data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)


print(data.sorted_keys(reverse=True))
print(data.sorted_values(reverse=True))
print(data.sorted_keys())

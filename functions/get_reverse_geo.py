"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
A simple function to return a nearest major city given a lat and long. The reverse_geocoder library
is an external library. In this instance it has a database of all world major cities with a population
gt 10,000 people so should be adequate for our use case.
"""

# Import the reverse_geocoder library. Link here: https://pypi.org/project/reverse_geocoder/
import reverse_geocoder as rg


def reverse_geo(lat, long):
    """Accepts a valid lat and long and returns the nearest major city with a population greater
    than 10,000 people."""
    coordinates = (lat, long)
    results = rg.search(coordinates)

    for key, value in results[0].items():
        if key == "name":
            city = value
        elif key == "cc":
            cc = value.lower()
    return city, cc


"""
A snippet to demonstrate how you might iterate through a csv
df = pd.read_csv("./testdata/chatter.csv")
for index, row in df.iterrows():
    df['city'] = reverse_geo(row['lat1'], row['long1'])
print(df.head())
"""

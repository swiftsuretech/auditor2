"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Here we attempt to retrieve a single record or 'flight plan'. Takes a record ID argument and attempts
to return a single record. If successful, it will enrich the returned data with some useful attributes,
Namely, a nearest City and Country Code.
"""

# Import our libraries:
import functions.gossip_data_frame as gdf
import functions.reversegeo as geo
import re


class Record:
    """A single record from the dataset with existing attributes enriched with further geo information"""

    def __init__(self, record_id):
        # TODO check the production dataset for field header. This may be incorrect
        self.result = gdf.DataSet().df[(gdf.DataSet().df.id == record_id)]
        if len(self.result):
            # We got a result. Populate our attributes.
            polygon = str(self.result.polygon)
            # Define a regex to capture our lat and long
            search_str = r'(?:POLYGON \(\()([0-9.\-]{3,})(?:\, )([0-9.\-]{3,})'
            self.lat, self.long = re.search(search_str, polygon).group(1), re.search(search_str, polygon).group(2)
            # Set also a nearest city and country code.
            self.city, self.cc = geo.reverse_geo(self.lat, self.long)
        else:
            # We didn't find a record. Return nulls instead of throwing an exception.
            self.lat = self.long = self.city = self.cc = None


test = Record(220)
print(test.lat, test.long, test.city, test.cc)

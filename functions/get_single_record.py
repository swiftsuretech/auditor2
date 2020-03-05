"""
Auditor2 by Dave Whitehouse | CGI Data Engineer | CII IDOT Team
Here we attempt to retrieve a single record or 'flight plan'. Takes a record ID argument and attempts
to return a single record in a dictionary. If successful, it will enrich the returned dictionary with
some useful attributes, namely, a nearest City and Country Code.
"""
# TODO When we switch to Elastic production data, we may be more efficient crafting a query for
#   a single record than loading up a dataframe just to filter it for a single record.

# Import our libraries:
import functions.get_all_records as gdf
import functions.get_reverse_geo as geo
import re


class Record:
    """A single record from the dataset with existing attributes enriched with further geo information"""

    def __init__(self, authid):
        # TODO check the production dataset for field headers. This is likely incorrect
        df = gdf.DataSet().df[(gdf.DataSet().df.authorizationID == authid)]
        if len(df):
            # We got a result. Populate our attributes.
            polygon = str(df['polygon'])
            # Define a regex to capture our lat and long
            search_str = r'(?:POLYGON \(\()([0-9.\-]{3,})(?:\, )([0-9.\-]{3,})'
            lat, long = re.search(search_str,
                                  polygon).group(1), re.search(search_str, polygon).group(2)
            # Set also a nearest city and country code.
            city, cc = geo.reverse_geo(lat, long)
            df['lat'] = lat
            df['transactionDate'] = df['transactionTime'].dt.date
            df['transactionTime'] = df['transactionTime'].dt.time
            df['long'] = long
            df['city'] = city
            df['cc'] = cc
            # Now the dataset is complete, turn it into a dictionary as it's only a single record.
            self.dict = df.to_dict(orient='list')
            self.dict['transactionDate'] = self.dict['transactionDate'][0].strftime('%d/%m/%Y')
            self.dict['startTime'] = self.dict['startTime'][0].strftime('%d/%m/%Y')
            self.dict['endTime'] = self.dict['endTime'][0].strftime('%d/%m/%Y')
            self.dict['geo'] = 'Search Area'
            self.dict['city'] = str(self.dict['city'][0]) + ', ' + str(self.dict['cc'][0]).upper()
            self.found = True
        else:
            # We didn't find a record. Set the 'found' attribute to False.
            self.found = False

# TODO - This module will need reworking as ES will return a json blob (dictionary)

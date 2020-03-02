import reverse_geocoder as rg


def reverse_geo(lat, long):
    global city, cc
    coordinates = (lat, long)
    results = rg.search(coordinates)

    for key, value in results[0].items():
        if key == "name":
            city = value
        elif key == "cc":
            cc = value.lower()
    return city


# df = pd.read_csv("./testdata/chatter.csv")
# for index, row in df.iterrows():
#     df['city'] = reverse_geo(row['lat1'], row['long1'])
#
# print(df.head())

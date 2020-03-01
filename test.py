from builddataframe import DataSet

test = DataSet()

test.filter(plat_filter='^The', user_filter='^Jos')
print(test.df)

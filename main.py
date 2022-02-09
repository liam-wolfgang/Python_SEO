# import pandas to download a keyword level report from semrush
import pandas as pd
keywords = pd.read_excel ('./assets/wolfgang_keywords.xlsx')

# Leave out keywords outside the top 15
low_hanging = keywords[keywords['Position'] < 15]
low_hanging_list = low_hanging.values.tolist()

# Transforming the list into a dictionary,
# URL = key & save the keyword, ranking & monthly searches
dict_urls = {}
for urls in low_hanging_list:
    if urls[6] in dict_urls:
        dict_urls[urls[6]] += [[urls[0], urls[1], urls[3]]]
    else:
        dict_urls[urls[6]] = [[urls[0], urls[1], urls[3]]]




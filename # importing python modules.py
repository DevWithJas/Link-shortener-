# importing python modules 

import pyshorteners

long_link = input("your link:")
shortener = pyshorteners.Shortener()
short_link = shortener.tinyurl.short(long_link)
print(short_link)



Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> from pytrends.request import TrendReq
>>> import matplotlib.pyplot as plt
>>> trends = TrendReq()
>>> trends.build_payload(kw_list=["Machine Learning"])
>>> data = trends.interest_by_region()
>>> data = data.sort_values(by="Machine Learning", ascending=False)
>>> data = data.head(10)
>>> print(data)
             Machine Learning
geoName                      
China                     100
Singapore                  40
St. Helena                 33
India                      30
Ethiopia                   27
Hong Kong                  25
South Korea                24
Nepal                      19
Pakistan                   19
Israel                     18
>>> data.reset_index().plot(x="geoName", y="Machine Learning",figsize=(20,15), kind="bar")
<AxesSubplot:xlabel='geoName'>
>>> plt.style.use('fivethirtyeight')
>>> plt.show()
>>> data = TrendReq(hl='en-US', tz=360)
>>> data.build_payload(kw_list=['Machine Learning'])
>>> data = data.interest_over_time()
>>> fig, ax = plt.subplots(figsize=(20, 15))
>>> data['Machine Learning'].plot()
<AxesSubplot:xlabel='date'>
>>> plt.style.use('fivethirtyeight')
>>> plt.title('Total Google Searches for Machine Learning', fontweight='bold')
Text(0.5, 1.0, 'Total Google Searches for Machine Learning')
>>> plt.xlabel('Year')
Text(0.5, 0, 'Year')
>>> plt.ylabel('Total Count')
Text(0, 0.5, 'Total Count')
>>> plt.show()

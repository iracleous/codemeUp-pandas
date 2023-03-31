# read json

import requests
import pandas as pd

url = "https://diavgeia.gov.gr/luminapi/opendata/organizations/6081/units.json"


datas = requests.get(url).json()['units'] 

#print(datas)
dataf = pd.DataFrame.from_dict(datas)

print(dataf)
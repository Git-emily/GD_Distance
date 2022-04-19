import pandas as pd
import numpy as np
import requests




def main(name,column):
    data_Location = []
    data = pd.read_csv(name+'.csv',sep=',')
    Location = data[column].tolist()
    n = 10
    split_Location = [Location[i:i+n] for i in range(0,len(Location),n)]
    for item in split_Location:
        name_Location = '|'.join(item)
        data_Location.append(name_Location)
    get_coordinate(data_Location,data,name)

def get_coordinate(data_Location,data,name):
    Location_list = []
    for address in data_Location:
        url = 'https://restapi.amap.com/v3/geocode/geo';
        parameters = {'key': "5c5cf68cefc1682dcbfdf84a3a7d88c2",
                    'address': address,
                    'batch': True}
        response = requests.get(url,parameters)
        response_json = response.json()
        coordinate = response_json['geocodes']
        for item in coordinate:
            Location_list.append(item['location'])
    print(Location_list)
    data['Cood'] = Location_list
    data.to_csv('Update_'+ name +'.csv',encoding = 'utf_8_sig')

def cal_distance():
    print('cal_distance')

if __name__ == '__main__':
    name = 'Location'#'甘肃发货信息'
    column = 'Location'#'place_of_loading'
    main(name,column)
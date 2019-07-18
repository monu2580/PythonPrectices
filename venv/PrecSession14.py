from newsapi import NewsApiClient
import json

import requests
"""api=NewsApiClient(api_key='e1a9551f4e9943258f776cdf4f387aa4')

top_headlines = api.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
top_headlines = api.get_top_headlines(sources='bbc-news,the-verge')

print(top_headlines)"""

"""url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=e1a9551f4e9943258f776cdf4f387aa4')
response = requests.get(url)
print (response.json())
newsapidata= response.json()
print(newsapidata)"""


import sys
import json
import requests
"""
    Class FonApi
    Author @jesusperiago
    Version 1
"""


class FonApi:

    __ApiUrl = 'https://fonoapi.freshpixl.com/v1/'

    def __init__(self, apikey, url=None):

        self.__ApiUrl = FonApi.__ApiUrl

        if url is not None:
            self.__ApiUrl = url

        self.__ApiKey = apikey

    def getdevice(self, device, position=None, brand=None):
        """
            Get device data object and return a json list
        :param device:
        :param position:
        :param brand:
        :return device list:
        """
        url = self.__ApiUrl + 'getdevice'
        postdata = {'brand': brand,
                    'device': device,
                    'position': position,
                    'token': self.__ApiKey}
        headers = {'content-type': 'application/json'}
        result = self.sendpostdata(url, postdata, headers)
        try:
            return result.json()
        except AttributeError:
            return result

    def sendpostdata(self, url, postdata, headers, result = None):
        """
            Send data to the server
        :param url:
        :param postdata:
        :param headers:
        :return requests.post result:
        """
        try:
            result = requests.post(url, data=json.dumps(postdata), headers=headers)

            # Consider any status other than 2xx an error
            if not result.status_code // 100 == 2:
                return "Error status page: " + str(result)
            # Try send the result text else send the error
            try:
                if result.json()['status'] == 'error':

                    if result.json()['message'] == 'Invalid Token. Generate a Token at fonoapi.freshpixl.com.':
                        return "Check __ApiKey"

                return result.json()['message']
            except:
                pass

            return result
        except requests.exceptions.RequestException as e:
            # A serious problem happened, like an SSLError or InvalidURL
            return "Connect error. Check URL"

f1 = FonApi('f37b737c1241bae30f280f947dccf5428da6d97a71271f8f');
print(f1.getdevice('Galaxy s9'))
print('')
print('')
DeviceData = f1.getdevice('iphone')

# for i in DeviceData:
#     print("*************************************")
#     print('')
#     print(i)

print(DeviceData[0])

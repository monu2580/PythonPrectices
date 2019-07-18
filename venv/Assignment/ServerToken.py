import googlemaps
import requests
# class ServerToken:
#
#     def __str__(self):
#         clintId = "tBn1cdVpU1tsC8olp-9Clo_Eb7S8Qctt"
#         sToken="KB3zJc6afzokXnX2VaXauL7GNLxgKjUoLgzrtiQI"
#         return sToken

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyBV4bw7_74Y5bWuGHiAz4jONqDNAJLrzqc')

resp_json_payload = response.json()
#strtLat=
print(resp_json_payload['results'][0]['geometry']['location'])
print(resp_json_payload['results'][1])
import requests
import datetime
import pytz
from classes import Root
from classes import Response

#Constants
MY_LATITUDE =  53.123482
MY_LONGITUDE = 18.0084380
LOCAL_TIMEZONE = pytz.timezone("Europe/Warsaw")

#Parameters to post
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

#Response for sunset and sunrise
response = requests.get(url=" https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

#response for iss location
response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()


data = Root.from_dict(response.json())
data_iss = Response.from_dict(response_iss.json())

sunrise_full = datetime.datetime.strptime(data.results.sunrise,"%Y-%m-%dT%H:%M:%S%z").astimezone(LOCAL_TIMEZONE)
sunset_full = datetime.datetime.strptime(data.results.sunset,"%Y-%m-%dT%H:%M:%S%z").astimezone(LOCAL_TIMEZONE)

czy_iss_longitude = data_iss.iss_position.latitude in (MY_LATITUDE-5,MY_LATITUDE,MY_LATITUDE+5)
czy_iss_latitude = data_iss.iss_position.longitude in (MY_LONGITUDE-5,MY_LONGITUDE,MY_LONGITUDE+5)
czy_iss = True if czy_iss_longitude and czy_iss_latitude else False

after_sunset =  True if sunset_full.time() < datetime.datetime.now().time() else False
before_sunrise = True if sunrise_full.time() > datetime.datetime.now().time() else False

if(after_sunset or before_sunrise) and czy_iss:
    print("Go look it should be there")
else:
    print("Nothing")



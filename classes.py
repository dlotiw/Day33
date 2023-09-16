from typing import Any
from dataclasses import dataclass


@dataclass
class Results:
    sunrise: str
    sunset: str
    solar_noon: str
    day_length: int
    civil_twilight_begin: str
    civil_twilight_end: str
    nautical_twilight_begin: str
    nautical_twilight_end: str
    astronomical_twilight_begin: str
    astronomical_twilight_end: str

    @staticmethod
    def from_dict(obj: Any) -> 'Results':
        _sunrise = str(obj.get("sunrise"))
        _sunset = str(obj.get("sunset"))
        _solar_noon = str(obj.get("solar_noon"))
        _day_length = int(obj.get("day_length"))
        _civil_twilight_begin = str(obj.get("civil_twilight_begin"))
        _civil_twilight_end = str(obj.get("civil_twilight_end"))
        _nautical_twilight_begin = str(obj.get("nautical_twilight_begin"))
        _nautical_twilight_end = str(obj.get("nautical_twilight_end"))
        _astronomical_twilight_begin = str(obj.get("astronomical_twilight_begin"))
        _astronomical_twilight_end = str(obj.get("astronomical_twilight_end"))
        return Results(_sunrise, _sunset, _solar_noon, _day_length, _civil_twilight_begin, _civil_twilight_end, _nautical_twilight_begin, _nautical_twilight_end, _astronomical_twilight_begin, _astronomical_twilight_end)

@dataclass
class Root:
    results: Results
    status: str

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _results = Results.from_dict(obj.get("results"))
        _status = str(obj.get("status"))
        return Root(_results, _status)


@dataclass
class IssPosition:
    latitude: float
    longitude: float

    @staticmethod
    def from_dict(obj: Any) -> 'IssPosition':
        _latitude = float(obj.get("latitude"))
        _longitude = str(obj.get("longitude")) 
        return IssPosition(_latitude, _longitude)

@dataclass
class Response:
    message: str
    timestamp: str  # Assuming the timestamp is an integer UNIX timestamp
    iss_position: IssPosition

    @staticmethod
    def from_dict(obj: Any) -> 'Response':
        _message = str(obj.get("message"))
        _timestamp = str(obj.get("timestamp"))
        _iss_position = IssPosition.from_dict(obj.get("iss_position")) 
        return Response(_message, _timestamp,_iss_position)

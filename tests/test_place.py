import os, sys
sys.path.append(os.path.abspath('.'))
import pytest
import urllib


from weather import place

obs = place.Place('vic', 'parkville')

def test_air_temperature():
    air_temperature = obs.air_temperature()
    assert air_temperature is not None
    assert air_temperature > -30.0
    assert air_temperature < 60.0

def test_station_id():
    station_id = obs.station_id()
    assert station_id is not None
    assert len(station_id) == 5

def test_404():
    with pytest.raises(urllib.error.HTTPError, match='HTTP Error 404: Not Found'):
        obs = place.Place('vic', 'zzz')

from weather_parser import parse_weather_data


def test__parse_weather_data__returns_correct_dict():
    data = {'main': {'temp': -1.48, 'feels_like': -8.25}, 'weather': [{'description': 'snow'}]}
    expected_output = {'temperature': -1.48, 'feels_like': -8.25, 'description': 'snow'}
    assert parse_weather_data(data) == expected_output

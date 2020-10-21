import json
import pytest

from app import *

test_total_sample_data = [12]
test_total_data = [({"total": 50000005000000})]


def test_total_invalid_url(app, client):
    result = client.get('/')
    assert result.status_code == 404


@pytest.mark.parametrize("expected", test_total_sample_data)
def test_sum_of_list_of_numbers(expected):
    inputlist=[1,2,3,6]
    actual_output = sum_of_list_of_numbers(inputlist)
    assert actual_output == expected


@pytest.mark.parametrize("expected", test_total_data)
def test_total(app, client, expected):
    result = client.get('/total')
    assert result.status_code == 200
    assert expected == json.loads(result.get_data(as_text=True))
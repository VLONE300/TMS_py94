from home_works.lesson19.app import client


def test_simple():
    my_list = [1, 2, 3, 4]
    assert 1 in my_list


def test_get():
    res = client.get('/')
    assert res.status_code == 200

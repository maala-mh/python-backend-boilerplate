def test_hc(client):
    assert 1 == 1, "invalid test"


def test_get_foo(client):
    client.post("/foo", json={"email": "maala.m.mhrez@gmail.com"})
    res = client.get("/foo").json()
    assert res, "oops! no foo was found!"

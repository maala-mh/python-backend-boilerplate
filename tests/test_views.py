def test_hc(client):
    res = client.get("/hc").json()
    assert res["message"] == "ok"


def test_convert(client):
    html = """
        <html>
        <head><h1>Hello, World!</h1></head>
        <body>This PDF is generated using PDFKit</body>
        </html>
    """
    res = client.post("/convert-to-pdf", json={"html": html}).json()
    breakpoint()
#    assert res["message"] == "ok"

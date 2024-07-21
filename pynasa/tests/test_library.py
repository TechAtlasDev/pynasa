import pynasa, datetime

def test_apod():
    nasa = pynasa.NASA(key="DEMO_KEY")
    apod = nasa.apod()
    assert apod != None
    assert apod.title != None
    assert apod.date == datetime.datetime.today().strftime('%Y-%m-%d')


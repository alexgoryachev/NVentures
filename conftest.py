import pytest
from fixture.application import Application
import json
fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    with open ("C:/dev/nVenture/target.json", ) as config_file:
        target = json.load(config_file)

    if fixture is None or not fixture.is_valid():
        print('Going to open page')
        fixture = Application(browser = browser, base_url = target["baseurl"])
        print (fixture.baseurl)
#    fixture.session.insure_login(username=target['username'], password=target['password']) - in case of log in
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        pass
        #fixture.session.insure_logout()  - in case of login
        #fixture.destroy()- in case of login
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action= "store", default = "Chrome")
    parser.addoption("--target", action= "store", default = "target.json")

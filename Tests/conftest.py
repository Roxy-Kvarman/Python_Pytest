import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.options import Options
import Utilities.Logger as L
import sys


@pytest.fixture(params=["chrome"], scope='class')
def set_up(request, test_log):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        web_driver = webdriver.Chrome(options=options, executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver.implicitly_wait(10)
        L.logging.info("Navigate to Main page")
        web_driver.get(TestData.BASE_URL)
        web_driver.implicitly_wait(10)
        request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.fixture(scope='class', autouse=True)
def test_log(request):
    L.logging.info("Test '{}' STARTED".format(request.node.nodeid))
    def fin():
        L.logging.info("Test '{}' COMPLETED".format(request.node.nodeid))
    request.addfinalizer(fin)


def pytest_runtest_call(__multicall__):
    try:
        __multicall__.execute()
    except KeyboardInterrupt:
        raise
    except:
        L.logging.exception('pytest_runtest_call caught exception:')
        raise




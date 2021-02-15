from page.main import Main
import time
from util.get_cookie import Utils


class TestLogin:
    def setup(self):
        self.main = Main()

    def teardown(self):
        pass

    def test_login(self):
        self.main.goto_login()




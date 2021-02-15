from page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def teardown(self):
        pass

    def test_register(self):
        assert self.main.goto_register().register()
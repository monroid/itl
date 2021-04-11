class TestApp:
    def test_converter_work(self, app):
        res = app.run(["-c", "3", "8.8.8.8"])
        print(res.stdout.split('\n'))

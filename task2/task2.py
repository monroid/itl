import subprocess


class App:
    def __init__(self, path=""):
        self.path = path

    def run(self, args=[]):
        cmd_arr = [self.path]
        cmd_arr.extend(args)
        cmd = subprocess.run(
            cmd_arr,
            text=True,
            stdout=subprocess.PIPE)
        return cmd

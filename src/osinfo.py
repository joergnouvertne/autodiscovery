import platform


class OSInfo:
    def __init__(self):
        self.os_name = self.get_os_name()

    def get_os_name(self):
        os_name = platform.system()
        if os_name == 'Darwin':
            os_name = 'MacOS'
        elif not os_name:
            os_name = 'Unknown'
        return os_name

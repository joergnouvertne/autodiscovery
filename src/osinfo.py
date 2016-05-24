import platform


class OSInfo:
    def __init__(self):
        self.os_name = self.get_os_name
        self.os_version = self.get_os_version

    @property
    def get_os_name(self):
        os_name = platform.system()
        if os_name == 'Darwin':
            os_name = 'MacOS'
        elif not os_name:
            os_name = 'Unknown'
        return os_name

    @property
    def get_os_version(self):
        os_version = 'Unknown'
        if self.get_os_name == 'Windows':
            os_version = platform.win32_ver()[0]
        elif self.get_os_name == 'MacOS':
            os_version = platform.mac_ver()[0]
        return os_version

    @property
    def get_info(self):
        info = {key: value for key, value in self.__dict__.items() if not (key.startswith('__') and key.endswith('__'))}
        return info

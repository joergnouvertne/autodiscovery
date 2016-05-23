import platform


class LinuxOSInfo:
    def __init__(self):
        self.platform_name = platform.system()

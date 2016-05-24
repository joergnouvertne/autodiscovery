import platform
import re


class OSInfo:
    def __init__(self):
        self.os_type = self.get_os_type
        self.os_name = self.get_os_name
        self.os_version = self.get_os_version
        self.os_release = self.get_os_release
        self.machine_type = self.get_machine_type
        self.hostname = self.get_hostname

    @property
    def get_os_type(self):
        os_name = platform.system()
        if os_name == 'Darwin':
            return 'MacOS'
        elif not os_name:
            return "Unknown"
        else:
            return os_name

    @property
    def get_os_name(self):
        os_name = self.get_os_type
        if os_name == 'Linux':
            return platform.linux_distribution()[0].strip()
        elif os_name:
            return os_name
        else:
            return "Unknown"

    @property
    def get_os_version(self):
        if self.get_os_type == 'Windows':
            return platform.win32_ver()[0]
        elif self.get_os_type == 'MacOS':
            return platform.mac_ver()[0]
        elif self.get_os_type == 'Linux':
            os_version = platform.linux_distribution()[1]
            if re.match("SUSE", self.get_os_name):
                with open("/etc/os-release", "r") as fobj:
                    for line in fobj:
                        if "VERSION_ID" in line:
                            os_version = line.split("=")[1].strip().strip('"')
                    if "." not in os_version:
                        os_version += ".0"
            return os_version
        else:
            return "Unknown"

    @property
    def get_os_release(self):
        os_type = self.get_os_type
        if os_type == 'Windows':
            return platform.version()
        elif os_type == 'Linux' or os_type == 'MacOS':
            return platform.release()
        else:
            return "Unknown"

    @property
    def get_machine_type(self):
        if platform.machine():
            return platform.machine()
        else:
            return "Unknown"

    @property
    def get_hostname(self):
        if platform.node():
            return platform.node().lower()
        else:
            return "Unknown"

    @property
    def get_info(self):
        info = {key: value for key, value in self.__dict__.items() if not (key.startswith('__') and key.endswith('__'))}
        return info

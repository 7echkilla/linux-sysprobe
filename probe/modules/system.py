import platform

from probe.module import Module

class System(Module):
    def __init__(self):
        """
        Information relevant to device
        """
        self.name = "system"
        self.description = "System information"

    def get_data(self):
        """
        Return dictionary with all CPU metrics
        """
        data = {}
        
        data.update(self._get_hostname())
        data.update(self._get_os())
        data.update(self._get_kernel())
        data.update(self._get_architecture())
        data.update(self._test())

        return data
    
    def _get_hostname(self):
        """
        Get device name
        """
        hostname = platform.node()

        return {"Device Name": hostname}
    
    def _get_os(self):
        """
        Get current OS
        """
        os = platform.system()

        return {"OS": os}
    
    def _get_kernel(self):
        """
        Get kernel version
        """
        kernel = platform.release()

        return {"Kernel": kernel}
    
    def _get_architecture(self):
        """
        Get device architecture
        """
        architecture = platform.machine()

        return {"Architecture": architecture}
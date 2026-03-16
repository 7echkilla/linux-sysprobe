import psutil

from probe.plugin import Plugin

class CPU(Plugin):
    """Utility for CPU"""

    name = "cpu"
    description = "CPU utility"

    def collect(self):
        return self._get_cpu_usage()
    
    def _get_cpu_usage(self):
        return {"cpu_usage": psutil.cpu_percent}
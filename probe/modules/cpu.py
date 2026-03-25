import os
import psutil

from probe.module import Module

class CPU(Module):
    def __init__(self):
        """
        Metrics relevant to CPU
        """
        self.name = "cpu"
        self.description = "CPU metrics"

    def get_data(self):
        """
        Return dictionary with all CPU metrics
        """
        data = {}
        
        data.update(self._get_usage())
        data.update(self._get_physical_cores())
        data.update(self._get_logical_cores())
        data.update(self._get_load_average())
        data.update(self._get_core_temperature())

        return data
    
    def _get_usage(self):
        """
        Get current CPU usage percentage
        """
        cpu_usage = psutil.cpu_percent()
        
        return {"CPU Usage (%)": cpu_usage}
    
    def _get_physical_cores(self):
        """
        Get number of physical CPU cores
        """
        cpu_count = psutil.cpu_count(logical=False)

        return {"Physical Cores": cpu_count}
    
    def _get_logical_cores(self):
        """
        Get number of logical CPU cores
        """
        cpu_count = psutil.cpu_count(logical=True)

        return {"Logical Cores": cpu_count}
    
    def _get_load_average(self):
        """
        Get load average
        """
        load_avg = os.getloadavg()
        one_minute = round(load_avg[0], 2)
        five_minute = round(load_avg[1], 2)
        fifteen_minute = round(load_avg[2], 2)

        string = f"1m: {one_minute}, 5m: {five_minute}, 15m: {fifteen_minute}"

        return {"Load Average": string}
    
    def _get_core_temperature(self):
        """
        Get CPU temperature (if supported)
        """
        try:
            temperature = psutil.sensors_temperatures()
            core_temperature = temperature.get('coretemp', [])
            cpu_temperature = core_temperature[0].current if core_temperature else "N/A"
        except AttributeError:
            cpu_temperature = "N/A"
        
        return {"CPU Temperature (°C)": cpu_temperature}
import psutil

from probe.plugin import Plugin

class Memory(Plugin):
    """Utility for RAM"""

    name = "memory"
    description = "memory utility"

    def collect(self):
        mem = psutil.virtual_memory()

        return {
            "percent": mem.percent,
            "used_gb": round(mem.used / (1024**3), 2),
            "total_gb": round(mem.total / (1024**3), 2)
        }
    
    def get_app(self):
        app = super().get_app()

        @app.command(name="free")
        def free_memory():
            mem = psutil.virtual_memory()
            print(f"Free Memory: {mem.free / (1024**3):.2f} GB")

        return app
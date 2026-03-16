import pkgutil
import importlib
import probe.plugins

from probe.plugin import Plugin

def load_plugins():
    """Detect and return plugins from directory"""

    plugins = {}

    for _, name, _ in pkgutil.iter_modules(probe.plugins.__path__):
        plugin = importlib.import_module(f"probe.plugins.{name}")

        for object in vars(plugin).values():
            if (isinstance(object, type) and issubclass(object, Plugin) and object is not Plugin):
                instance = object()
                plugins[instance.name] = instance

    return plugins

if __name__ == "__main__":
    print(load_plugins())
import pkgutil
import importlib
import probe.modules

from probe.module import Module

def load_modules():
    """
    Detect and load modules from designated directory
    """
    modules = {}

    for _, name, _ in pkgutil.iter_modules(probe.modules.__path__):
        module = importlib.import_module(f"probe.modules.{name}")

        for object in vars(module).values():
            if (isinstance(object, type) and issubclass(object, Module) and object is not Module):
                instance = object()

                if (not instance.name):
                    print(f"Skipped invalid module with no name")
                
                elif (instance.name in modules):
                    print(f"Skipped module with duplicate name: {instance.name}")
                
                else:
                    modules[instance.name] = instance

    return modules

if __name__ == "__main__":
    print(load_modules())
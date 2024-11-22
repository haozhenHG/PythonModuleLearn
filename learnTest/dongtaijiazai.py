import importlib
import sys,os
import inspect

class DynamicLoader:
    def __init__(self):
        self._obj_cache = {}  # Cache to store loaded classes

    def __getattr__(self, cls_name):
        if cls_name in self._obj_cache:
            return self._obj_cache[cls_name]

        # Define the paths where to search for the module
        valid_lib_paths = ['/path/to/your/modules']  # Replace with actual paths

        for lib_path in valid_lib_paths:
            for lib_file in os.listdir(lib_path):
                if lib_file.endswith(".py") and not lib_file.startswith('_'):
                    mod_name = lib_file[:-3]  # Remove '.py'
                    if mod_name not in sys.modules:
                        mod_path = os.path.join(lib_path, mod_name)
                        try:
                            spec = importlib.util.spec_from_file_location(mod_name, mod_path)
                            module = importlib.util.module_from_spec(spec)
                        except ImportError as e:
                            print(f"Failed to load {mod_name}: {e}")
                            continue
                        # Check if the class exists in the module
                        for name, cls in inspect.getmembers(module, inspect.isclass):
                            if name == cls_name:
                                self._obj_cache[cls_name] = cls
                                return cls()
        raise ImportError(f"Could not find {cls_name} in any modules")

# Usage
loader = DynamicLoader()
try:
    my_class = loader.DemoClass()  # This will trigger __getattr__
except ImportError as e:
    print(e)
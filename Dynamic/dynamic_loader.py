import importlib
import inspect
import sys,os

class DynamicLoader:
    def __init__(self):
        self._obj_cache = {}  # Cache to store loaded classes

    def load_class(self, module_name, class_name):
        # Check if class is already in cache
        if class_name in self._obj_cache:
            return self._obj_cache[class_name]

        # Get the path of the current file
        current_file = inspect.getfile(self.__class__)
        print('current_file:',current_file) # 'D:\\PythonProject\\Dynamic\\dynamic_loader.py'

        # Get the directory of the current file
        current_dir = os.path.dirname(current_file)
        print('current_dir:',current_dir) # 'D:\\PythonProject\\Dynamic'


        # Build the full path to the module
        mod_path = os.path.join(current_dir, module_name)
        print('mod_path:',mod_path)# 'D:\\PythonProject\\Dynamic\\module_a'

        print('sys.modules:',sys.modules)
        # Check if the module is a Python file and not already imported
        if mod_path.endswith('.py') and mod_path not in sys.modules:
            spec = importlib.util.spec_from_file_location(module_name, mod_path)
            module = importlib.util.module_from_spec(spec)
        else:
            module = sys.modules[module_name]

        # Get the class from the module
        for name, cls in inspect.getmembers(module, inspect.isclass):
            if name == class_name:
                self._obj_cache[class_name] = cls
                return cls()

        raise ImportError(f"Could not find {class_name} in {module_name}")
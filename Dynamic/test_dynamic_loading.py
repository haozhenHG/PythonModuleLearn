# Assuming dynamic_loader.py, module_a.py, and module_b.py are in the same directory

from Dynamic.dynamic_loader import DynamicLoader

# Create an instance of the DynamicLoader
loader = DynamicLoader()

# Load and use the DemoClass from module_a
demo_a = loader.load_class('module_a', 'DemoClass')
demo_a.display()  # Output: This is from module_a

# Load and use the DemoClass from module_b
demo_b = loader.load_class('module_b', 'DemoClass')
demo_b.display()  # Output: This is from module_b
class LibraryManager:
    def __init__(self, product=None):
        self._product = product

    def _get_lib_path(self):
        # 假设这是库路径的字典，实际应用中可能需要从文件系统或配置中获取
        return {
            'generic': '/path/to/generic/lib',
            'productA': '/path/to/productA/lib',
            'productB': '/path/to/productB/lib'
        }

    def get_valid_lib_paths(self):
        # 根据是否有产品信息来决定搜索哪些库路径
        if self._product:
            valid_lib_paths = [ self._get_lib_path()[x] for x in ([self._product, "generic"] if self._product else ["generic"])]

        else:
            valid_lib_paths = [self._get_lib_path()["generic"]]
        return valid_lib_paths

# 创建 LibraryManager 类的实例
# 如果没有产品信息，可以这样创建实例：manager = LibraryManager()
# 如果有产品信息，可以这样创建实例：
manager = LibraryManager(product='productA')
# 获取有效的库路径列表
valid_lib_paths = manager.get_valid_lib_paths()

# 打印有效的库路径
print(valid_lib_paths)
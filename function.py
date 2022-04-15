class Function:
    def __init__(self, function_id, function_imports, package_size):
        self.function_id = function_id
        self.function_imports = function_imports
        self.package_size = package_size

    def getLargestPackage(self):
        if(len(self.function_imports)):
            return {"", self.function_imports[0]}
        return {"Do not Have any packages to import from lambda : ", None}

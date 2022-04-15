class Function:
    def __init__(self, function_id, function_imports, exec_time):
        self.function_id = function_id
        self.function_imports = function_imports
        self.exec_time = exec_time

    def getLargestPackage(self):
        if(len(self.function_imports)):
            return {"", self.function_imports[0]}
        return {"Do not Have any packages to import from lambda : ", None}

from llvmlite import ir

class Save:
    def __init__(self, moudle: ir.Module):
        self.Moudle = moudle
        
    def save_file(self, name):
        with open(name, "w") as file:
            file.write(str(self.Moudle))
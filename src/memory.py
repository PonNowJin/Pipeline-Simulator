class Memory:
    def __init__(self, size=32):
        # 記憶體初始化，每個 word 預設為 1
        self.memory = [1] * size
        self.instruct_count = 0
        
    def read(self, address):
        """ 讀取 memory 值(byte-addressed, 但 word 為單位） """
        if address % 4 != 0:
            raise ValueError("Unaligned memory address")
        word_address = address // 4
        
        if 0 <= word_address < len(self.memory):
            return self.memory[word_address]
        raise ValueError("Invalid memory address")
    
    def write(self, address, value):
        """ 寫入 memory 值(byte-addressed, 但 word 為單位） """
        if address % 4 != 0:
            raise ValueError("Unaligned memory address")
        word_address = address // 4
        
        if 0 <= word_address < len(self.memory):
            self.memory[word_address] = value
        else:
            raise ValueError("Invalid memory address")
        
    def load_instruction(self, file_path:str):
        """ 讀入 input txt file """
        with open(file=file_path) as f:
            for line in f:
                self.memory[self.instruct_count] = line.rstrip()  # 去除行尾的換行符
                self.instruct_count += 1
        

    def dump(self, file=None):
        """顯示 memory 內容"""
        for i, val in enumerate(self.memory):
            print(f"W{i} ", end="", file=file, flush=True)
        print(file=file, flush=True)
        for i, val in enumerate(self.memory):
            print(f"{val}  ", end="", file=file, flush=True)
        print(file=file, flush=True)

            
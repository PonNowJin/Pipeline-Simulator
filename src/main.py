import argparse
from registers import Registers
from memory import Memory
from pipeline import PipelineSimulator
from pathlib import Path


def main():
    # 使用 argparse 解析終端機輸入的參數
    parser = argparse.ArgumentParser(description="Pipeline Simulator")
    parser.add_argument("input_file", type=str, help="Path to the input instruction file")
    args = parser.parse_args()

    # 獲取檔案路徑
    input_file = Path(args.input_file)
    if not input_file.exists():
        print(f"Error: File '{input_file}' does not exist.")
        return
    
    # 生成輸出檔案路徑
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)  # 確保 output 資料夾存在
    output_file = output_dir / f"{input_file.stem}.txt"  # 使用與輸入檔案相同名稱的 .txt 檔案
    
    # 初始化暫存器與記憶體
    instruct_memory = Memory(size=32)
    instruct_memory.load_instruction(input_file)
    pipeline = PipelineSimulator(instruct_memory, output_file=str(output_file), debug_reg_mem=False, debug_pipeline_reg=False)
    pipeline.run()
    
if __name__ == "__main__":
    main()

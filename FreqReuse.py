class Cell:
    def __init__(self,cell_id):
        self.cell_id = cell_id
        self.frequency = -1 #未分配頻率

def main():
    NUM_CELLS = 19  # 示例中小型網格的單元數
    REUSE_FACTOR = 7  # 頻率重用因子
    NUM_FREQUENCY = 7  # 可用頻率數量

    # 初始化頻率列表
    frequencies = [i + 1 for i in range(NUM_FREQUENCY)]

    # 初始化單元
    cells = [Cell(i) for i in range(NUM_CELLS)]

    for i in range(NUM_CELLS):
        assingned_frequency = frequencies[i % REUSE_FACTOR]
        cells[i].frequency = assingned_frequency

        # 確保沒有相鄰單元有相同的頻率
        # 這裡我們假設簡單的行優先鄰接關係以簡化問題
        if i > 0 and cells[i-1].frequency == assingned_frequency:
            cells[i].frequency = frequencies[(i+1)% REUSE_FACTOR]
    print("單元頻率分配")
    for cell in cells:
        print(f"單元 id :{cell.cell_id}, 頻率: {cell.frequency}")

if __name__ == "__main__":
    main()
# 从pathlib模板中导入Path类
from pathlib import Path

# 定义main函数
def main():
    # 用参数生成一个路径对象
    test_dir=Path("./test_files")

    # 如果路径存在
    if test_dir.exists():
        print("success find folder")
        print(f"files of folder:{list(test_dir.iterdir())}")
    else:
        print("failed to find folder")

# 如果我是被直接运行的那就调用main，如果不是，就什么都不做
if __name__ == "__main__":
    main()

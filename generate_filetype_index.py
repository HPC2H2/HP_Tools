import os
from collections import defaultdict

def generate_filetype_index():
    # 获取当前目录
    """
    生成当前目录下所有文件和文件夹的类型索引
    
    此函数会遍历当前工作目录下的所有项目,按照文件类型进行分类并生成索引文件。
    - 文件夹会被标记为 [文件夹] 类型
    - 无扩展名文件会被标记为 [无扩展名] 类型
    - 其他文件按扩展名分类
    
    生成的索引文件包含:
    - 当前目录路径
    - 项目类型总数
    - 每种类型的项目列表(按字母顺序排序)
    
    输出:
        在当前目录生成 filetype_index.txt 文件
    """
    current_dir = os.getcwd()
    
    # 创建一个字典来存储类型和对应的项目列表
    item_index = defaultdict(list)
    
    # 遍历当前目录下的所有项目
    for item in os.listdir(current_dir):
        # 跳过脚本本身
        if item == os.path.basename(__file__):
            continue
            
        # 判断是文件还是文件夹
        if os.path.isdir(item):
            # 文件夹
            item_index["[文件夹]"].append(item + os.sep)  # 添加斜杠表示是文件夹
        else:
            # 文件
            _, ext = os.path.splitext(item)
            ext = ext.lower()  # 统一转为小写
            item_index[ext if ext else "[无扩展名]"].append(item)
    
    # 按类型排序（文件夹排在最前面）
    def sort_key(item):
        if item[0] == "[文件夹]":
            return (0, item[0])
        elif item[0] == "[无扩展名]":
            return (2, item[0])
        else:
            return (1, item[0])
    
    sorted_items = sorted(item_index.items(), key=sort_key)
    
    # 写入到txt文件
    output_file = "filetype_index.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"当前目录内容索引: {current_dir}\n\n")
        f.write(f"共找到 {len(sorted_items)} 种项目类型\n\n")
        
        for item_type, items in sorted_items:
            f.write(f"=== {item_type} === ({len(items)}个项目)\n")
            for item in sorted(items):
                f.write(f"  - {item}\n")
            f.write("\n")
    
    print(f"已生成目录内容索引: {output_file}")

if __name__ == "__main__":
    generate_filetype_index()

import re

def add_markdown_numbers(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        counters = [0] * 6  # 支持 h1-h6
        new_lines = []
        for line in lines:
            match = re.match(r'(#+)\s*(.*)', line)
            if match:
                level = len(match.group(1)) - 1  # #=h1, ##=h2...
                counters[level] += 1
                # 重置子级计数器
                for i in range(level + 1, 6):
                    counters[i] = 0
                # 生成编号 (如 1.2.3)
                number = '.'.join(str(counters[i]) for i in range(level + 1) if counters[i] > 0)
                new_line = f"{match.group(1)} {number}. {match.group(2)}\n"
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        f.seek(0)
        f.writelines(new_lines)

add_markdown_numbers("搜索外挂.md")
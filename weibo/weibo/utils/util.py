import sys


def get_keyword_list(file_name):
    """获取文件中的关键词列表"""
    with open(file_name, 'r', encoding='utf-8') as f:
        try:
            lines = f.read().splitlines()
            lines = [line for line in lines]
        except UnicodeDecodeError:
            print(u'%s文件应为utf-8编码，请先将文件编码转为utf-8再运行程序' % file_name)
            sys.exit()
        keyword_list = []
        for line in lines:
            if line:
                keyword_list.append(line)
    return keyword_list

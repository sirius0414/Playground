import os
from doc2docx import convert
from docx import Document

def get_doc_title(docx_file):
    """获取 .docx 文档的标题"""
    try:
        doc = Document(docx_file)
        # 遍历文档中的段落，找到第一个非空的段落作为标题
        for paragraph in doc.paragraphs:
            title = paragraph.text.strip()
            if title:  # 如果标题不为空，返回标题
                return title
        return None  # 如果文档中没有找到非空的段落，返回 None
    except Exception as e:
        print(f"无法读取文件 {docx_file}: {e}")
        return None

def convert_and_rename_doc_files(input_dir, output_dir):
    """批量转换 .doc 文件为 .docx，并根据标题重命名"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".doc"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace(".doc", ".docx"))

            # 使用 doc2docx 将 .doc 转换为 .docx
            try:
                convert(input_path, output_path)
                print(f"成功转换：{file_name} 到 {output_path}")
            except Exception as e:
                print(f"转换 {file_name} 失败: {e}")
                continue

            # 获取文档标题作为新的文件名
            title = get_doc_title(output_path)
            if not title:
                # 如果没有找到标题，使用原文件名作为新文件名
                title = file_name.replace(".doc", "")

            new_file_name = f"{title}.docx"
            new_file_name = new_file_name.replace(" ", "_")  # 将空格替换为下划线，避免文件名问题

            # 重命名文件
            new_output_path = os.path.join(output_dir, new_file_name)
            try:
                os.rename(output_path, new_output_path)
                print(f"文件重命名为：{new_file_name}")
            except Exception as e:
                print(f"重命名失败：{e}")

# 使用示例
input_directory = r"G:/Rules/Raw"
output_directory = r"G:/Rules/Converted"

convert_and_rename_doc_files(input_directory, output_directory)

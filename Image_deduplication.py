import os
import hashlib


def find_duplicate_images(folder):
    """
    查找指定文件夹中重复的图片
    """
    # 用于存储所有图片的哈希值和路径
    image_hashes = {}
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder):
        for file in files:
            # 判断文件是否为图片
            if file.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                # 计算文件的哈希值
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                # 如果哈希值已经存在，说明是重复的图片，将其添加到重复列表中
                if file_hash in image_hashes:
                    image_hashes[file_hash].append(file_path)
                # 否则将哈希值和文件路径添加到哈希表中
                else:
                    image_hashes[file_hash] = [file_path]
    # 返回所有重复图片的列表
    return [image_paths for image_paths in image_hashes.values() if len(image_paths) > 1]


def delete_duplicate_images(folder):
    """
删除指定文件夹中的重复图片
    """
    # 获取所有重复图片的路径列表
    duplicate_images = find_duplicate_images(folder)
    # 遍历所有重复图片的路径列表
    for image_paths in duplicate_images:
        # 将第一个图片作为原始图片，其余的图片作为重复图片
        original_image_path = image_paths[0]
        duplicate_image_paths = image_paths[1:]
        # 删除所有重复图片
        for duplicate_image_path in duplicate_image_paths:
            os.remove(duplicate_image_path)
            print(f"Deleted duplicate image: {duplicate_image_path}")
        print(f"Original image: {original_image_path} has been kept.")


if __name__ == '__main__':
    delete_duplicate_images('板壳虫')  # 参数填要处理的文件夹

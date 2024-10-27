# 来源：https://www.cnblogs.com/lizaza/p/12896536.html

import os
import sys
import requests
import base64

# 替换为你的个人访问令牌和仓库信息
ACCESS_TOKEN = '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'
REPO_OWNER = 'cuimingyang'
REPO_NAME = 'image_bed'
BRANCH = 'develop'


def upload_image_to_github(image_path):
    # 读取图片文件并进行 Base64 编码
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # GitHub API URL
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{os.path.basename(image_path)}'

    # 构造请求数据
    data = {
        'message': 'Upload image',
        'branch': BRANCH,
        'content': encoded_image,
    }

    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    # 发送 PUT 请求
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Image uploaded successfully!")
        # 获取文件的 URL
        download_url = response.json().get('content').get('download_url')
        print(f'Image URL: {download_url}')
    else:
        print(f'Error uploading image: {response.status_code}, {response.json()}')


def main():
    print("请将图片文件拖入终端并按下回车：")

    # 通过 input() 获取拖放的文件路径
    image_path = input().strip()  # 获取输入并去除两端空白字符
    print(f"拖放的图片路径是: {image_path}")
    if os.path.isfile(image_path):
        upload_image_to_github(image_path)
    else:
        print(f"File not found: {image_path}")


if __name__ == "__main__":
    main()

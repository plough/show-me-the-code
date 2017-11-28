#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os


def main():
    IMAGE_DIR = 'images'
    OUTPUT_DIR = 'output'
    # iPhone5 的分辨率为 1136*640
    MAX_SIZE = (1136, 640)
    image_names = [fname for fname in os.listdir(IMAGE_DIR) if is_pic(fname)]

    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for image_name in image_names:
        image_path = os.path.join(IMAGE_DIR, image_name)
        im = Image.open(image_path)
        preferred_size = get_preferred_size(im, MAX_SIZE)
        output_im = im.resize(preferred_size)

        output_path = os.path.join(OUTPUT_DIR, image_name)
        output_im.save(output_path)


def is_pic(fname):
    """根据文件名判断是否为图片

    参数：
    fname -- 文件名
    """
    ftype = fname.split('.')[-1].lower()
    return ftype.endswith('jpg') or ftype.endswith('jpeg') or ftype.endswith('png') or ftype.endswith('gif')


def get_preferred_size(im, max_size, allow_rotate=True):
    """得到图片在限制条件下的最大等比缩放尺寸

    参数：
    im -- ImageFile 对象
    max_size -- 限制尺寸
    allow_rotate -- 是否允许旋转（若为True，则限制尺寸的宽、高可根据实际情况互换，使缩放后的尺寸尽可能大些）
    """
    width, height = im.size
    aspect_ratio = width / height
    if allow_rotate:
        if aspect_ratio > 1 and max_size[0] < max_size[1] or\
                aspect_ratio < 1 and max_size[0] > max_size[1]:
            max_size = max_size[::-1]
    if width > max_size[0]:
        width = max_size[0]
        height = width / aspect_ratio
    if height > max_size[1]:
        height = max_size[1]
        width = height * aspect_ratio
    return int(width), int(height)


if __name__ == "__main__":
    main()

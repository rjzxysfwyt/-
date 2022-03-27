import os
import random
import base64
from captcha.image import ImageCaptcha


lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']

# 定义验证码尺寸
width, height = 170, 80


def create():
    generator = ImageCaptcha(width=width, height=height)
    # 从lst中取出4个字符
    random_str = ''.join([random.choice(lst) for j in range(4)])
    # 生成验证码
    img = generator.generate_image(random_str)
    # 在验证码上加干扰点
    generator.create_noise_dots(img, '#000000', 4, 40)
    # 在验证码上加干扰线
    generator.create_noise_curve(img, '#000000')
    if os.path.exists('./images') is False:
        os.mkdir('./images')
    file_name = './images/' + random_str + '.jpg'
    img.save(file_name)
    with open(file_name, 'rb') as f:
        img_b64 = base64.b64encode(f.read())
    return random_str, img_b64


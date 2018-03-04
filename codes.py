# coding:utf-8
import random, os, uuid
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class Codes:
    '''
    #随机一个字母或者数字
    '''

    def random_chr(self):
        num = random.randint(1, 3)
        if num == 1:
            char = random.randint(48, 57)
        elif num == 2:
            char = random.randint(97, 122)  # a-z
        else:
            char = random.randint(65, 90)  # A-Z
        return chr(char)

    # 随机干扰字符
    def random_dis(self):
        arr = ["^", "_", "-", ".", "~"]
        return arr[random.randint(0, len(arr) - 1)]

    # 定义干扰字符颜色 RGB 0-255
    def random_color1(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255),)

    # 定义字符颜色
    def random_color2(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127),)

    # 生成验证码
    def create_code(self):
        width = 240
        height = 60
        # 创建一个图片 颜色规则，尺寸元组，RGB数值元组
        image = Image.new("RGB", (width, height), (192, 192, 192))

        # 创建FONT对象，定义字体和大小
        font_name = random.randint(1, 3)
        font_file = os.path.join(os.path.dirname(__file__), 'static/fonts') + '/%d.ttf' % font_name
        font = ImageFont.truetype(font_file, 30)
        # 创建draw画布，填充像素点
        draw = ImageDraw.Draw(image)
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                draw.point((x, y), fill=self.random_color1())

        # 填充干扰字符
        for v in range(0, width, 30):
            dis = self.random_dis()
            w = 5 + v
            # 距离图片上边距最多15像素，最低5像素
            h = random.randint(5, 15)
            draw.text((w, h), dis, font=font, fill=self.random_color1())

        # 填充字符
        chars = ""
        for v in range(4):
            c = self.random_chr()
            chars += str(c)
            # 随机距离图片上边距，高度最多15px，最低5像素
            h = random.randint(5, 15)
            # 占图片宽度1/4，10px间隙
            w = width / 4 * v + 10
            draw.text((w, h), c, font=font, fill=self.random_color2())
        # 模糊效果
        image.filter(ImageFilter.BLUR)
        # 生成唯一UID,保存在磁盘
        image_name = '%s.jpg' % uuid.uuid4().hex
        save_dir = os.path.join(os.path.dirname(__file__), 'static/codes')
        print(save_dir)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        image.save(save_dir + '/' + image_name, "jpeg")

        return dict(
            img_name=image_name,
            codes=chars.lower()
        )

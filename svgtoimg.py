import xml.etree.ElementTree as ET
import cairosvg
import colorsys

# 50개의 무지개 색상 생성 (HSV를 이용해 50개의 고른 색상)
def generate_rainbow_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hue = i / num_colors # hue 값은 0에서 1 사이를 균등하게 분배
        r, g, b = colorsys.hsv_to_rgb(hue,2.5,1)  # 최대 채도와 밝기로 변환
        colors.append((r, g, b))
    return colors

# RGB 값을 파스텔 톤으로 변환하는 함수
def pastelize_color(rgb, factor=0.7):
    r, g, b = rgb
    # 파스텔 톤으로 만들기 위해 RGB 값을 흰색과 섞음
    r = r + (1 - r) * factor
    g = g + (1 - g) * factor
    b = b + (1 - b) * factor
    return (r, g, b)

# RGB 값을 16진수로 변환
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

# SVG 네임스페이스 설정 (SVG 파일의 네임스페이스)
namespace = {'svg': 'http://www.w3.org/2000/svg'}
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# SVG에서 첫 번째 path의 색상을 바꾸는 함수
def change_first_path_color(svg_file, color, output_svg):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # 첫 번째 path 요소만 수정
    path = root.find('.//svg:path', namespace)
    if path is not None:
        path.set('fill', color)

    tree.write(output_svg)

# SVG를 PNG로 변환하는 함수
def convert_svg_to_png(input_svg, output_png):
    cairosvg.svg2png(url=input_svg, write_to=output_png, output_width=3000, output_height=6000)

# 파스텔톤 무지개 색상 생성
num_colors = 20
rainbow_colors = generate_rainbow_colors(num_colors)
pastel_colors = [pastelize_color(rgb) for rgb in rainbow_colors]
hex_colors = [rgb_to_hex(color) for color in pastel_colors]

# SVG 파일 경로
input_svg = 'Assets/Svgs/book/book.svg'

# 50개의 파스텔톤 무지개 색으로 첫 번째 path만 수정하여 저장 및 PNG 변환
for i, color in enumerate(hex_colors):
    output_svg = f'Assets/Svgs/book/4line/pastel_rainbow_{i+1}.svg'
    output_png = f'Assets/Images/book/4line/pastel_rainbow_{i+1}.png'
    
    # 첫 번째 path의 색상만 변경
    change_first_path_color(input_svg, color, output_svg)
    
    # SVG를 PNG로 변환
    convert_svg_to_png(output_svg, output_png)

print("첫 번째 path의 색상을 파스텔톤 무지개 색으로 변경 및 PNG 저장 완료!")

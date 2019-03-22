import pytesseract
from PIL import Image
image = Image.open("../images/1.jpg")
code = pytesseract.image_to_string(image,lang="chi_sim",config="--psm 6")
print(code)
#Use '--psm' instead of '-psm' as the option was deprecated.
#https://github.com/openpaperwork/pyocr/pull/100/commits/c136838b46cf49f06ac1dc5f2f9bc16232c11213
#各种语言包下载 https://github.com/tesseract-ocr/tessdata
#https://raw.githubusercontent.com/tesseract-ocr/tessdata/master/chi_sim.traineddata
#连接vpn 用代理下载比较快.

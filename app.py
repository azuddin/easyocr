from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = '/data/uploaded_files/receipt-sample.jpeg'
result = ocr.ocr(img_path, cls=True)

for line in result:
  print(line)

# draw result
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
texts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, texts, scores, font_path='/data/python/fonts/latin.ttf')
im_show = Image.fromarray(im_show)
im_show.save('/data/result/receipt-sample.jpg')
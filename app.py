import csv
import easyocr

file = open('/data/python/result.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Result'])

IMAGE_PATH = '/data/uploaded_files/receipt-sample.jpeg'

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH,paragraph="False")
result

writer.writerow([result])
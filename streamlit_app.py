import streamlit as st
import pytz
#from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

st.set_option('deprecation.showfileUploaderEncoding',False)
img_file = st.file_uploader(label='Upload a file',type=['png','jpg','jpeg','webp'])

a = st.text_input('Enter some text')
size = (720, 1463)
tz = pytz.timezone('Asia/Bangkok')
months = ('0',"ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค.")
current_datetime = datetime.now(tz)
mth = current_datetime.month
year = current_datetime.year + 543

if img_file and a:

    if len(a) == 6:
        text = (a[:2] +' '+ months[mth] + ' ' + str(year) + '     ' + a[2:-2] + ':' + a[4:])
    elif len(a) == 5:
        text = (a[:1] +' '+ months[mth] + ' ' + str(year) + '     ' + a[1:-2] + ':' + a[3:])

    img = Image.open(img_file)
    if img.size[1] != 1476:
        img = img.resize(size)

    w1 = Image.open('putches/water.png')
    w2 = Image.open('putches/waterline2.png')
    w3 = Image.open('putches/white.png')

    img.paste(w1,(170,340))#170,340  170,356
    img.paste(w2,(417,339))#417,339  417,355
    img.paste(w3,(270,338))#268,338  268,352

    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("putches/Noto Sans Thai UI Bold_new.ttf",size=23)#23
    idraw.text((250,333),text,(0,0,0),font=font)#250,349  , 235,336

    st.image(img)

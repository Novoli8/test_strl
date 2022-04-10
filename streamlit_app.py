import streamlit as st
from PIL import Image,ImageDraw,ImageFont

st.set_option('deprecation.showfileUploaderEncoding',False)

img_file = st.file_uploader(label='Upload a file',type=['png','jpg','jpeg','webp'])

a = st.text_input('Enter some text')
size = (720, 1463)

if img_file and a:
    
    if len(a) == 6:
        text = (a[:2] + '            2565' + '         ' + a[2:-2] + ':' + a[4:])
    elif len(a) == 5:
        text = (a[:1] + '           2565' + '       ' + a[1:-2] + ':' + a[3:])
    else:
        print("wrong")

    img = Image.open(img_file)
    if img.size[1] != 1476:
        img = img.resize(size)

    w1 = Image.open('putches/water.png')
    w2 = Image.open('putches/waterline2.png')
    w3 = Image.open('putches/white.png')
    w4 = Image.open('putches/thfn8.jpg')

    img.paste(w1,(170,356))#170,340
    img.paste(w2,(417,355))#417,339
    img.paste(w3,(268,352))#268,338

    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("putches/Inter-Bold.ttf",size=23)#23
    idraw.text((234,349),text,(0,0,0),font=font)#250,349  , 235,336
    img.paste(w4,(266,357))#266,355  , 269,341

    st.image(img)

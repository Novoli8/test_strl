import streamlit as st
from PIL import Image,ImageDraw,ImageFont

st.set_option('deprecation.showfileUploaderEncoding',False)

img_file = st.file_uploader(label='Upload a file',type=['png','jpg','jpeg'])

a = st.text_input('Enter some text')


if img_file and a:



    if len(a) == 6:
        text = (a[:2] + '           2564' + '         ' + a[2:-2] + ':' + a[4:])
    elif len(a) == 5:
        text = (a[:1] + '           2564' + '       ' + a[1:-2] + ':' + a[3:])
    else:
        print("wrong")

    img = Image.open(img_file)
    if img.size[1] < 1200:
        img = img.resize(720, 1463)
        
    w1 = Image.open('putches/water.png')
    w2 = Image.open('putches/waterline2.png')
    w3 = Image.open('putches/white.png')
    w4 = Image.open('putches/thfn.png')

    img.paste(w1,(170,353))
    img.paste(w2,(417,353))
    img.paste(w3,(268,352))

    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("putches/Inter-Bold.ttf",size=23)
    idraw.text((232,349),text,(0,0,0),font=font)
    img.paste(w4,(262,353))

    st.image(img)

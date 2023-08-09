images = ['1.jpg','2.png','3.png','4.png','5.jpg']
for img in images:
    if img.endswith('.png'):
        print('PNG found >>',img)
    if img.endswith('.jpg'):
        print('jpg found >>',img)
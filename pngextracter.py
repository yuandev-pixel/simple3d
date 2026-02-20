from PIL import Image
image = Image.open("D:\\gdt\\wp\\affiles\\kanadian.png")
width, height = image.size
rgb_values = [image.getpixel((y, x)) for x in range(width) for y in range(height)]
L=[]
print(rgb_values)
for color in rgb_values:
    L.append(str(color[0]/255)+' '+str(color[1]/255)+' '+str(color[2]/255)+'\n')
with open("kanadian.tdtext","w") as file:
	file.writelines(L)
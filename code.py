'''import numpy as np 
from PIL import Image
from image_slicer import slice

im=np.array(Image.open('rgb.jpg'))

print(im.dtype)
print(im.ndim)

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

print(im.shape)


im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]

pil_img = Image.fromarray(im_RGB)
pil_img.save('numpy_split_color.jpg')

pil_img=Image.fromarray(a[0])
pil_img.save('splitcolor.jpg')
a=slice('rgb.jpg',2)
#print(dir(a[0]))
pil_img=Image.fromarray(a[0])


def avg(arr):

	return sum(arr)/2

print(avg([8,8]))'''

def code(a):
	return a+1
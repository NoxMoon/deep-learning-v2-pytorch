import numpy as np
from glob import glob
from tqdm import tqdm
import matplotlib.pyplot as plt

# load filenames for human and dog images
human_files = np.array(glob("lfw/*/*"))
dog_files = np.array(glob("dogImages/*/*/*"))

# print number of images in each dataset
print('There are %d total human images.' % len(human_files))
print('There are %d total dog images.' % len(dog_files))


def square_crop(img):
    h, w = img.shape[0], img.shape[1]
    if len(img.shape)!=3:
        new_img = np.zeros([h,w,3])
        new_img[:,:,0] = img
        new_img[:,:,1] = img
        new_img[:,:,2] = img
        img = new_img
    if h>w:
        return img[(h-w)//2:(h-w)//2+w, :, :]
    else:
        return img[:, (w-h)//2:(w-h)//2+h, :]

from skimage import transform, io
paths = sorted(glob("dogImages/*/*/*"))
for img_path in tqdm(paths):
    try:
        img = io.imread(img_path)
        img = square_crop(img)
        img = transform.resize(img, (224,224))
        io.imsave(img_path.replace('dogImages', 'dogImages_resized'), img)
    except:
        print(f"{img_path} error")
       
       
#dogImages/train/098.Leonberger/Leonberger_06571.jpg error
#dogImages/train/103.Mastiff/Mastiff_06832.jpg error
#aws s3 sync dogImages_resized s3://sagemaker-us-east-2-319963865301/project-dog/dogImages-resized
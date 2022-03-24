import cv2
from tqdm import tqdm
import argparse, sys, os, time

def transparence2white(img):
    sp=img.shape  
    width=sp[0]  
    height=sp[1]  
    for yh in range(height):
        for xw in range(width):
            color_d=img[xw,yh]  
            if(color_d[3]==0):  
                img[xw,yh]=[255,255,255,255]  
    return img

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Translate transparence background to white')
    parser.add_argument('--folder', type=str, default="render",
                        help='picture folder')
    args = parser.parse_args(sys.argv[1:])
    
    for id in tqdm(os.listdir(os.path.join(args.folder))):
        for pic in os.listdir(os.path.join(args.folder,id)):
            pic_path = os.path.join(args.folder, id, pic)
            img=cv2.imread(pic_path,-1)
            img=transparence2white(img)
            cv2.imwrite(pic_path,img)
'''
Made by : Minsuk Sung
USAGE : python resize_img.py -i 입력폴더경로 -o 출력폴더경로 -s 사이즈크기
EXAMPLE : python resize_img.py -i ./img/test/ -o ./img/test_resized -s 224
CAUTION : 항상 경로 끝에 /를 넣어줘야합니다.
'''

import os
import sys
import cv2
import glob
from tqdm import tqdm
import argparse

def resize_img(fpath,size,output_path):

    resized_img = cv2.imread(fpath, cv2.IMREAD_COLOR)
    resized_img = cv2.resize(resized_img, dsize=(size, size), interpolation=cv2.INTER_AREA)
    cv2.imwrite(output_path+'/'+fpath.split('/')[-1], resized_img)

def process_img(input_path,output_path,size):
    # 기존 출력 폴더가 없다면 생성
    os.makedirs(output_path,exist_ok=True)

    # 변환하고자 하는 입력 폴더 안의 이미지 리스트
    flist = glob.glob(input_path+'*.jpg')

    # 입력 폴더 안에 폴더가 있는지 체크
    for cf in os.listdir(input_path):
        if os.path.isdir(input_path+cf):
            print('='*100)
            print('Error : {} is directory! All of contents in {} must not be directory!!'.format(cf,input_path.split('/')[-2]))
            print('='*100)
            return

    # 리사이징 작업
    for fpath in tqdm(flist):
        resize_img(fpath,size,output_path)

    # 변환된 파일의 갯수
    print('-'*100)
    print('Total {} images resized'.format(len(flist)))
    print('-'*100)

def main():
    parser = argparse.ArgumentParser(description='This code is written for resizing image by opencv')
    parser.add_argument('-i', type=str ,metavar='Input Folder Path', help='Where is input folder?')
    parser.add_argument('-o', type=str ,metavar='Output Folder Path', help='Where is output folder?')
    parser.add_argument('-s', type=int ,metavar='Output Image Size', help='What is shape of output image?',default=224)
    args = parser.parse_args()
	
    print('-'*100)
    input_path = args.i
    print('Input Folder Path : {}'.format(input_path))
    output_path = args.o
    print('Output Folder Path : {}'.format(output_path))
    target_size = args.s
    print('Target Image Size : {0} x {0}'.format(target_size))
    print('-'*100)

    process_img(input_path,output_path,target_size)

if __name__ == "__main__":
    main()
# 인텔코리아 강의자료 - 딥러닝을 이용한 이미지 분류

![](./img/intel-logo.jpg)

본 강의 자료는 인텔코리아에서 진행하는 딥러닝 관련된 교육 자료이므로 무단으로 사용시 법적 제재가 있을 수 있습니다.

## 강의 목적
Keras를 이용하여 여러가지 데이터셋을 학습 후 다양한 CNN모델을 통해서 이미지 분류를 하는 튜토리얼입니다.

## 환경설정
모든 강의자료는 아나콘다를 통해 가상환경을 생성한 뒤 아래와 같은 명령어를 통해 환경설정을 할 수 있습니다.
괄호 안은 가상환경의 이름이므로 괄호 이후 문자열을 복사하여 터미널에 입력해주시길 바랍니다.
```
(base) git clone https://github.com/mssung94/intel-image-classification.git
(base) cd intel-image-classification
(base) conda create -n keras python=3.6
(base) conda activate keras
(keras) mkdir bin data
(keras) pip install -r requirements.txt
(keras) jupyter notebook .
```

## 데이터
강의에서 사용할 데이터는 Google Drive에 업로드에 되어있습니다. 다운로드 후 사용하시길 바랍니다.
- Fashion MNIST :
- Kaggle Cat & Dog : 
- Kaggle Intel Scene Image :
- VOC2012 : 

## 강의 구성
|차수|내용|
|---|---|
|1강 |딥러닝에 대한 기본적인 지식과 이미지 분류를 하기 위한 CNN 구조 설명|
|2강 |`간단한 CNN 모델`을 만들어 **MNIST 데이터셋**을 학습 후 이미지 분류|
|3강 |`간단한 CNN 모델`을 만들어 **Fashion MNIST 데이터셋**을 학습 후 이미지 분류|
|4강 |`조금 더 깊은 CNN 모델`을 만들어 **CIFAR10 데이터셋**을 학습 후 이미지 분류|
|5강 |`VGG16 모델`을 통하여 **Kaggle Cat & Dog 데이터셋**을 학습 후 이미지 분류|
|6강 |`ResNet50 모델`을 통하여 **CIFAR100 데이터셋**을 학습 후 이미지 분류 (*변경예정*)|
|7강 |`ResNet50 모델`을 통하여 **Kaggle Intel Scene Image 데이터셋**을 학습 후 이미지 분류|
|8강 |`MobileNet 모델`을 통하여 **VOC2012**에 속해 있는 20가지 데이터셋을 학습 후 이미지 분류|
|9강 |`MobileNet 모델`을 통하여 **내가 원하는 클래스를 크롤링** 후 이미지 분류(*진행예정*)| 
|10강|학습된 h5파일을 caffemodel로 변경하기(*폐지예정*)| 

## 참고
- Intel Korea : https://www.intel.co.kr/content/www/kr/ko/company-overview/company-overview.html
- Intel OpenVINO : https://software.intel.com/en-us/openvino-toolkit
- Kaggle Cat & Dog (Original) : https://www.kaggle.com/c/dogs-vs-cats
- Kaggle Intel Scene Image (Original) : https://www.kaggle.com/puneet6060/intel-image-classification
- VOC2012 (Original) : http://host.robots.ox.ac.uk/pascal/VOC/voc2012/
- MobileNet : https://arxiv.org/pdf/1704.04861.pdf
- MobileNetV2 : https://arxiv.org/pdf/1801.04381.pdf

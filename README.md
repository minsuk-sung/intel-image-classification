# 인텔코리아 강의자료 - 딥러닝을 이용한 이미지 분류

![](./img/intel-logo.jpg)

본 강의 자료는 인텔코리아에서 진행하는 딥러닝 관련된 교육 자료이므로 무단으로 사용시 법적 제재가 있을 수 있습니다. 

## 강의 목적
Keras를 이용하여 여러가지 데이터셋을 학습 후 다양한 CNN모델을 통해서 이미지 분류를 하는 튜토리얼입니다.

## 환경설정
모든 강의자료는 아나콘다를 통해 가상환경을 생성한 뒤 아래와 같은 명령어를 통해 환경설정을 할 수 있습니다.
괄호 안은 가상환경의 이름이므로 괄호 이후 문자열을 복사하여 터미널에 입력해주시길 바랍니다. Tensorflow와 Keras 등 필수적인 라이브러리의 버전은 설치 후 확인 바랍니다.
```
(base) git clone https://github.com/mssung94/intel-image-classification.git
(base) cd intel-image-classification
(base) conda create -n keras python=3.6
(base) conda activate keras
(keras) pip install -r requirements.txt
(keras) jupyter notebook .
```

## 데이터 및 모델
강의에서 사용할 자료는 전부 Google Drive에 업로드에 되어있습니다. 다운로드 후 사용하시길 바랍니다.
다운로드에 어려움이 생긴다면 `mssung94@gmail.com`로 연락주시길 바랍니다.

### 데이터
데이터를 다운로드 후 `data`폴더 안에 옮겨주시길 바랍니다.
- Fashion MNIST :
- Kaggle Cat & Dog : 
- Kaggle Intel Scene Image :
- VOC2012 : 

### 모델
모델을 다운로드 후 `bin`폴더 안에 옮겨주시길 바랍니다.
- 20가지 클래스가 학습된 MobileNet : 

## 강의 구성
천천히 단계적으로 따라올 수 있도록 강의를 구성했습니다. 처음에는 딥러닝에 대한 기초지식과 Keras를 통하여 간단하게 CNN모델을 만드는 것부터 시작하여 후반에는 VGG16, ResNet 및 MobileNet의 Pretrained Model을 가지고 다양한 데이터셋을 학습하여 이미지를 분류합니다. 마지막으로 그렇게 학습된 h5파일을 Intel OpenVINO에서 사용할 수 있게 xml,bin파일로 변환하는 과정이 담겨있습니다. 또한 그렇게 변환된 xml과 bin파일을 통하여 OpenVINO에서 이미지 분류할 수 있습니다.

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
|10강|`Keras h5파일`을 `Tensorflow pb파일`를 거쳐 `OpenVINO xml,bin파일`로 변환 후 **OpenVINO를 이용**하여 이미지 분류| 

## 참고
- Intel Korea : https://www.intel.co.kr/content/www/kr/ko/company-overview/company-overview.html
- Intel OpenVINO : https://software.intel.com/en-us/openvino-toolkit
- Kaggle Cat & Dog (Original) : https://www.kaggle.com/c/dogs-vs-cats
- Kaggle Intel Scene Image (Original) : https://www.kaggle.com/puneet6060/intel-image-classification
- VOC2012 (Original) : http://host.robots.ox.ac.uk/pascal/VOC/voc2012/
- MobileNet : https://arxiv.org/pdf/1704.04861.pdf
- MobileNetV2 : https://arxiv.org/pdf/1801.04381.pdf

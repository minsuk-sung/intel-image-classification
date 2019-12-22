# 인텔코리아 강의자료 - 딥러닝을 이용한 이미지 분류
(Intel Koera - Image Classification using Deep Learning)

![](./img/intel-logo.jpg)

본 강의 자료는 인텔코리아에서 진행하는 딥러닝 관련된 교육 자료이므로 무단으로 사용시 법적 제재가 있을 수 있습니다. 

---

## Purpose
> Keras를 이용하여 여러가지 데이터셋을 이용하여 다양한 CNN모델을 학습 후 OpenVINO를 통해서 이미지 분류를 하는 튜토리얼입니다.

---

## Enviroments
모든 강의자료는 가상환경을 생성한 뒤 아래와 같은 명령어를 통해 환경설정을 할 수 있습니다.
괄호 안은 가상환경의 이름이므로 괄호 이후 문자열을 복사하여 터미널에 입력해주시길 바랍니다. 
```zsh
> git clone https://github.com/mssung94/intel-image-classification.git
> cd intel-image-classification
> pip3 install virtualenv  
> virtualenv myvenv --python=python3
> source myvenv/bin/activate
> (myvenv) mkdir data
> (myvenv) pip3 install -r requirements.txt
> (myvenv) jupyter notebook .
```

### Essential Library  
추후에 Keras의 h5파일을 Tensorflow의 pb파일로 바꾸는 과정과 pb파일을 OpenVINO의 xml과 bin파일로 바꾸는 과정에서 필수적으로 사용되는 라이브러리는 아래와 같습니다. 아래와 다른 환경설정시 변환에 어려움이 있을 수 있습니다.
> `Tensorflow` : **1.14**  
> `Keras` : **2.3.1**  
> `networkx` : **2.3**

---

## Data & Model
강의에서 사용할 자료는 전부 Google Drive에 업로드에 되어있습니다. 다운로드 후 사용하시길 바랍니다.
다운로드에 어려움이 생긴다면 `mssung94@gmail.com`로 연락주시길 바랍니다.

### Data List
데이터를 다운로드 후 `data`폴더 안에 옮겨주시길 바랍니다.
- Fashion MNIST : https://drive.google.com/open?id=1H-hCU9xULhORBbSlnyAXfzJPR-6myFai
- Kaggle Cat & Dog : https://drive.google.com/open?id=1udAgSe0hqUzkqvl_PoHIYvCD-V_z-v0B
- Kaggle Intel Scene Image : https://drive.google.com/open?id=1ec4Urjxvif0fenMyl6Jl1A1SW104yiDW
- VOC2012 : https://drive.google.com/open?id=10oEH4JDSLA6ifMayOqP0NhoymjcCiDDG

### Model
모델을 다운로드 후 `bin`폴더 안에 옮겨주시길 바랍니다.
- 20가지 클래스가 학습된 MobileNet : 

---

## Contents
천천히 단계적으로 따라올 수 있도록 강의를 구성했습니다. 처음에는 딥러닝에 대한 기초지식과 **`Keras`** 를 통하여 간단하게 CNN모델을 만드는 것부터 시작하여 후반에는 VGG16, ResNet 및 MobileNet의 Pretrained Model을 가지고 다양한 데이터셋을 학습하여 이미지를 분류합니다. 마지막으로 그렇게 학습된 h5파일을 Intel `OpenVINO`에서 사용할 수 있게 xml,bin파일로 변환하는 과정이 담겨있습니다. 또한 그렇게 변환된 xml과 bin파일을 통하여 OpenVINO에서 이미지 분류할 수 있습니다.

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
|9강 |`Keras h5파일`을 `Tensorflow pb파일`를 거쳐 `OpenVINO xml,bin파일`로 변환 후 **OpenVINO를 이용**하여 이미지 분류| 
|10강|`OpenVINO를 이용`하여 변환된 `MobileNetV2`로 **실시간으로** 이미지 분류|

## Licence
The MIT License (MIT)
Copyright (c) 2019 Minsuk Sung, Hoesung Ryu

## Reference
- Intel Korea : https://www.intel.co.kr/content/www/kr/ko/company-overview/company-overview.html
- Intel OpenVINO : https://software.intel.com/en-us/openvino-toolkit
- Kaggle Cat & Dog (Original) : https://www.kaggle.com/c/dogs-vs-cats
- Kaggle Intel Scene Image (Original) : https://www.kaggle.com/puneet6060/intel-image-classification
- VOC2012 (Original) : http://host.robots.ox.ac.uk/pascal/VOC/voc2012/
- MobileNet : https://arxiv.org/pdf/1704.04861.pdf
- MobileNetV2 : https://arxiv.org/pdf/1801.04381.pdf

## Contact
> 성민석(Minsuk Sung) : mssung94@gmail.com  
> 류회성(Hoesung Ryu) : skainof23@gmail.com

# foid (find object in document)
### Models
- [PubLayNet Model](https://www.dropbox.com/sh/1098ym6vhad4zi6/AABe16eSdY_34KGp52W0ruwha?dl=0)
- [Object Detect Model ](https://dl.fbaipublicfiles.com/detectron2/COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x/139173657/model_final_68b088.pkl)
- [Chart_Detect Model](https://drive.google.com/file/d/1-4FJBHbcz83H88aIZ-BnTHnyaHJu5W81/view?usp=sharing)
- [table detect and recognation](https://github.com/microsoft/table-transformer)
- - [Poopler](https://blog.alivate.com.au/poppler-windows/)
poopleri indirip C:\poppler-0.68.0\bin  sys env olarak pathe ekle
https://github.com/UB-Mannheim/tesseract/wiki  tessseract indir
https://www.youtube.com/watch?v=PY_N1XdFp4w


-- tabloları çizerken tablo crop üzerinde çizdiği  için sıkıntı olabilyo


-- foidi ubunutu içine aldığımda ilk yapmam gereken şey 
-- windows inbound fw ayarını yapmak  (iç dış hepsini açtım sonra 192.168.1.35 bu ip ile telnet atabildiğim için gidiyır)
-- poopleri indirmek için 
    step 1 sudo apt-get update
    step 2 sudo apt install -y software-properties-common
    step 3 sudo apt update
    step 4 sudo add-apt-repository main
    step 5 sudo add-apt-repository universe
    step 6 sudo add-apt-repository restricted
    step 7 sudo add-apt-repository multiverse 
    step 8 apt-get install -y poppler-utils
--- sonrası çalışıyor zaten











------------------------------------------------------------------------------
- sudo su - 
- apt update
- apt install python3.10
- apt upgrade
- python3 --version
- apt install python3-pip
- pip --version
- python3 -m pip install --upgrade pip
- python3 -m pip install "paddlepaddle" -i https://mirror.baidu.com/pypi/simple
- git clone https://github.com/PaddlePaddle/PaddleOCR
- cd PaddleOCR/ppstructure
- python3 -m pip install -r recovery/requirements.txt 
- cd ..
- python3 -m pip install -r requirements.txt
- pip3 install "paddleocr>=2.6"
- pip install -U opencv-python
- apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
- cp /mnt/d/c.png ~
- cd ~
- paddleocr --image_dir=c.png --type=structure --lang='en'
- cp -r output /mnt/d/vm      #first result
- cd PaddleOCR/ppstructure
- mkdir inference && cd inference
- wget https://paddleocr.bj.bcebos.com/PP-OCRv3/english/en_PP-OCRv3_det_infer.tar && tar xf en_PP-OCRv3_det_infer.tar
- wget https://paddleocr.bj.bcebos.com/PP-OCRv3/english/en_PP-OCRv3_rec_infer.tar && tar xf en_PP-OCRv3_rec_infer.tar
- wget https://paddleocr.bj.bcebos.com/ppstructure/models/slanet/en_ppstructure_mobile_v2.0_SLANet_infer.tar && tar xf en_ppstructure_mobile_v2.0_SLANet_infer.tar
- wget https://paddleocr.bj.bcebos.com/ppstructure/models/layout/picodet_lcnet_x1_0_fgd_layout_infer.tar && tar xf picodet_lcnet_x1_0_fgd_layout_infer.tar
- cd ..
- python3 predict_system.py --image_dir=c.png --det_model_dir=inference/en_PP-OCRv3_det_infer --rec_model_dir=inference/en_PP-OCRv3_rec_infer --rec_char_dict_path=../ppocr/utils/en_dict.txt --table_model_dir=inference/en_ppstructure_mobile_v2.0_SLANet_infer --table_char_dict_path=../ppocr/utils/dict/table_structure_dict.txt --layout_model_dir=inference/picodet_lcnet_x1_0_fgd_layout_infer --layout_dict_path=../ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt --vis_font_path=../doc/fonts/simfang.ttf --output=../output/

--  birde  predict_table.py için olanı yap

-- python3 table/predict_table.py --det_model_dir=inference/en_PP-OCRv3_det_infer --rec_model_dir=inference/en_PP-OCRv3_rec_infer --table_model_dir=inference/en_ppstructure_mobile_v2.0_SLANet_infer --rec_char_dict_path=../ppocr/utils/en_dict.txt --table_char_dict_path=../ppocr/utils/dict/table_structure_dict.txt --image_dir=c.png --output=../output/table

-- python3 table/predict_table.py --help 
-- python3 predict_system.py --help   bu ikisindeki parametreleri kullanarak bir şeyler yap



-- burada şimdi tek sayfa verirsen predict_system.py ile kullanırsan sana hem textleri hemde tablo bulursa onu tabloya çeviriyor.
-- ama gördükki bazı pnglerde tabloyuda resim olarak algılıyor bunu düzeltmek için thresold düşürebilirsin.  --layout_score_threshold=0.6 üzeri oluyor tabloyu buluyor

-- thresholdu çok düşürürsek resim içindeki diğer tüm tabloları buluyor aslında  (0.5 de yaptım buldu resmin kalitesi önemli)

-- diğer aksiyon bence şu olmalı tabloları içeren sayfaların tablo title bulunur. Eğer bir standart belirlenirse o tablo algılandığında  içindeki diğer tabloları ayıklayacak şekilde crop edilip öyle sokulur 



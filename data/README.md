# 공통 데이터셋: Imagenette

교재 전체의 평가와 양자화 Calibration에 사용하는 공통 데이터셋입니다. ImageNet 1,000개 클래스 중 10개를 추린 공개 데이터셋(Apache 2.0)이며, 저장소에 파일을 두지 않고 실습 노트북이 아래 주소에서 직접 내려받습니다.

- 내려받기 주소: https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz
- 구성: train 9,469장 / val 3,925장 (짧은 변 160px)

## 클래스와 ImageNet 인덱스 대응

| 폴더 이름(wnid) | 클래스 | ImageNet 인덱스 |
|---|---|---|
| n01440764 | tench | 0 |
| n02102040 | English springer | 217 |
| n02979186 | cassette player | 482 |
| n03000684 | chain saw | 491 |
| n03028079 | church | 497 |
| n03394916 | French horn | 566 |
| n03417042 | garbage truck | 569 |
| n03425413 | gas pump | 571 |
| n03445777 | golf ball | 574 |
| n03888257 | parachute | 701 |

폴더 이름을 정렬한 순서가 위 표의 순서와 같으므로, 교재 코드의 `IMAGENET_IDX = [0, 217, 482, 491, 497, 566, 569, 571, 574, 701]`는 정렬된 폴더 순서에 대응합니다.

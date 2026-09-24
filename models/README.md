# 모델과 단계별 산출물

교재의 주 실습 모델은 MobileNetV2, 비교 모델은 ResNet-18입니다(torchvision 사전학습 가중치).

각 단계의 검증된 산출물은 저장소 본체가 아니라 **Releases**에 첨부해 제공합니다. 앞 단계 실습을 마치지 못했을 때 내려받아 다음 단계를 진행합니다.

| 단계 | 산출물 | 사용 Part |
|---|---|---|
| ONNX 변환 | mobilenet_v2.onnx, resnet18.onnx | Part 03 이후 |
| 경량화 | *_fp16.onnx, *_int8.onnx | Part 04 |
| NPU 실행모델 | 양자화 HAR, HEF | Part 05 이후 |

DFC 설치 파일(`*.whl`)은 EULA상 재배포할 수 없으므로 Releases에도 올리지 않습니다.

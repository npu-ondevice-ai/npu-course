# 경량화 모델 비교표

작성자:            / 작성일:            / 노트북: n2-1_quantization.ipynb

## 1. 실행 조건
| 항목 | 값 |
|---|---|
| ONNX Runtime 버전 |  |
| 양자화 함수와 방식 | quantize_static, QDQ |
| Calibration 이미지 수·클래스 구성 |  |
| 검증셋 | Imagenette val ( )장 |

## 2. 크기와 정확도 (표 4-3 대응)
| 항목 | FP32 (기준) | FP16 | INT8 |
|---|---|---|---|
| MobileNetV2 크기 (MB) |  |  |  |
| ResNet-18 크기 (MB) |  |  |  |
| Top-1 정확도 (Imagenette val) |  |  |  |
| 정확도 변화 (%p) | 기준 |  |  |

## 3. 하락 원인 점검 (INT8 하락이 클 때)
| 점검 항목 | 확인 내용 | 결과 |
|---|---|---|
| Calibration set의 대표성 | 수량과 클래스 균형이 충분했는가 |  |
| 전처리의 일치 | Calibration과 추론의 전처리가 같았는가 |  |
| 범위 산정 방식 | 이상치에 휘둘리지 않았는가 |  |
| per-channel 적용 | 가중치에 채널별 Scale이 쓰였는가 |  |

## 4. 해석
- 크기 대비 정확도 변화의 판단:

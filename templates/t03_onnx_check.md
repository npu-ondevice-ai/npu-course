# ONNX 변환 모델의 동등성 검증 결과

작성자:            / 작성일:            / 노트북: n1-4_onnx.ipynb

## 1. 변환 조건
| 항목 | 값 |
|---|---|
| PyTorch 버전 |  |
| ONNX Runtime 버전 |  |
| Opset |  |
| 변환 방식 | dynamo=False (Tracing) |
| 입력 규격 (shape, dtype) | (1, 3, 224, 224), float32 |

## 2. 검증 결과 (표 3-4 대응)
| 검증 항목 | MobileNetV2 | ResNet-18 | 판정 기준 |
|---|---|---|---|
| 파일 크기(FP32) |  |  | 파라미터 수 × 4바이트와 일치 |
| 최대 절대 오차 |  |  | 1e-4 미만 |
| Top-1 일치 |  |  | 일치 |
| Latency (PyTorch, ms) |  |  | 동일 조건 측정 |
| Latency (ONNX Runtime, ms) |  |  | 동일 조건 측정 |

- 검증에 쓴 입력: 무작위 입력 1장 / 실제 이미지 ( )장
- 판정: 통과 / 재점검

## 3. 재점검 메모
- 오차가 기준을 넘은 경우 점검한 항목 (Opset, 입력 규격):

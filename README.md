# NPU 활용 과정 실습 저장소

교재 「NPU 활용 과정」의 실습 자료입니다. 실습은 Google Colab에서 진행하며 개인 PC에 따로 설치할 것은 없습니다. 기준 장비(Raspberry Pi 5 + AI HAT+)에서 측정한 결과는 `data/bench/`에 CSV로 제공하므로, 장비가 없어도 모든 분석 실습을 할 수 있습니다.

## 폴더 구성 (교재 표 1-7)

| 구분 | 내용 |
|---|---|
| `notebooks/` | 실습 노트북 14종 (본편 n1-2_env_setup ~ n2-5_project, 부록 nA1 ~ nA5) |
| `data/` | 샘플 이미지·동영상, 기준 장비 측정 CSV(`data/bench/`), 공통 데이터셋 안내(`data/README.md`) |
| `models/` | 변환·경량화 산출물을 모아 두는 폴더 |
| `templates/` | 산출물 기록 템플릿: 환경 점검표, 검증 결과표, 경량화 비교표, 성능 분석 보고서, 프로젝트 보고서, 부록 토큰 비용 보고서 |
| Releases | 단계별 검증 산출물 (ONNX, 양자화 모델, HAR, HEF) |

## 시작하기 (교재 PART 01 4절)

1. Hailo Developer Zone에 가입하고 Dataflow Compiler(DFC) 설치 파일을 내려받아, 본인 Google Drive의 `내 드라이브/hailo/` 폴더에 올립니다.
2. Colab에서 **파일 → 노트북 열기**를 선택하고, **GitHub** 탭에 이 저장소 주소(`https://github.com/npu-ondevice-ai/npu-course`)를 입력합니다.
3. 목록에서 `notebooks/n1-2_env_setup.ipynb`를 선택합니다.
4. **파일 → 드라이브에 사본 저장**으로 자신의 드라이브에 복사한 뒤 실습합니다. 저장소에서 바로 연 노트북은 원본이라 실행 결과와 수정 내용이 남지 않습니다.
5. STEP 1부터 차례로 실행하고, 각 STEP의 확인 포인트를 `templates/t01_env_check.md`에 기록합니다.

## 노트북과 교재의 대응

| 노트북 | 교재 위치 | 기록 템플릿 |
|---|---|---|
| n1-2_env_setup | PART 01 온디바이스 AI와 NPU의 이해 (4. 개발 환경 구성 및 점검) | t01_env_check.md |
| n1-3_pipeline | PART 02 온디바이스 AI 추론 파이프라인 | |
| n1-4_onnx | PART 03 ONNX 모델 변환과 검증 (2~3절) | t03_onnx_check.md |
| n1-5_io_errors | PART 03 ONNX 모델 변환과 검증 (4절 배포 오류 분석) | |
| n2-1_quantization | PART 04 모델 경량화 | t04_quant_compare.md |
| n2-2_dfc | PART 05 NPU 실행모델 변환과 에뮬레이션 | |
| n2-3_benchmark | PART 06 CPU·NPU 성능 분석과 최적화 (2절 실측 데이터 분석) | t06_bench_report.md |
| n2-4_e2e | PART 06 CPU·NPU 성능 분석과 최적화 (3절 End-to-End 지연 분해) | |
| n2-5_project | PART 07 온디바이스 AI 응용 미니프로젝트 | t07_project_report.md |
| nA1_tokenizer | 부록 1장 LLM 추론과 토큰의 경제학 | |
| nA2_token_latency | 부록 2장 토큰 처리량과 지연 | |
| nA3_token_bench | 부록 3장 프로세서별 토큰 효율 | |
| nA4_cost_calc | 부록 4장 클라우드와 온디바이스 비용 비교 | |
| nA5_report_calc | 부록 5장 미니프로젝트: 토큰 비용 최적화 보고서 | tA5_token_report.md |

노트북의 셀 제목은 교재의 [코드 N-N] 번호와 STEP을 그대로 따르며, 코드와 주석은 교재와 같습니다.

## 실습 환경

| 항목 | 기준 |
|---|---|
| 실행 환경 | Google Colab (무료), CPU 런타임 |
| NPU 개발도구 | Hailo Dataflow Compiler 3.34.0 (Hailo-8), Python 3.10 전용 환경에서 실행 |
| ONNX | Opset 13, `torch.onnx.export(..., dynamo=False)` |
| 기준 장비 | Raspberry Pi 5 (8GB) + AI HAT+ (Hailo-8), HailoRT·펌웨어 4.23.0 |

버전은 집필 시점 기준입니다. 라이브러리 버전이 바뀌면 같은 코드라도 결과가 달라질 수 있으니, 노트북의 버전 확인 셀 결과를 함께 기록해 두세요.

## Releases

앞 단계 실습을 마치지 못했다면 Releases에서 해당 단계의 산출물을 내려받아 다음 단계를 진행할 수 있습니다.

| 단계 | 파일 |
|---|---|
| ONNX 변환 (PART 03) | mobilenet_v2.onnx, resnet18.onnx |
| 경량화 (PART 04) | mobilenet_v2_fp16.onnx, mobilenet_v2_int8.onnx, resnet18_fp16.onnx, resnet18_int8.onnx |
| NPU 변환 (PART 05) | mobilenet_v2_parsed.har, mobilenet_v2_quantized.har, mobilenet_v2_quantized_l2.har, mobilenet_v2.hef |

## 주의

- DFC 설치 파일(`*.whl`)은 사용권 계약(EULA)에 따라 재배포할 수 없습니다. 이 저장소나 공유 폴더에 올리지 말고 각자 Hailo Developer Zone에서 내려받아 사용합니다.
- 부록 [코드 A1-2]와 [코드 A2-2]는 교재와 같이 빈칸(`____`)이 있습니다. 빈칸을 채운 뒤 실행합니다. [코드 A2-2]를 채우지 않으면 이후 셀에서 오류가 나므로 STEP 2를 먼저 완성합니다.
- 같은 세션에서 환경 구성 셀을 다시 실행해도 되도록, DFC 전용 환경은 `uv venv --clear`로 만듭니다.

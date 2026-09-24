# NPU 활용 과정 실습 저장소

NPU 및 온디바이스 AI 교재의 실습 자료입니다. 모든 실습은 Google Colab에서 진행하며, 개인 PC에 설치할 것은 없습니다.

## 폴더 구성

| 폴더 | 내용 |
|---|---|
| `notebooks/` | Part별 실습 노트북 |
| `data/` | 공통 데이터셋(Imagenette) 안내 |
| `models/` | 모델과 단계별 산출물 안내 (파일은 Releases에서 제공) |
| `templates/` | 산출물 기록 템플릿 |

## 시작하기

1. 교재 Part 01의 안내에 따라 Hailo Developer Zone에서 DFC 설치 파일을 내려받아 본인 Google Drive의 `내 드라이브/hailo/` 폴더에 올립니다.
2. `notebooks/n1-2_env_setup.ipynb`를 Colab에서 열고 STEP 1부터 차례로 실행합니다.
3. `templates/t01_env_check.md`에 점검 결과를 기록합니다.

## 주의

- DFC 설치 파일(`*.whl`)은 사용권 계약(EULA)에 따라 재배포할 수 없습니다. 이 저장소나 공유 폴더에 올리지 말고 각자 내려받아 사용합니다.
- 앞 단계 실습을 마치지 못했다면 Releases에서 해당 단계의 산출물을 내려받아 다음 단계를 진행할 수 있습니다.

"""
npu_env.py — NPU 활용 과정 공통 환경 설정

저장소 루트(npu-course/)에 두고, 각 노트북 첫 셀에서 import해 사용합니다.
경로는 모두 이 파일의 위치를 기준으로 조립하므로 Colab과 Raspberry Pi에서
수정 없이 동일하게 동작합니다.
"""
import os
import sys

#- 실행 환경 판별: Colab이면 True, Raspberry Pi 등 로컬이면 False
IN_COLAB = "google.colab" in sys.modules

#- 저장소 루트: 이 파일이 놓인 폴더
ROOT = os.path.dirname(os.path.abspath(__file__))

#- 저장소 표준 폴더 (지침서: notebooks/ · rpi/ · models/ · data/ · templates/)
DATA_DIR      = os.path.join(ROOT, "data")
MODEL_DIR     = os.path.join(ROOT, "models")
TEMPLATE_DIR  = os.path.join(ROOT, "templates")
BENCH_DIR     = os.path.join(DATA_DIR, "bench")

os.makedirs(MODEL_DIR, exist_ok=True)


def model_dir(model, precision):
    """모델·정밀도별 저장 폴더를 반환하고, 없으면 생성합니다.

    예) model_dir("mobilenet_v2", "int8") → <ROOT>/models/mobilenet_v2/int8
    precision: "onnx"(fp32) | "fp16" | "int8" | "hef"
    """
    path = os.path.join(MODEL_DIR, model, precision)
    os.makedirs(path, exist_ok=True)
    return path


def check():
    """중간 확인: 실행 환경과 필수 폴더 존재 여부를 출력합니다."""
    print("실행 환경  :", "Colab" if IN_COLAB else "로컬(Raspberry Pi 등)")
    print("저장소 루트:", ROOT)
    for name, path in [("데이터 폴더", DATA_DIR), ("모델 폴더", MODEL_DIR)]:
        print(f"{name} :", "OK" if os.path.isdir(path) else "없음 → 저장소 클론 상태 확인")

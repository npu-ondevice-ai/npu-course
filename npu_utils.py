"""
npu_utils.py — NPU 활용 과정 공통 실습 함수

추론 파이프라인 실습에서 학습자가 직접 작성한 함수를 모아 둔 모듈입니다.
해당 함수가 처음 등장하는 차시에서는 노트북에서 직접 작성하고,
이후 차시(양자화 비교, NPU 벤치마크 등)부터 이 모듈에서 import합니다.
"""
import time
import numpy as np


def measure(fn, n_warmup=10, n_runs=100):
    """추론 지연시간 측정 (추론 파이프라인 실습과 동일)

    fn       : 인자 없이 호출하는 추론 함수 (예: lambda: sess.run(None, feed))
    n_warmup : 측정 전 예열 횟수 — 첫 실행의 초기화·캐시 비용을 측정에서 제외
    n_runs   : 실제 측정 횟수

    반환: (평균, 중앙값, 95백분위, 최댓값) — 단위 ms
    """
    #- 예열: 결과를 버리고 실행만 반복
    for _ in range(n_warmup):
        fn()

    #- 측정: 매 실행 시간을 ms 단위로 기록
    times = []
    for _ in range(n_runs):
        t0 = time.perf_counter()
        fn()
        times.append((time.perf_counter() - t0) * 1000)

    #- 요약 통계: 평균은 이상치에 민감하므로 중앙값·p95와 함께 봄
    t = np.array(times)
    return t.mean(), np.median(t), np.percentile(t, 95), t.max()

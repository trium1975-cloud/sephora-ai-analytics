Markdown
# 💄 Sephora E-Commerce AI Pricing Strategy & MD Simulator
> **8,770건 실데이터 기반 통계 가설 검정(ANOVA) 및 4대 머신러닝 파이프라인 구축 프로젝트**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/trium1975-cloud/sephora-ai-analytics/blob/main/sephora_ai_analytics.ipynb)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2+-orange.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.0+-brightgreen.svg)

---

## 📌 Executive Summary
* **핵심 질문**: "고가 럭셔리 제품일수록 소비자 만족도(평점)도 비례하여 높을까?"
* **통계적 규명**: 8,770건 정제 데이터 분석 결과 가격-평점 상관계수는 $r \approx 0.05$로 무상관에 수렴하며, **일원분산분석(One-way ANOVA: $F = 42.95, p < 0.001$)**을 통해 가격대별 만족도 차이가 실재함을 입증.
* **최적 구간 도출**: 가격 저항이 가장 적고 만족도가 극대화되는 **$25 ~ $50 (Mid-tier Sweet Spot)**을 소싱 핵심 타깃으로 규명.
* **비즈니스 구현**: 신제품 런칭 시 매출 추정, 조기 퇴출 진단, VOC 감성 판별, 벤치마크 매칭을 일원화한 **Gradio 4단 대시보드(`app.py`)** 프로토타입 서빙.

---

## 📊 1. 데이터셋 및 4-Tier 가격 세그먼트

결측치와 0점 리뷰 노이즈를 전처리한 후, 세포라의 상품군 가격 분포(왜도 및 사분위수)를 기반으로 4대 가격 티어를 정의했습니다.

| 가격 세그먼트 (Tier) | 가격 범위 ($) | 데이터 표본 수 | 평균 평점 (Score) | 주요 특징 및 소비자 심리 |
| :--- | :--- | :--- | :--- | :--- |
| **Budget** | < $25 | 2,145건 | 4.05 / 5.0 | 입문용, 바이럴 상품 중심, 가격 민감도 극대화 |
| **Mid-tier (Sweet Spot)** | **$25 ~ $50** | **3,892건** | **4.28 / 5.0** | **품질 신뢰도와 가격 합리성이 공존하는 최다 판매 구간** |
| **Premium** | $50 ~ $100 | 1,980건 | 4.12 / 5.0 | 효능 중심 고관여 기능성 상품군, 리뷰 평점 분산 심화 |
| **Luxury** | > $100 | 753건 | 3.98 / 5.0 | 브랜드 헤리티지 의존, 기대치 대비 만족도 실망 리스크 존재 |

---

## 🧪 2. 통계 가설 검정 (One-way ANOVA)

4개 가격 구간에 속한 고객 평점 평균의 차이가 통계적으로 유의미한지 검증하기 위해 일원분산분석을 수행했습니다.

* **귀무가설($H_0$)**: 4개 가격 티어별 고객 평점 평균에는 유의미한 차이가 없다.
* **대립가설($H_1$)**: 적어도 한 개 이상의 가격 티어 간 평점 평균에 통계적 차이가 존재한다.

```text
========================================================================
             One-way ANOVA Test: Price Tiers vs. Ratings
========================================================================
F-statistic : 42.95
p-value     : 2.14e-27 (p < 0.001)  -->  귀무가설(H0) 기각 / 대립가설 채택
========================================================================

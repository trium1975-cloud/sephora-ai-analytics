<img width="949" height="526" alt="15_qna" src="https://github.com/user-attachments/assets/b0b929a5-f615-4ff8-b943-cbe88ffbc4de" />
<img width="946" height="530" alt="14_action_plan" src="https://github.com/user-attachments/assets/99652537-e91b-491d-a83f-05347af66ad2" />
<img width="2500" height="1407" alt="13_anova_stat" src="https://github.com/user-attachments/assets/79930478-4d85-45cf-8d25-fc199dc35ba1" />
<img width="2500" height="1407" alt="12_service_value" src="https://github.com/user-attachments/assets/75eb9e8f-5b3c-439e-bc75-396001f0f850" />
<img width="2500" height="1407" alt="11_section_serving" src="https://github.com/user-attachments/assets/6002a28a-7cfd-427d-8434-1bad0ebc4a5f" />
<img width="950" height="532" alt="10_ai_matrix" src="https://github.com/user-attachments/assets/df89629a-379a-4707-b321-33616ad502eb" />
<img width="2500" height="1407" alt="09_viral_insights" src="https://github.com/user-attachments/assets/92ee5760-ff13-4ad0-8edb-367fc154a0da" />
<img width="951" height="533" alt="09_research_question" src="https://github.com/user-attachments/assets/fba9f235-77f6-4de8-b6ef-3b798492947c" />
<img width="2500" height="1407" alt="07_core_finding" src="https://github.com/user-attachments/assets/e6c53b01-662b-4e90-a85f-83b081dd7809" />
<img width="2500" height="1407" alt="06_data_integrity" src="https://github.com/user-attachments/assets/bdf74932-76b3-480a-b606-33ec716b4844" />
<img width="2500" height="1407" alt="05_section_data" src="https://github.com/user-attachments/assets/c3dec5c1-32d2-43d6-867f-374f06de4d3f" />
<img width="2500" height="1407" alt="04_our_goal" src="https://github.com/user-attachments/assets/24109f1e-460f-4b6d-b442-98091bff5964" />
<img width="954" height="537" alt="03_overview" src="https://github.com/user-attachments/assets/cebb2cc4-21a7-4fab-92e5-d38af93373be" />
<img width="954" height="534" alt="02_agenda" src="https://github.com/user-attachments/assets/8f47c3d1-be7a-4b87-9a92-908c9b433e1f" />
<img width="955" height="534" alt="01_cover" src="https://github.com/user-attachments/assets/6e051575-6c1c-4427-97f2-d865b93b0bf4" />
# 💄 Sephora E-Commerce AI Pricing Strategy & MD Simulator

> **8,770건의 이커머스 실데이터 기반 가격대별 만족도 통계 검정(ANOVA), 4대 머신러닝 파이프라인 및 Gradio 의사결정 솔루션**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML_Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Gradio](https://img.shields.io/badge/Gradio-Web_App-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app/)
[![Open in Colab](https://img.shields.io/badge/Colab-Interactive_Demo-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](./sephora_ai_analytics.ipynb)

---

## 📌 Executive Summary

* **비즈니스 문제 정의**: "고가 화장품일수록 고객 만족도(평점)가 선형적으로 상승하는가?"에 대한 실증적 검증
* **데이터 정제 성과**: 9,168건 중 입점 초기 미평가 결측치(0.0점 노이즈 398건)를 식별 및 제거하여 **8,770건 유효 표본 확보**
* **통계적 가설 검정**: 일원분산분석(One-way ANOVA, $F=42.95, p<0.001$)으로 가격 구간별 유의미한 평점 차이 입증 및 최적 소싱 구간 도출
* **4-AI 파이프라인 구축**: 매출 시뮬레이터, 퇴출 진단, VOC 감성 분석, 벤치마크 추천의 4대 AI 엔진 모듈화
* **인터랙티브 웹 서빙**: 비개발자(MD/마케터)도 제안 가격과 목표 평점을 실시간 시뮬레이션할 수 있는 4단 탭 Gradio 대시보드 구현

---

## 🤖 4-AI Engine Architecture

| 구분 | 엔진 명칭 | 모델 알고리즘 | 입력 변수 (Features) | 출력 타깃 (Target) | 비즈니스 가치 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Engine 1** | **매출 규모 시뮬레이터** | Random Forest Regressor | 카테고리, 제안가격, 평점, 리뷰수 | 예상 누적 매출액($), 판매량 | 신제품 출시 전 목표 매출 사전 산출 |
| **Engine 2** | **조기 퇴출 위험 진단기** | Random Forest Classifier | 카테고리, 제안가격, 예상평점 | 퇴출 위험도(%), 위험 3단계 등급 | 악성 재고 및 조기 단종 리스크 방지 |
| **Engine 3** | **고객 리뷰 감성 판별기** | Rule-based NLP Pipeline | 고객 리뷰 영문 원문 텍스트 | 긍/부정 판정, 예측 신뢰도 | VOC 모니터링 자동화 |
| **Engine 4** | **벤치마크 경쟁 추천기** | Constraint Ranking Engine | 타깃 카테고리, 최대 예산 한도 | 최고 평점·바이럴 Top-5 상품 | 상품 기획 시 타깃 경쟁 모델 제시 |

---

## 📊 Core Statistical Findings

### 1. 일원분산분석 (One-way ANOVA) 검정 결과
* **귀무가설($H_0$)**: 4개 가격 티어(Budget, Mid-tier, Premium, Luxury) 간 고객 평점(만족도)의 평균 차이는 없다.
* **대립가설($H_1$)**: 적어도 한 개 이상의 가격 티어 간 고객 평점 평균에 유의미한 차이가 존재한다.
* **검정 통계량**: $F\text{-statistic} = 42.95$, $p\text{-value} = 1.34 \times 10^{-27}\ (p < 0.001)$ $\rightarrow$ **귀무가설 강력 기각**
* **분석 인사이트**: 
  * 가격과 평점의 선형 상관관계는 미미함($r \approx 0.05$).
  * $25~$50 선의 **Mid-tier 구간**이 가격 저항이 적고 평점이 고르게 상위권에 수렴하는 **소싱 최적 구간(Sweet Spot)**임을 규명.

### 2. 소셜 증거(Social Proof)의 파레토 법칙
* 상위 20% 품목이 하트(Love) 관심도의 78% 이상을 점유
* 바이럴 반응의 핵심 동인은 가격이 아닌 **리뷰 누적 수($r > 0.65$)**로 판명

---

## 💼 Data-Driven Action Plans

1. **소싱 전략 최적화**: 신규 입점 품목을 $25~$50 구간에 우선 배치하여 품질 불만 리스크를 낮추고 안정 마진 확보
2. **사전 조기 경보(Early Warning)**: 퇴출 위험도 50%를 초과하는 상품군은 초도 매입량을 40% 감축하고 사전 체험단 우선 배분
3. **소셜 프루프 중심 랭킹**: 단순 가격 순 정렬을 지양하고, 리뷰 수와 하트 수가 검증된 스테디셀러 위주의 추천 캐러셀 운영

---

## 🛠️ Tech Stack & Troubleshooting

* **Tech Stack**: Python, Pandas, Scikit-learn, Gradio, SciPy
* **Scikit-learn 멀티프로세싱 병목 해결**: 
  * 가상 머신 환경에서 CPU 충돌(`n_jobs=-1` 무한 대기) 방지를 위해 `n_jobs=1` 단일 스레드 최적화 적용 $\rightarrow$ 모델 2종 학습 시간 3초 이내로 단축
* **런타임 세션 재할당 대응**: 
  * 원천 데이터 무결성 검증 및 전처리 복구 파이프라인을 단일 셀 내 원스톱 로직으로 설계하여 메모리 휘발 문제 차단

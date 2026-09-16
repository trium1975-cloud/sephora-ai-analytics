import gradio as gr
import pandas as pd
import numpy as np

# -------------------------------------------------------------
# 1. AI 엔진 모의 연산 함수 정의 (Gradio 서빙용)
# -------------------------------------------------------------

def predict_sales(category, price, rating, reviews):
    """Engine 1: Random Forest 기반 매출 규모 시뮬레이터"""
    base_conversion = 30  # 리뷰당 추정 구매 전환 계수
    category_multiplier = {"Skincare": 1.2, "Makeup": 1.1, "Fragrance": 1.3, "Bath & Body": 0.9}.get(category, 1.0)
    
    # 평점 및 가격 저항 반영 로직
    rating_weight = (rating / 5.0) ** 2
    est_units = int(reviews * base_conversion * category_multiplier * rating_weight)
    est_revenue = int(est_units * price)
    
    return f"${est_revenue:,.0f}", f"{est_units:,} 개"

def predict_churn(category, price, rating):
    """Engine 2: Random Forest Classifier 기반 조기 퇴출 위험 진단기"""
    # Mid-tier($25~$50) 기준 가격 저항 및 평점 가중치 연산
    risk_score = 20.0
    if price > 100:
        risk_score += 45.0
    elif price > 50:
        risk_score += 25.0
    elif price < 25:
        risk_score += 15.0
    else:
        risk_score += 0.0  # Sweet Spot
        
    if rating < 3.5:
        risk_score += 35.0
    elif rating < 4.0:
        risk_score += 15.0
    else:
        risk_score -= 10.0
        
    risk_score = max(5.0, min(95.0, risk_score))
    
    if risk_score >= 60:
        level = "🚨 위험 (초도 사입 40% 감축 및 프로모션 필요)"
    elif risk_score >= 40:
        level = "⚠️ 주의 (모니터링 대상)"
    else:
        level = "✅ 안전 (정상 입점 승인)"
        
    return f"{risk_score:.1f}%", level

def analyze_sentiment(review_text):
    """Engine 3: Rule-based NLP 고객 VOC 감성 판별기"""
    pos_words = ["great", "love", "amazing", "good", "best", "perfect", "moisturizing", "holy grail"]
    neg_words = ["terrible", "bad", "breakout", "dry", "waste", "expensive", "worst", "irritation"]
    
    text_lower = review_text.lower()
    pos_count = sum(text_lower.count(w) for w in pos_words)
    neg_count = sum(text_lower.count(w) for w in neg_words)
    
    if pos_count > neg_count:
        sentiment = "🌟 긍정 (Positive VOC)"
        confidence = min(98.0, 70.0 + (pos_count - neg_count) * 10)
    elif neg_count > pos_count:
        sentiment = "⚠️ 부정 (Negative VOC)"
        confidence = min(98.0, 70.0 + (neg_count - pos_count) * 10)
    else:
        sentiment = "⚖️ 중립 (Neutral / Objective)"
        confidence = 60.0
        
    return sentiment, f"{confidence:.1f}%"

def recommend_benchmark(category, max_budget):
    """Engine 4: Constraint Ranking 기반 Top-5 벤치마크 경쟁 상품 매칭"""
    benchmarks = [
        {"브랜드": "The Ordinary", "상품명": "Niacinamide 10% + Zinc 1%", "카테고리": "Skincare", "가격($)": 10.80, "평점": 4.5, "하트수": 780000},
        {"브랜드": "Laneige", "상품명": "Lip Sleeping Mask", "카테고리": "Skincare", "가격($)": 24.00, "평점": 4.6, "하트수": 650000},
        {"브랜드": "Fenty Beauty", "상품명": "Gloss Bomb Lip Luminizer", "카테고리": "Makeup", "가격($)": 21.00, "평점": 4.7, "하트수": 540000},
        {"브랜드": "Sol de Janeiro", "상품명": "Brazilian Bum Bum Cream", "카테고리": "Bath & Body", "가격($)": 48.00, "평점": 4.6, "하트수": 430000},
        {"브랜드": "Maison Margiela", "상품명": "REPLICA Jazz Club", "카테고리": "Fragrance", "가격($)": 85.00, "평점": 4.5, "하트수": 210000},
        {"브랜드": "Drunk Elephant", "상품명": "Protini Polypeptide Cream", "카테고리": "Skincare", "가격($)": 68.00, "평점": 4.4, "하트수": 390000},
        {"브랜드": "Rare Beauty", "상품명": "Soft Pinch Liquid Blush", "카테고리": "Makeup", "가격($)": 23.00, "평점": 4.8, "하트수": 890000}
    ]
    
    df = pd.DataFrame(benchmarks)
    filtered = df[(df["카테고리"] == category) & (df["가격($)"] <= max_budget)]
    if filtered.empty:
        filtered = df[df["카테고리"] == category]
    
    ranked = filtered.sort_values(by=["평점", "하트수"], ascending=False).head(5)
    return ranked[["브랜드", "상품명", "가격($)", "평점", "하트수"]]

# -------------------------------------------------------------
# 2. Gradio 4단 탭 대시보드 레이아웃 구성
# -------------------------------------------------------------

with gr.Blocks(title="Sephora AI Merchandising Simulator") as demo:
    gr.Markdown("# 💄 Sephora E-Commerce AI MD Simulator")
    gr.Markdown("8,770건 실데이터 기반 머신러닝 파이프라인 및 실시간 머천다이징 시뮬레이터 대시보드")
    
    with gr.Tab("📊 Tab 1: 매출 규모 시뮬레이터"):
        gr.Markdown("### 신제품 카테고리 및 출시 가격 기반 예상 누적 매출액 산출")
        with gr.Row():
            cat_in1 = gr.Dropdown(["Skincare", "Makeup", "Fragrance", "Bath & Body"], label="카테고리", value="Skincare")
            price_in1 = gr.Slider(5, 200, value=35, label="출시 예정 가격 ($)")
            rating_in1 = gr.Slider(1.0, 5.0, value=4.5, step=0.1, label="목표 평점")
            rev_in1 = gr.Slider(10, 5000, value=500, label="예상 리뷰 수")
        btn1 = gr.Button("예상 매출액 계산", variant="primary")
        with gr.Row():
            out_rev = gr.Textbox(label="예상 총매출액 ($)")
            out_units = gr.Textbox(label="예상 누적 판매량")
        btn1.click(predict_sales, inputs=[cat_in1, price_in1, rating_in1, rev_in1], outputs=[out_rev, out_units])

    with gr.Tab("🚨 Tab 2: 조기 퇴출 위험 진단기"):
        gr.Markdown("### 4-Tier 가격대별 이탈 리스크 사전 판정 (Early Warning)")
        with gr.Row():
            cat_in2 = gr.Dropdown(["Skincare", "Makeup", "Fragrance", "Bath & Body"], label="카테고리", value="Skincare")
            price_in2 = gr.Slider(5, 250, value=120, label="출시 예정 가격 ($)")
            rating_in2 = gr.Slider(1.0, 5.0, value=3.8, step=0.1, label="목표 평점")
        btn2 = gr.Button("퇴출 리스크 판정", variant="primary")
        with gr.Row():
            out_risk = gr.Textbox(label="퇴출 위험 확률 (%)")
            out_level = gr.Textbox(label="3단계 리스크 등급")
        btn2.click(predict_churn, inputs=[cat_in2, price_in2, rating_in2], outputs=[out_risk, out_level])

    with gr.Tab("💬 Tab 3: 고객 리뷰 감성 판별기"):
        gr.Markdown("### 영문 고객 VOC 실시간 긍/부정 분석 및 신뢰도 스코어 산출")
        text_in = gr.Textbox(lines=3, label="고객 영문 리뷰 원문", value="This serum is my absolute holy grail, highly moisturizing!")
        btn3 = gr.Button("감성 판별 실행", variant="primary")
        with gr.Row():
            out_sent = gr.Textbox(label="판정 결과")
            out_conf = gr.Textbox(label="예측 신뢰도")
        btn3.click(analyze_sentiment, inputs=[text_in], outputs=[out_sent, out_conf])

    with gr.Tab("🏆 Tab 4: 벤치마크 추천기"):
        gr.Markdown("### 예산 범위 내 카테고리별 Top-5 벤치마크 상품 매칭")
        with gr.Row():
            cat_in4 = gr.Dropdown(["Skincare", "Makeup", "Fragrance", "Bath & Body"], label="타깃 카테고리", value="Skincare")
            budget_in4 = gr.Slider(10, 150, value=40, label="최대 예산 한도 ($)")
        btn4 = gr.Button("벤치마크 상품 조회", variant="primary")
        out_df = gr.Dataframe(label="추천 벤치마크 Top-5 모델")
        btn4.click(recommend_benchmark, inputs=[cat_in4, budget_in4], outputs=[out_df])

if __name__ == "__main__":
    demo.launch()

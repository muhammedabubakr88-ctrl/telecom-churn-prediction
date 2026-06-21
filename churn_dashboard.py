# MTN Nigeria Churn Prediction Dashboard
# Built by muhammedabubakr88-ctrl

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="MTN Churn Predictor", page_icon="📡", layout="wide")

st.markdown('''
<style>
    .main { background-color: #0f1117; }
    .block-container { padding-top: 2rem; }
    .metric-card {
        background: linear-gradient(135deg, #1e2130, #252a3a);
        border: 1px solid #2e3450;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        text-align: center;
    }
    .risk-low {
        background: linear-gradient(135deg, #0d3b2e, #1a5c46);
        border: 1px solid #27ae60;
        border-radius: 10px;
        padding: 1rem 1.5rem;
    }
    .risk-medium {
        background: linear-gradient(135deg, #3b2a0d, #5c4a1a);
        border: 1px solid #f39c12;
        border-radius: 10px;
        padding: 1rem 1.5rem;
    }
    .risk-high {
        background: linear-gradient(135deg, #3b0d0d, #5c1a1a);
        border: 1px solid #e74c3c;
        border-radius: 10px;
        padding: 1rem 1.5rem;
    }
    .stButton > button {
        background: linear-gradient(90deg, #ffcc00, #ff9900);
        color: #0f1117;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-size: 1rem;
        width: 100%;
    }
    .stButton > button:hover { opacity: 0.9; }
    .section-divider { border-top: 1px solid #2e3450; margin: 2rem 0; }
</style>
''', unsafe_allow_html=True)

DATA = {
    "CustomerID": ["C001", "C002", "C003", "C004", "C005", "C006", "C007"],
    "CallDrops":  [1, 2, 3, 5, 6, 7, 8],
    "DataUsage":  [10, 9, 8, 5, 4, 3, 2],
    "ChurnRisk":  [10, 20, 30, 60, 70, 85, 95],
}

df = pd.DataFrame(DATA)
X = df[["CallDrops", "DataUsage"]]
y = df["ChurnRisk"]
model = LinearRegression()
model.fit(X, y)

st.markdown("## 📡 MTN Nigeria — Customer Churn Prediction Dashboard")
st.markdown("Real-time churn risk analysis powered by Machine Learning")
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-card"><h3 style="color:#ffcc00!important">{len(df)}</h3><p style="color:#aaa;margin:0">Total Customers</p></div>', unsafe_allow_html=True)
with col2:
    high = (df["ChurnRisk"] > 60).sum()
    st.markdown(f'<div class="metric-card"><h3 style="color:#e74c3c!important">{high}</h3><p style="color:#aaa;margin:0">High Risk</p></div>', unsafe_allow_html=True)
with col3:
    med = ((df["ChurnRisk"] > 30) & (df["ChurnRisk"] <= 60)).sum()
    st.markdown(f'<div class="metric-card"><h3 style="color:#f39c12!important">{med}</h3><p style="color:#aaa;margin:0">Medium Risk</p></div>', unsafe_allow_html=True)
with col4:
    low = (df["ChurnRisk"] <= 30).sum()
    st.markdown(f'<div class="metric-card"><h3 style="color:#27ae60!important">{low}</h3><p style="color:#aaa;margin:0">Low Risk</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("### 📋 Section 1 — Customer Dataset")
show_raw = st.toggle("Show raw data", value=True)
if show_raw:
    def color_risk(val):
        if val <= 30:   return "background-color:#0d3b2e; color:#27ae60"
        elif val <= 60: return "background-color:#3b2a0d; color:#f39c12"
        else:           return "background-color:#3b0d0d; color:#e74c3c"
    styled = df.style.applymap(color_risk, subset=["ChurnRisk"])
    st.dataframe(styled, use_container_width=True, hide_index=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("### 📊 Section 2 — Visualizations")
vcol1, vcol2 = st.columns(2)

with vcol1:
    fig1 = px.scatter(df, x="CallDrops", y="ChurnRisk", size="ChurnRisk",
        color="ChurnRisk", color_continuous_scale="RdYlGn_r",
        text="CustomerID", title="📉 Call Drops vs Churn Risk", template="plotly_dark")
    fig1.update_traces(textposition="top center", marker=dict(line=dict(width=1, color="#ffcc00")))
    fig1.update_layout(paper_bgcolor="#1e2130", plot_bgcolor="#1e2130", font_color="#e8eaf6")
    st.plotly_chart(fig1, use_container_width=True)

with vcol2:
    fig2 = px.scatter(df, x="DataUsage", y="ChurnRisk", size="ChurnRisk",
        color="ChurnRisk", color_continuous_scale="RdYlGn_r",
        text="CustomerID", title="📶 Data Usage vs Churn Risk", template="plotly_dark")
    fig2.update_traces(textposition="top center", marker=dict(line=dict(width=1, color="#ffcc00")))
    fig2.update_layout(paper_bgcolor="#1e2130", plot_bgcolor="#1e2130", font_color="#e8eaf6")
    st.plotly_chart(fig2, use_container_width=True)

fig3 = px.bar(df, x="CustomerID", y="ChurnRisk", color="ChurnRisk",
    color_continuous_scale="RdYlGn_r", title="📊 Churn Risk per Customer",
    template="plotly_dark")
fig3.update_layout(paper_bgcolor="#1e2130", plot_bgcolor="#1e2130", font_color="#e8eaf6")
st.plotly_chart(fig3, use_container_width=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("### 🤖 Section 3 — Machine Learning Model")
mcol1, mcol2, mcol3 = st.columns(3)
coef_cd, coef_du = model.coef_
with mcol1:
    st.markdown('<div class="metric-card"><p style="color:#aaa;margin:0">Algorithm</p><h4 style="color:#ffcc00!important;margin:0.3rem 0">Linear Regression</h4></div>', unsafe_allow_html=True)
with mcol2:
    st.markdown(f'<div class="metric-card"><p style="color:#aaa;margin:0">CallDrops Coefficient</p><h4 style="color:#ffcc00!important;margin:0.3rem 0">{coef_cd:.2f}</h4></div>', unsafe_allow_html=True)
with mcol3:
    st.markdown(f'<div class="metric-card"><p style="color:#aaa;margin:0">DataUsage Coefficient</p><h4 style="color:#ffcc00!important;margin:0.3rem 0">{coef_du:.2f}</h4></div>', unsafe_allow_html=True)

with st.expander("How the model works"):
    st.markdown(
        "The model learns the relationship between two customer signals and churn risk.\n\n"
        "- **CallDrops** — More dropped calls means higher frustration and higher churn risk\n"
        "- **DataUsage** — Lower data usage means disengaged customer and higher churn risk\n\n"
        "Formula: ChurnRisk = (CallDrops x coeff1) + (DataUsage x coeff2) + intercept"
    )

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("### 🎯 Section 4 — Predict Churn Risk")
pcol1, pcol2 = st.columns([2, 1])

with pcol1:
    call_drops = st.slider("📞 Call Drops (per month)", min_value=0, max_value=20, value=5, step=1)
    data_usage = st.slider("📶 Data Usage (GB per month)", min_value=0, max_value=20, value=5, step=1)
    predict_btn = st.button("🔮 Predict Churn Risk")

with pcol2:
    st.markdown("**Feature Reference**")
    st.markdown("| Signal | Impact |\n|---|---|\n| High Call Drops | Up Risk |\n| Low Data Usage | Up Risk |\n| Low Call Drops | Down Risk |\n| High Data Usage | Down Risk |")

if predict_btn:
    raw_pred = model.predict([[call_drops, data_usage]])[0]
    prediction = max(0, min(100, round(raw_pred, 1)))

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("#### 📈 Prediction Result")

    if prediction <= 30:
        css_class, label, emoji, color = "risk-low", "LOW RISK", "✅", "#27ae60"
        detail = "This customer is unlikely to churn. Maintain service quality to retain them."
    elif prediction <= 60:
        css_class, label, emoji, color = "risk-medium", "MEDIUM RISK", "⚠️", "#f39c12"
        detail = "This customer shows warning signs. Consider a proactive retention offer."
    else:
        css_class, label, emoji, color = "risk-high", "HIGH RISK", "🚨", "#e74c3c"
        detail = "Immediate action required. Escalate to retention team with a priority offer."

    rcol1, rcol2 = st.columns([1, 2])
    with rcol1:
        st.markdown(
            f'<div class="{css_class}"><h2 style="color:{color}!important;margin:0">{emoji} {prediction}%</h2>'
            f'<h4 style="color:{color}!important;margin:0.3rem 0">{label}</h4></div>',
            unsafe_allow_html=True)
    with rcol2:
        st.markdown("**Customer Profile Entered:**")
        st.markdown(f"- 📞 Call Drops: **{call_drops}** per month")
        st.markdown(f"- 📶 Data Usage: **{data_usage} GB** per month")
        st.markdown(f"**Recommendation:** {detail}")

    gauge_fig = px.bar(x=["Churn Risk"], y=[prediction], color=[prediction],
        color_continuous_scale="RdYlGn_r", range_y=[0, 100],
        template="plotly_dark", title=f"Churn Risk Score: {prediction}%")
    gauge_fig.update_layout(paper_bgcolor="#1e2130", plot_bgcolor="#1e2130",
        font_color="#e8eaf6", showlegend=False)
    gauge_fig.add_hline(y=30, line_dash="dash", line_color="#27ae60",
        annotation_text="Low / Medium threshold")
    gauge_fig.add_hline(y=60, line_dash="dash", line_color="#f39c12",
        annotation_text="Medium / High threshold")
    st.plotly_chart(gauge_fig, use_container_width=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<p style="color:#555;text-align:center;font-size:0.8rem">MTN Nigeria Churn Intelligence System · Powered by scikit-learn & Streamlit</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#888;text-align:center;font-size:0.85rem">Created by <b style="color:#ffcc00">muhammedabubakr88-ctrl</b></p>', unsafe_allow_html=True)

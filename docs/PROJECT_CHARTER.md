# Cross-Asset Volatility-Surface & Relative-Value Lab  
**Project Charter – v1.0 (2025-05-28)**  

---

## 1 Purpose
Develop an *arbitrage-free* volatility-surface engine across equity-index and commodity underlyings and exploit surface-driven **relative-value (RV) mispricings**.  
Outputs feed two goals:  
1. **Daily live RV Trade Sheet** + VaR for a hypothetical buy-side options pod.  
2. A publishable research paper targeting *Risk* or *Quantitative Finance*.

## 2 Objectives & KPIs

| Area | Metric | Target | Rationale |
|------|--------|--------|-----------|
| Alpha | **Post-cost Sharpe** (2015-24) | ≥ 1.20 | Capacity-adjusted; slippage model applied |
| Risk | **Static-arb violations** | 0 per surface | Hard constraint |
| Risk | **P&L attribution error** | ≤ 5 % of daily realized P&L | Model greeks must explain desk P&L |
| Risk | **1-day 99 % VaR back-test exceptions** | ≤ 4 per 252 trading days | Basel traffic-light rule (green zone) |
| Calibration | Wall-clock / surface | ≤ 1 s | JAX JIT on 32-core CPU |
| Ops | Dashboard redraw | ≤ 1 s for 5-y surface | Streamlit UX |

## 3 In Scope
* Underlyings: **SPX, NDX, VIX, CL (WTI), GC (Gold)**
* Option expiries (tenor grid): **Weekly, monthly & quarterly contracts from 1 week out to 2 years**
* Strike coverage: **5 Δ to 95 Δ in 5-Δ buckets (≈ 0.5 x spot to 2 x spot)**
* Trade types: **Calendar, Vertical (10 Δ wings), Index-Component Dispersion**
* Data window: **2015-01-02 → 2024-12-31**
* Overnight (EOD) frequencies only—intraday reserved for Phase 7+

## 4 Out of Scope (Phase 0-3)
* FX, Crypto, or single-stock surfaces  
* Stochastic rates (use simple cubic-spline bootstrapped OIS)  
* Execution algos beyond a parametric cost model

## 5 Deliverables
| # | Artifact | Format |
|---|----------|--------|
| 1 | `vol_lab` Python package + Docker image (`vol-lab:<sha>`) | PyPI-ready & GHCR |
| 2 | **Daily RV Sheet** & VaR PDF | CSV + PDF emailed by `live` mode |
| 3 | Five-page memo & 90-sec demo video | PDF + .mp4 |
| 4 | Clean 5-year option parquet subset | DVC-tracked, redistributable |
| 5 | Research paper draft | LaTeX + figures |

## 6 Timeline (Gantt)

| Phase | Dates (target) | Owner | Exit Criterion |
|-------|----------------|-------|----------------|
| 0 Prep & Scoping | **2025-05-24 → 05-31** | Ryan Sevante | Charter & data contract v1.0, CI green |
| 1 Data IO & Cleaning | 06-01 → 06-14 | — | Parquet lake + QC report |
| 2 SVI/SABR Engine | 06-15 → 07-12 | — | RMSE < 0.25 vol pts, runtime ≤1 s |
| 3 Pricing & Greeks | 07-13 → 08-02 | — | Vanilla priced vs vendor bench |
| 4 RV Back-tester | 08-03 → 08-30 | — | Sharpe ≥ 1.2 pre-cost |
| 5 Streamlit UI & CLI | 08-31 → 09-20 | — | Live dashboard <1 s latency |
| 6 Paper & Video | 09-21 → 10-05 | — | Draft submitted for peer review |

## 7 Stakeholders
| Role | Name / Handle | Responsibility |
|------|---------------|----------------|
| Principal Investigator | **Brennan Thompson** | Design, coding, paper |
| Quant mentor | TBD (Discord) | Technical review |

## 8 Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| OPRA licensing restricts data sharing | High | Med | Use IEX *academic* OPRA + share only 5-yr sample |
| Compute/storage cost | Med | Low | DuckDB + ZSTD Parquet, free AWS S3 tier |
| Interview/job search drains time | High | Med | Buffer 2 wks in Phase 4 & 5 |
| Strategy overfits in back-test | High | Med | Walk-forward OOS, Purging/Embargo, White’s Reality Check |
| Surface calibration unstable on low-liq strikes | Med | High | Strike filtering + Tikhonov regularisation |

## 9 Assumptions
* Python 3.1x environment; JAX CPU backend (no GPU dependency).  
* Free or academic licences cover redistribution of *aggregated* data.  
* 32-core local workstation + occasional AWS m6i.4xlarge spot for heavy suites.
* Results and artifacts are **for academic / educational use only; no live capital is traded**

## 10 Version Control & Reproducibility
* **Poetry** for Python deps; **Docker** image per git SHA.  
* **DVC** tracks `data/`; remote = `s3://vol-lab-dvc`.  
* **GitHub Actions** runs lint + unit on every push; nightly slow suite.

---

_Last updated: 2025-05-28_

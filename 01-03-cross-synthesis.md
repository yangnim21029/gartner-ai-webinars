# 01–03 跨場綜合：一套 Gartner framework 換三套 C-suite 外衣

> CIO（01）/ CHRO（02）/ CCO（03）三場共用同一套 Gartner framework，只換不同 C-suite 的詞彙。這份是把三場拉在一起的深度對照；04–08 各自主題不同，尚未納入（索引見 [MOC.md](./MOC.md)）。
> 沉澱日：2026-05-28

---

## 三場是什麼

| # | 標題 | 講者 / 角色 | 主軸 | 資料夾 |
|---|---|---|---|---|
| 01 | Accelerate Your AI Journey With Business Capability Maps | Alexander Hoeppe（VP Analyst，製造） | CIO 視角：用 BCM 把 AI 投資錨在 capability 而不是 use case | [`01-ai-journey-business-capability-maps/`](./01-ai-journey-business-capability-maps/) |
| 02 | Stop Funding Features and Start Building Value — How CHROs Win With HR AI | Harsh Kondoli + Lydia Wu | CHRO 視角：North Star → Where to Play → Design for Value | [`02-hr-ai-stop-funding-features/`](./02-hr-ai-stop-funding-features/) |
| 03 | Transforming Communications for an AI-enabled World | Paul Catherwood + Emily L. | CCO 視角：逃離 efficiency trap，把 comms 從 cost center 變 strategic partner | [`03-comms-ai-enabled-world/`](./03-comms-ai-enabled-world/) |

每個資料夾結構一致：`video.mp4` / `notes.md`（H2 知識點，最完整）/ `transcript.{srt,vtt,txt,json}`。

---

## 共通骨架：一套 framework 換三套外衣

三場用同一套 Gartner 內部 framework，只是換不同 C-suite 的詞彙。看穿這層，未來碰任何 Gartner 的 C-level 報告都能對號入座。

### 1. 同一個核心 thesis：對話單位從 use case 拉到 outcome

| 場 | 「對的對話單位」 | 「錯的對話單位」 |
|---|---|---|
| CIO | Business Capability（三五年不變的能力） | Use case（vendor 半年就推新版本） |
| CHRO | North Star outcome（CEO 在意的 2-3 個指標） | AI 工具部署數量 |
| CCO | Value proposition（comms 在 enterprise 的角色） | AI use case 清單 |

**共通失敗模式**：拿到 AI 預算就直接挑 use case，沒先鎖 outcome。三場各自的開場數據都是這個故事的不同切面（60% POC 失敗 / 95% HR AI 沒拿到 value / 半數 CCO 說 Gen AI 沒達期待）。

### 2. 同一個 Value × Feasibility 矩陣

三場都用同一張二維圖把 use case 分類：

- **Likely wins** — value 高 + feasibility 高 → 馬上做
- **Calculated risks** — value 高但 feasibility 還沒成熟 → 小規模試
- **Marginal gains** — value 低 → 不要 distract 注意力

Gartner 維護的 use case 庫：CIO 場 200+、CCO 場 18 個 comms 專用。CHRO 場沒給總數但同一邏輯。

### 3. 同一個 Portfolio 三層分配

換了三套詞，做同一件事：

| 場 | 低風險（70%） | 中（20%） | 高風險（10%） |
|---|---|---|---|
| CIO | Defend（augment 員工生產力） | Extend（process transformation） | Upend（藥廠級押注） |
| CHRO | Within boundaries（已驗證） | Pushing（價值在但範圍不清） | Breaking（連價值都不確定） |
| CCO | Crawl（champion + ground rules） | Walk（重設 workflow + role） | Run（重談 SLA + strategic partner） |

CIO/CHRO 是「投資組合分配」，CCO 是「時序推進」— 但都在處理「Within = 安全但沒未來、Breaking = 燒錢但贏者通吃」的兩難。

### 4. 同一條 Readiness 軸

| 場 | 維度 | 容易被忽略的維度 |
|---|---|---|
| CIO | Business / Technology / Process / People（再細分 AI 7 維） | Business 跟 Strategy & Governance — 多數人只看 Technology |
| CHRO | People / Process & Governance / Technology / Data | Motivation 跟 Ease of Use — 不是技能訓練 |
| CCO | 用 Crawl-Walk-Run 取代正式 readiness 評估 | 重新談 SLA — 沒換 SLA 等於沒換 value proposition |

**共通鐵則**：Data readiness ≠ 資料 100% 乾淨，是「對這個 capability 有沒有結構」。CIO/CHRO 兩場原話一致。

### 5. 同一個 Agent 警告

三場都明說：**Vendor 賣的 high-agency agent 在多數場景是 marketing**。

- CIO 場：Agency 5 級光譜，Level 1 fully autonomous 在多數產業是 science fiction。多數企業合理停在 Level 3-4
- CHRO 場：HR 領域今天零個 proven high-agency agent at scale。Agent-washing = 昨天的 chatbot 改名漲價
- CCO 場：Lenovo 8 週縮到幾秒的案例「不叫 agentic AI」，是 daisy chain of fine-tuned LLM。**不需要 agentic 也能拿到戲劇性 ROI**

**共通判準**：問 vendor「跟去年 v1 比，能 reason 哪幾步以前沒辦法？autonomy 高了多少？」答不出來 = agent-washing。

### 6. Human-in-the-loop 是設計選擇不是補丁

三場原話一致：HITL 不是「自動化做不完的退讓」，是 deliberate design。CIO 場講 ethical judgment 跟 escalation；CHRO 場講 reputational risk；CCO 場兩個案例（Lenovo、Hitachi）都強調 every output 都有 human eyes。

---

## 三場各自獨有、別忘了

### 01 BCM 場獨有
- **Pace Layer**（commodity / keep up / differentiating）— 顏色決定 AI 投資優先序，differentiating 區 ROI 最高
- **Value Stream + Digital Thread** — BCM 是 Lego（沒順序），value stream 補上 sequence + KPI 關係
- **AI Opportunity Radar** — BCM × use case 的視覺化映射，一眼看出投資集中在 core / back / front / product 哪一象限
- **AI Ambition Pattern** — productivity-first vs customer-first vs product-innovation-first，產業會有典型偏好

### 02 HR AI 場獨有
- **「12 個月後我要看到什麼今天沒發生的事？」** — Lydia 的 framing question，比抽象設目標好用
- **「How do I know it's NOT working?」** — 簽 vendor 前必問，測 partner 真心 + 早期 warning sign
- **Deterministic HR vs Probabilistic AI 的 Catch-22** — 不強迫 AI 變 deterministic，設計外圍 sandbox 框住它能動的範圍
- **AI Adoption Triad**：Skills + Motivation + Ease of Use — 取代失效的 ADKAR
- **隱藏流程詛咒** — 你以為流程在跑，其實是兩個人的 Excel 撐起來。AI 上線前要 process discovery
- **Break-even 看 portfolio 不看單一 use case** — 單算每個 use case 都過不了，加總才看得到 NPV

### 03 Comms 場獨有
- **Efficiency Trap**（整場最重要的 framing）— 只追效率 = 變便宜的 reactive 部門，不會更有價值
- **Toolmate 思維** — AI 不是 replacement 是 collaborator，handoff 設計是 comms leader 自己的工作
- **Comms 工作光譜**（comms-led ↔ blurry ↔ business-led）— 哪些該主動 atrophy（tactical content creation），哪些 lean in（strategic content partnering、connector）
- **Pyramid → Diamond talent pipeline** — entry-level 變少，mid-career 變多，傳統 5 年訓練週期撐不下去
- **AEO（Answer Engine Optimization）** — AI 也是 audience，內容要寫「人愛讀 + AI 好抓」雙向兼容
- **Narrative Health / Trust Barometer** — 取代 reach/impression/sentiment 的 strategic metric
- **Synthetic Audience** — LLM 模擬 persona 替代 focus group。第一次用必須 parallel 跟真實 focus group 校準

---

## 兩個跨場次的隱藏 hack

1. **Temperature setting** — CHRO + CCO 兩場都明說。Vendor admin 一定有 access，「AI 太死板」常是 config 沒調而不是模型不行。負面 feedback 先 audit 自己的 setup
2. **「不知道 baseline 就無法歸因」** — CHRO + CIO 都強調。沒 baseline 跟 control group，sales 上升你證明不了是 AI 還是季節性。能 A/B 就 A/B，不能就 before/after

---

## Contradiction / Open Question

三場交叉看也不是全對齊，留意這幾條：

1. **Build vs Buy 立場略不同** — CHRO 場明說「Build 是 last resort」；CCO 場觀察「Build 在 comms tech 回潮」（chatbot/digital front door）但同意「沒治理的 build 兩年變 tech debt」。差別在領域 — HR 高度 packaged，comms 高度組織特定
2. **CIO 場 60% 失敗的主因是 change management；CHRO 場主因是 ROI 講不清** — 這兩條其實是同一件事的 IT 視角 vs HR 視角，CCO 場把它整合成 「value proposition reframe」
3. **Defend/Within 該占比例多少？** — CIO 場給 70%，CHRO 場給 70%，CCO 場沒給數字但 crawl phase 暗示一樣。但三場都警告「100% Defend 沒未來」— 比例的下限是什麼沒人答

---

## Vendor 視角（給 User 的留意）

這三場 webinar 是 Gartner 教 C-level buyer 怎麼篩 AI vendor 跟 AI 案。反過來看，你做 AI 軟件就是被這套 framework 篩的對象。值得內化的提醒：

- **你的產品定位是 use case 還是 capability？** — 用 use case 詞彙 pitch 會被 Gartner 客戶歸到「3 年後 obsolete」那堆
- **你能不能讓 buyer 算出 portfolio 級 break-even？** — 單一 use case ROI 算不出來是 vendor 共通問題，能教 buyer 算 portfolio 的 vendor 比較容易續約
- **「How do I know it's NOT working?」這題你答得出來嗎？** — 答不出來 = signals not a partner
- **不要 agent-wash** — 把工具改名叫 agent 但 reasoning / autonomy / adaptability 沒升級，C-level buyer 越來越會問三維對比
- **Temperature 跟 setup audit 該預設開放** — buyer 越來越知道這層存在，藏起來會被當不專業

# Gartner AI Webinars — 筆記庫 + BCM 工作區

Gartner 公開 AI webinar 的逐字稿與知識點筆記（8 場），加上一條從 01 場延伸出來的 Business Capability Map（BCM）工作線。下面用「你可能想問的問題」直接帶你到對的檔案。

**這裡有什麼**
- **8 場 webinar**（`01-`–`08-`）：每場一資料夾，內含 `notes.md`（H2 知識點，最完整）、`source.md`、`transcript.{srt,vtt,txt,json}`。影片太大不進 repo。
- **總索引就在本檔**：8 場總表、按主題找、新增指南，往下捲。
- **[`bcm/`](./bcm/)** — BCM 方法、三家公司實作範例、參考範本。
- **[`01-03-cross-synthesis.md`](./01-03-cross-synthesis.md)** — CIO/CHRO/CCO 三場深度跨場對照。

---

## Q：想快速抓某場的重點，看哪？
進該場資料夾的 `notes.md`。不確定看哪場 → 先從下表挑。

## Q：8 場分別在講什麼？

照資料夾編號排序。每場一條，連 notes.md（最完整的單場知識點筆記）。

| # | 主題 | 講者 | 視角 | Notes |
|---|---|---|---|---|
| 01 | AI Journey with Business Capability Maps | Alexander Hoeppe | CIO・把 AI 投資錨在 capability 不是 use case | [notes](./01-ai-journey-business-capability-maps/notes.md) |
| 02 | Stop Funding Features and Start Building Value | Harsh Kondoli + Lydia Wu | CHRO・North Star → Where to Play → Design for Value | [notes](./02-hr-ai-stop-funding-features/notes.md) |
| 03 | Transforming Communications for an AI-enabled World | Paul Catherwood + Emily L. | CCO・逃離 efficiency trap，crawl-walk-run | [notes](./03-comms-ai-enabled-world/notes.md) |
| 04 | How to Create a Workforce That Can Keep Up With AI | Kabeh Vaziri + Soyeb Barot | CIO・三場仗 capacity / emotion / redesign，錨在不變的能力 | [notes](./04-workforce-keep-up-with-ai/notes.md) |
| 05 | How to Identify, Fund and Measure High-Value AI Use Cases | Frances Karamouzis | CIO/CFO・blue→green money，AI use case 的財務紀律 | [notes](./05-high-value-ai-use-cases-finops/notes.md) |
| 06 | Steps for Procurement to Become AI-First | Ryan Polk | CPO・三預測，pattern vs judgment，tribal knowledge 被迫結帳 | [notes](./06-procurement-ai-first/notes.md) |
| 07 | IT 2030: How CIOs Should Reinvent IT for the AI Age | Rajesh Kandaswamy | CIO・四 archetypes 選 North Star，tiny teams，stack 三層 readiness | [notes](./07-it-2030-reinvent-it-for-ai-age/notes.md) |
| 08 | Leading EA in 2026: A Guide for AI-Enabled Transformation | Lucas Kobat | Head of EA・身份危機，五 imperatives，搶 AI 領導真空 | [notes](./08-leading-ea-ai-transformation/notes.md) |

## Q：想找某個概念在哪幾場出現過？

跨場次標籤索引 — 想找某個概念在哪幾場出現過，從這裡跳。

### Framework / 方法論
- **Value × Feasibility 矩陣**：[01](./01-ai-journey-business-capability-maps/notes.md) (use case 庫 200+) / [02](./02-hr-ai-stop-funding-features/notes.md) (likely wins / calculated risks / marginal gains) / [03](./03-comms-ai-enabled-world/notes.md) (18 個 comms use case) / [05](./05-high-value-ai-use-cases-finops/notes.md) (600+ 分析師打分庫；feasibility 給技術聯隊、value 給業務打)
- **Portfolio 三層分配**：[01](./01-ai-journey-business-capability-maps/notes.md) Defend/Extend/Upend ｜ [02](./02-hr-ai-stop-funding-features/notes.md) Within/Pushing/Breaking ｜ [03](./03-comms-ai-enabled-world/notes.md) Crawl/Walk/Run ｜ [05](./05-high-value-ai-use-cases-finops/notes.md) Defend/Extend/Upend 含預算 cap（10/80/5-15%）與三種管法（cost center / profit center / VC）
- **Funding funnel + litmus test（vet → prioritize → 綁戰略支柱）**：[05](./05-high-value-ai-use-cases-finops/notes.md)
- **POV→POC→pilot 迭代法（每關重算帳，去管理層五次）**：[05](./05-high-value-ai-use-cases-finops/notes.md)
- **Readiness 評估**：[01](./01-ai-journey-business-capability-maps/notes.md) 4 維 + AI 7 維 ｜ [02](./02-hr-ai-stop-funding-features/notes.md) People/Process/Tech/Data 4 維 ｜ [06](./06-procurement-ai-first/notes.md) data readiness 四步（use case pass/fail 盤點）｜ [07](./07-it-2030-reinvent-it-for-ai-age/notes.md) stack 三層（AI → agent → democratization ready）
- **IT 未來態四 archetypes（Lean / Amplified / Democratized / Dual Builder）**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — 不是進化鏈是選擇題，跟 CEO 對齊；現場 poll：democratized 41% 領先
- **轉型速度三檔（cautious / opportunistic / AI-first）**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — cybersecurity 連 cautious 檔都必須自動化
- **Build vs buy 2×2（技術複雜度 × 業務差異化）**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — headless 談判、長約警告；poll：36% somewhat more build
- **EA 五 imperatives（領導真空 / untangle rollout / dynamic arch / 雙帽投資 / 用 AI 重造 EA）**：[08](./08-leading-ea-ai-transformation/notes.md) — 迭代式改良救不了，要 complete reimagination
- **Adaptive governance 四風格（control / outcome / agile / autonomous）**：[08](./08-leading-ea-ai-transformation/notes.md) — agentic 時代靠 autonomous 檔 + guardian agent
- **Dynamic state architecture（不畫終點、即時重構）**：[08](./08-leading-ea-ai-transformation/notes.md) — future state 還沒實現組織已迭代五六輪；sovereignty 風險逼出來的
- **Elevator architect（雜草層 / portfolio / 瞭望塔三層移動）**：[08](./08-leading-ea-ai-transformation/notes.md) — 瞭望塔的價值在敢下剪刀
- **Pace Layer（commodity / keep up / differentiating）**：[01](./01-ai-journey-business-capability-maps/notes.md) — capability 戰略地位三色標記
- **Capability 語言（穩定的分析單位）**：[01](./01-ai-journey-business-capability-maps/notes.md) business capability ｜ [04](./04-workforce-keep-up-with-ai/notes.md) job capability 三層（core/contextual/shared）+ workflow 切 2030 衝擊
- **AI 介入三檔（AI-cautious / task-specific / AI-first）**：[04](./04-workforce-keep-up-with-ai/notes.md) — 同一職位的重設計深度是選擇不是宿命

### Agent / Agentic AI
- **Agency 5 級光譜**：[01](./01-ai-journey-business-capability-maps/notes.md) — Stock follower → Autonomous，Kanban 螺絲容器例
- **Agent 6 維能力**：[01](./01-ai-journey-business-capability-maps/notes.md) — Perception/Decisioning/Actioning/Agency/Adaptability/Knowledge
- **Agent-washing 警告**：[02](./02-hr-ai-stop-funding-features/notes.md) HR 零個 proven high-agency ｜ [03](./03-comms-ai-enabled-world/notes.md) Lenovo 不叫 agentic 是 daisy chain ｜ [06](./06-procurement-ai-first/notes.md) 紅線定義：不靠人類 prompt 行動才算 agent
- **Multi-agent 解剖（orchestrator + sub-agents）**：[06](./06-procurement-ai-first/notes.md) — orchestrator 不做事，做釐清需求與調度；agent 要進 org chart
- **Human-in-the-loop 是設計選擇**：[01](./01-ai-journey-business-capability-maps/notes.md) / [02](./02-hr-ai-stop-funding-features/notes.md) / [03](./03-comms-ai-enabled-world/notes.md) / [04](./04-workforce-keep-up-with-ai/notes.md) / [06](./06-procurement-ai-first/notes.md) — 04 補「訊號線斜率是設計決策」；06 補「人機接力傳棒、人放在判斷結果的位置」

### ROI / Metrics / 對 CFO 講話
- **Baseline + Attribution**：[01](./01-ai-journey-business-capability-maps/notes.md) / [02](./02-hr-ai-stop-funding-features/notes.md) — 沒 control group 無法歸因
- **Vendor benchmark 必須 contextualized**：[02](./02-hr-ai-stop-funding-features/notes.md)
- **Break-even 看 portfolio 不看單案**：[02](./02-hr-ai-stop-funding-features/notes.md)
- **Value Realization Dashboard**：[02](./02-hr-ai-stop-funding-features/notes.md) — 季度 cadence 對 CEO/CFO
- **Blue money vs green money（time saved ≠ money saved）**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 1,600 人平線；green 只來自改流程
- **Marginal cost to deliver 是 green money 門檻**：[05](./05-high-value-ai-use-cases-finops/notes.md) — KYC 例：裁人不動邊際成本就不算省
- **Return on employee / ROI / return on future**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 三桶各有價值語言，別用 ROI 量全部
- **Narrative Health / Trust Barometer**：[03](./03-comms-ai-enabled-world/notes.md) — 取代 reach/impression
- **Risk mitigation value（避免 crisis）**：[03](./03-comms-ai-enabled-world/notes.md)

### Vendor 篩選
- **「How do I know it's NOT working?」**：[02](./02-hr-ai-stop-funding-features/notes.md) — 簽 vendor 前必問
- **Temperature setting 隱藏控制器**：[02](./02-hr-ai-stop-funding-features/notes.md) / [03](./03-comms-ai-enabled-world/notes.md)
- **Build / Buy / Blend**：[02](./02-hr-ai-stop-funding-features/notes.md) HR 視角 ｜ [03](./03-comms-ai-enabled-world/notes.md) Comms 視角 ｜ [05](./05-high-value-ai-use-cases-finops/notes.md) 用戶數過門檻 build 勝 buy（15 use case 模板各有 buy/build tab）｜ [06](./06-procurement-ai-first/notes.md) 判準＝competitive differentiation（差異化→build、效率→buy）
- **Vendor 一年改三四次價格 schema**：[05](./05-high-value-ai-use-cases-finops/notes.md) — vendor 自己沒獲利在找 break-even；procurement 要入打分團隊
- **打分 audit trail 進合約**：[05](./05-high-value-ai-use-cases-finops/notes.md) — vendor 不服低分，就把標準寫進條款

### Talent / Change Management
- **AI Adoption Triad（Skills + Motivation + Ease of Use）**：[02](./02-hr-ai-stop-funding-features/notes.md) — 取代失效的 ADKAR
- **Toolmate 思維**：[03](./03-comms-ai-enabled-world/notes.md) — AI 不是 replacement 是 collaborator ｜ [08](./08-leading-ea-ai-transformation/notes.md) AI 當 toolmate 陪分散的交付團隊
- **Assurance by partnership（陪跑取代文件審查）**：[08](./08-leading-ea-ai-transformation/notes.md) — design-first 失效，別要 75 頁文件
- **AI 不是 silver bullet（判斷與同理心編不進 code）**：[08](./08-leading-ea-ai-transformation/notes.md) — 跟 04 human foundation 同構；AI 只 scale decision support 不取代 decision
- **Pyramid → Diamond pipeline**：[03](./03-comms-ai-enabled-world/notes.md) — entry-level 變少、mid 變多 ｜ [07](./07-it-2030-reinvent-it-for-ai-age/notes.md) tiny teams 把底層擠窄，IT 整體確認同一幾何
- **Tiny teams（pattern → 平台 → 到處套用）**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — AI 沒有 clear end state，大 program team 失效；agents about process not product
- **Red-line role description**：[03](./03-comms-ai-enabled-world/notes.md) — 跟 team 一起做
- **Writing 退場 / Storytelling 上場**：[03](./03-comms-ai-enabled-world/notes.md) ｜ [04](./04-workforce-keep-up-with-ai/notes.md) data storytelling 列 risky-to-lose
- **Capacity 三訊號 + unplanned work（AI slop、escalation 信任）**：[04](./04-workforce-keep-up-with-ai/notes.md) — capacity 是設計出來的不是省出來的
- **情緒適應曲線（跌是物理、回升是工程）**：[04](./04-workforce-keep-up-with-ai/notes.md)
- **Skills atrophy 洋蔥（risky vs acceptable）**：[04](./04-workforce-keep-up-with-ai/notes.md) — 判準：會不會削弱挑戰 AI 的能力
- **Archetype 換軌（SOC analyst → D&A compliance champion）**：[04](./04-workforce-keep-up-with-ai/notes.md)
- **Junior talent 法律業 associate 模式（僱學習能力）**：[04](./04-workforce-keep-up-with-ai/notes.md) — entry-level 不消失但 ramp 變陡 ｜ [06](./06-procurement-ai-first/notes.md) Da Vinci 案例：保護練判斷的活動，明知 AI 能做也不給
- **Pattern vs judgment 兩桶工作**：[06](./06-procurement-ai-first/notes.md) — AI 只拿得走「數學已定義」的工作；04 工作四分法的姊妹版
- **Mentorship 斷層（senior 選 AI 不選 junior）**：[06](./06-procurement-ai-first/notes.md) — 「Who are you going to pick?」
- **工作總量會增加不會減少（ideas→actions 距離縮短）**：[06](./06-procurement-ai-first/notes.md) — 對沖裁員敘事的論證
- **Role redesign 四步（生產力從個人搬到企業）**：[06](./06-procurement-ai-first/notes.md) — productivity trapped in individual role design

### 失敗模式 / 警告
- **60% AI 計畫 2027 會 fail**：[01](./01-ai-journey-business-capability-maps/notes.md) — change management 是主因
- **95% HR AI 沒拿到 value**：[02](./02-hr-ai-stop-funding-features/notes.md) — 治理問題不是技術問題
- **半數 CCO 說 Gen AI 沒達期待**：[03](./03-comms-ai-enabled-world/notes.md) — 卡在 efficiency trap
- **隱藏流程詛咒**：[02](./02-hr-ai-stop-funding-features/notes.md) — 兩個人的 Excel 撐起整個 AI 案
- **Future state 通常被 overestimate**：[01](./01-ai-journey-business-capability-maps/notes.md)
- **Level 1 Fully Autonomous 是科幻**：[01](./01-ai-journey-business-capability-maps/notes.md)
- **1.4M 筆裁員資料 <1% 是 AI productivity**：[04](./04-workforce-keep-up-with-ai/notes.md) — chaos 不是 substitution
- **60% 企業沒有 skills atrophy 策略**：[04](./04-workforce-keep-up-with-ai/notes.md)
- **一次 escalation 抹掉整批 AI 收益**：[04](./04-workforce-keep-up-with-ai/notes.md) — elimination 式流程改造的代價
- **「AI 能做什麼、人類撿剩下的」是危險的提問順序**：[04](./04-workforce-keep-up-with-ai/notes.md) — 人類變殘差項，18 個月重算一次
- **只有 11% CFO 量得出 AI ROI、>80% 客戶投了沒拿到價值**：[05](./05-high-value-ai-use-cases-finops/notes.md) — AI value gap
- **POC purgatory：>60% POC 沒進 production**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 缺 no-go 機制的下場
- **算了成本沒算價值就 fund**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 2025 集體通病；value 評估要在 fund 之前
- **Tribal knowledge 是隱形負債**：[06](./06-procurement-ai-first/notes.md) — 沒寫下來的決策邏輯＝部署不了的 use case；2027 只有 20% 組織夠格玩 multi-agent
- **想用 agent 拯救爛流程**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — 「Ironically, agents work best when the process has clarity and the data is clean」；例外太多 → hard code → 報酬遞減
- **IT 外建造的技術沒人規劃**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — democratized 41% 領先但 dangerously underinvesting；97% 某程度接受 democratization
- **EA 的身份危機（能不能用 AI 取代 EA）**：[08](./08-leading-ea-ai-transformation/notes.md) — 34% heads of EA 證明不了價值；三群 stakeholder 同時不滿
- **AI sprawl 是技術風險**：[08](./08-leading-ea-ai-transformation/notes.md) — 多數 CEO 三年內要 autonomous systems；EA 要當 source of truth 判「需不需要 AI」
- **官方文案 vs 實際內容落差**：[06](./06-procurement-ai-first/notes.md) — 宣稱 5 predictions 實講 3，multitier transparency 沒出現

### 案例
- **Lenovo daisy chain 8 週→幾秒**：[03](./03-comms-ai-enabled-world/notes.md)
- **Hitachi Energy 自建 LLM 平台**：[03](./03-comms-ai-enabled-world/notes.md)
- **製造業夜班 virtual coach 救庫存（每位 manager 省 $10K）**：[02](./02-hr-ai-stop-funding-features/notes.md)
- **TA 自動化省下兩個 scheduler 全職**：[02](./02-hr-ai-stop-funding-features/notes.md)
- **醫療產品公司 walk 階段省 $6.5M agency spend**：[03](./03-comms-ai-enabled-world/notes.md)
- **98% 準確率模型沒讓 attrition 動 2%**：[04](./04-workforce-keep-up-with-ai/notes.md) — 考核座標從模型品質換成 business outcome
- **週末 prototype、三個月上 production**：[04](./04-workforce-keep-up-with-ai/notes.md) — 瓶頸在協作介面不在建模
- **Claude Code 派 vs 架構派（5-6 世代同場）**：[04](./04-workforce-keep-up-with-ai/notes.md) — Soyeb 教學現場觀察
- **「I'm going to bend that value line」**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 透明地選擇不回本的投資
- **Level 1 support 幾百人 → <10 人；特定 infra ops 成本 -75%**：[05](./05-high-value-ai-use-cases-finops/notes.md) — I&O 占 CIO 預算 ~70%
- **銀行 KYC 幾千人、500+ 步**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 裁人不一定變 green money
- **物流 last mile +20% 準時 / DIY 零售 +10% 營收 / 醫院急診等待時間**：[05](./05-high-value-ai-use-cases-finops/notes.md) — 三種記分板
- **Da Vinci 手術機器人 vs 住院醫師 pipeline**：[06](./06-procurement-ai-first/notes.md) — 明知機器人能開刀也不讓，人要練判斷
- **兩個 AI 互相談判 → 動態合約**：[06](./06-procurement-ai-first/notes.md) — negotiation 列下降技能的理由
- **Token economics：爛資料貴到不如僱人**：[06](./06-procurement-ai-first/notes.md) — 標準化是 AI 的折扣券
- **銀行 CIO 的數億美元支票（Claude Code 自建 + 開源 vs 續約大 vendor）**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — vendor 對華爾街宣稱 20-30% 效率但帳單沒降
- **Payroll email agent → pattern → 平台**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — tiny team 轉型標準動作
- **UI 層整個送給業務「knock yourself out」**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — agent 把自動化的線往 workflow 層推
- **Vendor management 八個月改 rating-based**：[07](./07-it-2030-reinvent-it-for-ai-age/notes.md) — department of no 的翻身訊號
- **CIO 親口「你現在是我們的 venture capitalist」**：[08](./08-leading-ea-ai-transformation/notes.md) — EA 雙帽角色的真人版；呼應 05 Upend 當 VC 管
- **EA repository + AI assistant 消滅重複問答**：[08](./08-leading-ea-ai-transformation/notes.md) — scale decision support 的最小 quick win
- **EA 工作 AI 化 14%→23%→30%**：[08](./08-leading-ea-ai-transformation/notes.md) — 不自我重造就變回路障

## Q：01–03 為什麼常被綁在一起？
它們是 CIO / CHRO / CCO 三場，**共用同一套 Gartner framework、只換 C-suite 外衣**。跨場對照（同一個 thesis、Value×Feasibility、portfolio 三層、readiness、agent 警告）整理在 [`01-03-cross-synthesis.md`](./01-03-cross-synthesis.md)。

## Q：什麼是 BCM？怎麼自己做一張？
- **概念**：01 場 [`notes.md`](./01-ai-journey-business-capability-maps/notes.md)，含四副讀法眼鏡（視角／高度相對／底圖vs疊加層／單位純度）。
- **怎麼做**：[`bcm/bcm-製作重點.md`](./bcm/bcm-製作重點.md) 的 9 步走查。最難的是第 3 步「單位純度」——別把 outcome／process／use case 當能力放進框。

## Q：BCM 畫完之後怎麼用、怎麼養？
它是 ongoing governance backbone，不是畫完存檔的文件。[`bcm/bcm-使用與治理.md`](./bcm/bcm-使用與治理.md) 涵蓋：把 use case 映射上去（AI Opportunity Radar、6 維 agent 能力、Defend/Extend/Upend、技術+資料源+整合）、AI readiness（contextual）、Capability→Value Stream→Process→IT＋Digital Thread、每能力 metadata 卡、把 bottom-up POC 接回 BCM、每季/半年的 update cadence。

## Q：有做好的 BCM 範例嗎？
`bcm/` 累積 19 家**真實公司**，各一份「輸入功課 HTML」＋一張「BCM 圖」。橫跨製造（TSMC、BASF）、品牌零售（L'Oréal、Pandora、The RealReal）、訂閱內容（Netflix、NYT）、平台與遊戲（CMoney、PoE2）、服務代理（We Are Social）、非營利研究法人（工研院 ITRI）、分發基建與廣告分發（Cloudflare、TollBit、The Trade Desk、AppLovin）、內容分發（ByteDance、小紅書、SmartNews、OpusClip）。各家差異化落點不同，方法照各家研究推導、非套版。完整對照表與每家視角見 [`bcm/README.md`](./bcm/README.md)。

## Q：BCM 的「功課」跟「圖」差在哪？為何分開？
- **功課 HTML** = 底圖：穩定事實（戰略目標 + 能力清單，分 value-realizing / value-enabling）。
- **圖 PNG** = 疊加層：pace layer 上色 + AI 釘點——隨戰略視角會變的判斷。

分開是因為 pace／AI 是「疊加層」，不是能力的天生屬性（01 場讀法）。

## Q：這些數字可信嗎？
每份功課底部有「資料註記」，標出口徑、估計值、待補，並附來源清單。**內部欄位（owner／系統／KPI／data readiness）非公開、一律標待補**——只有公司自己填得了。

## Q：怎麼生一張新的 BCM？
用 `bcm-creator` skill（在本機 `~/.claude/skills/`，**不在這個 repo**）：釐清 → 研究 → 功課 HTML（含 polish）→ raster 圖。

## Q：怎麼新增一場 webinar？（給未來的自己）

### 1. 開資料夾

照 `NN-kebab-slug/` 編號連續開：

```
09-<下一場主題的 kebab slug>/
```

### 2. 必備檔案

每個資料夾結構固定：

| 檔名 | 內容 | 是否 commit |
|---|---|---|
| `video.mp4` | 原片 | ❌ gitignored（檔案太大留本地） |
| `transcript.txt` | 純文字逐字稿 | ✅ |
| `transcript.srt` | 帶 timestamp 字幕 | ✅ |
| `transcript.vtt` | WebVTT 字幕 | ✅ |
| `transcript.json` | qwen-asr 原始輸出 | ✅ |
| `notes.md` | take-note skill 產出 | ✅ |
| `source.md` | 來源 URL、講者、官方描述 | ✅ |
| `transcript-readable.md` | 逐字稿可讀版（講者標記＋分段＋ASR 對原音覆核），選配；04 有 | ✅ |

下載+轉錄走 yt-dlp → qwen-asr pipeline，產出已含前 4 個。`notes.md` 走 take-note skill 從 `transcript.txt` 生；想重做就再跑一次 `/take-note`。

### 3. 注釋索引（本檔）

寫完 notes.md 之後，**回到本 README 做三件事**：

1. 「8 場分別在講什麼」表加一列（標題的場數跟著改）
2. 「想找某個概念」標籤頁掃過 — 新場碰到的概念有對應 tag 就加 link，沒有就新開
3. 如有新類型框架 / 警告 / 案例，補進對應 section

### 4. Commit message 風格

照 conventional commits：

```
feat(09-<slug>): add <title> notes + transcripts
```

或新場分兩 commit：

```
chore(09-<slug>): add transcripts (txt/srt/vtt/json)
feat(09-<slug>): add take-note knowledge map
```

---

## 結構

```
.
├── 01-ai-journey-business-capability-maps/   # 01–08：每場 notes.md + transcript + source.md
├── 02-hr-ai-stop-funding-features/
├── …  06, 07
├── 08-leading-ea-ai-transformation/
├── 01-03-cross-synthesis.md    # CIO/CHRO/CCO 三場深度對照
└── bcm/                        # BCM 方法、TSMC/L'Oréal/Pandora 範例、參考範本
```

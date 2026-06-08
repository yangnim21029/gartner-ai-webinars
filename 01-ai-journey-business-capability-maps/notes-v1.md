# Accelerate Your AI Journey With Business Capability Maps

> **來源**：Gartner Webinar，Alexander Hoeppe（VP Analyst，製造業專精，但跨產業適用）
> **涵蓋**：用 Business Capability Map (BCM) 把 AI 投資錨在策略上 — 從 use case 評估到 readiness 評估到 agency spectrum 到 business case 三型態，串成完整 governance pipeline

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| BCM | Business Capability Map，企業能力地圖，列出組織「該做的事」 |
| Capability | 能力，業務「該做或正在做」的事（例：execute production、assess credit risk）|
| Process | 流程，同一個 capability 可以有不同實作（用機器人還是用人）|
| Value-realizing capability | 直接連到 business outcome 的能力（例：增加 CX）|
| Value-enabling capability | 支撐 value-realizing 但不直接產生價值的能力（例：CRM 管理）|
| Pace Layer | Gartner 招牌術語：commodity / keep up / differentiating，標記能力的戰略地位 |
| Value Stream | 把 capabilities 串成有 sequence 的流，補上 BCM 缺少的「順序」 |
| Digital Thread | Value stream 對應到 data flow 跟 IT system landscape 的整條線 |
| AI Opportunity Radar | 把 BCM 跟 use case 映射的視覺化工具 |
| Agency Spectrum | AI 自主度光譜，5 級從 stock follower 到 fully autonomous |
| Machine Customer | 機器自己當買方（例：Kanban 容器自動下單）|
| Defend / Extend / Upend | 三種 AI 業務 case 類型，從增量到顛覆 |
| Bimodal | 同時 top-down 跟 bottom-up，避免單一方向 |
| AGV | Automated Guided Vehicle，自動導引車 |
| Lights-out Factory | 全自動工廠，無人值守 |

---

## 這場 webinar 要回答的事

Alexander Hoeppe 鎖定的問題很具體：CIO / IT leader 投 AI 投了一堆 POC，60% 失敗。原因不在技術，在跟 business outcome 對不齊。三件事：

1. **解釋為什麼 process map 不夠用，BCM 才是 AI 投資的對的單位**
2. **示範怎麼用 BCM + Use Case Assessment + Readiness Assessment + Opportunity Radar 串成一條 AI prioritization pipeline**
3. **教 IT leader 從「我做完了一個 AI POC」進化到「我把 AI 押在三個 business capability 上，KPI 動了 X」**

## 要建立的心智模型

讀之前你可能想：「BCM 是 enterprise architect 玩的東西，跟 AI 沒關係。」讀完要多出來這幾個鉤子：

- **Capability ≠ Process**：能力說「做什麼」、流程說「怎麼做」 — AI 該對齊前者
- **BCM 是 governance 工具不是文檔**：每年 revisit，不是建完就放
- **Use Case 要丟到 value × feasibility quadrant**：每個 use case 都該被分類
- **Agency 是光譜不是開關**：你的 AI 落在 5 級的哪一級，決定風險與價值
- **Defend / Extend / Upend portfolio**：別把所有錢押在同一種 case 類型

下面 ~50 個 H2 把這五個鉤子串起來。

---

## POC 失敗主因是 business misalignment 不是技術

Gartner 自家 survey 數字：AI POC 失敗的 top 4 原因裡有 3 個跟 business 對齊有關 — (1) 部署後才發現還有需求沒收集，(2) 沒辦法展示 ROI 證明值得多投錢，(4) business impact 沒有被證明。**唯一一條不是 business 的是 security**。技術問題反而很少卡死 AI POC。意思很清楚：你的 AI 不是因為模型不夠強而失敗，是因為跟 stakeholder 沒對齊期待跟價值定義。

## 60% AI 計畫 2027 會失敗，主因是 change management

Gartner 預測：**到 2027 年，60% 的 enterprise AI initiative 會 fail to achieve expected outcomes，主因是 change management 跟 workforce engagement 不足**。注意這條預測 — 不是模型問題、不是預算問題，是人的問題。AI 不是 IT 部門部署完就算結束，是整個組織要 redesign 工作方式。沒有 business stakeholder 從一開始就 engage，POC 永遠 scale 不上去。

## AI 不是 project，是 journey

Alexander 不斷強調這個 framing：AI 沒有「start date 跟 end date」這種項目邊界。技術一直成熟、use case 一直長出來、組織能力一直升級 — 是一條 continuous 的旅程。**如果你用 project 管理方法治理 AI（一次性預算、結案報告），你會在每個版本之間斷掉**。需要 ongoing governance，而 BCM 正是這條 journey 的地圖。

## 4 個 readiness 維度：Business、Technology、Process、People

Gartner 把 AI readiness 拆成四維。**Business** 最重要 — 你 align 到 outcome 了嗎？**Technology** — 你有 legacy debt、obsolete equipment、poor data quality 嗎？**Process** — 你的 business process 跟 governance process 都 ready 嗎？**People** — 你有 prompt engineer、AI architect 這些新角色嗎？這四維評完才知道從哪起步。多數 IT leader 只看 technology readiness，跳過其他三維，這也是 POC 失敗的常見原因。

---

## 什麼是 capability？「業務該做的事」

Capability 定義很簡單：**「what businesses do or should do to achieve a business outcome」**。語氣是動作的：execute production、plan merchandise assortment、assess credit risk、operate network infrastructure。注意這幾個例子的特徵 — **跨產業都成立、行動性強、不涉及怎麼做**。一家銀行 200 年前要 assess credit risk，今天也要 assess credit risk，只是「怎麼做」從紙本變 AI。Capability 是不變的骨幹。

## Capability 不重複、不重疊、不常變

跟 process 比，capability 的特性鮮明：(1) **不重複** — 同一條 capability 在組織裡只有一個 owner；(2) **不重疊** — capability 之間邊界清楚；(3) **不常變** — 三五年不大動。這三條讓 BCM 適合當 strategic 對話的單位。Process map 一年改 N 次，沒辦法承載「我們戰略上要押哪幾條 capability」這種 multi-year 對話。

## Process 變很快，capability 不變

Alexander 給的例子：製造業要 execute production 是不變的，但「用 robot 還是用人」「用 AGV 還是用堆高機」「彈性製造還是大規模製造」這些是 process — **demand / supply shift 一發生 process 就改**。如果你用 process map 當 AI 投資的單位，每次重整就要重做 prioritization。用 capability 當單位，一次 prioritization 撐三五年。

## Process Map 太細，BCM 是 strategic conversation 工具

很多客戶會說「我們已經有完整 process map 了，BCM 多此一舉」。Alexander 回應：**「BCM 跟 process map 是兩個工具，不是替代關係」**。Process map 細到看不到森林，需要 EA 級的人才能讀；BCM 一頁紙，CFO / CEO / CIO 都能讀。Strategic decision 需要 BCM 的抽象度，operational excution 需要 process map 的細節。**用錯了工具，對話就死在裡面**。

## C-level 不想看 process map，他們看 BCM

實務經驗：Alexander 跟 CFO、CEO 開過很多次會，他們對 EA 的 process model 一律抱怨「too much detail、too slow、too much effort」。但對 BCM 一頁紙的反應完全不同 — 因為 **BCM 提供「公司業務 end-to-end 視野」**。CFO / CEO 喜歡看大圖、喜歡看 owner 標清楚、喜歡看 strategic priority 標出來。BCM 滿足這三個條件，process map 不能。

---

## BCM 一頁紙結構：objective 在上、capability 在左、scorecard 在下

Gartner 的 BCM 模板長這樣：**頂部** 是 business objectives（成長 / 利潤 / CX 等戰略指標）；**左側** 是 value-realizing capabilities（直接連到 outcome 的能力）；**底部** 是 digital execution scorecard（KPI 階層）；**底層** 是 value-enabling capabilities（支撐前面的基礎能力）。一頁紙就能跟 board 對話「我們戰略押在哪、KPI 怎麼動」。

## Value-realizing vs Value-enabling capability

兩種 capability 角色不一樣。**Value-realizing**：直接 deliver outcome（例：increase customer experience 直接連到 10% revenue 增長）。**Value-enabling**：自己不產生價值，但少了它 value-realizing 跑不起來（例：CRM 系統管理 — 沒它 CX 無法 scale）。**BCM 必須同時 show 這兩層**，不然你會誤把資料中台這種 enabling 投資砍掉，後面整個 stack 倒。

## 10+ 個產業有現成 BCM 模板

Gartner 提供 10+ 個產業（再加 sub-industry 更多）的 standard BCM 模板。你不一定要用它，但可以拿來 **檢查自己的 BCM 有沒有 capability 漏掉**。從零畫一張 BCM 很容易遺漏；從模板出發，刪減客製化，覆蓋率高很多。模板還會標出 industry-typical 的 KPI，可以對照自家的差在哪。

## Level 0 / Level 1 通常夠用

BCM 的層級結構：level 0 是最粗的能力分群（例：「manage operations」），level 1 是具體 capability（例：「execute production」「manage quality」）。**多數 BCM 對話停在 level 1 就夠**，因為再往下就接近 process。能力地圖 ≠ 流程地圖，不要混淆。

## 何時要挖到 level 2 / 3？

什麼時候要拆下去？Alexander 給的判準是 **「當一個 capability 同時支撐多個 business outcome」**。例如「manage talent」可能同時影響 productivity、innovation、retention — 這時要拆 level 2 才知道哪個子能力對哪個 outcome 貢獻多少。**最佳實踐：通常 level 2-3 夠用，超過 level 6 就是在做 process model 不是 capability model**。

## Pace Layer：commodity / keep up / differentiating

BCM 上的 capability 用三種顏色標記戰略地位：**Commodity**（白色）— 沒競爭力的標配，買現成的就好；**Keep up**（中色）— 業界標準，必須維持別落後；**Differentiating**（深色）— 你的競爭優勢，值得 AI 重投資。**Pace layer 顏色決定 AI 投資的優先序**：differentiating 區的 AI 投資 ROI 通常最高，commodity 區用現成 SaaS 即可。

## 不是所有 capability 都要 detailed modeling

如果你有 50 個 level 1 capability，每個都拆 level 2 又有 6-8 個 sub-capability — 馬上就是幾百個 model，工作量爆炸。**Alexander 的鐵則：只對 business-critical 的 capability 做 detailed modeling**。其他先用 high-level 標出來就好。把建模工作集中在戰略性 capability 上，避免變成 paperwork project。

---

## 從 BCM 接到 Use Case：Gartner 200+ Use Case Assessment

Gartner 維護一個 use case 庫，超過 200 個 AI use case maturity assessment，橫跨各產業。每個 use case 都被評估在 **value × feasibility quadrant** 上。**Value**：對 broader business objective 的貢獻；**Feasibility**：technical feasibility + internal maturity。這給你一個 starting point，不用從零自己 build。

## 預測性維護 = 經典 high value + high feasibility

製造業最 textbook 的 example：**predictive maintenance** 落在 quadrant 右上角。Vendor 有 mature 標準解決方案，asset-intensive industry 有大量 case study（能源、製造、運輸、礦業）。意思是：**從 Gartner 的視角它是 likely win，但對你來說不一定 — 取決於你的 technical debt 多深、equipment 多舊**。Gartner quadrant 給的是「general 視角」，自家還要做 contextualization。

## Direct-impact 跟 Enabling use case 要分開排

每個 use case 都被標成兩類：**direct-impact**（直接 deliver outcome，例：predictive maintenance）跟 **enabling**（不直接但支撐其他 use case，例：industrial data management）。一個常犯的錯：把 enabling use case 跟 direct-impact 放同一個優先級排隊。Alexander 強調 **enabling 必須先做，否則 direct-impact 沒地基**。

## Logical Dependencies：industrial data management 必須先做

具體例子：你想做 predictive maintenance，但 industrial data 沒清洗、沒打通、沒 metadata，predictive 跑不起來。所以即使 predictive maintenance 是 high value，**logical sequence 上 industrial data management 必須先做**。Use case roadmap 不只是 prioritize value 跟 feasibility，還要 prioritize **依賴關係**。這條常常被忽略，結果一堆 use case 同時開卻沒一個能 deliver。

## AI Readiness 7 維度評估

選好 use case 後，要評 readiness — Gartner 有 7 維度評估工具：**Strategy、Value、Organization、People & Culture、Governance、AI Engineering、AI Data**。每維度從 1-5 分。**重點不是當前分數高低，是 current vs future 的 gap**。Gap 越大要做的功越多。多數組織誤以為 readiness 是「人才 / 資料兩個維度」，忽略 strategy 跟 governance — 這就是後期 scale 不出去的主因。

## Current vs Future State — Gap Analysis

具體做法：對每個 capability 做兩次評分 — **current state**（今天的成熟度）跟 **future state**（兩三年後要達到的）。中間的差距就是「要 close 的工作量」。Alexander 提醒：**future state 通常被 overestimate** — 「兩年達成 lights-out factory」這種目標不切實際。一個都沒有產業案例的目標，你不會是第一個。

## AI Opportunity Radar：BCM 跟 use case 映射

當你有 BCM + Use case quadrant + Readiness assessment，下一個工具是 **AI Opportunity Radar** — 把所有 use case 在 BCM 上的位置畫出來。Radar 切成四象限：**Core capability**（內部營運）、**Back office**（enabling）、**Product & services**（產品創新）、**Front office**（客戶接觸）。看一眼就知道你的 AI 投資集中在哪、忽略了哪。

---

## AI Ambition Patterns

不同產業有不同 ambition pattern。Alexander 觀察：(1) **Productivity-first** — 集中在 core / internal operations / supply chain（典型製造業）；(2) **Customer-first** — 集中在 front office（零售業、銀行常見）；(3) **Product-innovation-first** — 集中在 product & services（高科技、藥廠）。**沒對錯，但 ambition 不同決定你 BCM 上的 pace layer 顏色該打在哪**。

## 同個 BCM 模板，不同產業 ambition 不同

兩家用 Gartner 同一個 BCM 模板的公司，可以選完全不同的 differentiation 區。一家製造業可能 differentiating 全集中在 production execution / quality；一家消費品公司可能集中在 brand / customer insight / pricing。**BCM 是 framework，不是策略 — 策略決定你把顏色打在哪些 box 上**。

---

## 不是每個 use case 都要 Generative AI

Alexander 直接打臉一個 common mistake：「我們要做 AI，所以每個 use case 都要用 Gen AI」。**錯**。Gartner 維護的 use case 跟 AI 技術 mapping table 顯示：很多 use case 用 traditional ML、optimization algorithm、rule-based system 就夠了，Gen AI 反而是 overkill。**選錯技術不只是浪費錢，還會把 deterministic 流程灌入 probabilistic 行為**。

## 6 維 AI Agent Capability

Gartner 評估 AI agent 的 6 個能力維度：**Perception**（看 / 聽 / 讀）、**Decisioning**（決策）、**Actioning**（執行）、**Agency**（自主度）、**Adaptability**（適應）、**Knowledge**（知識存取）。一個 agent 不一定 6 維都高 — 多數 use case 只需要其中 2-3 維強。**用這 6 維評 vendor 的 agent，比聽他們講「我們有 agentic AI」可靠十倍**。

## Human-in-the-loop 不是退讓，是設計選擇

很多 PM 把 human-in-the-loop 看成「自動化沒做完的補丁」。Alexander 反駁：**human in the loop 是 deliberate design**。有些 use case 需要 adaptability、需要 ethical judgment、需要 escalation，這時候人在 loop 裡不是 weakness 而是 strength。**追求 maximum automation 是錯的目標**，正確的目標是 maximum value，而 value 有時候要由人補上。

## 5 級 Agency：Stock Follower 到 Autonomous

Gartner 把 agency 切成 5 級。**Level 5：Stock follower** — 你開系統看 report；**Level 4：Emerging** — 你掃條碼，系統給你 detail；**Level 3：Basic** — 系統提供洞察，人決定（例：庫存 20% 警示）；**Level 2：Assistive** — 機器跟人協作；**Level 1：Autonomous** — 機器自己決定自己執行。**多數企業實際運作在 Level 3-4，Level 1 在多數產業是 science fiction**。

## Kanban 螺絲容器例子貫穿五級

Alexander 用一個鮮活例子貫穿五級。**Level 5**：你打開 WMS 看「螺絲還剩多少」；**Level 4**：你掃條碼，系統說「庫存 87 個」；**Level 3**：感測器測到 20% 警示提示你補貨；**Level 2**：機器建議補貨量，你確認；**Level 1**：Kanban 容器自己下單給供應商（這就是 **machine customer** — 機器自己當買方）。一個簡單的庫存問題，五級 agency 都能跑。

## Level 1 Fully Autonomous 多數產業是 science fiction

Alexander 明確警告：**「Level 1 fully autonomous, ignoring humans」在多數產業是科幻**。為什麼？因為 end-to-end value chain 太複雜，任何一個自動決策出錯都會擴散。在「selective process」可以做 Level 1（例：機械手臂單一動作），但 end-to-end value chain 不可能。所以當 vendor 跟你 pitch「fully autonomous AI agent」，那是 demo 不是現實。

## 多數公司停在 Level 3 / Level 4，這是合理的

不要因為「停在 Level 3」覺得 AI 投資失敗。**Level 3 已經是 significant 的進步** — 從 reactive 變 proactive，從 manual reporting 變 system suggestion。從 Level 5 跳 Level 3 比從 Level 3 跳 Level 1 容易得多，ROI 也好算得多。**追求合理的 agency 級別 > 追求最高 agency**。

---

## Business Case 三型態：Defend / Extend / Upend

Alexander 把 AI business case 分三型。**Defend**：incremental，augment 員工生產力，ROI 預測穩、return on employee 好算（例：軟體開發 AI 助手）。**Extend**：classical ROI，process transformation，vendor 有 packaged solution（例：customer service automation）。**Upend**：future investment，high uncertainty + high upside（例：drug discovery、新材料設計）。

## Defend：穩、可預測、好算

Defend 的特徵：用 AI **augment** 既有員工的工作，不改流程結構。例：開發人員用 AI 寫 code、HR 用 AI 寫 JD、行銷用 AI 寫文案。**算 ROI 很容易 — 每人每月省 X 小時 × Y 美金 = 多少現金流回**。風險低，但天花板也低。多數企業從 Defend 起步，這是對的入門路徑。

## Extend：有 vendor packaged solution，ROI 清楚

Extend 的特徵：**改寫 process 而不只是 augment**。Customer service 從 ticketing 改成 AI agent + human escalation；保險 claims 從 manual review 改成 AI auto-approval + exception path。**因為有 vendor packaged solution + customer case study，business case 算得出來**。Extend 是大多數 enterprise 的「主戰場」，投資集中在這型最容易看到 ROI。

## Upend：高風險高回報，藥廠級

Upend 是 frontier — **連 value 本身存不存在都不確定**。Alexander 舉藥物開發為例：用 AI 發現新分子、新配方、新療法。一個成功的 drug discovery 可能值幾十億，但 80% 的嘗試會失敗。**Upend 投資需要極長的 patience capital + 對失敗的容忍度**。不是每家公司都該做 Upend，但完全不做 Upend 的公司沒有 future advantage。

## 三型態的風險與報酬比

組合視角：**Defend 報酬低風險低，Extend 中等，Upend 高報酬高風險**。健康的 AI 投資 portfolio 通常是 70% Defend+Extend / 20% Pushing / 10% Upend。**完全集中在 Defend 的組織沒未來，完全集中在 Upend 的組織燒錢，找平衡**。這跟 HR webinar 提的 Within / Pushing / Breaking boundaries portfolio 是一樣的思維框架。

---

## 恍然大悟一：AI 投資的 unit 不是 use case，是 capability

走到這裡你應該感覺到了：**Gartner 整個 framework 都在做一件事 — 把 AI 投資的單位從「use case」拉高到「capability」**。Use case 來來去去（vendor 一直推新功能），但 capability 是組織的骨幹。對著 capability 投資，三年後還在；對著 use case 投資，半年就 obsolete。**BCM 不是 EA 的玩具，是 AI 治理的對的單位**。

---

## BCM 是 Lego Brick，沒順序

但 BCM 有個天生限制：**它列了 capability 但沒講順序**。像一盒 Lego brick — 你有紅藍綠的方塊但不知道哪個先哪個後。在 strategic 對話這沒問題，但要 operationalize 就需要補上 sequence。這就是下一個工具 — Value Stream — 出場的原因。

## Value Stream 補上 Sequence 跟 KPI Relationship

**Value Stream** 是把 capability 串成「為了 deliver X outcome，要依序通過 A → B → C」的流。每個 capability 在 stream 上有 KPI、有 input、有 output、有 dependency。Value stream 通常從 BCM level 2-3 出發，因為 level 1 太抽象不適合做 sequencing。**BCM 是 box，value stream 是 arrow**。

## Process 再往下接到 IT System Landscape

Capability → Value stream → Process → IT system 是一條完整的精緻 chain。Process 是「在這條 value stream 上，這條 capability 具體怎麼跑」。Process 再往下對應到具體的 application、data source、integration。這條 chain 越往下越細，但每一層都對齊上一層。**這就是為什麼 BCM 要先做好 — 後面所有層都掛在它上面**。

## Digital Thread：Value Stream 對應到 Data Flow

Alexander 提到一個 emerging concept — **Digital Thread**：把 value stream 跟 data flow 對應起來。**每個 capability transition 都伴隨資料的轉換跟移動**。可以從 BCM 一路往下看到「客戶下單這條 value stream 觸發了哪些資料表更新、哪些 system call、哪些 ML model 預測」。Digital thread 是 enterprise 的神經系統。

## 每個 Capability 有 Metadata：Input、Output、Owner、Support System

BCM 不只是 box 跟箭頭。**每個 capability 底下有一張 metadata 卡片**：data input、data output、supporting systems、responsible owner、definition。**這張卡片才是 governance 的 unit**。沒填 metadata 的 BCM 是裝飾品，填了 metadata 的 BCM 才能 drive 投資決策、責任歸屬、跨部門溝通。

## Data Readiness 評估獨立於資料乾淨度

Data readiness 不是「資料有沒有 100% 乾淨」。Alexander 說的更精準：**「每個 capability 對 data 的需求是什麼？我們的 data 結構支援這個需求嗎？」** 5 級評估：1 級 = 完全沒結構；5 級 = 結構完整、metadata 齊全、real-time 可用。同一份資料對 A capability 可能是 5 級，對 B capability 可能是 2 級 — readiness 是 contextual 的。

---

## Governance：BCM 是 Ongoing Tool 不是 One-time 文檔

最常見的失敗模式：**BCM 一次性建完，存到 SharePoint，然後三年沒人看**。Alexander 強調 BCM 是 **ongoing governance tool**。每半年或每年要 revisit：哪些 capability 的 pace layer 變了？哪些 use case 進入 likely win？哪些 readiness gap closed 了？BCM 動，AI 投資 portfolio 才跟著動。**沒 cadence 的 BCM 就是一張死掉的圖**。

## Future Vision 通常太樂觀

Alexander 重複強調：**多數組織把 future vision 寫得太樂觀**。「兩年內 lights-out factory」「明年完全 AI-driven recruiting」這種目標沒有 industry case study 支撐。**Realistic future vision 是基於 case examples 推算的，不是基於 ambition 拍腦袋的**。如果 Gartner 找不到任何案例證明你的 future vision 可行，那它不是 vision，是幻覺。

## Bimodal：Top-down Strategy + Bottom-up POC

完整的 AI 推進需要 **bimodal approach**：**Top-down** — BCM、Use case prioritization、Readiness assessment 都是 strategic 動作，由 leadership 帶動；**Bottom-up** — POC、prototype、end-user pilot 都是 operational 動作，由 team 親手做。兩條同時跑才能讓 use case 有 strategic 對齊（top-down）又有真實 user 驗證（bottom-up）。**只走 top-down 就是 PPT 治理；只走 bottom-up 就是無頭蒼蠅**。

## POC 為什麼失敗 — 沒持續 Track Performance

回到開場那條 60% 失敗的數字。Alexander 的解釋：**POC 失敗主因不是 POC 本身做不出來，是上線後沒持續 track**。BCM 的角色在這裡再次浮現 — 它讓你知道每個 AI 投資對應哪條 capability、要動哪個 KPI、由誰負責。沒 BCM 當 governance backbone，POC 一上線就被遺忘，三個月後沒人記得當初 KPI 訂在哪。

---

## Bonus：Pace Layer 可以同一個 Capability 在不同 Objective 下不同

Q&A 段一個有意思的細節：**同一個 capability 對不同 business objective 可能是不同 pace layer**。例如「manage talent」對「成長」可能是 differentiating，對「成本控制」可能是 keep up。所以 BCM 的 pace layer 標記其實是個 matrix（capability × objective）不是單一向量。**如果你發現一個 capability 有多重 pace layer 角色，這是訊號要拆到 level 2**。

## AI 跟 Business Strategy 必須對齊

被問到「AI 是不是只是 resource」，Alexander 回答更深：**很多公司有 business strategy、IT strategy、data strategy，但沒有 AI strategy**。AI strategy 不是 IT strategy 的子集，因為 AI 對 business model 跟 operating model 的影響太深，需要獨立規劃。**沒 AI strategy 的公司會失去競爭力，但有 bad AI strategy 的公司會直接受傷**（合規、信任、客戶體驗）。

## Eye on Innovation Award：Gartner 收集成功案例

Gartner 有個 **Eye on Innovation Award**，收集各產業真實的 AI 成功案例。對 Gartner 客戶跟非客戶都開放。**為什麼這個有用 — 因為案例越多，benchmark 越精準，未來 use case prioritization 越可信**。如果你的組織有成功 AI deployment，提名也是分享 — 你會拿到別人的 case 來對照自家做法。

---

## 恍然大悟二：BCM 把 AI 從「IT 部門的 PoC」拉回「全公司的策略治理」

整場 webinar 串起來其實是一個 reframe — **AI 不是 IT 的事，是 enterprise 的事**。但要讓 AI 變成 enterprise 級對話，你需要一個 stakeholder 都看得懂的對話單位。Process map 太細、product roadmap 太窄、project plan 太短 — 只有 BCM 同時滿足「夠抽象 C-level 看得懂」「夠具體可以 attach 投資」「夠穩定 multi-year 對話」。

BCM 不是要取代你既有的工具，是把它們**串起來的那條線**。沒這條線，你的 AI 投資永遠是孤島 POC 的合集；有這條線，你的 AI 投資是組織能力的 compound growth。

整場 webinar 真正在賣的不是 BCM 模板，是「AI 治理需要 enterprise 級對話單位」這個觀念。

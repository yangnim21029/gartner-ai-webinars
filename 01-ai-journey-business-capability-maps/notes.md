# Accelerate Your AI Journey With Business Capability Maps

> **來源**：Gartner Webinar, Alexander Hope（VP Analyst，製造業出身，跨產業適用）
> **涵蓋**：用 Business Capability Map (BCM) 把 AI 投資從「挑 use case」拉成「治理 capability」，串起 use case 評估、readiness 評估、agency 光譜、business case 三型態的完整 pipeline

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| BCM | Business Capability Map，把組織該做的事畫成一頁地圖 |
| Capability | 業務該做或正在做的事（execute production、assess credit risk）— 講「做什麼」 |
| Process | 流程，同一個 capability 可以有不同實作 — 講「怎麼做」 |
| Value-realizing | 直接連到 business outcome 的能力（例：增加 CX 直接連到 revenue）|
| Value-enabling | 自己不產生價值但支撐 value-realizing 跑得起來的能力（例：CRM 管理）|
| Pace Layer | commodity / keep up / differentiating 三色標記 capability 的戰略地位 |
| Value Stream | 把 capability 串成有 sequence 的流，補上 BCM 沒有的順序 |
| Digital Thread | Value stream 對應到 data flow 跟系統 landscape 的整條線 |
| AI Opportunity Radar | 把 BCM 跟 use case 映射的視覺化工具 |
| Agency Spectrum | AI 自主度的 5 級光譜，從 stock follower 到 fully autonomous |
| Machine Customer | 機器自己當買方（Kanban 容器自動下單）|
| Defend / Extend / Upend | 三種 AI business case 類型，從增量到顛覆 |
| Bimodal | 同時跑 top-down 戰略跟 bottom-up POC 兩條 |
| AGV | Automated Guided Vehicle，自動導引車 |
| Lights-out Factory | 全自動工廠，無人值守 |

---

## 這場 webinar 要做的事

Alexander 鎖定 CIO / IT leader 一個很具體的痛：AI POC 砸了一堆，60% 失敗，原因不在模型強度也不在預算。他要交付三件事：

1. **解釋為什麼 process map 不夠用、BCM 才是 AI 投資的對的對話單位**
2. **示範 BCM → Use Case Assessment → Readiness → Opportunity Radar 怎麼串成一條 AI prioritization pipeline**
3. **把 IT leader 從「做完一個 POC」升級成「押注 N 個 capability，每個 KPI 動了 X」**

## 要建立的心智模型

讀完這篇你要建立 5 個認知：

1. POC 失敗 90% 是 business 對齊問題，不是技術問題
2. Capability 跟 process 是兩個工具不是替代關係 — 一個講「做什麼」一個講「怎麼做」
3. Use case 該被丟到 value × feasibility 二維圖才能排序，不能憑印象做
4. Agency 是 5 級光譜不是「自動或手動」的開關，Level 1 在多數產業是科幻
5. AI 投資該長成 Defend / Extend / Upend 的 portfolio，不是押單一型態

下面 ~55 個 H2 就是把這幾點拆開填滿。

---

## POC 失敗的主因都跟 business 對齊有關

Gartner survey 直接打臉一個常見假設：AI POC 失敗 top 4 原因裡，**三個跟 business 對齊有關**。第一是「部署後才發現還有需求沒收集」— 也就是當初 IT 自己跑沒拉 business 進來；第二是「無法 demonstrate ROI 證明值得加碼」；第四是「business impact 沒被證明」。唯一一條不是 business 的是 security。意思很硬：你的 AI 不是因為模型不夠強而停在 POC，是因為跟 business stakeholder 沒對齊期待跟價值定義。

## 60% AI 計畫到 2027 會 fail，敗在 change management

接著 Gartner 把這條 survey 推到預測：到 2027 年，**60% 的 enterprise AI initiative 會 fail to achieve expected outcomes**，主因是 change management 跟 workforce engagement 不足。注意這條跟前面那條同源 — 都不是技術問題、不是預算問題，是人沒被帶進來。AI 不是 IT 部門部署完就結束，是整個組織要 redesign 工作方式。沒有 business stakeholder 從一開始 engage，POC 永遠 scale 不上去。

## AI 不是 project 是 journey，所以治理方式得換

Alexander 反覆強調這個 framing：AI 沒有「start date 跟 end date」這種項目邊界。技術一直成熟、use case 一直長出來、能力一直升級。如果你用 project 管理（一次性預算、結案報告）治理 AI，每個版本之間就會斷掉。需要的不是 PMO 流程，是 ongoing governance — BCM 之所以是 AI 投資的對的單位，正是因為它跟 AI 一樣是 ongoing 的。

## 4 維 readiness：Business、Technology、Process、People

要起步前先評 readiness。**Business** — 你 align 到 outcome 了嗎？**Technology** — 你有 legacy debt、obsolete equipment、poor data quality 嗎？**Process** — 你的業務流程跟治理流程都 ready 嗎？**People** — 你有 prompt engineer、AI architect 這些新角色嗎？多數 IT leader 只看 Technology 一維就 go，這就是後段 scale 不上去的根因。Business 那一維才是最重要的。

---

## Capability = 業務「該做或正在做的事」

進到主菜。Capability 定義很簡單：**「what businesses do or should do to achieve a business outcome」**。語氣是動詞的：execute production、plan merchandise assortment、assess credit risk、operate network infrastructure。注意這幾個例子的共同特徵 — **跨產業都成立、行動性強、不涉及怎麼做**。一家銀行 200 年前要 assess credit risk，今天也要 assess credit risk，只是「怎麼做」從紙本變 AI。Capability 是不變的骨幹。

## Capability 不重複、不重疊、不常變

Capability 的特性鮮明：**(1) 不重複** — 一條 capability 在組織裡只有一個 owner；**(2) 不重疊** — capability 之間邊界清楚；**(3) 不常變** — 三五年不大動。這三條讓 BCM 適合當 strategic 對話的單位。Process map 一年改 N 次，沒辦法承載「我們戰略上要押哪幾條 capability」這種 multi-year 對話。

## Process 變很快是因為 demand/supply shift 一發生 process 就改

具體對比：製造業要 execute production 是不變的，但「用 robot 還是用人」「用 AGV 還是用堆高機」「彈性製造還是大規模製造」這些是 process。**Demand / supply shift 一發生 process 就改**。如果你用 process map 當 AI 投資的單位，每次重整就要重做 prioritization；用 capability 當單位，一次 prioritization 撐三五年。差別不在工具好壞，差別在你願不願意被市場波動牽著重做 roadmap。

## BCM 跟 process map 是兩個工具不是替代關係

很多客戶會說「我們已經有完整 process map 了，BCM 多此一舉」。Alexander 的回應：**兩個工具同時存在，服務不同對話**。Process map 細到看不到森林，需要 EA 級的人才能讀；BCM 一頁紙，CFO/CEO/CIO 都能讀。Strategic decision 需要 BCM 的抽象度，operational execution 需要 process map 的細節。**用錯工具，對話就死在那個抽象度裡** — 拿 process map 給 CFO 看會被嫌「too much detail」，拿 BCM 給 operations 用會被嫌「沒指引到底怎麼做」。

## C-level 為什麼喜歡 BCM — 一頁紙看完整公司

跟 CFO/CEO 開過很多會的 Alexander 觀察：他們對 process model 的反應一律是「too much detail、too slow、too much effort」。但對 BCM 反應完全不同 — 因為 BCM 提供 **「end-to-end view of the business」**。CFO/CEO 喜歡大圖、喜歡看 owner 標清楚、喜歡看 strategic priority 在哪幾個 box 上。這三條 BCM 都做到，所以 board 級對話會走 BCM。

## BCM 一頁紙的結構：objective 在上、capability 在左、scorecard 在下

具體模板長這樣：**頂部**是 business objectives（成長 / 利潤 / CX 等戰略指標）；**左側**是 value-realizing capabilities；**底部**是 digital execution scorecard（KPI 階層）；**底層**是 value-enabling capabilities。一頁就能跟 board 對話「我們戰略押在哪、KPI 怎麼動」。這個結構刻意做得簡單，是因為要服務的對話本身是抽象的 — 細節留給下層工具。

## Value-realizing 跟 value-enabling 必須同框

兩種 capability 角色不一樣。**Value-realizing**：直接 deliver outcome（例：increase customer experience 直接連到 10% revenue 增長）。**Value-enabling**：自己不產生價值，但少了它 value-realizing 跑不起來（例：CRM 系統管理 — 沒它 CX 沒辦法 scale）。BCM 必須同時 show 這兩層，不然你會誤把資料中台這種 enabling 投資砍掉，後面整個 stack 倒。**砍 enabling 是 BCM 治理最常見的錯**。

## Gartner 有 10+ 產業的 BCM 模板，從這裡出發比較不會漏

Gartner 提供 10+ 個產業（加 sub-industry 更多）的 standard BCM 模板。你不一定要用它，但可以拿來 **檢查自己的 BCM 有沒有 capability 漏掉**。從零畫一張 BCM 很容易遺漏；從模板出發、刪減客製化，覆蓋率高很多。模板還會標出 industry-typical 的 KPI，可以對照自家差在哪。**不從模板開始的代價，是你不知道你不知道什麼**。

## 多數 BCM 對話停在 Level 1 就夠

BCM 有層級結構：level 0 是最粗的能力分群（「manage operations」），level 1 是具體 capability（「execute production」「manage quality」）。多數 BCM 對話停在 level 1 就夠，因為再往下就接近 process。能力地圖 ≠ 流程地圖。如果你 level 1 就有 50 條，每條再拆 level 2 就是幾百個 model — 工作量爆炸，價值卻沒等比成長。

## 何時要挖到 Level 2 或 3：當一個 capability 同時支撐多個 outcome

判準很明確：**當一個 capability 同時影響多個 business outcome，就要拆下去**。例如「manage talent」可能同時影響 productivity、innovation、retention — 這時要拆 level 2 才知道哪個子能力對哪個 outcome 貢獻多少。**Alexander 的鐵則：通常 level 2-3 就夠，超過 level 6 就是在做 process model 不是 capability model**。

## 只對 business-critical 的 capability 做 detailed modeling

如果 level 1 有 50 個、每個都拆 level 2 又有 6-8 個 sub，馬上就幾百個 model，工作量爆炸。**Alexander 的鐵則：只對 business-critical 的 capability 做 detailed modeling**。其他先用 high-level 標出來就好。把建模工作集中在戰略性 capability 上，避免變成 paperwork project — 沒人有時間維護幾百個 model，建完就被遺忘。

## Pace Layer：commodity / keep up / differentiating 決定投資優先序

BCM 上的 capability 用三種顏色標戰略地位：**Commodity**（白色）= 沒競爭力的標配，買現成的就好；**Keep up**（中色）= 業界標準，必須維持別落後；**Differentiating**（深色）= 你的競爭優勢，值得 AI 重投資。**這三色直接決定 AI 投資的優先序**：differentiating 區的 AI 投資 ROI 通常最高，commodity 區用現成 SaaS 即可。沒上 pace layer 的 BCM，所有 capability 看起來一樣重，prioritization 就只能靠誰嗓門大。

## 同一個 capability 對不同 objective 可以是不同 pace layer

Q&A 補了個重要細節：**同一個 capability 對不同 business objective 可能落在不同 pace layer**。例如「manage talent」對「成長」可能是 differentiating，對「成本控制」可能是 keep up。所以 pace layer 標記其實是個 matrix（capability × objective）不是單一向量。**如果你發現一個 capability 有多重 pace layer 角色，這就是訊號要拆到 level 2**，把對不同 objective 的子能力分開來。

---

## 恍然大悟一：AI 投資的對話單位是 capability 不是 use case

走到這裡你應該感覺到了。整個 framework 都在做一件事 — **把 AI 投資的單位從「use case」拉高到「capability」**。Use case 來來去去（vendor 一直推新版本），capability 是組織的骨幹。對著 capability 投資，三年後還在；對著 use case 投資，半年就 obsolete。

這也解釋了為什麼 60% POC 會失敗 — 不是 POC 本身做不出來，是 POC 完成之後沒掛在任何長期治理的鉤子上。三個月後沒人記得當初 KPI 訂在哪，因為 KPI 沒掛在 capability 上。

BCM 是把 use case 釘在組織骨幹上的那根釘子。

---

## Use case 庫：Gartner 200+ 條跨產業 AI use case 評估

接到 use case 層。Gartner 維護一個 use case 庫，**超過 200 條 AI use case maturity assessment**，橫跨各產業。每條都被評估在 **value × feasibility quadrant** 上。**Value**：對 broader business objective 的貢獻；**Feasibility**：技術可行性 + 內部成熟度。這給你一個 starting point，不用從零自己 build。

## 預測性維護是 high value + high feasibility 的 textbook 案例

製造業最 textbook 的範例：**predictive maintenance** 落在 quadrant 右上角。Vendor 有 mature 標準解，asset-intensive industry 有大量 case study（能源、製造、運輸、礦業）。**但這是 Gartner 的視角，不一定是你的視角** — 取決於你的 technical debt 多深、equipment 多舊。Gartner 給的是 general 視角，自家還要做 contextualization。

## Direct-impact 跟 Enabling 兩種 use case 不能放同一個優先級排隊

每條 use case 都被標兩類：**direct-impact**（直接 deliver outcome，例：predictive maintenance）跟 **enabling**（不直接但支撐其他 use case，例：industrial data management）。常犯的錯：**把 enabling 跟 direct-impact 丟同一個 prioritization workshop 排**。結果 enabling 永遠輸給 direct-impact，因為 ROI 看起來小。但 enabling 沒做，direct-impact 沒地基。

## Industrial data management 必須先於 predictive maintenance

具體例子：你想做 predictive maintenance，但 industrial data 沒清洗、沒打通、沒 metadata，predictive 跑不起來。所以 logical sequence 上 **industrial data management 必須先做**。Use case roadmap 不只 prioritize value 跟 feasibility，還要 prioritize **依賴關係**。這條常被忽略，結果一堆 use case 同時開卻沒一個 deliver — 因為大家都在等對方的資料。

## AI Readiness 7 維評估，重點是 gap 不是當前分數

選好 use case 後評 readiness。Gartner 7 維工具：**Strategy、Value、Organization、People & Culture、Governance、AI Engineering、AI Data**。每維 1-5 分。**重點不是當前分數高低，是 current vs future 的 gap**。Gap 越大要做的功越多。多數組織誤以為 readiness 就是「人才 / 資料兩維」，忽略 Strategy 跟 Governance — 這就是後期 scale 不出去的主因。

## Future state 通常被 overestimate

Alexander 警告：**多數組織把 future vision 寫得太樂觀**。「兩年內 lights-out factory」「明年完全 AI-driven recruiting」這種目標沒有 industry case study 支撐。Realistic future vision 是基於 case examples 推算的，不是基於 ambition 拍腦袋的。如果 Gartner 找不到任何案例證明你的 future vision 可行，那它不是 vision，是幻覺。**把 future state 設得越樂觀，gap 看起來越嚇人，但實際是 vision 不切實際，不是組織能力不足**。

## AI Opportunity Radar：BCM × use case 的視覺化

當你有了 BCM + Use case quadrant + Readiness assessment，下一個工具是 **AI Opportunity Radar** — 把所有 use case 在 BCM 上的位置畫出來。Radar 切四象限：**Core capability**（內部營運）、**Back office**（enabling）、**Product & services**（產品創新）、**Front office**（客戶接觸）。**一眼就知道你的 AI 投資集中在哪、忽略了哪**。沒這張圖，prioritization 是個別 use case 排序；有這張圖，能看出組合是不是平衡。

## AI Ambition Pattern：不同產業有不同集中區

不同產業在 Radar 上集中區不同。Alexander 觀察三種：**Productivity-first** — 集中在 core / internal operations / supply chain（典型製造業）；**Customer-first** — 集中在 front office（零售、銀行常見）；**Product-innovation-first** — 集中在 product & services（高科技、藥廠）。**沒對錯，但 ambition 不同決定 BCM 上 pace layer 顏色該打在哪**。同樣一張 BCM 模板，兩家公司可以選完全不同的 differentiation 區。

---

## 不是每個 use case 都要 Generative AI

Alexander 直接打臉一個 common mistake：「我們要做 AI，所以每個 use case 都要用 Gen AI」。**錯**。Gartner 維護的 use case × AI 技術 mapping 顯示：很多 use case 用 traditional ML、optimization algorithm、rule-based system 就夠，Gen AI 反而是 overkill。**選錯技術不只浪費錢，還會把 deterministic 流程灌入 probabilistic 行為** — 結果準確率比舊系統還差，引入新的合規風險。

## AI Agent 的 6 維能力：別聽 vendor 籠統說「我們有 agent」

Gartner 評估 AI agent 的 6 個能力維度：**Perception**（看 / 聽 / 讀）、**Decisioning**（決策）、**Actioning**（執行）、**Agency**（自主度）、**Adaptability**（適應）、**Knowledge**（知識存取）。一個 agent 不一定 6 維都高 — 多數 use case 只需要其中 2-3 維強。**用這 6 維評 vendor 的 agent，比聽他們講「我們有 agentic AI」可靠十倍**。

## Human-in-the-loop 是 deliberate design 不是補丁

很多 PM 把 human-in-the-loop 看成「自動化沒做完的補丁」。Alexander 反駁：**HITL 是 deliberate design**。有些 use case 需要 adaptability、需要 ethical judgment、需要 escalation — 這時人在 loop 裡不是 weakness 而是 strength。**追求 maximum automation 是錯的目標**，正確的目標是 maximum value，而 value 有時候要由人補上。

## 5 級 Agency：Stock Follower → Autonomous

Gartner 把 agency 切 5 級。**Level 5：Stock follower** — 你開系統看 report；**Level 4：Emerging** — 你掃條碼，系統給你 detail；**Level 3：Basic** — 系統提供洞察，人決定（庫存 20% 警示）；**Level 2：Assistive** — 機器跟人協作；**Level 1：Autonomous** — 機器自己決定自己執行。**這 5 級不是好壞排序，是適用情境不同的光譜**。多數企業實際運作在 Level 3-4。

## Kanban 螺絲容器例子貫穿五級

Alexander 用一個鮮活例子貫穿五級。**Level 5**：你打開 WMS 看「螺絲還剩多少」；**Level 4**：你掃條碼，系統說「庫存 87 個」；**Level 3**：感測器測到 20% 警示提示你補貨；**Level 2**：機器建議補貨量，你確認；**Level 1**：Kanban 容器自己下單給供應商（這就是 **machine customer** — 機器自己當買方）。一個簡單的庫存問題，五級 agency 都跑得起來 — 沒有絕對「對」的級別，看你願意把多少決策權交給機器。

## Level 1 Fully Autonomous 多數產業是 science fiction

Alexander 明確警告：**「Level 1 fully autonomous, ignoring humans」在多數產業是科幻**。為什麼？因為 end-to-end value chain 太複雜，任何一個自動決策出錯都會擴散。在「selective process」可以做 Level 1（機械手臂單一動作），但 end-to-end value chain 不可能。所以當 vendor pitch「fully autonomous AI agent」，那是 demo 不是現實。**買 Level 1 等於買幻覺**。

## 多數公司停在 Level 3 / 4 是合理的，不是失敗

不要因為「停在 Level 3」覺得 AI 投資失敗。**Level 3 已經是 significant 的進步** — 從 reactive 變 proactive，從 manual reporting 變 system suggestion。從 Level 5 跳 Level 3 比從 Level 3 跳 Level 1 容易得多，ROI 也好算得多。**追求合理的 agency 級別 > 追求最高 agency**。健康的 AI 治理是知道自己停在哪一級、為什麼停在那、什麼時候該往上跳一級。

## 一個 use case 通常需要多種 AI 技術 + 多種資料源

Alexander 提醒一個 vendor 常隱藏的事實：**一個 use case 從來不是「用一個 AI」做的**。Predictive maintenance 需要時序資料、影像辨識、optimization 排程、可能還要 LLM 寫 report — 中間穿插 ETL、整合多套系統。當 vendor pitch「我們的 AI 解決你的 X」，要追問「需要哪幾種技術 + 哪幾個資料源 + 哪些整合工程」。沒問清楚，POC 跑得起來但 production 跑不動。

---

## Business Case 三型態：Defend / Extend / Upend

Alexander 把 AI business case 分三型。**Defend**：incremental，augment 員工生產力，ROI 預測穩、return on employee 好算（軟體開發 AI 助手）。**Extend**：classical ROI，process transformation，vendor 有 packaged solution（customer service automation）。**Upend**：future investment，high uncertainty + high upside（drug discovery、新材料設計）。**三型風險報酬不同，組合在一起才是健康的 portfolio**。

## Defend：穩、可預測、好算 ROI

Defend 的特徵：用 AI **augment** 既有員工的工作，不改流程結構。例：開發人員用 AI 寫 code、HR 用 AI 寫 JD、行銷用 AI 寫文案。**算 ROI 很容易 — 每人每月省 X 小時 × Y 美金 = 多少現金流回**。風險低，但天花板也低。多數企業從 Defend 起步，這是對的入門路徑 — 先建立 ROI 對話的信用，再去碰更難的。

## Extend：有 packaged solution、ROI 清楚，是主戰場

Extend 的特徵：**改寫 process 而不只是 augment**。Customer service 從 ticketing 改成 AI agent + human escalation；保險 claims 從 manual review 改成 AI auto-approval + exception path。**因為有 vendor packaged solution + customer case study，business case 算得出來**。Extend 是大多數 enterprise 的「主戰場」，投資集中在這型最容易看到 ROI。

## Upend：藥廠級高風險高回報

Upend 是 frontier — **連 value 本身存不存在都不確定**。Alexander 舉藥物開發為例：用 AI 發現新分子、新配方、新療法。一個成功的 drug discovery 可能值幾十億，但 80% 嘗試會失敗。**Upend 需要極長的 patience capital + 對失敗的容忍度**。不是每家公司都該做 Upend，但完全不做 Upend 的公司沒有 future advantage。

## 三型同時跑才健康，全押 Defend 沒未來、全押 Upend 燒錢

組合視角：**Defend 報酬低風險低，Extend 中等，Upend 高報酬高風險**。健康的 AI 投資 portfolio 通常是大比例 Defend + Extend、小比例 Upend。**全押 Defend 三年後沒有差異化，全押 Upend 三年後燒光現金**。組合視角才能讓 AI 投資跟 business strategy 平衡。

---

## 恍然大悟二：BCM 是 ongoing governance backbone 不是 one-time 文檔

最常見的失敗模式：**BCM 一次性建完，存到 SharePoint，三年沒人看**。Alexander 強調 BCM 是 ongoing governance tool。每半年或每年要 revisit — 哪些 capability 的 pace layer 變了？哪些 use case 進入 likely win？哪些 readiness gap closed 了？

為什麼這條重要：因為前面整套 framework（BCM、use case quadrant、readiness、agency、business case 三型）如果只在年度規劃跑一次，那它跟 PPT 沒差。BCM 真正的價值是 **變成組織持續對話的單位** — 季會用它、執行長用它、投資決策用它。

沒 cadence 的 BCM 就是一張死掉的圖。

---

## BCM 是 Lego Brick，沒有順序

BCM 有個天生限制：**它列了 capability 但沒講順序**。像一盒 Lego — 你有紅藍綠方塊但不知道哪個先哪個後。在 strategic 對話這沒問題，但要 operationalize 就需要補上 sequence。這就是下一個工具 — **Value Stream** — 出場的原因。

## Value Stream 補上 sequence 跟 KPI 關係

**Value Stream** 是把 capability 串成「為了 deliver X outcome，要依序通過 A → B → C」的流。每個 capability 在 stream 上有 KPI、有 input、有 output、有 dependency。Value stream 通常從 BCM level 2-3 出發，因為 level 1 太抽象不適合做 sequencing。**BCM 是 box，value stream 是 arrow**。

## Process 再往下接到 IT system landscape

完整鏈是 Capability → Value stream → Process → IT system。Process 是「在這條 value stream 上，這條 capability 具體怎麼跑」。Process 再往下對應到具體的 application、data source、integration。**每一層都對齊上一層**，所以 BCM 要先做好，後面所有層都掛在它上面。BCM 沒做、直接做 process model，相當於蓋房子從中間樓層開始 — 樓上 OK 但地基沒對齊整體 building 結構。

## Digital Thread：value stream 對應到 data flow

Alexander 提到一個 emerging concept — **Digital Thread**：把 value stream 跟 data flow 對應起來。**每個 capability transition 都伴隨資料的轉換跟移動**。可以從 BCM 一路往下看到「客戶下單這條 value stream 觸發了哪些資料表更新、哪些 system call、哪些 ML model 預測」。Digital thread 是 enterprise 的神經系統 — 它讓「資料治理」跟「業務治理」變成同一回事而不是兩條平行線。

## Capability metadata 才是 governance 的真正 unit

BCM 不只是 box 跟箭頭。**每個 capability 底下有一張 metadata 卡片**：data input、data output、supporting systems、responsible owner、definition。**這張卡片才是 governance 的 unit**。沒填 metadata 的 BCM 是裝飾品；填了 metadata 的 BCM 才能 drive 投資決策、責任歸屬、跨部門溝通。建 BCM 但不填 metadata，是只蓋了門面沒做機房。

## Data Readiness 是 contextual 的，不是「資料 100% 乾淨」

Data readiness 不是「資料零錯誤」。Alexander 說得很精準：**「每個 capability 對 data 的需求是什麼？我們的 data 結構支援這個需求嗎？」** 5 級評估：1 級 = 完全沒結構；5 級 = 結構完整、metadata 齊全、real-time 可用。**同一份資料對 A capability 可能是 5 級，對 B capability 可能是 2 級** — readiness 是 contextual 的。等到資料 100% 乾淨才開始 AI 投資的公司，永遠不會開始。

---

## AI Strategy 不是 IT Strategy 的子集

被問到「AI 是不是只是 resource」，Alexander 回答更深：**很多公司有 business strategy、IT strategy、data strategy，但沒有 AI strategy**。AI strategy 不是 IT strategy 的子集，因為 AI 對 business model 跟 operating model 的影響太深，需要獨立規劃。沒 AI strategy 的公司會失去競爭力；但**有 bad AI strategy 的公司會直接受傷**（合規、信任、客戶體驗）。

## Eye on Innovation Award：用真實案例校準 framework

Gartner 有 **Eye on Innovation Award**，收集各產業真實的 AI 成功案例，對客戶跟非客戶都開放。**為什麼這個有用 — 因為案例越多，benchmark 越精準，未來 use case prioritization 越可信**。如果你的組織有成功 AI deployment，提名也是分享 — 你會拿到別人的 case 來對照自家做法。**框架沒有真實案例校準就是學者的玩具**。

## Bimodal：top-down strategy + bottom-up POC

完整的 AI 推進需要 **bimodal approach**。**Top-down** — BCM、Use case prioritization、Readiness assessment 都是 strategic 動作，由 leadership 帶動。**Bottom-up** — POC、prototype、end-user pilot 都是 operational 動作，由 team 親手做。**兩條同時跑才能讓 use case 有 strategic 對齊（top-down）又有真實 user 驗證（bottom-up）**。只走 top-down 就是 PPT 治理；只走 bottom-up 就是無頭蒼蠅。

## POC 沒持續 track performance 是最後一道死因

回到開場 60% 失敗的數字。Alexander 補上最後一塊拼圖：**POC 失敗主因不是 POC 本身做不出來，是上線後沒持續 track**。BCM 的角色在這裡再次浮現 — 它讓你知道每個 AI 投資對應哪條 capability、要動哪個 KPI、由誰負責。沒 BCM 當 governance backbone，POC 一上線就被遺忘，三個月後沒人記得當初 KPI 訂在哪。

---

## 恍然大悟三：BCM 把 AI 從「IT 部門的 PoC」拉回「全公司的策略治理」

整場 webinar 串起來是一個 reframe — **AI 不是 IT 的事，是 enterprise 的事**。但要讓 AI 變成 enterprise 級對話，你需要一個 stakeholder 都看得懂的對話單位。Process map 太細、product roadmap 太窄、project plan 太短 — 只有 BCM 同時滿足「夠抽象 C-level 看得懂」「夠具體可以 attach 投資」「夠穩定 multi-year 對話」。

BCM 不是要取代你既有的工具，是把它們**串起來的那條線**。沒這條線，你的 AI 投資永遠是孤島 POC 的合集；有這條線，AI 投資是組織能力的 compound growth。

整場 webinar 真正在賣的不是 BCM 模板，是「AI 治理需要 enterprise 級對話單位」這個觀念。

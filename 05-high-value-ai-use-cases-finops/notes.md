# How to Identify, Fund and Measure High-Value AI Use Cases

> **來源**：Gartner Webinar, Frances Karamouzis（Distinguished VP Analyst）
> **涵蓋**：CIO/CFO 視角的 AI use case 經濟學。Blue money vs green money、AI value gap 三大 root cause、funding funnel + litmus test、Value × Feasibility 雙團隊打分、15 個 use case 的成本/價值模板、Defend / Extend / Upend 組合管理、POV→POC→pilot 迭代法、POC purgatory

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| Blue money | 不會流進損益表的價值：省工時、滿意度、cost avoidance |
| Green money | 會流到 general ledger 上某條成本線或營收線的錢 |
| General ledger | 總帳，公司每一條成本與營收的正式帳本，P&L 的底層 |
| P&L | Profit and Loss，損益表，CFO 在 earnings call 上講的東西 |
| FTE | Full-Time Equivalent，全職人力當量 |
| Cost avoidance | 「我們避免了某筆未來支出」，聽起來像省錢，上不了帳 |
| Funding funnel | 幾百個點子進、少數獲投資出的漏斗式審核流程 |
| Litmus test | 你的企業判準：use case 要過哪幾關才准動錢 |
| POV | Proof of Value，先在紙上算清楚值不值，再決定投 |
| POC | Proof of Concept，小規模驗證技術可行性 |
| POC purgatory | POC 煉獄：幾百個 POC 掛著，超過六成上不了 production |
| Defend / Extend / Upend | use case 三桶：顧競爭地位、賺錢主力、賭翻盤 |
| Everyday AI | Gartner 對 digital workplace 類日常 AI 工具的統稱 |
| AI-ready data | Gartner 框架，18 個變數定義資料夠不夠格餵 AI |
| Technical debt | 技術債，過去抄捷徑累積的整修成本 |
| KYC | Know Your Customer，銀行的客戶身份審查流程 |
| I&O | Infrastructure & Operations，基礎設施與維運部門 |
| Marginal cost to deliver | 多交付一單位服務的總邊際成本，green money 的門檻 |
| NPS | Net Promoter Score，客戶推薦淨值 |
| Agentic AI | 會自主規劃並執行多步任務的 AI，不只生成內容 |

---

## 這場 webinar 要做的事

Frances Karamouzis 要把「怎麼選、怎麼出錢、怎麼量 AI use case」做成可以照抄的財務紀律，具體交付四件事：

1. 用 2025 全年的客戶資料診斷 AI value gap：為什麼投了錢的組織超過 80% 拿不出價值
2. 給一套 enterprise-wide 的 funding 框架：funding funnel、litmus test、Value × Feasibility 雙團隊打分
3. 示範 Gartner 的工具怎麼用：600+ 個分析師打分的 use case 庫、15 個常見 use case 的三年成本/價值試算模板
4. 給一個跟 CFO 溝通的語言：Defend / Extend / Upend 三桶，各自的預算 cap、管理方式、價值定義

## 要建立的心智模型

讀完這篇你要建立五個認知：

1. 省下的時間不是省下的錢 — 個人生產力（blue money）跟流進損益表的錢（green money）是兩種東西，2025 年絕大多數組織只收穫了前者
2. AI 拿不到價值的 root cause 不是技術，是三件組織的事：說不清價值、算錢不夠嚴謹、business 端沒人改流程
3. 價值評估要發生在 fund 之前，不是上線之後 — 而且不是算一次，是 POV→POC→pilot 每一關重算一次
4. 同一個 use case 在不同組織的 feasibility 不同，因為 feasibility 一半在問你的資料底子，所以別抄別人的矩陣落點
5. AI use case 是一個 portfolio：Defend 當 cost center 管、Extend 當 profit center 管、Upend 當 VC 管，混著管必然出錯

下面 46 個 H2 就是把這五點拆開填滿。

---

## 「Top use case」不存在絕對版本

開場 Frances 先拆自己講題裡的字：**top is in the eye of the beholder**。同一場 call 上每個組織的「最佳」判準都不同 — 私企量 ROI，公部門根本不量 ROI。Gartner 自己用「top」時只用在客觀可量的東西（revenue、headcount、排名）。2025 年實際上浮到檯面的「top」長什麼樣？**兩位數百分比的成本節省、一個會計年度內交付** — 這不是普世真理，是那一年的市場焦慮的形狀。先解構「top」，是因為整場的方法論都建立在「判準要自己定」這個前提上。

## 2025 年的集體通病：算了成本，沒算價值，就把錢投下去了

Frances 對 2025 的診斷一句話：**客戶花了大量時間評估 cost，卻在 fund 之前沒有評估 value**。順序錯置的後果貫穿全場 — 錢出去了，回頭才發現說不出拿到什麼。這就是講題裡「funding」這個字存在的理由：funding 的紀律不在「批不批」，在「批之前你算過什麼」。

## 三個數據：董事會在押注、CEO 在押注、CFO 量不出來

Gartner 的三個數據點擺在一起就是故事：**63% 的董事會把科技與創新投資列為穿越全球不確定性的頭號策略**；**72% 的 CEO 押注 AI 是成長的主要驅動力**；但**只有 11% 的 CFO 能具體量出 AI 投資的 ROI**。上面兩個數字解釋了為什麼錢還在流（spending 持續強勁，不受各區域經濟波動影響），第三個數字解釋了為什麼這場 webinar 存在 — 押注的人跟對帳的人，中間斷了一層。

## Tunnel vision：整年盯著個人生產力看

2025 實際發生的事，Frances 稱為 tunnel vision：**整年只盯著個別員工（FTE）的生產力**。每個人都在量「這個工具幫某人省了幾小時」。但 Gartner 的研究結論直接否定這條路：**個人 FTE 的生產力提升沒有轉化成財務價值**。為什麼盯著它？因為它最好量、最快有數字 — 低垂的果實摘起來最順手，順手到 1,600 人的數據都攔不住。

## 1,600 人的調查畫出一條平線：時數省了，績效沒動

**超過 1,600 人的樣本畫出一條平線：省 1 小時跟省 5 小時，績效沒有差別。** X 軸是省下的小時數（1 到 5+），Y 軸是管理層回報的實際績效（revenue 或 cost savings 有沒有交付）。Gartner 按 function、按 industry 切開看，趨勢一致。Frances 說她筆電裡有十幾頁 slide 都在講同一件事：**time saved is not money saved**。省下的時間如果沒被導去產生新價值，它就只是蒸發了。

## Blue money：聽起來是錢，上不了帳的價值

一位客戶的原話給了這場最好用的詞彙：**blue money**。定義：**沒有直接 P&L 影響的價值** — 不會流到 general ledger 的任何一條成本線或營收線，所以進不了損益表。典型例子：某人省了三五個小時、NPS 上升、客戶滿意度上升、員工 AI literacy 提升，還有 Frances 最常聽到的 **cost avoidance**（我們避免了一筆原本要花的錢）。Gartner 不是說這些沒價值 — 是說 **CFO 沒辦法在 earnings call 上展示它們**。

## Green money：會流到帳上的錢，只來自流程的真改變

**Green money 是 blue money 的精確反面**：錢流到具體的成本線或營收線上 — sales conversion rate 上升、cycle time 下降、庫存水位改善、總銷售件數增加。這些 KPI 的共同點：**每一個都有具體的 functional leader 為它負責**。那位客戶的下半句話點出來源：green money **只能來自關鍵的業務改變 — 改 process workflow**。個人省時是 blue，流程重構才可能變 green；這個分界線就是整場的地基。

## CFO 的 earnings call 是價值的試金石

Blue 跟 green 的分界線為什麼劃在 general ledger？因為組織對外的價值敘事最終要過一關：**CFO 在 earnings call 上講「我們用 AI 做了很棒的事」之後，接下來幾季就要回答 ROI 在哪、什麼時候到、多少**。Gartner 團隊做了一個研究：下載 2025 上半年所有 earnings calls，分析 AI 投資跟結果之間能不能拉出 correlation 或因果。上市公司都被掛在這個鉤子上 — 所以一個進不了帳本的價值故事，在組織的最高溝通場合等於不存在。

## AI value gap：超過 80% 的客戶投了錢，沒拿到價值創造

把以上加總就是 **AI value gap**：投資與回報之間的裂口。**大約超過 80% 的客戶回報「投了很多、沒拿到 value creation」**。Frances 補了一句重要的時間判斷：如果一年前你聽 Gartner 的 webinar，數據長得差不多 — 同樣的熱情、同樣的高期待。意思是這條 gap 不是新聞，是持續了至少兩年的結構性問題，而 2026 必須改變的不是熱情，是方法。

---

## 恍然大悟：價值的定義權不在你的簡報裡，在 general ledger 上

這一段看似在報數據，其實在奪回價值的定義權：你說省了幾小時、滿意度漲了幾分，都不算數 — **算數的只有會流到總帳上某一條線的錢**。這個定義一立，2025 年的集體成績單就現形了：1,600 人的平線、11% 的 CFO、80% 的 value gap，全是同一件事的三個切面 — 大家收穫了一倉庫的 blue money，而組織的記分板只認 green。

先接受記分板，再開始打球；下半場的所有框架都是為了把 blue 換成 green。

---

## Root cause 不是技術不夠好

診斷 value gap 的根因，Frances 先排除最方便的嫌疑犯：**AI 跟 agentic 技術確實還不成熟，但失敗的通常不是技術**。失敗的是三件組織的事：價值說不清、算錢不嚴謹、流程沒人改。這個排除很重要 — 如果你把 gap 歸咎於技術，你的對策會是「等下一代模型」；歸咎於組織，對策才會是這場 webinar 給的那套財務紀律。跟 04 場的結論同構：問題從來不在模型，在組織怎麼用模型。

## Root cause #1：說不清價值 — 辨識、翻譯、溝通三連敗

第一大根因（Frances 說 by far 最大）：**你的團隊跟 functional leaders 能不能辨識、翻譯、溝通真正的價值來源** — 怎麼把價值切分清楚（delineate）、怎麼讓它透明。實際發生的是反面：大家把注意力過度押在看起來最低垂的果實上，也就是個人 FTE 生產力。為什麼說不清？因為說清楚需要懂流程的人跟懂技術的人坐在一起把「這一步省的時間會變成哪條帳上的錢」講出來 — 而這兩群人，恰好講不同的語言。

## 語言不通的老問題，在 AI 時代翻倍

IT 團隊跟 business 團隊講不同語言是老摩擦，但 AI 把它**複利化**了：因為桌邊多了兩個同樣深度涉入的團隊 — **data 團隊跟 security 團隊**。四群人、四套詞彙、四種優先級，要共同回答「這個 use case 值多少錢」。語言不通在兩人對話裡是摩擦，在四方會議裡是僵局 — 這解釋了為什麼後面的方法論要明文規定誰打哪個分數。

## Root cause #2：財務 rigor 缺席 — back of the envelope 不算數

第二大根因：**沒有真正做數學計算**，只做了信封背面的粗估。Frances 講的 financial governance 是具體的：你的企業要有一套框架規定**怎麼 vet、怎麼 prioritize、怎麼依 litmus test 決定 fund 誰**，然後執行它。缺了這層的後果有三：價值根本沒被量化（只活在簡報上）、成本估算粗劣、以及 funding 各行其是。

## Agentic 的成本，連 Gartner 都要另開一個計算器

成本估算為什麼粗劣？因為難度升級了：**從 gen AI 走到 agentic AI，成本的算法是另一套**，比 gen AI 更難。Gartner 自己的對應就是證據：**他們維護兩個不同的 cost calculator**，一個給 AI/gen AI、一個給 agentic — 複雜到必須分家。如果連專門做這件事的分析師都要兩套工具，你的團隊用一張信封背面去估 agentic 專案的三年成本，誤差不是百分比級的，是倍數級的。

## 錢不再都流經 CIO：funding 的一致性碎掉了

Funding 不一致的結構原因：**預算分散了**。以前的模式是錢進 CIO 的 budget、CIO 對專案負責；現在 sales 的頭、marketing 的頭、supply chain 的頭、finance 的頭**各自有預算、各自出去 fund AI initiatives**，而且各用各的財務標準。這直接推導出後面框架的第一個要求 — enterprise-wide 不是說一個人批所有案子，是說**所有人用同一套 rigorous、repeatable 的框架**，批的人可以多個，尺只能一把。

## Root cause #3：流程改變沒人做 — business 端的 ownership 真空

第三大根因回到那句 green money 的來源：價值來自改流程，**而改流程是 business 團隊的工作** — workflow 重構、operating model 調整、做這些流程的人的 metrics 改寫、信任的建立。應然的分工：IT 跟 data 團隊開發測試方案的同時，business 團隊扛起業務轉變的 ownership。實然：**business 端沒做**。結果是時間估算全面失準 — 方案上線了，流程沒變，價值自然沒到，然後大家回頭怪技術。

---

## 恍然大悟：三個 root cause 是同一個洞的三面牆

說不清價值、算不清錢、沒人改流程 — 三件事共享同一個結構：**organizations 把 AI 當技術專案在管，而它是業務變革在跑**。技術專案的習慣是 IT 接單、一次過會、上線交付；業務變革要求業務端擁有價值定義權、財務端全程重算、流程端真的動刀。用前者的管理慣性跑後者的工程，三個 root cause 就會同時出現 — 它們不是三個獨立的病，是同一個診斷的三個症狀。

修法也因此不是三帖藥，是換一套作業系統 — 下半場的框架就是那套系統。

---

## 前提：一套 rigorous、repeatable、enterprise-wide 的 funding 框架

下半場的一切建立在一個前提上：你的組織要實作**一套嚴謹、可重複、全企業一致的 AI funding 框架**。三個形容詞各有所指：rigorous 對治信封背面粗估，repeatable 對治一案一例外，enterprise-wide 對治預算碎片化。Frances 特別澄清 enterprise-wide 的意思：**不是只有一個人批所有案子** — 批的入口可以多個，但每個入口用同一套框架。一致性在尺，不在人。

## Funding funnel：點子永遠不缺，缺的是一致的篩法

框架的形狀是個漏斗（Gartner 暱稱 funding funnel，Frances 說你要叫別的名字、畫別的圖都行 — 原理才是重點）：**點子有幾百個，能 fund 的永遠是一小撮**。三道工序。**Vet**：每一個點子都要被審，沒有免檢通道。**Prioritize**：把點子互相對照排序 — 尤其當它們來自 finance、HR、supply chain 不同部門時，要放上同一把尺。**Litmus test**：用你企業自己的判準決定誰過線。漏斗的價值不在篩掉多少，在「每個進來的點子都走同一條路」。

## Litmus test 要綁在 business strategy 的支柱上

Litmus test 怎麼定？錨點是業務戰略：**CEO 講過的戰略支柱（例如第一支柱是 cost cutting），每個獲准的 use case 幾乎都要 tag 到一個或多個支柱上**。Frances 說這正是多數客戶嚴重缺失的一環。例外可以有 — 某個 use case 願意給更長的時間跨度、接受更低的 ROI — 但例外必須**前置透明**：預期的價值創造是什麼、初年成本加 recurring 成本是多少，先講清楚再進 portfolio。Litmus test 沒有 one size fits all，每家組織自己定，但每一次審批都要重新執行它。

## Value × Feasibility 矩陣：兩軸都要數學算，不是感覺貼

框架的核心工具：把所有點子陣列在兩軸上 — **feasibility 軸跟 business value 軸**，然後**用數學計算**每個點子的兩個座標，不是開會憑感覺貼便利貼。矩陣上的 customer profiling、cross-selling 這些點位只是示意 — 同一個 use case 在每個產業、每個客戶的位置都不同。這個「不同」不是誤差，是資訊。

## 同一個 use case，四個產業落在四個位置

Frances 的例子：**asset predictive maintenance 在四個不同產業的客戶矩陣上，落點四個地方**。為什麼？看 feasibility 的組成就懂了 — 假設兩家公司評同一個 use case，一家過去幾年認真投資了資料底盤，feasibility 自然落在高端；另一家的資料又髒又散，同一個 use case 的 feasibility 就低。**落點是「這個 use case 的潛力」乘上「你的家底」的積**，所以抄別人的矩陣等於抄別人的家底 — 沒有意義。

## 「每個人都想要資料，但沒有人想為資料付錢」

Feasibility 偏低的那種組織，Frances 引了他們自己的話：**「Everybody wants data, but no one wants to pay for the data.」** 五年沒投資資料基礎建設（data fabric），現在要清資料、建 metadata、定期 curate — 是一座山。她也坦白劃界：data 是能讓成本大幅擺動的最大變數之一（Gartner 另有 25 位分析師專門做 data，這場不深入）。但這句話值得留著 — 它解釋了為什麼那麼多組織的 AI feasibility 分數，其實是五年前資料投資決策的延遲帳單。

## Gartner 的 600+ use case 庫：分析師打好分，還可以找他吵架

不用從零打分：Gartner 的互動工具裡有**超過 600 個由領域分析師打分的 use cases**，按產業、按 business function 切（manufacturing 裡再分 product lifecycle、design & engineering、operations；HR 裡再分 talent management、acquisition、learning）。每個 use case 看得到打分的分析師是誰、value 跟 feasibility 的權重、分數、以及打分理由的敘事。Frances 特別推銷一個用法：**不服就去 inquiry 跟分析師辯** —「我不信 predictive maintenance 能打這個分」。把分數背後的打分敘事與場邊細節挖出來，比分數本身值錢。

## 兩個團隊、兩條軸：feasibility 給技術聯隊，value 給業務

打分不是一個人的工作，是**團隊運動，而且是兩支隊伍**。**Feasibility 軸**由 technology/digital leaders 聯隊打：IT、data、security、enterprise risk，再加 finance 跟 procurement。**Value 軸**必須由 **business teams 打 — 不是 IT、不是 data 團隊**，因為只有業務端說得出「要拿到這個價值，最小的 scope 跟 scale 是多少、要盯哪幾個 KPI」。打分的過程同時是心理建設：業務端要在打分時消化一件事 — **流程改變、operating model、人的 metrics，責任在他們身上**。分數是副產品，ownership 才是主產品。

## Procurement 入隊的理由：vendor 一年改三四次價格 schema

技術聯隊裡 procurement 的位置常被忽略，Frances 給了一個市場現實當理由：**gen AI 跟 agentic 市場上的許多 vendor 不只改價格，連定價的 schema 都一年改三四次** — 因為他們自己還不賺錢，在找自己的 break-even point。一個成本模型如果假設 vendor 定價穩定，三個月後就過期。所以 feasibility 打分需要有人持續追蹤 vendor 的價格與計價結構 — 這是 procurement 的本業，把他們排進隊伍是讓成本估算保鮮的機制。

---

## 恍然大悟：打分的真正產出不是分數，是責任的簽收

這一段教的矩陣、漏斗、litmus test，機械地看是篩選工具，但每個設計都在偷渡同一件事 — **把責任前置地、白紙黑字地分派出去**。Litmus test 逼高層把戰略支柱講明；feasibility 打分逼技術聯隊對交付風險簽名；value 打分逼業務端承認流程改變是自己的工作。2025 年的三大 root cause（說不清、算不清、沒人改）之所以發生，正是因為這些責任從來沒被簽收過。

矩陣上每一個點的座標，都是兩支團隊各自押上名字的承諾。

---

## Feasibility 的變數清單：從 vendor 成熟度到上線後的治理

Feasibility 具體看什麼？Frances 列了一張變數清單：軟體與平台成熟度、vendor 生態（是 startup 嗎？活得下來嗎？）、自家 IT 與 data 團隊的技能/IP/方法、technical debt 水位、**AI-ready data**（Gartner 有一整套 18 變數的框架定義資料夠不夠格）、security 與 compliance 與法規 — 以及一個常被漏掉的：**上線之後治理它的可行性**。變數可以自選、可以加權，但每一項都要落到分數，而且要寫下打分理由 — 理由會有自己的下游讀者。

## 打分的 audit trail 要交給兩種人：執行團隊跟律師

每個分數背後的「為什麼」（audit trail）有兩個下游讀者。第一是**接手執行的團隊**：他們要知道哪裡被打了低分，風險在哪。第二個更妙 — **你的律師**：如果某個 vendor 在某項上被打了低分，vendor 跳出來說「不可能，我們才不是 5 分 6 分」，律師接的下一句是：**「那你不會介意我們把『達到或超過這個標準』寫進合約條款吧。」** 打分流程的價值一路貫穿到合約談判 — 評估不是儀式，是彈藥。

## Value 變數的終點：每一項都要翻譯成 general ledger 上的 KPI

**業務端的每個 value 變數，終點都要翻譯成 general ledger 上的一條 KPI** — 列變數只是中繼站。變數本身：customer centricity、業務流程的改變幅度、talent 的 delta（誰要 upskill、誰要 reskill）、新的 metrics 長什麼樣。Gartner 的 value calculator 做的就是這個連接。這就是 blue/green 分界線的工程化：任何一個 value 變數如果翻譯不出一條帳上的線，它就還是 blue money 的候選人，進不了 green 的計算。

## 15 個最常見 use case 的三年帳本，攤開給你抄作業（但別照抄）

Rita Sallam 領銜、15 位分析師（含 Frances）做的研究：**取 15 個最常見的 use cases，逐個算出初始成本、recurring 成本、跟三年的價值創造**。打開是一份 15 個 tab 的 Excel，每個 use case 帶完整的計算 audit trail。以 gen AI 輔助客服為例，還分 **buy 跟 build 兩個 tab** — 因為用戶數過某個門檻後，build 會比 buy 划算。初年成本算的是全口徑：不只付給 vendor 的錢，還有 rollout、training、部署、整合。Frances 的警告：**這是教材不是答案** — 你的資料、KPI、vendor 都跟模板裡的客戶不同，學的是算法，不是抄落點。

## Break-even 線每個 use case 都不同 — 有人還故意選不回本的

每個 tab 都畫了累計價值線（藍）與累計成本線（橘），交叉處就是 break-even 點，**而 15 個 use case 的 break-even 各不相同**。一個反例：有位客戶**明知成本線壓過價值線還是投了**：他要的是 sales cycle 的洞察，他有預算、願意付。他的原話：**「I'm going to bend that value line.」** — 三年後那條線不會長這樣，因為我們會改流程、改工作方式。這個反例反而證明了框架的用途：**框架不禁止你做虧本的投資，框架逼你「知道自己在虧本，並說得出為什麼值得」**。

## Use case 是想法，case study 是發生過的事

方法論的最後一塊：Gartner 把同一套思路套到 **case studies**（客戶實際做完的案子）上 — 每一個都回答同一個問題：**這個結果對應到哪條營收成長或成本節省**。用法是接力：你在 use case 庫裡選了一個、打了分，可以順藤摸瓜找到同一個 use case 的完成版 case study，看別人實際拿到了什麼。兩位 data & analytics（D&A）分析師（transcript 拼為 Aura Papo、Carly Eodin，拼法未驗證）收集這批案例時，連背後該用哪種 data simulation 技術才能達到那些結果都分析了。

## 三個 case study：物流、零售、醫院 — 三種記分板

三個例子各踩一種價值型態。**物流商**（最後一哩配送）：目標 on-time delivery 提升 20%、車隊成長壓在 5% 以下，全是成本驅動的 KPI。**跨國 DIY/居家修繕零售**：目標年營收成長 10%，同時保持庫存與生產平衡、避免長期 overstock，營收成長型。**區域醫療網絡**：急診等待時間，KPI 直接連到病人的治療與生命，**a whole other level of value**。三個例子合起來重申開場的話：top 與 best，由觀者定義 — 但無論哪種記分板，**每個 outcome 都連著一條帳上的線（或公部門的使命線）**。

## 500 步的流程裡，make-or-break 的只有少數幾步

跟業務端合作時你會發現：**他們知道 KPI 是什麼 — 問題是他們能不能說出價值的底層構造**。Frances 的解剖：一條流程可能有 500 步，其中 50 步是全行業都一樣的 commodity 重複步驟，而真正 **make-or-break、構成差異化價值的，是流程裡少數幾個 targeted 的環節**。價值評估的功力就在這裡 — 不是「這條流程值多少」，是「這條流程的哪幾步值錢」。AI 打中那幾步才有 green money，打中另外 450 步就是 blue money 的量產線。

---

## 恍然大悟：框架的終點不是回本，是透明

15 個 tab 的 Excel、audit trail、break-even 圖，表面是省你功課的模板，實際在立一條紀律：**每一筆投資都在陽光下回本，或在陽光下不回本**。那位「I'm going to bend that value line」的客戶是這條紀律的最高級展示 — 他不是逃過了計算，他是算完之後、帶著完整的帳本選擇了相信自己能改變曲線。虧損一旦攤開，就不再是風險管理的失敗，是被定價過的賭注。

看不見的虧損叫黑洞，看得見的虧損叫策略。

---

## Defend / Extend / Upend：跟 CFO 說話用的三個桶

評估完的 use cases 落進三個桶，這套語言是設計來**跟 CFO 開會用的**。**Defend**：給你競爭平價（competitive parity）的案子，邊際增益、微創新，常常沒有 ROI 或很少；digital workplace、everyday AI 多半在這桶。**Extend**：給你競爭優勢的案子，擴市場、增營收、降本增利，**ROI 最高的一桶**。**Upend**：翻盤型，時間跨度常超過一個會計年度，不是每家都有耐心跟本錢。三個桶不是貼標籤的遊戲：每次批准一個 use case 都 tag 一桶，季度末你就能對 CFO 報告「我們的錢怎麼分布、每桶占多少」。

## 比例參考：10% / 80% / 5-15%，disruptor 可以拉到 50%

預算（或案件數）的分配參考：**Defend 桶 cap 在 5-15%（抓 10%）** — 因為不產 ROI，要設上限防它膨脹；**Extend 桶吃大頭，約 80%**；**Upend 桶 5-15%，挑一兩個就好**，甚至可以第一輪先不放。但 Frances 強調沒有對錯：**想當行業 disruptor 的客戶有人把 Upend 拉到 50%** — AI-first、AI everywhere、流血也要站在最前緣；多數中間路線的 fast follower 則守住 Extend。比例是你的戰略表態，重點只有一個：**litmus test 裡要有 cap，而且每次審批都執行**。

## 三個桶要用三種方式管：cost center、profit center、VC

分桶的真正理由（除了跟 CFO 溝通）：**這三種案子的管理邏輯互不相容**。**Defend 當 cost center 管**（控成本、設上限）；**Extend 當 profit center 管**（盯利潤、要交付）；**Upend 當 VC 管**：**二十個成一個**，大多數不會走到 production，這是常態不是失敗。混著管的災難可以想像：用 profit center 的標準殺掉所有 Upend（它們短期都不回本），或用 VC 的寬容養肥 Defend（它們本來就不該花大錢）。桶的邊界就是管理邏輯的邊界。

## 三個桶的價值也叫不同的名字：return on employee、ROI、return on future

價值側同樣三分。**Defend = return on employee**：員工賦能 — AI literacy、digital dexterity，這是它沒有傳統 ROI 卻仍值得投錢的理由。**Extend = 真 ROI**：帳上看得到的那種。**Upend = return on your future**：你做這些案子是在學 agentic、學演算法、學這些工具的行為模式 — 買的是組織面對下一輪技術的學習曲線。三個名字防止一種常見的錯誤對話：拿 ROI 的尺去量 Defend 跟 Upend，量出來都是零，然後砍掉組織的地基跟未來。

## 舊方法死了：design-build-run 加一次性 business case

舊世界的玩法：**business case 做一次**，給領導層審（他們問一堆尖銳問題、挖很深、讓你難堪），然後一旦批了，就「你上路吧」，接著線性地 design、build、run 到底。Frances 直接宣判：**這套老方法在 AI 上不管用了**。原因藏在前面講過的所有不確定性裡：成本 schema 一年變三四次、POC 之後假設全要重寫、scale 不 scale 得起來沒人敢保證 — 一次性的批准制度假設世界在批准後保持靜止，AI 的世界偏偏不。

## 新方法：POV 出發，每過一關就重算一次帳

取而代之的是**動態、迭代**的循環，你可能要回去見管理層**多達五次**。從靶心出發是 **POV（proof of value）**：在紙上算 feasibility 跟 value，過了 litmus test 才 fund。接著 **POC**：結束時**重算成本、重驗價值假設**（因為 POC 教了你新東西），做 go/no-go 決策 — 前進，還是承認這會是個吞錢黑洞、把案子先擱置。過了再做 **pilot**：又學到更多，**再重算一輪**。然後 execute。還沒完：scale 的不確定性通常要你**再跑兩輪迭代**才能安心。Frances 的安慰：做多了，這個循環會變快、變成 second nature。

## 去見管理層五次不是失敗，是方法本身

把新舊方法並排，差別最大的一格是「見管理層的次數」：舊方法一次過會、終身免檢；新方法五次回鍋、每次帶著更新過的帳本。這個設計把「重算」從尷尬變成制度 — **POC 之後修正成本估算不是承認當初算錯，是這個方法論的預設動作**。組織如果還用舊文化讀新方法（「怎麼又來要錢」「當初不是批過了」），迭代就會被羞辱成失敗 — 所以這套方法要連著它的敘事一起導入。

## POC purgatory：幾百個 POC 掛著，六成以上上不了 production

不迭代、不重算、不做 go/no-go 的下場有個專有名詞：**POC purgatory（POC 煉獄）**。Gartner 的客戶裡有人**啟動了幾百個 POC，全掛在那裡 — 超過 60% 從未進到 production**。錢一直在燒（spending, spending, spending），結果一直沒來。煉獄的成因恰恰是缺了那個「table it」的勇氣與機制 — go/no-go 裡的 no-go 不是浪費了 POC 的錢，是阻止 POC 的錢變成 production 的更大黑洞。會殺案子的框架才養得出活的 portfolio。

---

## 恍然大悟：portfolio 思維的本質是允許不同的錢有不同的死法

三個桶、三種管法、三個價值名字、五次回鍋、no-go 的勇氣 — 整段在打掉一個迷思：「每筆 AI 投資都該回本」。真正的紀律反而是分化：Defend 的錢買地基（別指望回報，設好上限）、Extend 的錢買利潤（嚴格要求回報）、Upend 的錢買彩券與學費（二十中一，認賠十九）。每種錢有自己該有的死法，而 POC purgatory 的本質就是**不准任何案子死，於是所有案子一起活在煉獄**。

敢讓案子死的組織，才有資格讓案子活。

---

## 終局分工：business 對價值負責，technology 對交付負責

收尾的權責表只有兩行。**Business leaders** 對價值創造負責：人的行為改變、決策方式改變、工作方式改變，最終是競爭優勢。**Technology leaders** 對 workmanship 負責：品質、準時、預算內交付；技術、資料、軟體、infra 與維運、cyber 安全防護；管理主要成本，連帶管理多數技術風險。這張表跟 root cause #3 首尾呼應：當初 value gap 的成因就是 business 端的 ownership 真空，這張表就是把真空填上的正式文件。

## 價值要更透明，技術卻在變黑箱 — 兩條反向的曲線

兩側的透明度正在反向移動。**Business 側被迫走向 value transparency**：整套框架逼你把價值切分、翻譯、攤開。**Technology 側卻在走向 opacity**：你再也不能審查一千萬行 code 了，AI 方案越來越是黑箱。一邊越來越透明、一邊越來越不透明，交叉的含義是**前置的工作變多了**：你不能在事後打開箱子看，所以只能在事前用 feasibility 打分、合約條款、audit trail 把風險鎖住。

## Q&A：IT ops 的價值在哪 — level 1 support 從幾百人到十人以內

最高票問題：AI 在 IT operations 哪裡最有價值？Frances 先聲明自己不是 I&O 分析師，但給了兩個親見的案例：一個客戶把 **level 1 支援從幾百人做到剩不到十個人**；另一個客戶把**特定 infra ops 區域的交付成本砍了 75%**。她也給了結構性的理由：**I&O 仍占 CIO 預算的七成左右**，所以它天然是成本節省的大本營 — Gartner 在這個領域養了超過一百個分析師。工具面則指向 use case 庫裡的 IT service desk 分頁：endpoint anomaly response、intelligent categorization、incident 處理。

## Q&A：以前上 SAP 也這樣折磨過 ROI 嗎 — 有，而 AI 已經到了那個量級

有人問：過去的技術浪潮有沒有這樣 agonize ROI？Frances 的回答分兩層。第一層：有 — 當年的 SAP、Oracle、ServiceNow、Salesforce 大案（百萬到上億美元，含產品、顧問、流程重組），都走過這種 rigor。**AI 需要同樣待遇的原因是它已經到了那個量級**：AI 專案最終都會走進百萬美元級，連 scope 有限的小組織都會被數字嚇到。第二層更根本：**AI is not a technology decision only. AI is a business decision.** — 它穿透的領域遠超 IT，所以它的審批也得用業務投資的規格。

## Q&A：裁人省的錢是 green money 嗎 — it depends，門檻是 marginal cost to deliver

最尖銳的問題留在最後：因 AI 裁員省下的錢算 green money 嗎？Frances 的回答：**it depends**，並用銀行的 KYC 流程解剖。大銀行裡碰 KYC 的是**幾千人**（不是幾百），流程**超過 500 步**，各區域法規版本不同。她見過裁掉或大幅提效 10 人、20 人、100 人**而拿不到 green money** 的案例。變數有四：流程的複雜度、scope、tacit knowledge（在人腦裡）vs explicit knowledge（有文件）的比例、exception 處理的結構。判準一句話：**裁人若沒有改變 total marginal cost to deliver，錢就不會流成 green** — 你只是把工作擠到剩下的人身上，帳本上的交付成本沒動。

---

## 恍然大悟：整場在教一種翻譯 — 把 AI 的故事翻成會計的語言

回看全場的每個工具：blue/green 是詞彙表、value calculator 是文法、Defend/Extend/Upend 是文體、POV→POC 的迭代是改稿流程 — 合起來是一門**把 AI 翻譯成會計語言的課**。為什麼非學不可？因為組織裡資源的最終仲裁語言就是會計語言：earnings call、general ledger、marginal cost。不會翻譯的團隊，做出再好的東西也只能說「我們省了很多時間」— 然後在下一輪預算會議上輸給會翻譯的人。

技術的價值不是做出來的那一刻誕生的，是被翻譯成帳本語言的那一刻才誕生的。

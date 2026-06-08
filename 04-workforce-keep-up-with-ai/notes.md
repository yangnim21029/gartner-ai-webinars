# How to Create a Workforce That Can Keep Up With AI

> **來源**：Gartner Webinar, Kabeh Vaziri（Managing VP）+ Soyeb Barot（Distinguished VP Analyst, Chief of Research；兼任大學 adjunct professor 教 ML 與軟體工程）
> **涵蓋**：CIO 視角的 workforce 轉型三場硬仗 — capacity reallocation、emotional adaptation、work redesign。含 capability 三層共享語言、五條 workforce 訊號、skills atrophy 洋蔥圖、data scientist 深拆案例、職涯 archetype 換軌路徑

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| Capacity reallocation | AI 省下的人力時間重新分配到哪 — 不只是「省了幾小時」 |
| Emotional adaptation | 員工對 AI 衝擊的心理適應曲線，會先跌再（不一定）回升 |
| Work redesign | 重設計工作內容，讓人去做以前做不到的新價值 |
| Core capability | 這個職位無論在哪家公司、幾年資歷都一定擁有的能力 |
| Contextual capability | 看條件才擁有的能力 — 團隊結構、個人信任度、業務情境決定 |
| Shared capability | 跨職位共同貢獻給組織的能力（研究、工具評估、跨部門協作） |
| Skills atrophy | 技能萎縮 — AI 接手後人類不再練、就此失去的能力 |
| Unplanned work | AI 改流程後冒出的計畫外工作：handoff 摩擦、AI slop、escalation |
| AI slop | AI 產出的低品質內容，反而製造下游清理工作 |
| Messy middle | 轉型中段 — capacity 看似有了卻很脆弱、人人喊忙的過渡期 |
| Heat map | 把一個職位的 capability 標色，看哪些會被 AI 接手的圖 |
| AutoML | 自動選模型、調參數的工具，連「該用哪個 model」都不用人判斷 |
| Platform builder | Data scientist 的演化 archetype 之一：轉去建 agent 平台 |
| Compliance champion | 管 AI/資料治理合規的 archetype，SOC analyst 可換軌過來 |
| SOC analyst | Security Operations Center 分析師，資安監控職 |
| D&A | Data & Analytics，資料與分析部門 |
| FTE | Full-Time Equivalent，全職人力當量 |
| Context engineering | 設計餵給 AI 的上下文的工程方法 |
| FOMO | Fear of Missing Out，「別人都會、只有我落後」的焦慮 |
| MVP | Minimum Viable Product，最小可行產品 |
| SDLC | Software Development Lifecycle，軟體開發生命週期 |
| ModelOps / GenAIOps / AgentDevOps | 模型、生成式 AI、agent 各自的部署維運方法論 |

---

## 這場 webinar 要做的事

兩位講者花了一年研究 AI 對職位的衝擊，這場要交付四件事：

1. 用 Gartner 自家數據重新定調「AI 搶工作」的敘事 — 1.4M 筆裁員資料的分析結論
2. 把 workforce 轉型拆成三場互相依賴的仗：capacity reallocation、emotional adaptation、work redesign，並解釋為什麼順序錯了會全盤皆輸
3. 用 data scientist 當解剖標本，示範「capability 語言」怎麼把一個職位拆到可以重設計 — 同樣方法已套用在 20+ 個 IT 職位
4. 給 CIO 五條可追蹤的 workforce 訊號，加一張 CIO/CHRO/CFO 的三方分工表

## 要建立的心智模型

讀完這篇你要建立五個認知：

1. AI 對 workforce 的衝擊不是裁員，是 chaos — 職位快速變形、邊界重畫，1.4M 筆裁員資料裡不到 1% 跟 AI productivity 有關
2. Workforce 轉型是三場互相依賴的仗 — 情緒沒顧好就沒人幫你創造 capacity，沒 capacity 就沒得 redesign
3. AI 創造的 capacity 天生脆弱 — unplanned work 會回頭吃掉它，而三條訊號線的斜率是你的設計決策，不是自然現象
4. 技能分「可以萎縮」跟「不能萎縮」 — 判準不是新舊，是它屬不屬於 human foundation
5. 職涯要錨在不變的能力上 — 追「明日技能」18 個月後就要再追一次，錨在問題解決與好奇心才有 optionality

下面 50 個 H2 就是把這五點拆開填滿。

---

## AI 已經滲到工作的核心，不是灑在表面

Gartner 數據：**24% 的組織已經在多個 business unit 把 AI 規模化**，且預期 AI agents 承擔的工作比例三年內顯著上升。這不是「某個部門在試 AI」的階段了 — 有些組織還在把 AI 灑在工作流程上（sprinkling on workflows），但越來越多組織走向有方法的部署。差別在哪：灑的組織得到零星的個人提速，方法化的組織開始動到「誰做什麼工作」這個結構問題。後者才會碰到這場 webinar 要講的三場仗。

## 市場要的不再是單一深度專家，是複合背景

**Combined、synthesized backgrounds 變搶手** — AI 接手例行分析後，市場要的不再是「一個人、一項獨門專業、一個 domain」，而是一個人身上疊著多種知識。這讓 CIO 找人變難：CIO 明明手上有人才，卻說不清缺的是哪種複合背景。第二，**創新與問題解決的溢價上升** — Gartner 調查 CIO 與高管，IT 人員最關鍵的兩項技能正是 innovation 跟 problem-solving。因為 routine 的部分 AI 拿走了，剩下的工作天然偏向沒有標準答案的部分。

## 60% 的企業對 skills atrophy 沒有任何策略

超過半數企業選擇留人增強（augmenting）而非換人（replacing）— 偏偏留下來的人，技能正在無人管理地萎縮：只有 40% 的企業對 skills atrophy 有策略，意思是 **60% 的企業眼睜睜看技能萎縮而沒有計畫**。atrophy 的機制很簡單：if you don't use a skill, you might just lose it。AI 接手任務的同時也接走了練習機會，而組織根本沒在記帳「我們正在失去哪些能力」。這個伏筆到後面的洋蔥圖才會收 — 萎縮不可怕，不挑選哪些可以萎縮才可怕。

## 1.4M 筆裁員資料，不到 1% 跟 AI productivity 有關

2025 全年 Gartner 分析了 **140 萬筆 AI 相關裁員資料點，發現以 AI productivity 為由的不到 1%**。裁員原因很多，但「AI 讓我們不需要這些人了」不是把數字推高的那個。這個數據直接打掉新聞敘事 — 因為如果 AI 真的在大規模替代人力，這個比例不可能這麼低。資料指向另一個結論：AI 造成的不是 substitution，是別的東西。

## AI 帶來的是 chaos，不是裁員故事

Kabeh 給那個「別的東西」起了名字：**chaos**。不是說沒有人會失業 — 會有。而是衝擊的主體不是 job loss，是 **rapid evolution of existing jobs**：大量職位在變形（morphing）、新職位在生成、舊職位的邊界在重畫。這個區分決定你的應對姿勢：如果是裁員故事，你做的是人力規劃；如果是 chaos，你要管理的是「每個人的工作都在腳下移動」的組織 — 這難得多，也是這場 webinar 存在的理由。

## Workforce 對話其實是三個對話，而你們可能各講各的

AI 對 workforce 的衝擊不是一個對話，是三個：**capacity reallocation**（AI 幫我們做更多重要的事，還是只讓我們更忙？）、**emotional adaptation**（AI 會撕裂組織還是動員組織？）、**work redesign**（AI 能讓我們創造以前不存在的價值嗎？）。拆開講的實際理由：**你在講其中一個，對面的人可能在跟你講另一個**。CIO 講 capacity、員工心裡在跑 emotion、CHRO 想的是 redesign — 三個人以為在同一個會議，其實在三個會議。

## 三場仗互相依賴：情緒垮了就沒有 capacity，沒 capacity 就沒得 redesign

這三個對話不是並列選項，是依賴鏈。**員工沒有情緒投入，就不會幫你創造 capacity**（他們會守著舊工作不放）；**創造不出 capacity，就沒有資源做 work redesign**（人都被現有工作綁死）。反過來，redesign 讓人看得到值得期待的下一步，又回頭餵 emotional adaptation。這個互鎖讓 workforce 對話比想像中複雜 — 你不能挑一場打，三場是同一場。

## 第一個可見的勝利應該給人，不是給報表

所有組織的第一直覺都是先打 capacity — 因為最好量化：「我們把 AI 放這裡，這個職位省下幾分幾小時」，check the box。但 Kabeh 直接反對：**your first visible win should be with your people**。理由是依賴鏈的方向 — 先讓員工感覺自己是實驗的主人而不是實驗品，他們才會從「擔心飯碗」翻轉成「興奮地想要明天的工作」。先拿了 people 跟 capacity 這兩個勝利，再轉成 intentional 的 work redesign，這才是 **the most durable way** — 順序本身就是策略。

---

## 恍然大悟：你以為在談技術部署，其實在談三場必須同時贏的仗

開場八個點看似在鋪數據，其實在做一件事：把「AI 來了要裁多少人」這個錯的問題，換成「三場互相依賴的仗要怎麼打」。1.4M 筆資料證明裁員是假議題，chaos 才是真議題；而 chaos 的管理單位不是 headcount，是三個同時進行又互相餵養的對話。多數組織輸在開局 — 挑了最好量化的 capacity 先打，卻不知道 capacity 的彈藥是員工的情緒投入。

順序錯了，三場全輸；這就是為什麼它叫 transformation 而不叫 rollout。

---

## Job 太滑溜，分析得從一個具體職位下刀

Gartner 的方法論選擇：不從 workforce 全景講起，**從一個具體職位解剖起** — 這場用 data scientist。理由是 job 這個東西出名地滑溜：同一個 title 在不同公司是不同工作，同一家公司裡坐在內部 IT 的軟體工程師跟坐在交易室的也是兩種人。直接談「workforce 的 AI 衝擊」會空轉，談「這個職位的哪些能力會被 AI 接手」才有抓手。Gartner 已用同一方法拆完 20+ 個 IT 職位，HR 等業務職位也在拆。

## Capability 是跨組織的共享語言，job description 不是

拆職位的單位不是任務清單，是 **capability**，分三層。**Core capabilities**：這個職位無論在哪、幾年資歷都一定擁有的能力 — 你是 data scientist，這些就是你的。**Contextual capabilities**：看條件 — 團隊怎麼設、你個人累積多少信任、業務情境是什麼，也許你擁有、也許不。**Shared capabilities**：無論什麼職位都會貢獻給組織的共同能力。這三層解決了 job description 不可比的問題 — 因為 capability 不隨公司變，它才能當分析的座標系。

## Data scientist 解剖：core 是問題框定，contextual 是 domain 直覺

套到 data scientist 上：**core** 是 problem framing、data preparation、hypothesis testing — 不管你在保險公司還是供應鏈公司，這就是你的工作底盤。**Contextual** 是「這個 domain 哪些 feature 重要」的直覺 — 保險的 feature 跟供應鏈的 feature 是兩個世界，還有部署策略、ethics 與 responsible AI。**Shared** 是研究與創新、工具評估、跨部門協作。一個職位被這樣拆完，才能逐格問：這一格，AI 能接嗎？

## 丟過牆的時代結束了

Soyeb 點名一個舊習慣的死亡：data scientist 建完模型「throw it off the fence」丟給工程團隊收尾的日子過去了。跨部門協作從加分項變成 core capability — 因為 AI 時代的模型不是交付物，是活在 production 裡持續被監控、持續漂移、持續要人協作維護的東西。這個轉變預告了後面的主題：職位的價值重心從「我做出了什麼」移向「我跟系統跟人協作出了什麼結果」。

## 重設計有三檔：AI-cautious、task-specific、AI-first

同一個 data scientist 職位，AI 介入有三種深度。**AI-cautious**：AI 是個 static、disconnected 的助手，建議程式碼跟視覺化，人類照單全收或不收。**Task-specific automation**：agentic 工具自主執行設計好的任務（特徵工程、訓練、部署 fine-tuned 模型），人類監督結果、解讀、把關 problem framing 跟模型選擇。**AI-first**：一串可互操作的 agents 跨平台協調，人類只做高層監督、設 ethical guardrails、推創新邊界。三檔不是優劣排序，是你要選的位置 — 而選擇權在你手上。

## AI 越成熟，人類越往 judgment、orchestration、strategy 移

三檔連起來看是一條單向的遷移路徑：**AI 接手 physical execution，人類移向判斷、編排、策略**。Soyeb 的關鍵句：**「We are not eliminating the work, we are changing who does what.」** 工作沒有消失，是重新分配給不同的執行者。這句話聽起來安撫，實際上是警告 — 「who does what」的重新分配正是前面說的 chaos，每個人的工作內容都會被改寫，只是不見得被取消。

## Heat map 最常見的誤讀：把它當自動化清單

把職位的 capability 標色做成 heat map，顏色深淺顯示 AI 介入度。**多數組織犯的錯：停在 automation** — 看著圖說「這些格子能自動化，太好了，省人」。Soyeb：如果只用 AI 縮小職位，**你得到 efficiency，得不到 growth**。因為 heat map 上深色格子（AI 接手）的真正意義不是「可以砍」，是「人的時間釋放出來了」— 最大的機會在把人類工作**擴張**到更高價值的區域，而不是把職位**收縮**到剩下的格子。

## 縮小職位是消費 capacity，擴張人類工作是投資 capacity

把 efficiency 跟 growth 的分岔講透：同樣一格「AI 可接手」，兩種反應。消費型 — 砍掉這部分工時，省下的錢進損益表，然後呢？沒有然後。投資型 — 釋放的時間導向以前沒人有空做的事：複雜問題、創意工作、ethical 把關。前者的天花板是現有工作的總量（你最多省 100%），後者沒有天花板（新價值沒有上限）。這個分岔在 webinar 後段會長成 work redesign 那場仗。

---

## 恍然大悟：capability 語言把「AI 會不會搶我工作」變成可以逐格回答的問題

這一段的真正貢獻是方法論：job 不可分析，capability 可以。把滑溜的 job title 拆成 core / contextual / shared 三層格子，「AI 衝擊」就從一團焦慮變成一張可以逐格判讀的 heat map。然後同一張圖有兩種讀法 — 自動化清單（縮小職位、收割效率）或 capacity 地圖（釋放時間、擴張價值），讀法的差別就是 efficiency 跟 growth 的差別。

圖是同一張，輸贏在你拿它來砍還是拿它來建。

---

## Capacity 有三條訊號線，不是一條

把 X 軸設成時間（從 automation 早期到你選的 steady state），三條線同時在跑。第一條：**humans doing less**，人類做今天這份工作的比例下降。第二條：**AI doing more**，AI 接手的比例上升，兩條線的差距就是你創造的 capacity。第三條最常被漏看：**unplanned work 的湧現**，一條突起的曲線回頭吃掉前兩條線創造的空間。只看前兩條線的組織會高報自己的 capacity，然後困惑為什麼大家還是這麼忙。

## Unplanned work 從哪來：handoff 摩擦、AI slop、對 escalation 的過度信任

計畫外工作有三個來源。一，**handoff friction** — 流程改了，人不知道事情該流向哪。二，**AI slop** — AI 產出的劣質內容變成下游的清理工作。三，最深的一個：很多組織改 workflow 是 **from a place of elimination** — 砍任務、砍 handoff、重排順序，砍掉的安全網全押在 escalation 流程上。平常沒事，一出事就是大事。

## 一次 escalation 就能抹掉整批 AI 收益

Kabeh 引用一位 CIO 上週的原話：**「It takes only one escalation to wipe out a whole bunch of benefits that we thought we had harvested from AI.」** 機制：elimination 式的流程改造把冗餘砍光，所以例外狀況沒有緩衝，直接升級成跨團隊救火 — 一次救火燒掉的工時，可能等於 AI 幾個月省下的總和。更麻煩的是這種損耗**早期量不到**，所以它不會出現在你的 ROI 報表上，只會出現在員工的疲憊感裡。

## 三條線的斜率是設計決策，不是自然現象

三條線怎麼走、彼此什麼關係，**entirely up to you**。你怎麼部署 AI、給誰用、推進多快、保留多少冗餘 — 每個選擇都在改變線的斜率。多數組織把這三條線當天氣（觀測、抱怨、適應），Gartner 要你把它當建築圖（設計、施工、驗收）。中段那個 capacity 看似有了卻碎一地、人人喊忙但不是 good busy 的狀態，就是 **messy middle** — 它不是必經的宿命，是設計不良的症狀。

## 員工的情緒曲線：好奇 → 驕傲混著 FOMO → 恐懼 → 新身份

一個 data scientist 的情緒路徑有四站，而最後一站不保證抵達。起點是 **good faith + curiosity + caution**（這東西能幫我畫圖表、整理草稿，有意思）；接著 **productivity + pride + FOMO** — 以前要做很久的事現在很快，但「別人好像都比我會用，我是不是做錯了什麼」；然後反轉：**「如果它能做好我工作的這一塊，我工作剩下的部分呢？」** — 邊界變模糊，對未來的擔憂變具體；最後抵達（或抵達不了）**new identity**。

## 情緒線會自己跌下去，但不會自己爬回來

關鍵警告：情緒曲線在 messy middle 有一個 dip，而 **it is not a given that this line is going to go back up**。有些職位真的會消失，有些人的線真的就一路向下。把線拉回來是 executives 的主動工程，不是時間的自然療癒。誰值得拉？Kabeh 講了兩次：**不只看職位重要性，更看「有能力 learn、unlearn、reinvent 自己」的人** — 職位會過期，但能自我改造的人是跨職位的資產。

## 別在 atrophy 裡丟掉 domain expertise 跟 institutional knowledge

Soyeb 補上組織視角：情緒線跌落的過程裡，最大的隱形損失是**帶著 domain 專業跟組織記憶的人先走了**。這些人身上的東西不在文件裡 — 哪個 feature 在這個行業有效、哪次事故教會了組織什麼。所以「投資願意重塑自己的人」不只是溫情，是資產保全：你要的是這些知識的載體願意搭上轉型的車，而不是在 messy middle 心冷離場。

## 團隊變小、多學科、解完即散

重複性分析交給 AI 後，團隊跟著變形：**更小、多學科、為一個業務問題聚合、解完就解散**。Data scientist 越來越像 domain expert，帶著 business acumen 做翻譯，在不同團隊邊界間流動，以 outcome 為座標做決策。也因為 routine 卸載了，一個 data scientist 能監督、引導、精煉多個模型，把人的時間集中在 complex、creative、ethical 的挑戰上。

## 新工作型態預設了一種人格 — 不是每個人都喜歡監督 AI

緊接著一個誠實的但書：**「That also means that this has to be the person that enjoys that type of work.」** 從親手建模型變成監督一群模型、從技術執行變成跨界翻譯 — 這對某些人是解放，對另一些人是失去工作裡最愛的部分。職位重設計不能只畫能力矩陣，還得問：這個新形狀的工作，現在的人**想做嗎**？這個問題沒人替你答，也回扣前面 — 情緒線回不回得來，一半取決於新工作對這個人有沒有吸引力。

---

## 恍然大悟：capacity 不是省出來的，是設計出來的

這一段把「AI 省時間」的素樸算術拆了。表面上 capacity = AI 做的 − 人類做的；實際上要減掉第三項 unplanned work，而第三項的大小由你的設計品質決定 — 砍光冗餘的流程會在一次 escalation 裡吐回所有收益。情緒那條線也一樣：跌是物理，回升是工程。五條訊號裡沒有一條是自然現象，全部是你的決策的影子。

把這些線當天氣的組織在 messy middle 裡掙扎，把它當建築圖的組織在裡面施工。

---

## 洋蔥圖：哪些技能可以放心萎縮，哪些萎縮了就回不來

Skills atrophy 不可避免，可管理。Gartner 的洋蔥圖把 data scientist 的技能分四區：左邊是 **risky** vs **acceptable** 的萎縮技能，右邊是 **foundational/enduring** vs **new & emerging** 的保留與新增技能。這張圖的存在本身就是答案 — 前面說 60% 企業對 atrophy 沒策略，策略長什麼樣？就長這樣：一張明確說「這些可以丟、這些不准丟」的清單。

## Human foundation 四件事：好奇、倫理、商業感、說故事

洋蔥的核心是 **human foundation**：analytical curiosity、ethical reasoning、business acumen、data storytelling。這四項沒有一項是技術 — 它們是「用技術的人」的底層作業系統。它們被放在核心的理由：AI 對這四項的替代力最弱，而職位怎麼變形，這四項都帶得走。後面 Q&A 講職涯韌性時會回到這裡 — 錨點就是這一圈。

## Enduring skills：假設形成、模型選擇、實驗設計

第二圈是隨時間仍然站得住的技術能力：hypothesis formulation、知道哪個模型適合什麼問題的 model selection、feature variables 的判斷、實驗設計、把實驗推進到 MVP 再規模化。這些跟 human foundation 的差別：它們是技術的，但位於**判斷層**而非執行層 — AutoML 可以代跑模型，但「這個問題值不值得建模」的判斷沒有外包對象。

## New & emerging：multi-agent 架構、自主度設計、responsible AI 治理

第三圈是這個職位正在長出的新技能：responsible AI governance、跨應用的 cross-functional 整合、**multi-agent architectures 的設計**、判斷工作流該給多少 autonomy、以及「哪些元件該容器化成可跨用例復用的 agent，而不是堆一個 monolithic model」。這些全是**架構層**技能 — data scientist 的新增技能樹不在「更會建模」，在「更會設計模型跟 agent 怎麼協作」。

## Risky to lose：資料解讀、說故事、模型驗證

哪些技能萎縮了是災難？**Data interpretation、storytelling、model validation** — 因為這三項是人類對 AI 的把關線。模型驗證特別關鍵：你得有能力**挑戰 AI 給的模型**、拆解它的分析、說出「這個不對」。這個能力一旦萎縮，組織就失去了對 AI 輸出說不的資格 — 從此 AI 說什麼是什麼。Spellchecker 讓你忘記拼字無所謂，AI 讓你忘記怎麼驗證模型，性質完全不同。

## Acceptable to lose：資料清理、圖表選擇 — 30% 的工時可以放手

對照組：**routine data cleaning** 萎縮就萎縮吧。Soyeb 直說他帶過的 data scientist 把**將近 30% 的時間花在資料準備**上 — 這部分 AI 接手，他樂見團隊忘記 data integration 的底層細節。同類：標準化統計分析、基礎視覺化的選擇（Soyeb 的原例：對 sales 簡報該用 bar chart 還是 Bayesian plot，這種判斷 AI 代勞沒有損失）。判準浮出來了：**會不會削弱你挑戰 AI 的能力**。會的，risky；不會的，acceptable。

## 釋放的 capacity 別拿去清三年的 backlog

第三場仗 work redesign 開打：AI 釋放 capacity 之後，**人類接下來做什麼**？Soyeb 先堵死最自然的答案：「終於可以清那堆積壓三年的 backlog 了」— 不行。Backlog 是過去的工作，你只是把省下的時間倒進舊坑。Redesign 的標準嚴格得多：**new、inspiring、value-creating** — 要是以前不存在的價值，不是以前沒做完的工作。這個區分回扣 efficiency vs growth：清 backlog 是 efficiency 思維的殘影。

## 工作四分法：routine 自動化、coordination 加速、sense-making 增幅、connections 倍增

怎麼分析「人類接下來做什麼」？把工作拆四類，各自對應 AI 的不同動詞：**routine**：AI automates，直接接管；**coordination**（系統間的 handoff）：AI accelerates，加速但人還在環裡；**sense-making**（分析、找創新機會）：AI bolsters，人出想法 AI 幫忙展開；**connections**（建立關係、對業務跟行業的深度理解）：AI multiplies，人的獨有資產被 AI 放大。四個動詞畫出一條清楚的價值梯度：越往右，人類越不可替代，redesign 該把人往右搬。

## 98% 準確率的模型，沒讓客戶流失率動 2% 就是沒價值

Data scientist 的考核座標正在換軸。Soyeb 親歷的對話：data scientist 辯護「我的模型有 98% 準確率」，業務方回「但 customer attrition 連我們期待的 2%、5% 都沒動」。**Ownership boundaries 模糊化的結果是 data scientist 越來越被 business outcomes 考核，而不是被模型品質考核** — 你可以擁有全公司最準的模型，但指標沒動就是沒價值。這呼應 capability 解剖裡 business acumen 入核心圈：不是錦上添花，是考核標準已經搬家了。

## 週末能 prototype，三個月才能上 production — 瓶頸不在建模

一個暴露真瓶頸的對比：有組織的 data scientist **一個週末就能 prototype、週一模型就緒，然後花三個月才把它整進 production 環境**。建模速度跟交付速度差了 12 倍，差距全在協作介面：跟工程的整合、跟業務的對齊、平台的承接力。所以 redesign 要長出的能力是快速 prototype、迭代、再走出去的全鏈路 — 也再次解釋為什麼 cross-functional collaboration 從加分項變成 core capability。

---

## 恍然大悟：atrophy 不是風險清單，是一份你必須簽名的取捨文件

這段表面在列技能清單，實際在逼一個決策：AI 接手任務 = 人類停止練習 = 技能萎縮，這條鏈不可逆轉，你唯一的選擇權在「讓哪些技能萎縮」。判準也給了 — 凡是支撐你**挑戰 AI** 的能力（解讀、驗證、說故事）不准丟，凡是 AI 代勞無損判斷力的（清資料、選圖表）放心丟。不簽這份文件的組織等於默簽了另一份：全部技能隨機萎縮，包括有一天想對 AI 說「你錯了」的能力。

60% 的企業還沒意識到自己正拿沉默當簽名。

---

## Zoom out：2030 的衝擊分析不照職位切，照 workflow 切

Gartner 的 IT 2030 衝擊分析刻意**不分析任何一個職位**。鏡頭從 data scientist 拉到整個 D&A 部門後，分析單位不是 data engineer、data product manager 這些 role 會怎樣，而是六段 workflow 會怎樣：make data available、govern、engineer、predict & optimize、enable value、decide & act。每段標出受影響 FTE 百分比、哪裡增員、哪裡持平、哪裡要大規模 reskilling。

## 職位是衣服，workflow 責任才是身體

為什麼用 workflow 不用職位？因為職位名稱在快速變形（前面的 chaos），用會變形的東西當分析單位，分析跟著過期。**Workflow 的責任不會消失 — 資料永遠要可用、要治理、要變成決策** — 變的只是誰（人或 agent）扛哪段。所以規劃要把責任**錨在 workflow 上**，讓職位作為「責任的當前打包方式」自由變化。這跟 capability 語言是同一招的兩個尺度：個人層面用 capability 穿透 job title，部門層面用 workflow 穿透 org chart。

## Data scientist → platform builder：核心是 agent orchestration 跟 AI engineering

職涯路徑也用同一套語言鋪。Data scientist 演化成 **platform builder** 的路徑拆三層：core 要補 agent orchestration 的深度理解、AI engineering 基礎（ModelOps / GenAIOps / AgentDevOps）；portable 的共享層是 prompt engineering、跨域整合 — 這些大家都在練；這個 archetype 獨有的是 AI infrastructure、API 與 microservices 管理、DevOps 與 CI/CD、AI orchestration。三層各管一件事：core 決定能不能上路，portable 決定帶得走什麼，獨有層決定這個 archetype 跟別人的差異 — 所以這張清單能直接當對話工具，跟你的 data scientist 攤開講「你要去那裡的話，缺的是這幾格」。

## 跟人才的對話從「你的 KPI」變成「三五年後你想在哪」

這套 archetype 路徑圖的第一用途是對話工具：**跟你的 data scientist 坐下來問，agentic AI 時代裡你三年、五年後想成為什麼** — platform builder？compliance champion？translator？然後反推 upskilling 路徑。這正是前面兩條線的交點：情緒線要回升，靠的是員工看得到自己在未來的位置；capacity 要轉成新價值，靠的是有人準備好接新工作。一張路徑圖同時餵兩場仗。

## SOC analyst 可以換軌成 D&A compliance champion — 跨域不是從零開始

路徑圖更大的價值在**跨域換軌**。一個 SOC analyst 想成為 D&A compliance champion：他已經有 security monitoring、governance/risk/compliance、ethical oversight 的底子 — 這些直接折抵。要補的 core 是 context engineering 跟 AI governance；portable 層補資料管理（結構/半結構/非結構內容怎麼管）；這個 archetype 獨有的是 data audit 與 compliance posture、policy 管理與法規執行、AI 模型風險管理。換軌的本質：**core 能力打底，缺口才需要上課** — 這比「砍掉資安部、招聘合規人」便宜得多，也人道得多。

## 五條訊號合體：三條 capacity 線 + 情緒線 + 新價值線

收束前面所有線圖：**AI does more、humans do less、unplanned demand surge**（capacity 三條），加上**情緒適應線**（先跌，被你拉回來），加上 **work redesign 的新價值線**（你創造出來的、以前不存在的工作價值）。五條線就是 CIO 的 workforce 儀表板 — 看出你的組織在轉型的哪個位置、哪條線在惡化、下一步該對哪條線動手。

## Messy middle 是轉換期：capacity 已釋放，價值未承接

五線圖的中段就是 messy middle 的正式定義：**AI 已經開始釋放 capacity，但組織還沒把它轉成新價值**的過渡帶。三場仗在這裡交匯 — capacity 線拉開了缺口、情緒線正在谷底、新價值線還沒起飛。組織最容易在這裡誤判：看 capacity 線以為成功了，看忙碌感以為失敗了，其實兩者都對 — 這就是轉換期的定義，而能不能走出去取決於你是否同時在打三場仗。

## 三方變革：CIO 出 capacity，CHRO 出 readiness，CFO 出 constraints

最後一張表把三場仗分給三個 C-suite。**Capacity reallocation**：CIO 作為技術管家提供 capacity potential，CHRO 創造組織 readiness，CFO 給出財務約束。**Emotional adaptation**：CIO 跟業務領導建 trust，CHRO 管理 skepticism 與 fear。**Work redesign**：CIO、CHRO、業務領導三方合謀。Kabeh 收尾：**「When it goes wrong, everything goes wrong. But also when it goes well, everything goes well.」** — 三場仗、三個人，沒有單獨獲勝這回事。

---

## 恍然大悟：個人用 capability、部門用 workflow、職涯用 archetype — 同一招的三個尺度

這段看似在講 2030 預測跟職涯路徑，骨子裡是同一個方法論的三次套用：**找到比表象更穩定的分析單位**。Job title 會變形，capability 不變；org chart 會重組，workflow 責任不變；具體技能 18 個月過期，archetype 的三層結構不過期。所有規劃都該錨在穩定層，讓易變層自由變化 — 這樣 chaos 來的時候，你的地圖還能用。

預測未來不可能，但選一個不隨未來變形的座標系是可能的。

---

## 五六個世代第一次同場工作，而每個世代都以為別人跟自己一樣

Q&A 第一個亮點：史上第一次有**五到六個世代同時在職場**，對 AI 的理解方式跟採納方式各不相同。Kabeh 點出盲點的結構：**無論你是哪個世代，你都預設其他人經歷同樣的變化、用同樣的方式學習** — 而負責招聘跟培養 junior 的 hiring manager，恰好是另一個世代的人，用自己的學習方式想像別人該怎麼學。世代差異不是新話題，但 AI 把「怎麼學新工具」變成日常，差異從背景噪音變成日常摩擦。

## Claude Code 派 vs 架構派：兩代人的做事方式都對了一半

Soyeb 在大學教 ML 的第一手觀察：給學生出 agentic 架構的實作題，**年輕世代打開 Claude Code 直接開始蓋**，有 15-20 年資歷的工程師則**先想清楚架構、SDLC、企業級軟體的地基**才動手。兩個極端各對一半 — 一邊有敏捷跟原型速度，一邊有三四十年累積的 enterprise-grade 最佳實踐。Soyeb 的結論不是選邊，是這個時點的稀有機會：**兩邊互相學** — 快的學會為什麼要有地基，穩的學會週末就能驗證想法。

## 「AI 能做什麼，人類撿剩下的」— 這個思考方向本身是危險的

有觀眾問業界是否 over-indexing on AI capabilities。Kabeh 同意，並指出危險的具體形狀：**「我們太常先問 AI 能做什麼，然後把 leftover 留給人類。」** 這個順序的問題在於它把人類定義成殘差項 — AI 的能力每 18 個月變一次，殘差項就跟著每 18 個月重算一次，你的 workforce 規劃永遠在追著 AI 的尾燈跑。

## 終態不可知，所以要錨在不變的東西上

「我們不知道未來 18 個月、3 年會長什麼樣 — **that end state is truly unknowable**。」這句話聽起來是放棄，其實是策略的前提：既然追「明日的職位、明日的技能」注定每 18 個月重來一次，就反過來問 — **什麼不變？** Human foundation（問題解決、創造力、創新、對使用者的同理）不變，核心技術能力的判斷層不變。錨在這裡，workforce 就有了 **optionality** — SOC analyst 能變 compliance champion，正因為他的中層能力是可攜的。

## AI can substitute humans, but it can also make us superhumans

Kabeh 對 over-indexing 之問的收尾：**「AI has the ability to substitute humans, but it can also make us superhumans. It is up to us what side of that story we want our organizations to be.」** 這不是雞湯 — 前面整場已經給了兩條路的工程圖：substitute 之路是 heat map 當砍人清單、capacity 拿去清 backlog、情緒線放著跌；superhuman 之路是擴張人類工作、新價值承接 capacity、把人拉過 messy middle。兩條路用的是同一批工具。

## Junior talent 學法律業：僱用的是學習能力，不是現有技能

最後一個問題最棘手：AI 輔助開發的環境裡，junior 的位置在哪？Kabeh 最喜歡的模型借自法律業：**律所僱 associate，買的不是他現在會什麼，是他「無論未來的案子長怎樣都學得會」的潛力**。對應到科技業：僱 junior 看 learn/unlearn/reinvent 的能力加核心技術底子，但別太用力檢查具體技術技能 — 那些技能很可能在他成長為資深之前就過期了。

## Entry-level 不會消失，但 ramp 變陡了 — 需要刻意的 coaching

Soyeb 補完 junior 議題的另一半：**entry-level 職位不會消失，但價值爬坡變陡了** — 以前 junior 靠做 routine 工作邊做邊學，現在 routine 給了 AI，junior 必須更快爬到判斷層才開始產生價值。坡變陡的補償機制只有一個：**stronger intentional coaching**。組織不能再假設 junior 會在 routine 工作裡自然長大，得刻意建造學習的鷹架。Kabeh 給 junior 本人的建議則是一句金句：**「Stay curious even if AI makes it easy not to be.」**

---

## 恍然大悟：整場 webinar 在教同一件事 — 把賭注從「會變的」搬到「不變的」上

回看全場，每個框架都在做同一個動作：**在加速變化的系統裡找到不動點，把規劃、考核、招聘、職涯全部錨上去**。前半場的不動點是 capability 跟 workflow，後半場輪到 human foundation 跟學習能力 — 連 junior 招聘都在錨定「不隨技術棧過期的潛力」。這就是「keep up with AI」的真正解法：不是跑得跟 AI 一樣快（不可能，它 18 個月換一代），而是站在 AI 怎麼換代都不會移動的地方。

跟得上 AI 的 workforce，恰恰是那個不去追 AI 的 workforce。

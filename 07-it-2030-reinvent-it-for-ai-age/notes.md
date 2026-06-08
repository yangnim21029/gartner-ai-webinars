# IT 2030: How CIOs Should Reinvent IT for the AI Age

> **來源**：Gartner Webinar, Rajesh Kandaswamy（Distinguished VP Analyst）。研究始於 2025 年底，與多位同事合作，吸收大量客戶回饋成形；workforce 段直接引用 Kabeh Vaziri 團隊的研究（即本筆記庫 04 場的同一條線）
> **涵蓋**：CIO 視角的「IT 自身怎麼被 AI 重造」。四個 North Star archetypes（Lean / Amplified / Democratized / Dual Builder）、三種轉型速度、tiny teams 與鑽石組織、tech stack 三層 readiness（AI → agent → democratization）、build vs buy 2×2、三場現場 poll 數據

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| Democratization | 業務部門自己動手建科技——shadow IT 的去污名化升級版 |
| Shadow IT | 業務繞過 IT 偷偷建系統的舊稱，帶風險與失控的負面意涵 |
| Vibe coding | 用自然語言跟 AI 對話式寫程式，不逐行手寫 |
| No-code agent builder | 不寫程式就能組 AI agent 的工具 |
| Archetype | 原型——這裡指 IT 未來態的四種典型模型 |
| Lean IT | 需求持平、IT 靠 AI 變得更小更有效率 |
| Amplified IT | 需求上升、人數編制（headcount）不升、AI 效率補上缺口 |
| North Star | 北極星——全組織抬頭對齊的那個未來態 |
| Enablement | 把人扶上手的配套：工具、訓練、護欄 |
| Reskilling | 重訓——把現有員工的技能組合換到新工作需要的版本 |
| Democratized IT | 需求大增、IT 不擴編、部分需求由業務自建滿足 |
| Dual Builder IT | IT 與業務都在 build、組織像 tech company 運作 |
| SDLC | Software Development Lifecycle，軟體開發生命週期 |
| Tiny teams | 一兩個開發加一兩個業務的小隊，靠 AI 放大產出 |
| UAT | User Acceptance Testing，使用者驗收測試 |
| Headless application | 只買底層引擎不買 UI 的「無頭」軟體 |
| AI-ready / agent-ready / democratization-ready | tech stack 的三層就緒：餵得動 AI → 跑得動 agent → 接得住業務自建 |
| Rogue agent / agent sprawl / orphaned agent | 失控 agent／agent 蔓生／沒人認領的孤兒 agent |
| Front office / back office | 面對客戶的應用／後台營運的應用 |
| Opportunistic（速度檔位） | 搭業務投資 AI 的順風車升級 IT |
| AI-first（速度檔位） | 不等業務，主動超前投資 IT 的 AI 化 |

---

## 這場 webinar 要做的事

Rajesh 要回答董事會正在問 CIO 的問題——「比起用 AI 交付業務價值，你是不是該先重造 IT 自己」，交付三樣東西：

1. 一組未來態模型：四個 archetypes 當 North Star，讓 CIO 跟 CEO 對齊「IT 要長成什麼樣」
2. workforce 的重訓藍圖：哪些職能自動化到什麼程度、reskilling 多深、用什麼速度走（cautious / opportunistic / AI-first）
3. tech stack 的演化路線：從 AI readiness 走向 agent readiness 與 democratization readiness，外加 build vs buy 的 2×2 決策圖

## 要建立的心智模型

讀完這篇你要建立五個認知：

1. IT 的未來態不是單選題的標準答案——四個 archetypes 沒有進化順序，選保守不算錯，唯一的錯是跟 CEO 沒對齊
2. Democratization 已經去污名化——五年前叫 shadow IT 人人喊打，現在 97% 的組織某種程度上接受它，而 IT 對「IT 外建造的技術」嚴重缺乏規劃
3. AI 時代沒有 clear end state，所以組織形態從大 program team 變 tiny teams——找 pattern、建平台、小隊到處套用
4. 說來諷刺，agents 最適合的反而是乾淨的流程——想用 agent 拯救爛流程的人，會在例外被一條條寫死的過程中撞上報酬遞減
5. Tech stack 的就緒是三層疊加不是三關闖完——AI-ready 還沒做完，agent-ready 跟 democratization-ready 已經在排隊

下面 41 個知識點就是把這五點拆開填滿。

---

## 能重塑 IT 的力量很多，AI 是根本的那一股

地緣政治、經濟景氣都會衝擊 IT，但 Rajesh 開場就把位階定好：**AI 是會從根本重塑 IT 的那股力量**。這個定位決定了問題的等級——景氣是天氣，AI 是地殼變動；天氣影響你今年的預算，地殼變動決定你的組織還要不要長成現在這個形狀。所以這場的問題不是「IT 怎麼用好 AI」，是「IT 自己要不要被重造」。

## 三個壓力源：效率、democratization、build vs buy

「該不該重造 IT」之所以變成董事會問題，壓力來自三處。一，**AI 驅動的效率**：寫程式、管 IT 都在變容易（沒有媒體吹的那麼誇張，但真實存在），那未來的 IT 該變大還是變小？二，**業務想自己建科技的興趣大增**。三，**build vs buy 的天平在動**：既然能用 AI 直接做、或用 AI 寫程式，自建比例是不是該比以前高？三個壓力源各自打開一個本場的章節。

## Shadow IT 改名了：democratization 的去污名化

業務自建科技不是新現象——幾年前它叫 **shadow IT**，意涵是負面的：沒有護欄的科技濫用，最後爛攤子砸回 IT 頭上。現在它改名 **democratization**，而且還在一路推進：no-code agent builders、vibe coding 這類工具讓業務建得出像樣的東西。名字的轉變不是公關，是實力對比變了——以前業務建的東西注定殘破，現在工具讓他們建得像樣，IT 從「圍堵」轉向「接生」只是時間問題。

## 銀行 CIO 的大支票：三個不想簽的理由

一張**數億美元的 enterprise software 支票**，讓一家大型全球銀行的 CIO 簽不下手——她拿著它問 Rajesh 該不該簽。三個猶豫：一，**不知道 AI 接下來會改變什麼**，簽了長約等於押注現狀；二，**這家 vendor 對華爾街宣稱 AI 帶來 20-30% 效率，但我的帳單沒有降 20-30%**，效率紅利進了 vendor 的口袋，沒進客戶的；三，**買的功能只用一部分**。三個理由各自擊中軟體採購的舊假設：穩定的需求、對等的議價、整包的價值。

## 她的替代方案：用 Claude Code 重建，然後開源

這位 CIO 的下一句更激進：**「我是不是該抽一組開發者，用 Claude Code 之類的工具把這套軟體的一部分自己建出來——然後與其自己維護，直接整個 open source？」** 時間點是 2025 年 9 月，**在市場重挫軟體股之前**。一位管理數億美元軟體預算的買方，已經在認真評估用「自建 + 開源」取代「續約大 vendor」的可行性——這不是論壇上的嘴炮，是真金白銀的決策現場。

## 三個交付物：North Star、reskilling 的深度與速度、tech stack

三個交付物的順序本身有意義：**先定終點（North Star archetypes），再定人怎麼走（reskilling 的深度與速度），最後定地基怎麼改（tech stack）**。倒過來做的組織會先改地基、再發現終點不在那個方向。三項裡最常被漏掉的是速度：AI-first 的全押跟高度謹慎都可以是對的，看產業性質——reskilling 多深是一題，走多快是另一題。

## 未來態的三個決定因素：supply、demand、democratization 胃口

決定你的 archetype 要看三個因素。**Supply**：AI 效率讓同樣或更少的人做更多事；人數跟工作產出量是兩個變數，脫鉤的幅度看你的胃口。**Demand**：不是業務今天的樣子，是他們的志向——要進新市場嗎？要拉毛利、改客服嗎？軌跡往哪走？**Democratization 的胃口**：你的業務想自己建多少？前兩個因素是老的供需對接，第三個是新變數——它的出現讓「IT 的未來態」第一次不完全由 IT 決定。

---

## 恍然大悟：IT 的未來規格，第一次要由 IT 以外的人共同決定

開場七個點的共同訊息藏在第三個因素裡：supply 跟 demand 是 CIO 熟悉的變數，democratization 不是——它問的是「業務想自己動手到什麼程度」，答案在業務手上、在 CEO 腦中、在工具的演化裡，唯獨不在 IT 的規劃文件裡。銀行 CIO 的支票猶豫也是同一件事的鏡像：連 buy 的對象都在被 AI 重新定價。IT 規劃的座標系從「我們能交付多少」換成了「整個組織想怎麼建科技」。

重造 IT 的第一步不是技術盤點，是去問一圈 IT 以外的人。

---

## Lean IT：需求持平，IT 變小

第一個 archetype：**需求大致不變，但期待 IT 靠 AI 更有效率，規模比今天小一點**。這不是失敗者的選項——Rajesh 遇過直說「我的 CEO 就是期待 lean IT」「我們被私募基金持有，就是要這樣走」的組織。Lean 的本質是把 AI 紅利全數兌換成成本下降，適合技術只是支撐、穩定壓倒一切的處境。

## Amplified IT：需求上升，headcount 不動，AI 補缺口

第二個 archetype：**看得到需求增加，但沒有擴編 IT 的胃口——用 AI 驅動的效率去接住多出來的需求**。AI 紅利的兌換方式從「省人」換成「擴產」：同一批人交付更多。這是四個模型裡最不需要說服別人的一個：不動組織結構、不動權責邊界，只動生產函數，所以它也常是預設值——而預設值自有預設值的風險。

## Democratized IT：需求大增，業務自己接一部分

第三個 archetype：**需求顯著增加、IT 資源不增，預期一部分需求由業務直接滿足**。IT 仍然要靠 AI 多交付，但承認一件事：需求的增速已經超過 IT 產能的增速，缺口由業務自建補上。這個模型的成敗不在 IT 的交付力，在 IT 的**接生力**——enablement、護欄、工具策展做得好不好，決定業務建出來的是資產還是下一代 shadow IT。

## Dual Builder IT：全公司都在 build，像 tech company 運作

第四個 archetype 最激進：**技術的潛力大到組織開始像 tech company 思考——減少 buy、增加 build，業務要變得更會建，IT 也要加碼投資**。所有人都在 build，所以叫 dual builder。它對應的處境是技術本身就是競爭武器：競爭者或新進者推出一個技術產品就可能傷到你的生意。它呼應銀行 CIO 的軼事：「自建 + 開源取代大 vendor」就是 dual builder 的思維在運作。

## 四個 archetypes 不是進化鏈，是選擇題

Rajesh 特別防一個誤讀：**這不是從 lean 一路升級到 dual builder 的 progression**。有人從 amplified 走向 democratized、從 democratized 走向 dual builder，都可以，但沒有「自然的下一關」。判斷只有兩個軸：**你的 AI 轉型只動技術側，還是也要動業務側**（前者 lean/amplified 夠用，後者要 democratized/dual builder）；以及**技術對你的生意多 vital**——有些地方穩定壓倒創新（stability trumps innovation），lean/amplified 是對的答案。同樣重要的：**你選的，跟你 CEO 心裡想的，是同一個嗎？**

## 現場 poll：democratized 41% 領先，94% 的人心裡有答案

現場投票結果：**democratized IT 41%、amplified 35%、dual builder 10%、lean 8%、不知道 6%**。Rajesh 的兩個讀法：一，democratized 領先、amplified 居次，跟 Gartner 在客戶對話裡看到的一致；二，**只有 6% 說不知道**——94% 的 CIO 對未來態心裡有圖像。追問也跟著來：有圖像，但有 deliberate plan 嗎？圖像跟高管對齊了嗎？

## 最危險的低投資：IT 外建造的技術，沒人在規劃

現在 IT 部門裡所有的功課都在「IT 怎麼在 AI 世界做得更好」，**但對「將在 IT 之外被建造的技術」，規劃投資少得危險（we are dangerously underinvesting in planning）**。Poll 都顯示 democratized 是最大宗了，問題就變得很實際：enablement 準備了嗎？governance 準備了嗎？工具呢？41% 的人選了一個自己還沒開始為它鋪路的未來——這是全場最大的知行落差。

---

## 恍然大悟：選 archetype 的真正產出不是答案，是跟 CEO 的同一張藍圖

四個 archetypes 看似分類學，實際是一個對齊儀式：lean 還是 dual builder 沒有對錯（私募控股選 lean 跟科技競爭選 dual builder 都是理性的），錯的只有一種——CIO 心裡的圖跟 CEO 心裡的圖不是同一張。Poll 的 94% 知道答案令人安心，但「知道自己的答案」跟「組織共享這個答案」中間隔著整個轉型的成敗；而 41% 選 democratized 卻沒人規劃 IT 外的建造，就是這條縫隙的具體形狀。

North Star 的價值不在它指哪，在於全組織抬頭看到的是同一顆星。

---

## Human-AI 協作有五級，不是「取代／不取代」二選一

Workforce 段直接引用 Kabeh Vaziri 團隊的研究（04 場的同一條線）：human-AI 協作用**五點量表**衡量，不是換不換人的二元題。最低級是**旁邊開著用**：開發者開個 AI chatbot 生 code snippet，複製貼上。中間級是**任務級**：同一個開發者用 AI 生成測試腳本、跑測試、寫文件。最高級是**整條 SDLC**：不只開發，設計、部署、測試全程有 AI。級距拉開之後，「該自動化到第幾級」才變成一個可以討論的決策。去年 symposium 的數據：今天約五分之一的 IT 工作有 AI 參與，幾年內會是全部。

## 速度有三檔：cautious、opportunistic、AI-first

自動化能到幾級是一回事，**你該用什麼速度走是另一回事**。三檔：**cautious**，謹慎壓倒創新，產業性質使然；**opportunistic**，趁業務投資 AI 的時候順勢把 IT 的升級夾帶進去；**AI-first**，不等業務，主動超前投資。檔位沒有對錯，但有後果：你選的檔位決定了每個 IT 職能的自動化天花板。

## Software engineering 2030 自動化 4.8/5——headcount 卻在漲

AI-first 公司的 2030 預測裡，最搶眼的數字：**software engineering 的自動化程度 4.8/5**，enterprise applications 也很高，IT core 則沒那麼高。直覺推論「那 headcount 該掉了」——Rajesh 說資料相反：**software engineering 跟 cybersecurity 的 headcount 趨勢向上**。機制跟 06 場的工作誕生公式同構：效率降低了單位需求，但釋放的能力創造了更多可被滿足的新需求，淨需求反而增加。CIO 們的現場體感一致：需求在漲。

## Cybersecurity 的特殊地位：連 cautious 檔都必須自動化

每條職能線都隨檔位放緩，唯一的例外是 **cybersecurity**：就算你選 cautious，這條線仍然要求一定程度的自動化投資。理由一句話講完：**你不完全掌控自己的命運**——對手是 bad actors，他們的攻擊速度不會因為你選了謹慎檔而放慢。安全的自動化不是效率選項，是軍備競賽的入場費。

## AI 時代沒有 clear end state——但你還是要鞋子

組織形態的前提變了。ERP、core banking、供應鏈、internet——過去的大轉型都有清楚的終點，所以可以開大 program team 直奔目標。**AI 沒有 clear end state**：Rajesh 問在場的人，幾乎沒人說得出自家組織的 AI 終態。他的比喻：這像「跑一場有終點的賽事」跟「朝一個方向跑」的差別——兩種都要訓練、都要鞋子，差別只在你知不知道終點在哪。不知道終點不是不跑的理由，是換一種跑法的理由。

## Payroll 公司案例：一隻 email agent 的誕生

一家 payroll 公司常收到客戶 email：「Lucy 不是做 30 小時，是 42 小時，週末跑薪資前改一下。」格式五花八門，以前靠人工處理。他們建了一隻 AI agent：**讀信、判斷要做什麼、抽出資料、查內部系統、驗證、跟人類確認、執行修改**。客戶開心（更快）、公司開心（更省）。到這裡只是一個不錯的自動化故事——真正的招在下一步。

## Use case 不可複製，pattern 可以：平台 + tiny team

公司發現這個 use case 沒辦法到處複製，**但底下的 pattern 可以**：處理 email → 抽資料 → 驗證 → 問人類 → 執行交易。同一個 pattern 在客服、sales enablement、其他領域都成立。於是他們把 pattern 做成**平台**，配一支**極小的技術團隊**，搭一兩個業務端的人，**主動**到各領域找機會套用。Rajesh 把這定為當代 AI 轉型的標準動作：找到新做法 → 挖出底層 pattern → 平台化 → 有條不紊地到處套用。不開大團隊，開小分隊。

## Tiny team 的成員都要 stretch——agents 跟著 process 走，不跟著 product

Tiny team 可能就一兩個開發加一兩個業務人，所以**每個人都要越界**：開發者不能說「我只寫程式」，資料庫、測試都要碰；業務人可能要設計 UI、跑 UAT。邊界要跟著工作的形狀走——這個邏輯放大到組織層也成立，而它戳破了近年的組織風潮：很多公司剛辛苦推完 product teams，很好，但 **agents are not about products; they are about process**。Agent 沿著流程跑，流程橫切多個產品團隊的邊界，所以 product team 的切法接不住 agent 的工作形狀。剛改完組織的人，可能要再改一次。

---

## 恍然大悟：終點消失的時候，組織的單位從「程式」變成「pattern」

大 program team 的存在前提是終點清楚——知道要去哪，才敢編列千人團隊直奔。AI 把終點抹掉了，於是組織的合理單位縮小到能快速試錯的尺寸：tiny team 抓一個 use case、挖出 pattern、平台化、再帶著平台去掃描整個組織。這個迴路裡真正能重複使用的資產不是程式碼，是 **pattern**——payroll 公司賣的不是那隻 email agent，是「讀信驗證執行」這個可遷移的形狀。04 場說團隊「為一個業務問題聚合、解完即散」，這場補上了聚散之間留下的東西。

沒有終點的賽道上，跑得快的不是大部隊，是帶著地圖複印機的小隊。

---

## 金字塔變鑽石：tiny teams 把組織底層擠窄了

把 tiny teams 的趨勢推演到底：它們多半在組織低層運作——實際做事的地方——一兩個人加 AI 就能交付。低層的人數需求縮減，**組織形狀從金字塔變成鑽石**：底窄、中寬。03 場從 comms 行業看到同一個形狀（entry-level 變少、mid 變多），這場從 IT 整體確認了它不是單一行業的現象，是 AI 時代的組織幾何。

## 底層變窄之後，明天的領導人從哪裡來

鑽石形狀直接逼出兩個問題：**我們準備好做這個改變了嗎**，以及更深的——**底層變窄，明天的領導人在哪裡養成**？這是本筆記庫第三次撞上同一面牆：04 場的「entry-level ramp 變陡需要刻意 coaching」、06 場的「達文西手術機器人不接管手術、保護住院醫師 pipeline」，到這場的鑽石組織。三場三個視角，問題一個字不差——自動化吃掉的不是職位，是職位附帶的養成功能。

## 第二場 poll：97% 的組織某種程度接受 democratization

現場第二次投票，問 democratization 的態度：**選擇性鼓勵 33%、允許但沒有清楚的企業策略 24%、謹慎限制中 24%、積極推動且有平台與護欄 16%、積極勸阻 3%**。Rajesh 的解讀抓在那個 3%：**五年前問 shadow IT，勸阻的比例會高得多**——AI 改變了人們對「業務用技術」的心態。97% 某種程度的接受，加上第一場 poll 的 democratized 41%，方向已經沒有懸念，剩下的全是執行題。

## Democratization 的治理 = enablement：說 no 已經不是選項

**這個時代對 democratization 說 no 已經不太可能**——democratization 在前進，工具一代比一代易用。有觀眾問：當年 Microsoft Access 生出一堆 shadow IT，怎麼擁抱 AI 又不讓 AI 程式碼重演歷史？Rajesh 先收掉「圍堵」這個幻想，再給出路。能做的是同時抓 governance 跟 enablement：**策展工具**（給特定業務人指定工具，展現熟練度後再升級權限）、**sandbox**（圈一塊地讓人安全地建）、**按 business capability 挑場地**（挑你能控風險又有效益的能力區先開放）。治理的單位不是工具，是場地。

## 「Department of no」的翻身法：用一個具體的流程改革當訊號

另一個問題直戳痛處：過去三年把自己做成「department of no」的 IT 團隊，怎麼在 AI 浪潮前翻身？Rajesh 的藥方是**用具體訊號宣告行為改變**：給一群業務人開 no-code agent builder 的場地、簡化一條人人有感的流程。他舉一位 AI leader 的實例：把 vendor management 從 assessment-based 改成 rating-based——以前審一個 vendor 要八個月，而「八個月」在一個 15 個月前還沒人聽過 AI agent 的世界裡，等於拒絕參賽。流程改革是 IT 能發出的最響亮的「我們變了」。

## 高監管產業不是不能玩，是挑 pocket 玩

產業差異的問題，Rajesh 給了務實的答案：高監管產業（銀行、部分醫療）的 dual builder 空間較小（合規讓全面自建變難），**但他們不是放棄，是挑小範圍（pockets）玩**：在組織裡圈出特定區域做 democratization 跟 dual builder，配足夠的護欄。更值得記的是趨勢句：連公部門跟高監管醫療都在問「我哪些部分可以 democratize」——整體向 democratization 與 dual builder 漂移，跟幾年前完全不同。

## Agents 的最大反諷：它們最適合的，是本來就乾淨的流程

高監管環境的 agentic ROI 問題，引出全場最值得抄下來的句子。先列風險清單：rogue agent、agent sprawl、orphaned agents 都真實存在。但 ROI 的關鍵不在監管強度，在 use case 的強度，而最大的陷阱是：**想用 agent 自動化一條低效、不清不楚、資料髒的流程**。Rajesh 講了兩次：**「Ironically, agents work best when the process has clarity and the data is clean.」** 配套警告：流程沒有 scale 就沒有效益；例外太多就會陷入一次次 hard code，**報酬遞減馬上到**。解法：先**為 agent 重新設計流程**（不是為人類設計），或跨單位合併流程再上 agent——然後仍然要算完整的 ROI business case，把 agent 的變動成本算進去。

---

## 恍然大悟：democratization 的治理難題，跟 agent 的部署難題，是同一道題

這一段的四個 Q&A 共用一個結構：**先把地整好，才能放東西上去**。Democratization 要先圈場地、配護欄，才能放業務進來建；agent 要先把流程弄清楚、資料弄乾淨，才放得上去——想反過來用 agent 拯救爛流程、用 democratization 掩蓋治理真空，都會在例外與事故裡付出加倍的代價。06 場的 tribal knowledge 結帳、05 場的 feasibility 看資料家底，到這場的「agents work best when the process has clarity」——四場 webinar 用四種口音說同一句話。

AI 不獎勵勇敢的組織，獎勵整潔的組織。

---

## AI-ready 只是第一關：agent readiness 跟 democratization readiness 在排隊

Tech stack 段的核心訊息：你們都在拚 AI readiness（data 要 AI-ready、apps 要 AI-enhanced、middleware 要夠強、infra 要扛得住），很難，Rajesh 都懂。**但 2030 的 stack 演化是三層：AI readiness 之後是 agent readiness，再來是 democratization readiness**。而且不是闖完一關開下一關——業務的需求會逼你三層並行，有些工作就是得提早做。

## Agent readiness 的第一步是 audit——順便停掉過時的計畫省錢

Agent readiness 怎麼開始？退一步問：**你的 IT stack 哪些部分能給 agent 最高的槓桿**？該為它們做什麼投資？然後是一個常被漏掉的省錢動作：**盤點那些在「大家認識 AI agents 之前」設計的轉型計畫**——有些還在跑。與其按舊圖紙轉型一次、再為 agent 轉型第二次，不如現在就停掉重排。轉型最貴的不是做，是做兩次。

## 出事的時候，誰接電話

**業務建的東西出事時，接電話的多半還是你組織裡的人**——Rajesh 對 democratization readiness 最根本的質問就這麼直白。業務想從「用技術」走向「建技術」，很好，但他們也想「運維它、保護它」嗎？所以 democratization 的設計必須包含 ownership 的談判：業務要 own 到哪一層？這段對話要趁早，因為事故發生後再談分工，結論永遠是 IT 收爛攤。

## Hold the line 的分層：日常開放，核心固守

Ownership 談判的可行解是分層：圈出 **everyday democratization** 的區域（這些業務可以自己建）；同時圈出 hold the line 的區域，例如銀行的 core banking：**業務可以用，但 IT 建、IT 運維**。這個分層既給了 democratization 出口，又守住了不能出事的底線——而且它天然銜接 dual builder 的路徑：先分層，再逐步把可開放區擴大。

## 把 UI 層整個送給業務：「Knock yourself out」

分層的極端案例：一位全球最大企業之一的 CIO 告訴 Rajesh，他們**正在認真考慮把所有 UI 的建造整個交給業務**：IT 不再管 UI，業務直接自理，原話的態度是「knock yourself out」（隨你們玩）。應用的分層結構（上層 UI、中層 workflow 與 business logic、底層 systems of record——存放主資料的核心系統）裡，democratization 從最上層開始啃；而 **AI agents 正在把那條線往下推**，workflow 跟 business logic 也開始可以由 agent 承擔。每個 CIO 都該標出自己的線在哪、打算讓它降到哪。

## Build vs buy 的 2×2：技術複雜度 × 業務差異化

回應銀行 CIO 的支票問題，Rajesh 給了一張 2×2：軸是**建造的技術複雜度**跟**業務差異化程度**。四格四策。**簡單 + 無差異**：換掉，用 custom AI 自建或找 AI-native 新 vendor，別在裡面買嵌入式 AI。**簡單 + 高差異**：這是你的命脈卻好建，危險，趕快用 AI 或新 vendor 強化位置。**複雜 + 低差異**：不值得換，在上面加 AI 就好。**複雜 + 高差異**：策略級投資，把優勢再往深處挖。把你的關鍵應用一個個丟上這張圖，2030 的軟體策略就有了底稿。

## Headless 談判與長約警告：vendor 想往上爬，你要往下拆

2×2 的延伸動作：與其整包買下從 UI 到底層的軟體，**開始跟 vendor 談 headless（無頭）或拆包（unbundled）的買法**。Rajesh 預告：他們不會喜歡——vendor 的策略是往上爬，賣你更多 AI agents。他在一場會議問「誰**沒**被 enterprise vendor 推銷過 AI agents」，前排有人苦笑說天天被打電話。配套警告：**在會被 AI 衝擊的領域，長約要想清楚再簽**（transcript 此句語意稍含糊，依上下文取「簽長約前三思」解）——銀行 CIO 那張支票的猶豫，就是這條警告的真人版。

## 第三場 poll：build 派抬頭，36% 要 somewhat more build

現場第三次投票，問 2030 的 build vs buy 組合會怎麼移：**somewhat more build 36%、不變 26%、somewhat more buy 19%、significantly more build 10%、significantly more buy 10%**。兩個 significantly 互相抵消，四分之一不動，剩下的明顯偏向 build——跟 Gartner 的觀察一致。Rajesh 的追問：說要 build 更多的人，**配套投資跟上了嗎**——跨 SDLC 的 AI 工程工具、挑「競爭優勢領域」而非 commodity 來 build、管理轉移的方法？方向票好投，配套錢難花。

---

## 恍然大悟：stack 的三層 readiness，其實是三次主權重劃

AI-ready 是技術題（資料、中介層、算力），但 agent-ready 跟 democratization-ready 是主權題：agent 把自動化的線從 UI 往下推進 workflow，democratization 把建造權從 IT 往外推給業務，build vs buy 的天平把價值鏈從 vendor 手裡拉回自家——三層 readiness 每一層都在重劃「誰擁有什麼」的地圖。這解釋了為什麼 vendor 瘋狂推銷 agents、為什麼長約變危險、為什麼 ownership 談判要趁早：所有玩家都看見了同一場重劃，先佔位的人定規則。

Readiness 聽起來是準備工作，其實是圈地運動。

---

## 能不能跳關：yes and no，但絕不是純 sequential

有人問：能不能跳過 AI-ready 直接做 agent-ready，甚至直奔 democratization-ready？Rajesh 的回答兩面都給：**有依賴**——AI-ready data 是 agent readiness 跑不掉的地基；**但有些可以獨立先行**——例如 agent readiness audit（盤點哪段應用 stack 要先就緒）不需要等整個 AI readiness 鋪完。操作建議：三層一起想、不急著全部定案，部分工作現在就動。把它想成疊加的工程，不是闖關的遊戲。

## Agent 輸出品質的架構模式：有，但還嫩

高風險 use case 怎麼確保 agent 輸出品質？Rajesh 誠實回答：**evaluation patterns 跟 guardrail patterns 存在，Gartner 也出版了一批，但成熟度遠不如 agent 的開發面**。這個誠實值得保留——它標出了 2026 年中 agentic 工程真正的弱點：建得出來，驗得還不夠好。對照 04 場「model validation 是 risky-to-lose 技能」，人類的驗證能力在這個空窗期裡格外值錢。

## 最大的顛覆會落在哪：front office 還是 back office，看你的生意

最後一個問題：短期內 mix 改不動，但哪裡會先被重度顛覆？Rajesh 的答案是條件式的：**客戶與品牌導向的組織，顛覆先到 front office apps**（你跟軟體互動的方式）；**資產密集的組織（如石油天然氣），先到 back office**。沒有普世答案，但有普世方法：問自己的價值是在介面上創造的，還是在資產運轉裡創造的——顛覆會從價值密度最高的地方進門。

## Deliberate plan 是 IT 能為 AI 時代做的最大一件事

Rajesh 的收束把全場壓成一句：**「Having a deliberate plan and transforming IT is the single biggest thing that IT can do to transform your business for the AI era.」** 三段內容各自回扣：archetype 給計畫一個終點、workforce 給計畫一個速度、tech stack 給計畫一個地基。而 deliberate 這個詞是對照組出來的——對照的是 94% 心裡有圖像、卻對 IT 外的建造嚴重缺乏規劃的現狀：有圖像不等於有計畫。

---

## 恍然大悟：這場的真正主題不是 IT 2030，是「誰來決定 IT 是什麼」

回看全場，「重造 IT」聽起來是內部工程，實際是四張談判桌：跟 CEO 談 North Star、跟業務談 ownership、跟 vendor 談拆包、跟未來的領導人才談養成。Deliberate plan 的真正功能在這裡現形——它不是進度表，是談判籌碼：四張桌上有計畫的那一方定規則，沒計畫的那一方接受別人的計畫。94% 心裡有圖像、卻沒人規劃 IT 外建造的現狀，翻譯過來就是：多數人帶著感覺上桌，等著被有計畫的人開價。

2030 的 IT 不是被 AI 重塑的——是被那些先想清楚的人重塑的。

# Leading EA in 2026: A Guide for AI-Enabled Transformation

> **來源**：Gartner Webinar, Lucas Kobat（Director Analyst, Chief of Research for Enterprise Architecture）。互動式場次，含兩輪現場 poll 與大量 Q&A
> **涵蓋**：Head of EA 視角的 2026 生存指南。EA 的身份危機與三群不滿的 stakeholder、五大 imperatives（AI 領導真空、untangle AI rollout、dynamic architectures、雙帽投資顧問、用 AI 重造 EA 自己）、adaptive governance 四風格、assurance by partnership、EA 工作 AI 化的 14%→23%→30% 曲線

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| EA / Head of EA | Enterprise Architecture 企業架構／企業架構主管 |
| BU | Business Unit，業務單位 |
| CIO / CTO / COO | 資訊長／技術長／營運長等 C 字頭高管 |
| TOGAF | 最流行的 EA 框架之一，常被組織當聖經執行 |
| AI sprawl | AI 工具與 agent 在組織裡無序蔓生的狀態 |
| Composite AI | 把機器學習跟生成式 AI 配對使用，取得更精細的能力 |
| Agentic systems | 主要不需人類介入就能運作的自主系統 |
| Adaptive governance | 治理風格隨情境切換的框架，四檔：control / outcome / agile / autonomous |
| Guardian agent | 專門看管其他 AI agent 的 agent |
| Elevator architect | 能上下移動樓層的架構師：下到交付現場、中到 portfolio、上到瞭望塔 |
| Future state / current state | 目標架構藍圖／現況架構 |
| Dynamic state architecture | 不畫固定終點藍圖，即時監控現況、動態重構的架構方法 |
| Sovereignty（主權風險） | 雲、AI、業務能在哪個地理區運作與採購的限制風險 |
| Assurance by partnership | 用陪跑取代文件審查的品質保證方式 |
| Orchestration layer | 讓多個 agent 協同完成組織目標的調度層 |
| CoE | Center of Excellence，卓越中心 |
| POC | Proof of Concept，概念驗證 |
| Magic Quadrant | Gartner 的供應商評比框架 |
| Signature survey | Gartner 對 heads of EA 的年度旗艦調查 |
| Design-first | 先畫完整設計文件再動工的舊習慣 |
| Toolmate | 把 AI 當隊友而非工具的協作概念 |

---

## 這場 webinar 要做的事

Lucas Kobat 要回答「EA 這個職能在 AI 時代還有什麼用」，分三段交付：

1. 診斷 2026 年 EA 的現狀：三群 stakeholder 的不滿、signature survey 的信心數據、AI sprawl 與成本困境的雙面夾擊
2. 給五個 imperatives：搶進 AI 領導真空、untangle AI rollout、建 dynamic architectures、同時當 financial advisor 跟 VC、用 AI 重造 EA 自己
3. 收一輪現場 poll 與 Q&A，標定同行的優先順序（dynamic architectures 險勝）與共同障礙

## 要建立的心智模型

讀完這篇你要建立五個認知：

1. EA 的身份危機不是抽象焦慮——delivery 團隊已經在問「能不能用 AI 取代 EA」，34% 的 heads of EA 承認自己證明不了價值
2. AI 領導權是一個真空——多數組織沒有 dedicated AI leader，誰先補位誰定方向，而 EA 的跨域視角是最有資格的候選人
3. EA 的舊作業系統（design-first、文件保證、固定藍圖）在 AI 速度下全面失效——替代品是輕護欄、陪跑、動態重構
4. EA 要同時戴兩頂帽：financial advisor 砍現在的浪費，venture capitalist 掃 12-24 個月的地平線
5. 重造別人之前先重造自己——EA 工作的 AI 增強比例兩年內要從 14% 走到 30%，自己做到了，走進房間才有 credibility

下面 38 個知識點就是把這五點拆開填滿。

---

## 三群 stakeholder，三種不滿，同一個結論

EA 服務的三群人各有怨言，而且積怨已久。**Delivery 團隊**：EA 拖慢交付，是治理路障。**業務領導**：我只想趕快拿到我的新工具，怎麼繞過架構治理？**高管**：你們給的指引太技術、太 IT 中心，看不懂也用不上。三條怨言的箭頭指向同一個結論：這個職能的存在理由正在被質疑——而質疑的具體形狀，比想像中難聽得多。

## 「能不能用 AI 取代 EA」——這句話已經被問出口了

三群人的質疑各自有了 2026 年版本：delivery 團隊跟 IT 開始問**「我們能不能直接用 AI 能力取代 EA」**；業務領導問「這個 EA 團隊到底為什麼存在」；高管看著 EA 的產出問「價值在哪」。第一句最致命——當你的服務對象開始評估用 AI 換掉你，問題已經不是滿意度，是替代性。這也是整場 webinar 的張力來源：EA 要嘛搶到 AI 的方向盤，要嘛變成 AI 的替代清單上的一行。

## Survey 證據：EA 自己也知道——34% 承認證明不了價值

2026 Heads of EA signature survey 的數據跟怨言對得上。Heads of EA **最沒信心**的三件事：爭取 EA 的資源、預算或人力；幫組織判斷與導航這個動盪世界的衝擊；把 AI 規模化（在自己團隊內與全企業）。再疊一刀：**34% 的 heads of EA 承認無法有效展示 EA 能力的價值與投資報酬**。內外證詞一致，診斷成立：問題不在個別團隊做得差，在職能本身的版本過舊。

## 迭代式改良救不了，需要 complete reimagination

Lucas 的判決：多群 stakeholder 的需求同時落空，**對 EA 職能做迭代式的小修小補註定失敗**——需要的是 complete reimagination，整個重新想像。這個判決框住了後面五個 imperatives 的高度：它們不是「把現有 EA 做得更好」的優化清單，是一份換職能作業系統的重灌指南。EA 的 identity crisis 不靠修身養性解決，靠換身份解決。

## AI sprawl 是海嘯，CEO 們三年內就要 autonomous

為什麼是現在？因為 AI 能力正像 tidal wave 打進組織：AI-ready data 計畫、edge AI、全員配發生成式工具、agent 進工作流、composite AI（機器學習配生成式）。浪頭上是 **agentic systems**——CEO survey 顯示**多數 CEO 計畫在三年內採用主要不需人類介入的自主系統**。風險清單跟著漲：資料隱私、資安與營運風險、法規、AI 加雲端成本。三群 stakeholder 都在找「組織裡的某個人」來接這件事——**EA is well positioned**，前提是接得起來。

## 成本困境：好砍的都砍完了

另一面夾擊來自錢。成本優化已經連續多年是 top priority，**容易砍的選項早就砍完**；地緣政治天天上頭條（供應鏈、市場、原料採購），氣候事件再補一刀。短期再砍會傷到成長野心本身，長期的結構性削減又慢又難。組織卡在一個平衡題上：**怎麼騰出資源餵養成長，同時扛住今天的短期風險與成本**。這道題後面會長成 imperative 4 的雙帽角色。

## EA 2026 的任務清單：穿過噪音，飛出軌道

Lucas 借 Artemis II 的比喻把任務定出來：EA 要幫組織發射一個**穿過噪音、飛離混戰**的軌道出口。具體四件事：幫組織收割 AI 的紅利同時控住風險；導航經濟與地緣的波動；推動成長野心；縮小 IT 交付能力的差距。執行手段就是五個 imperatives：搶進 AI 領導真空、untangle AI rollout、建 dynamic architectures、guide 技術投資、用 AI 重造 EA——後面逐個拆。

---

## 恍然大悟：EA 的危機不是被忽視，是被三邊同時需要卻三邊都不及格

開場的診斷有個反直覺的結構：EA 不是沒人要（AI sprawl 需要人管、成本平衡需要人算、三群 stakeholder 都在找救兵），EA 是**被需要的方向太多、而現有的版本一個都接不住**。「用 AI 取代 EA」的問題跟「EA 來當 AI 領導」的機會，是同一枚硬幣的兩面：職能的價值真空有多大，補位的獎勵就有多大。所以 Lucas 才說小修小補必死——半新不舊的 EA 同時讓三群人繼續失望。

身份危機的解法從來不是辯護舊身份，是搶下新身份。

---

## AI 領導權是真空的：多數組織沒有 dedicated AI leader

Imperative 1 的事實基礎：CEO 們相信 AI 是三年內最會顛覆自家業務的技術，**但多數組織沒有一個專責的 AI leader**。後果是 EA 最熟悉的那種病：去中心化的實驗、冗餘、重複投資——每個部門自己玩自己的。真空的意思是：這個位子沒有世襲的主人，CIO、CTO、資料分析主管、COO 都可能被指派——**誰先補位、誰能服眾，誰就定組織的 AI 方向**。

## 66% 的 EA leaders 押注自己：2026 年底前成為 AI expert

補位競賽已經開跑：signature survey 顯示 **66% 的 EA leaders 說自己個人投入要在 2026 年底前成為 AI expert**。這個數字跟其他資料點互相印證——heads of EA 正在大批走進 AI 領導角色。三分之二的同行在自我升級，這對剩下三分之一是淘汰訊號：當「懂 AI」成為 EA 主管的標配，不懂的人連辯護舊身份的資格都沒有。

## Make the case：EA 的獨特資產是三向視野

搶位的第一步是說服領導層**EA 是企業級 AI 協同工作的最佳駐地**。論據是視野的幾何：head of EA 同時看得到**業務想去哪**、**IT 組織能撐起什麼**、以及**哪條 roadmap 是現實的**——三向交集是組織裡幾乎沒有第二個角色擁有的。CIO 看得到技術、COO 看得到營運、資料主管看得到資料，但把野心翻譯成可行路線的位置，結構上就是 EA 的。

## 當 source of truth：判斷「什麼需要 AI、什麼根本不需要」

搶位的第二步是在濃霧裡當客觀的聲音。霧有兩層：**vendor 以破紀錄的速度迭代能力**，同時**他們承諾的很大一部分只是行銷炒作**——兩層疊起來，什麼可行、什麼可得、什麼有價值，全看不清。EA 要做的是 source of truth：對每一項 AI 技術與供應商，給出「現實 vs 炒作」的判讀，最終回答那個最省錢的問題——**這裡需要 AI 嗎，還是根本不需要**。

## Orchestrate 投資對齊：每個 BU 都覺得自己需要不一樣的 AI

搶位的第三步直面政治：**每個業務單位都會認為自己需要不同的 AI，每個交付團隊都有自己最愛的模型或工作流**。EA 的工作是把所有人拉到同一張桌、往同一個方向推——這必然包含艱難的取捨：投哪些 AI 技術、不投哪些。不做這個協調的代價前面已經演過：AI sprawl 海嘯、無謂的複雜度、一路堆高的技術債。

## Adaptive governance 四檔：從規則治理到自動治理

搶位的第四步是治理的換檔。Adaptive governance 有四種風格：**control**（靠規則與合規）、**outcome**（按價值排序與分流）、**agile**（持續重新排序、持續重評）、**autonomous**（把治理流程自動化、設計成 agentic 工作方式能通過的形狀，甚至引入 guardian agents 看管其他 agent）。AI 時代的重點在最後一檔：治理對象會自己行動時，治理本身也得會自己行動——用人開會審 agent，速度上就輸了。

## Elevator architect：下到雜草、上到瞭望塔，狠心修剪

搶位的最後一步是建 **AI watchtower** 量測成敗，而它屬於一個更大的隱喻：**elevator architect**。會搭電梯的架構師在三層樓之間移動：下到雜草層幫交付團隊全速推進 AI initiatives；中層幫 portfolio 與業務夥伴鋪一條通往成功的 roadmap；最上層進瞭望塔，看清什麼有效、什麼無效——然後**快速 kill 掉無效的**，把 portfolio 修剪成真正能贏的形狀。塔的價值不在看得遠，在敢下剪刀。

---

## 恍然大悟：領導真空的入場費，是願意當壞人

五步搶位法（說服、判讀、協調、治理、修剪）有一條隱形的共同線：每一步都要**說別人不想聽的話**——告訴 vendor 的擁護者「這是炒作」、告訴 BU「你的最愛不投」、告訴專案主人「這個要關掉」。AI 領導真空之所以是真空，部分原因正是這些話沒人想說；EA 的跨域視野給了它說這些話的資格，但資格要兌現成權威，靠的是一次次把難聽的判斷說對。

真空裡最稀缺的不是懂 AI 的人，是敢給 AI 說不的人。

---

## 只有 40% 的 EA leaders 相信 AI 投資會帶來財務正效益

Imperative 2（untangle the AI rollout）的起點數據很冷：**只有約四成 EA leaders 相信當前的 AI 投資會對組織財務表現產生實質正面影響**。Lucas 的解讀：這是 EA 的職業病式悲觀——我們看得到組織各處往不同方向狂奔的去中心化實驗。但悲觀不是策略；untangle 的意思是讓各群 stakeholder 開始**押對的注、停止互相輾壓**，把亂線理成能規模化的 enterprise AI。處方是三個動詞：enable、deploy、adapt——取代舊的 design-first。

## Enable：輕護欄、行動優先於文件——別再要求 75 頁文件

第一個動詞：**讓快速且安全的 AI 實驗成為可能**。具體做法是下到雜草層看交付團隊實際在做什麼、業務在要什麼，然後給**輕量、清楚、實用的護欄**，並且 **encourage action over documentation**。Lucas 點名舊習慣的代表作：「動工前先交一份 75 頁的 solution architecture document」——這種要求只會把 EA 重新釘回路障的位置。護欄的存在理由是讓車開得更快，不是讓車停下來填表。

## Deploy：把驗證過的 patterns 用既有管道放大

第二個動詞：**部署持續演化的最佳實踐與 patterns**。EA 陪著交付團隊跑的過程中會看到什麼有效、什麼無效，而 EA 的結構優勢是手上已經有放大器：與高管的管道、與業務領導的管道、centers of excellence、communities of practice。把單點驗證過的做法透過這些管道推向全組織，交付團隊就能跑得更快也更安全。這跟 07 場 tiny team 的 pattern→平台→套用是同一個動作的 EA 版。

## Adapt：決定什麼 scale、什麼 kill——必要時當 therapist

第三個動詞最考驗人性：**調整架構以規模化成功，同時清楚客觀地決定什麼要 scale、什麼要 kill**。Lucas 把這叫 the art of architecture：你常常要扮演 business leader 的 **therapist**——他深愛自己的 shiny new object，但對組織最好的決定可能是關掉它、釋放資源、再投資到別處。EA 要做的是把那個人帶上桌、帶進局，**幫他理解放手能得到什麼**。05 場說「敢讓案子死的組織才有資格讓案子活」，這場補上了執行細節：案子的死亡需要心理輔導。

## Framework 是 inspiration，不是 aspiration

Gartner 不為任何 EA framework 站台——TOGAF 也一樣。Framework 的用途是 **inspiration**：看看外面有什麼、什麼可能、我的組織實際需要什麼。它永遠不該是 **aspiration**——把框架逐條執行到底，是「為了做 EA 而做 EA」。判準跟全場一致：工具服務於組織的野心，不是反過來。把 TOGAF 當聖經的團隊，正好就是被嫌「太技術、太慢」的那種 EA。

## AI 團隊說架構歸他們？Collaborative，不要 combative

AI 團隊想搶架構主導權時，EA 的正解是合作不對抗。有觀眾問：AI 團隊宣稱架構該由他們主導、EA 只管技術架構，怎麼辦？Lucas 先承認現實：AI 領導權在不同組織落在不同人頭上，資料分析、COO、企業應用主管都可能被指派，**而每個都帶著自己的 siloed lens**。EA 的正確姿勢是合作不對抗：「我知道你被指派了這件事——另外三個小組也被指派了。我們對一下誰在做什麼，別重複投資。」這個「橫著看全場」的動作幾乎只有 EA 做得了——用提供視野的方式搶回影響力，比爭頭銜高明。

## 衝 POC 不算帳的解法：在到達 POC 之前問對問題

在大家抵達 POC 之前把對的問題問完——這是業務跟開發團隊不評估價值就衝 POC 的解法。功課有四項：盯產業動態、跟業務夥伴真對話、查證 vendor 能力的可行性，以及直接用 Gartner 的 **AI use case dashboard**：按產業、按職能切，每個 use case 給 **business benefit × feasibility（含風險）**的排名加實證 case studies。這正是 05 場 Frances 展示的那個 600+ use case 工具。重點不是拖慢 POC：**是在大家抵達 POC 之前，至少把對的問題問完**。

---

## 恍然大悟：EA 的新品管哲學——從擋在前面改成跑在旁邊

Enable、deploy、adapt 三個動詞合起來是一次品管哲學的遷移：舊 EA 的品質保證靠**事前的文件與審查**（75 頁文件、過會、蓋章），新 EA 的品質保證靠**事中的陪跑與修剪**（輕護欄、放大有效的、勸退無效的）。觸發遷移的是速度差：AI 實驗的迭代週期短於文件的撰寫週期，擋在前面的人不是把關，是堵車。而陪跑比擋路難得多——它要求 EA 看得懂雜草層的工作，還要有勸人放手的心理技術。

路障跟護欄的差別，在於車流是被擋下來，還是被引導著加速。

---

## 只有 25% 的 heads of EA 對架構的應變力有信心

Imperative 3（dynamic architectures）的起點數據：最近一次 agenda poll 裡，**只有 25% 的 heads of EA 對「架構能適應快速的業務變化」很有信心**。四分之三的人自知追不上變化——而變化的來源不只是技術，是接下來這個正在竄升的風險類別。

## Sovereignty 風險：兩個地區一翻臉，架構就斷

竄升到許多組織風險清單頂端的是**主權（sovereignty）**：cloud sovereignty、AI sovereignty、business sovereignty——我們被允許在哪裡營運？能從哪裡採購能力？能跟位於哪裡的夥伴合作？這對架構是直接打擊：**兩個地區突然不能貿易，或某地的財政政策重到無法營運，很多架構當場斷裂**。地緣政治從新聞版面走進了架構圖——這是 04-07 場都沒展開、這場補上的維度。

## 傳統 future state 的死法：組織跑得比藍圖快

傳統 EA 的劇本：先畫 **future state architecture**（業務與技術能力、交付模式、技術投資、治理模式、目標成果怎麼拼在一起），再盤 **current state**，然後規劃從這裡走到那裡。死因是速度：**等你接近那張美麗的 future state 圖時，組織的 current state 已經迭代了五六輪**——地緣動盪、成本壓力、主權風險，每一波都把起點改掉。藍圖沒有錯，藍圖只是過期得比畫得快。

## Dynamic state architecture：不畫終點，監控現在

替代品是 Gartner 正在定型的新概念：**dynamic state architecture**。不再為一個固定的長期願景做規劃，而是**即時監控 current state 怎麼變，然後動態重構**。落到操作層：把 future state 的每個 building block（能力、交付模式、投資方式、治理）逐個檢視，問同一個問題——這一塊能不能更 autonomous、更自動化、或至少能更模組化地重新組裝？這跟 07 場「AI 沒有 clear end state」是同一個世界觀的架構版：終點不可知，就把可重構性當終點。

## Assurance by document → assurance by partnership

只保留兩樣 artifact，其餘用 partnership 換 document。AI 專案該要求交付團隊產出哪些 EA artifacts？Lucas 把舊習慣再埋一次：有時候就是沒時間做傳統文件。底線那兩樣是**value × feasibility（含風險）的分析**，加上**至少考慮過替代方案**（build / buy / blend）。其餘的，用一個漂亮的口號替代：**與其追求 assurance by document，追求 assurance by partnership**——下去陪交付團隊跑，風險浮現時當場接住，而不是把所有複雜度塞進一份日後沒人翻的文件。

## Orchestration layer 會改七次才對——但現在就要開始建

有觀眾問到把 EA 指引寫成 markdown 餵進 agentic 系統的 context layer——Lucas 順勢把 orchestration layer 的重要性講透：**每個 vendor 都宣稱自己有 multi-agent system**（Salesforce、SAP、Oracle 全在推），各家的 agents 進了你的組織之後，**誰讓它們協同完成你的目標**？答案是你的 orchestration layer——而它不能用「三年後長這樣」的漂亮圖來建：**它會改七次才改對**。所以姿勢是 dynamic state 的姿勢：現在就開始建，緊盯它怎麼變，邊跑邊重構。這跟 06 場 orchestrator agent 的解剖互為表裡：06 講 agent 怎麼調度，這場講調度層本身怎麼蓋。

---

## 恍然大悟：架構的交付物從藍圖換成了「重構的能力」

傳統 EA 賣的是藍圖（future state 的那張美圖），dynamic state architecture 賣的是**重構的速度**——監控、判斷、重組這個循環跑得多快。Sovereignty 風險把這個轉變從理論變成急迫：藍圖應付不了「兩個地區明天翻臉」這種輸入，只有可重構的系統應付得了。Assurance by partnership 跟 orchestration layer 的「改七次」都是同一個世界觀的器官：在終點不可知的世界裡，**對的一次比不上改得快的七次**。

架構師的新 KPI 不是圖畫得多準，是組織轉向時架構跟不跟得上。

---

## 79% 的 EA leaders 對成本優化被正式究責

Imperative 4 的事實基礎：**79% 的 EA leaders 宣稱自己對 IT 成本優化策略負責、且對實際實現的優化成果被究責**——進年度目標、算進績效考核。這接回開場的成本困境：好砍的砍完了，剩下的平衡題（短期省錢 vs 長期成長）被放到了 EA 桌上。Gartner 的處方自相矛盾：要 EA 一人分飾兩角，同時戴兩頂帽。

## Financial advisor 帽 + VC 帽：一手砍浪費，一手掃地平線

兩頂帽各管一邊。**Financial advisor** 管現在：推進成本削減與優化、消滅浪費、最大化價值、讓 IT 支出對齊業務策略。**Venture capitalist** 管未來：掃描 **12 到 24 個月地平線**上的技術機會與風險（post-quantum cryptography、physical AI、把 AI 裝進多功能人形機器人），識別、評估、enable 那些能帶來創新與競爭優勢的投資。兩頂帽缺一頂都危險：只有 advisor 帽會把組織省進死胡同，只有 VC 帽會把組織燒到沒明天。

## 「你現在是我們組織的 venture capitalist」——CIO 親口說的

這個定位不是 Gartner 的一廂情願。Lucas 分享：幾週前對一群 heads of EA 講這套時，其中一位說他的 CIO 前幾天走進他辦公室，原話是**「你作為 head of EA 的角色，就是當我們組織的 venture capitalist」**。CIO 們已經在用這個語言發包了。對照 05 場「Upend 桶要當 VC 管、二十中一」——CFO 的 portfolio 語言跟 CIO 的角色語言正在會合，EA 恰好站在會合點上。

## 不用 AI 重造 EA 的人，會變成自己最怕的那種路障

Imperative 5 把鏡頭轉向內：**不主動用 AI 優化 EA 活動的 heads of EA，會在業務與 IT 不斷上升的需求面前變成路障**——而「路障」正是這個職能最想撕掉的標籤。數據顯示重造已在進行：EA 工作被 AI 增強的比例，**去年 14%、今年 23%、明年自估 30%**——兩年內翻倍再加碼，三分之一的 EA 活動將有 AI 參與。曲線的斜率本身就是訊息：同行都在裝引擎，原地踏步等於倒退。

## 七步重造路徑（上）：盤 use case、定組織型、選工具、查現有工具

Gartner 給的 EA 操作模式轉型路徑，前四步。**Assess AI's potential**：盤點 EA 自己的 AI use cases，看 EA 工具商在提供什麼、手上的企業級 AI 授權能搬來做什麼，目標是把過勞的架構師卸載。**Organize for AI-augmented EA**：定協作的組織型，架構師分散還是集中？AI 能力當 **toolmates** 陪著分散的交付團隊？（03 場的 toolmate 概念在這裡長出了 EA 版。）**Identify high-value EA AI tools** 與 **audit EA tools for AI readiness**：雙向掃描——通用 AI 工具能搬進來的，跟 EA 專用工具正在內建的。

## 七步重造路徑（下）：控風險、小試證明、以身作則

後三步。**Mitigate AI-specific risks**：幻覺、資料品質這些風險比以往任何時候都更被認識，先列清單再上工具。**Prove AI-enabled value**：別搞 big bang，挑幾個 use case（roadmap 生成、reference architecture 生成、架構治理審查）小規模試、對少數 stakeholder 驗證，**證明有價值再 scale**。**Lead by example**：這條路徑可以複製到供應鏈、財務、行銷——但 EA 自己先走完，**走進房間才有 credibility**。要當全組織的 AI 領導，最硬的名片是自己職能的 AI 化成績單。

## AI 不是 silver bullet：判斷與同理心編不進程式碼

組織把「EA 現代化」最常搞錯什麼？Lucas 的回答：**還是把 AI 當銀彈**。EA 角色裡拿不走的東西是**人類的判斷力與同理心**——設計、roadmap、在 stakeholder 之間當 therapist 的策略性工作，在 AI 世界裡只會更關鍵。AI 真正幫的只有一件事——**消滅重複**。這跟 04 場 human foundation（不能萎縮的核心圈）嚴絲合縫：每一場 webinar 都在不同職能上畫出同一條「這裡 AI 進不來」的線。

## EA repository 加一個 AI assistant，就消滅一整類重複問答

最具體的 quick win：架構師每天被交付團隊問同樣的問題——「這個技術的 pattern 是什麼」「我們 portfolio 裡有沒有這個應用」「有沒有滿足這組業務需求的現成東西」。**在 EA repository 上面放一個 AI assistant，這一整類重複問答就消失了**，架構師的時間被釋放回判斷層。這個 use case 的形狀很關鍵：AI 沒有做任何架構決策，它只是讓架構知識的檢索不再需要排隊等人——scale 的是 decision support，不是 decision 本身。

---

## 恍然大悟：EA 拿什麼資格領導全組織的 AI？拿自己當 demo

Imperative 4 跟 5 表面是兩件事（管錢、自我改造），合起來是同一個信用工程：VC 帽要求 EA 對技術地平線有判斷力，而證明判斷力最快的方式是把判斷用在自己身上——14%→23%→30% 的曲線就是 EA 的自我 demo。「Lead by example」不是道德口號，是政治策略：當你要說服每個 BU 接受你的 AI 取捨時，「我們自己職能先做完了這個轉型」是唯一不能被反駁的論據。

要驗證一個架構師值不值得信，看他自己的架構。

---

## 現場 poll：dynamic architectures 險勝 reimagine EA with AI

收尾的 poll 問「五個 imperatives 裡哪個是你 2026 下半年的 top focus」：**building dynamic and adaptive architectures 險勝 reimagine EA with AI**。Lucas 對第一名的解讀直接連回新聞頭條：中東、歐洲、美國，各區域的互動天天在變，**sovereignty 風險竄升**正在改變組織對「vendor 在哪、resilience 怎麼設計、架構怎麼做情境推演」的思考。同行的優先順序本身就是市場訊號：應變力的焦慮壓過了所有其他議程。

## 觀眾自報的最大障礙：治理、沒有清楚的 leader、EA 沒後盾

第二個問題請觀眾自報「實現 EA 成功的最大挑戰」，回答**多元而分散**：治理問題、AI initiatives 沒有清楚的 leader（誰負責都說不清，一灘渾水）、EA 職能在公司內缺乏強力後盾。沒有單一共同主題——但這三類剛好對應前面的三個 imperatives（governance 對 imperative 1 的 adaptive governance、leader 真空對 imperative 1 的補位、後盾缺失對 imperative 5 的 credibility 工程）。觀眾的痛點清單，反過來驗證了議程設計。

## 工具市場：EA vendors 全在加 AI，有一份 Magic Quadrant 可查

最後一個問題要工具推薦。Lucas 的回答：**EA 工具市場的 vendor 全都在往工具裡加 AI 能力**——已經在用 EA 工具的，查你的 vendor 新增了什麼；還沒用的，看今年由 Austin Steinmetz 領銜的 **EA 工具 Magic Quadrant**，或者看 EA 市場之外有什麼工具能滿足需求。配上 14%→23%→30% 的曲線讀：工具供給跟需求曲線在同步爬坡，2026 是 EA 工具選型的活躍年。

---

## 恍然大悟：整場在教 EA 一件事——把「被取代的焦慮」翻譯成「補位的清單」

回看全場的結構：開場是「能不能用 AI 取代 EA」的存在威脅，收尾是五張補位清單（領導真空、rollout 整理、動態架構、雙帽投資、自我重造）——同一股 AI 浪潮，從威脅被翻譯成了職位說明書。翻譯的樞紐是一個判斷：AI 取代得了 EA 的文件、審查、重複問答，取代不了跨域視野、艱難取捨、跟 stakeholder 的心理工程——所以把前者主動交給 AI、把自己搬進後者，焦慮就變成了議價力。這也是 04 到 08 五場 webinar 共同的底層公式，在 EA 這個「最怕被問價值」的職能上演了最極端的版本。

最怕被 AI 取代的職能，恰好是最有資格指揮 AI 的職能——差別只在誰先動手。

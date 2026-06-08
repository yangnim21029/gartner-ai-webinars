# Steps for Procurement to Become AI-First

> **來源**：Gartner Webinar, Ryan Polk（Sr Director Analyst, Chief of Research）。前作是同事 Andrew Greenwald 兩個月前的 future of procurement 場，這場是其中 AI 主題的深挖
> **涵蓋**：CPO 視角的 AI-first 路線圖。三個技術趨勢、agent 的紅線定義、三個預測（2027 data maturity / 2030 新角色 / 2030 orchestration）、pattern vs judgment 兩桶工作、mentorship 斷層與 Da Vinci 案例、role redesign 四步
> **注**：官方文案宣稱 5 prediction themes，實際場上講了 3 個；文案裡的 multitier supplier transparency 主題未出現在內容中

---

## 詞彙表

| 詞 | 意思 |
|---|---|
| Context window | AI 模型一次能讀進多少資訊的上限 |
| Chain-of-thought | 模型先推理再回答的能力，「先想再講」 |
| Multimodal | 文字、圖片、影音都能進能出，anything in, anything out |
| Agentic AI / AI agent | 能感知環境並**不靠人類下指令**就行動的 AI |
| Agent washing | 把不是 agent 的東西也叫 agent 的市場行銷現象 |
| Copilot | 很會幫忙但每步都要人類 prompt 的 AI 助手 |
| Multi-agent system | 一個 orchestrator agent 調度多個 sub-agents 的架構 |
| Orchestrator agent | 接住人類需求、再分派給子 agent 執行的總管 agent |
| Structured / semi-structured / unstructured data | 表格裡的資料／SOP 與政策文件／聊天記錄、信件、腦中的東西 |
| Business process mining | 用資料挖出組織實際流程長怎樣的技術 |
| Ontology（of business） | 業務的本體論：決策用到哪些概念、彼此什麼關係 |
| Tribal knowledge | 部落知識——只存在某些人腦中、沒文件化的組織運作知識 |
| Pattern-based work | 照規則、SOP、慣例走的工作 |
| Judgment-based work | 沒有規則可循、需要人拍板的工作 |
| Spend taxonomy / spend cube | 支出分類體系／多維度切支出資料的分析庫 |
| ERP | Enterprise Resource Planning，企業資源規劃系統 |
| CPO | Chief Procurement Officer，採購長 |
| RFX | RFI/RFP/RFQ 等採購徵詢文件的統稱 |
| Tail spend | 金額小、頻率雜的長尾採購支出 |
| Token economics | 用 token 計價的成本帳：模型讀爛資料要花多少錢 |
| Da Vinci | 達文西手術機器人，輔助腹腔鏡手術 |

---

## 這場 webinar 要做的事

Ryan Polk 要回答「procurement 怎麼變成 AI-first」，拆成四件事：

1. 鋪當下的技術地基：context window、reasoning、multimodal 三條趨勢怎麼合流成 agentic AI，以及 agent 的嚴格定義
2. 給三個三到五年期的預測：2027 年只有 20% 的採購組織有資格玩 multi-agent、2030 年 20% 的採購人佔據 AI 驅動的新角色、2030 年 30% 的組織由 AI orchestrate 採購
3. 用 pattern vs judgment 兩桶工作的框架，論證「AI 來了反而可能需要更多人」
4. 給 CPO 兩張行動清單：data readiness 的四步路線圖、role redesign 的四步創造性破壞

## 要建立的心智模型

讀完這篇你要建立五個認知：

1. Agent 的分界線是「不靠人類 prompt 就能行動」——市場上大多數自稱 agent 的東西過不了這條線
2. 卡住 AI 部署的不是模型，是 semi-structured 跟 unstructured data——你的決策邏輯大半活在 SOP、聊天記錄跟某人腦中
3. AI 拿走的是「數學已被定義」的 pattern 工作；judgment 工作沒有 training database，拿不走
4. 工作總量會增加不會減少——技術縮短 ideas 到 actions 的距離，每縮短一次，工作事件就生得更快
5. AI 是 mentorship 的天敵：senior 會把活交給不用睡覺的模型而不是 junior，不刻意保護「練判斷的活動」，職涯階梯會斷

下面 45 個知識點就是把這五點拆開填滿。

---

## Context window 變大，等於 AI 的周邊視覺變廣

第一條技術趨勢：**AI 模型的 context window 近年急遽擴大**。Context window 是模型回應一個請求時一次能吃進的資訊量。為什麼重要：人類能在日常工作裡行動自如，靠的是視覺、聽覺、感覺進來的海量周邊資訊；模型能吃的脈絡越多，回應就越準、越精確。Context window 的擴張等於把模型從「只看你打的那句話」升級成「看得到你工作現場的周邊」——準確度的天花板跟著抬高。

## Reasoning 是「先想再講」，直接打掉一批幻覺

第二條趨勢：**模型長出推理能力**。用過新一代模型的人見過 chain-of-thought：模型在給答案之前，把自己的思考過程跑一遍。Ryan 的比喻是 think before you speak。效果有兩層：幻覺率下降，以及模型能接住更複雜的任務——複雜問題需要多步推理，沒有「先想」的模型只能一步到位地猜。這條趨勢把模型沿著成熟度曲線往上推了一格。

## Multimodal：anything in, anything out

第三條趨勢：**模型能吃、能吐多種形態的資料**。昨天的模型是 text in, text out；今天與未來的模型是 anything in, anything out——文字進圖片出、圖片進文字出、影片進音訊出。對採購的意義一句講完：unstructured data（合約掃描檔、會議錄音、供應商簡報）正是採購的日常，multimodal 是讓 AI 讀得了這些東西的前提。

## 三條趨勢線合流，指向同一個詞：agentic

把三條進步線疊起來看，方向只有一個：**AI 正在變得 agentic**。脈絡夠大（看得到環境）、會推理（想得了多步）、什麼都能讀（接得住真實世界的雜訊）——這三件事湊齊，模型才有資格從「回答問題」走向「完成任務」。Agentic 是過去 12 到 18 個月最大的 buzzword，而 buzzword 的下場通常是被濫用——濫用已經是市場的現在進行式。

## Agent washing：人人都聲稱自己有 agent

Ryan 從 Gartner 的位置看到的市場現況：**大量的 agent washing**。Vendor 社群、評論者、所有人都聲稱自己有個 AI agent——因為話題太熱，不掛這個詞就沒人聽。這跟 02 場講 HR vendor、03 場講 comms vendor 的 agent-washing 警告同一回事，但採購人有額外的職業曝險：你不只自己買 AI 工具，你還替全公司把關 vendor——辨識 agent washing 是 CPO 團隊的新核心技能。

## Agent 的紅線：不靠人類 prompt 就能行動

Gartner 的 agent 定義有兩個動詞跟一條紅線。兩個動詞：**perceive**（感知環境）跟 **act**（對環境行動）。紅線：**行動獨立於人類的 prompt**。Copilot 再強，每一步都等人類下指令，就還在紅線的這一邊；跨過紅線的系統，自己決定下一步並執行。這條線畫得這麼硬是有用意的——下次 vendor demo 時你只需要問一個問題：「拿掉人類的 prompt，它還會動嗎？」

## 窄域 agents 已經上場：談判、支出分析、orchestration

Sourcing 與 procurement 已經出現**窄域的 AI agents**——紅線之上已經有住戶：negotiation agents、spend analytics agents，而 orchestration agents 是最近被討論最多的新類別。「窄域」是關鍵修飾詞——這些 agent 在單一、邊界清楚的任務上跨過了紅線，離「把整條採購流程交給 agent」還有距離。

## 大量 pilot，尚未 at scale：卡住的東西在組織自己家裡

現況的誠實總結：**很多 pilot，還沒有人 broadly at scale**。為什麼卡住？不是模型不夠聰明——三條技術趨勢都在往對的方向跑。卡住的東西藏在組織自己家裡，這就是第一個預測要拆的：資格問題。

---

## 恍然大悟：agent 不是買來的功能，是組織自己要先夠格的能力

這一段表面在介紹技術趨勢，實際在重新分配責任：模型側的三條線（context、reasoning、multimodal）全在進步，所以「AI 還不夠好」越來越不成立藉口；同時 agent 的紅線定義把市場噪音切掉——大多數叫 agent 的東西只是 copilot。剩下的問題就尖銳了：技術夠了、定義清了，為什麼還是只有 pilot？因為跨紅線的系統要自己感知、自己行動，**它感知的是你的資料、行動靠的是你的流程**——而那兩樣東西的狀態，vendor 賣不給你。

Agent 的瓶頸不在貨架上，在你家倉庫裡。

---

## 預測一：2027 年，只有 20% 的採購組織夠格玩 multi-agent

第一個預測：**到 2027 年，只有兩成的採購組織會有足夠的 data 與 process 成熟度去使用 multi-agent systems——而做到的那兩成，會拿到真實的競爭優勢**。這個數字的重點不是悲觀，是門檻的位置：八成的組織會被擋在門外，擋住他們的不是預算也不是模型授權，是接下來幾個 H2 要拆的東西——資料成熟度的真正定義。

## Data management 的誤區：以為它只是 spend taxonomy

採購人聽到 data management，直覺想到的是**結構化資料的治理**：spend taxonomy、合約庫、master vendor list。Ryan 直說這名字名實不符（misnomer）——那些重要，但不是故事的全貌。**AI 時代的資料策略是 structured + semi-structured + unstructured 三類的組合**，而真正把大家卡住的，是後兩格。這個誤區的危險在於它給人虛假的安全感：「我們的 spend cube 很乾淨」跟「我們的資料 AI-ready」是兩個不相干的命題。

## 做個思考練習：你今天的工作，靠哪些資料從 A 走到 B

Ryan 給了一個自我檢測法：挑一件你或你的員工今天做的任務，問**「從 A 點走到 B 點，我實際需要哪些資料」**。有些在 Excel、Power BI、Tableau——結構化，住在儲存格裡。但他願意賭更多錢的是：你更依賴的是 SOP 文件、流程文件、政策文件（semi-structured），以及 Teams 對話、Outlook 信件、開完會留在你腦中的需求理解（unstructured）。這個練習的價值是讓你親眼看到自己的決策邏輯住在哪——大半不在任何系統裡。

## AI 需要的資料，跟人類需要的一模一樣

把練習的結論推一步：人類靠三類資料的 sensory input 完成工作，**AI 要接手同一件工作，需要的是完全相同的資料**。這是整段 data 論述的支點：AI 不是魔法，它是另一個需要看 SOP、讀對話脈絡、懂政策例外的「新員工」。你沒辦法把一個人類員工教會的東西，是因為它沒寫下來——同一個原因會讓 AI 也學不會。

## 大家都不會管 semi/unstructured data，因為成長過程沒練過

Ryan 對採購的診斷（並聲明這不是針對採購，所有部門都一樣）：**我們很不會管理 semi-structured 跟 unstructured data**。原因是出身：整個行業的資料肌肉都是在 structured 側練的——ERP、spend cube、報表。半結構與非結構資料從來不歸誰管，於是它們散落在文件堆、聊天記錄跟人的腦袋裡。對話現在必須轉向：這兩類資料怎麼治理——這是 AI 投資報酬率的真正分母。

## 先進公司在文件化「決策的數學」

走在前面的組織在做兩筆投資：**business process mining**（挖出流程實際長怎樣）跟**業務的 ontology**（決策用到哪些概念、什麼關係）。Ryan 把目標講得很白：**你是否完全理解你的決策背後的數學，而且把它寫在紙上了**——寫下來的那一刻，它就成了 AI use case 的 training database，可供模型學習與回查。沒寫下來的決策邏輯，對 AI 等於不存在。

## Data readiness 第一步：每個 use case 做 pass/fail 的資料盤點

跟 IT 合作的路線圖，第一步最關鍵：**拿你的 AI use case 清單，逐個問「這個 use case 的決策邏輯用到的所有資料點——跨三類資料——我完全理解嗎？」**這是 pass/fail 的一關。多數人會在這裡發現兩件事之一：(a) 我根本不知道這個決策用到哪些資料；(b) 我知道，但它只在某人腦中，哪裡都沒寫。Ryan 的原話：你會很快發現**有多少 tribal knowledge 在撐著這個組織**。不及格的 use case 只有兩條路：丟掉，或排一個文件化計畫。

## 後三步：governance、pipelines、refine——一個虛循環

第二步是 **governance**：知道用什麼資料還不夠，要問「這份資料能在 AI 情境裡用嗎」（倫理、合規、隱私），答案有時是 yes 有時是 no。第三步交給 IT：**準備 data pipelines**，把散落三類的資料源接到模型上；這段由 IT 主導，採購通常不擁有。第四步 **refine & test**：確保它在實務裡真的會動，然後循環回頭。Ryan 自承三四分鐘講完的東西實際複雜得多，但結構就是這四步——成敗的重心壓在前兩步。

---

## 恍然大悟：tribal knowledge 是組織的隱形負債，AI 來了才被迫結帳

這一段的方法論（盤點、governance、pipeline、refine）平凡無奇，真正的洞見是那個 pass/fail 測試照出來的東西：**組織能運轉，靠的是大量沒寫下來的決策邏輯**——它們住在資深員工的腦中、Teams 的對話裡、「大家都知道」的默契裡。過去這是免費的潤滑劑，現在它變成負債：AI 學不了沒寫下來的東西，所以每一條 tribal knowledge 都是一個部署不了的 use case。2027 年那 20% 跟 80% 的分界線，就劃在誰先把腦中的數學寫到紙上。

文件化從來不是行政工作——它是把組織智慧從人質狀態贖回來。

---

## 預測二：2030 年，20% 的採購人佔據 AI 驅動的新角色

第二個預測：**到 2030 年，兩成的採購專業人員會佔據由 AI 驅動的新角色，CPO 必須因此改寫 talent 策略並 upskill 團隊**。敘事的接力棒在這裡交接：data 是難關但能克服，一旦克服，壓力立刻轉到人的身上。Ryan 點名這是市場上**被忽略的對話**——所有人都在談自動化什麼，沒人在談人要變成什麼。

## 人類的工作只有兩桶：pattern-based 跟 judgment-based

框架先行：人類今天做的工作，大致落進兩個桶。**Pattern-based work** 跟著規則、norms、制度化的做法走——有政策、有程序、有 SOP；組織裡位階越低，pattern 工作占比越高。**Judgment-based work** 不跟規則走——它要求一個人**拍板**：應對 COVID、應對地緣政治動盪、應對每三到六個月就來一次的黑天鵝。兩個桶的分界不是難易度，是「有沒有規則可循」。

## AI 拿走 pattern 桶，因為那裡的數學已經被定義

預測的機制：**AI 會接管或大幅增強 pattern-based 的工作**。理由跟 data 段一脈相承：凡是我們理解決策數學的地方（知道什麼資料進去、怎麼組合、產出什麼），**那個理解本身就是 training database**，AI 就能學著複製。換句話說，一件工作能不能被 AI 拿走，判準不是它重不重要，是它的邏輯有沒有被定義過。諷刺的是：SOP 寫得越完整的工作，越早被接管。

## Judgment 桶拿不走：黑天鵝沒有 training database

對照組：**Gartner 不認為 AI 會顯著接管 judgment-based 的工作**。理由同樣是資料：那裡沒有描述決策的資料。Ryan 的例子選得準：六年前的今天大家在談 COVID——當時不存在任何 training database 能告訴你最佳應對策略，那只能靠人類的直覺、判斷與技能。所以長期的遷移方向是：agents 接走 pattern，人類緩慢地向 judgment 移動——跟 04 場「人類往 judgment、orchestration、strategy 移」的結論精確互鎖。

## 「所以需要更少人」——Ryan 不買單

從框架直觀推論：採購今天的工作大半是 pattern，AI 接走它們，所以需要更少人。Ryan 承認這個推論有一部分對，**但他要給一個反論**：AI 衝擊經濟的同時會發生兩件事——business 的節奏劇烈加速、工作的總量大幅增加。他的論證工具是一條工作誕生公式。

## 工作的誕生公式：有人有想法，想法被執行

Ryan 的模型：**工作從哪裡來？組織裡有人產生一個 idea，那個 idea 最終需要被 action，兩件事都發生時，一個工作事件就誕生了**。技術出現之前，ideas 到 actions 的距離很長：想法要人工翻面、人工批判、人工打磨，才能走到可執行的狀態。網路與電腦把這段距離截短，看看現場就懂：一千人在這場 webinar 上即時聽想法、即時提問、即時打磨，想法到可行動的速度快了一個量級。結果呢？**沒有人會說我們今天做的工作比三十年前少**——距離縮短，工作事件的出生率上升。

## AI 是往火上倒汽油：它連 idea 都會自己生

把模型推到 AI：過去的技術只幫你打磨想法，**AI 不只能打磨，還能產生新的想法**——idea 端跟 action 端同時提速。Ryan 的比喻是 pouring gasoline on the fire。後果就是預測的那兩件事：節奏再加速、總量再膨脹。而且我們已經活在裡面——過去幾年 Gartner 大量著墨的 **cognitive overload**（怎麼讓團隊扛住規模化的快速變化）就是這個趨勢的前菜。

## 淨效果：中間的人減少，兩端的人增加

把兩條線疊起來算淨值：pattern 桶（中間）的人力需求會淨減少，但 **non-standard 與 judgment 的兩端會淨增加**——因為節奏加速代表更多新奇情境、更多沒有前例的需求，每一個都需要人類介入。Ryan 的結論：人力需求可能淨持平，甚至增加。這個論證給了 CPO 一個跟團隊溝通的底氣：AI-first 的路線圖不必然是裁員路線圖——前提是你真的把人往兩端搬，而不是讓他們在被掏空的中間枯坐。

---

## 恍然大悟：能不能被 AI 拿走，取決於你的工作有沒有被「寫下來」過

兩桶工作的框架跟 data readiness 那段是同一個洞見的兩面：**AI 的能力邊界就是「已定義的決策數學」的邊界**。文件化越完整的工作越早被接管；從沒被定義過的判斷工作，AI 連學習材料都沒有。這給個人跟組織各留了一道判斷題——個人問：我的價值有多少建立在「照規則執行」上？組織問：我們要把省下的人搬去兩端，還是假裝中間還能住人？而工作總量的膨脹保證了一件事：兩端的位子，比想像中多。

你的護城河不是你會做什麼，是你能在沒有規則的地方做決定。

---

## 技能的三欄清單：下降、核心、新興

Talent 策略第一題：judgment 主導的世界裡，什麼技能值錢？Ryan 給了三欄。**下降欄**：deductive analysis、process execution、financial acumen、legal acumen——這些支撐 pattern 執行的技能會越來越不重要。**核心欄**：agility、collaboration、strategic thinking、influence。**新興欄**：跟 AI 模型有效協作、design thinking、使用 AI 的 ethical decision making。第一個行動就從這張表開始：盤點現有團隊的能力組合，看 gap 在哪——因為今天僱用與培養的標準，幾乎全是為 pattern 執行設計的。

## Negotiation 居然在下降欄——因為談判是已定義的數學

Q&A 裡有人挑戰：談判怎麼會是下降技能？Ryan 說團隊內部也來回辯了好幾個月，最後的理由回到同一個判準：**negotiation 的數學已經被定義了**——game theory 是一整個學門，Harvard 有完整的談判課程體系；這裡的「數學」不是數字，是談判發生時的關係性概念。被定義 = AI 能學 = AI 能做。談判 chatbot 已上線、autonomous negotiation 方案已能跟人類談——再推一步，**兩個 AI 互相談判**會打開動態合約、即時合約更新、人類做不到的無限排列組合。重要性不變，但作為人類技能的稀缺性在跌。

## 教育模型壞了：6 歲進學校，學的東西要撐 50 年

Talent 策略第二題：新技能去哪裡學？Ryan 先把房間裡的大象指出來：全世界的教育系統建立在一個假設上——小孩四到六歲進學校、十七到二十三歲出來，**出來時帶的知識與技能要支撐接下來四五十年的職涯**。他的形容詞是 asinine（蠢得離譜）——這個假設跟今天世界移動的速度完全脫節。每五到十年把人送回學校也不現實，所以缺口只能由別人填：企業自建課程？行業協會？in-house curriculum？這題沒有標準答案，但沒有答案的組織會輸。

## 十年後這張技能表會重新洗牌——持續教育是新的差異化

技能清單不是一次性的：**十年後會有這張 slide 的新版本**——右欄掉出頁面、中欄右移、左欄移中、左邊長出全新的一欄。所以真正的問題不是「這次要補什麼課」，是**怎麼建立持續教育的機制**。「終身學習」喊了幾十年，差別在於 AI 把它從口號變成了實質的競爭差異——技能的半衰期第一次短於一份工作的任期。

## AI 是 mentorship 的天敵：你會選 junior 還是不用睡覺的模型

Talent 策略第三題最尖銳：AI 正在拆掉**真人 mentorship 的誘因**。Ryan 的思想實驗：你是 senior，手上有一塊工作可以下放——給 junior，或給 AI 模型。一邊 24/7 不睡覺、要多少版本給多少版本、不用顧慮怎麼給回饋；一邊是個要教、要等、要關照情緒的人類。**Who are you going to pick？**答案不言自明，而每一次選了模型，職涯階梯就斷掉一格。回想你自己怎麼走到今天的位置：多數人不是靠教室訓練，是靠某段 mentorship 關係給的 stretch opportunities（略超出當時能力的任務）。AI 正在無聲地拆掉這個機制。

## 解法：保護「建立 judgment 的活動」，明知 AI 能做也不給

最先進的公司在問的問題：**怎麼治理那些「AI 做得了、但對人類發展判斷力至關重要」的活動**——也就是刻意圈出一塊地，明文規定 AI 不准碰，因為人要在那裡練功。這不是懷舊也不是保護主義，是 pipeline 管理：不答這題的組織，幾年後會同時面對技能錯配跟職涯階梯的斷層——junior 上不來，senior 沒接班人。

## Da Vinci 案例：不讓機器人開刀，因為住院醫師要練手

Ryan 留給大家的案例：**達文西手術機器人**問世後，幾個醫院系統發現主刀醫師開始把手術環節外包給機器人——而不是給住院醫師練。醫院很快意識到：**再不保護住院醫師實際參與手術的機會，幾年後主刀醫師的 pipeline 就斷了**。於是他們明文劃線：我們知道機器人做得了這部分手術，但不讓它做——人要透過這個環節練出判斷，才能成為未來的主刀。這是「保護練判斷的活動」最具體的版本，跟 04 場「entry-level ramp 變陡需要刻意 coaching」是同一題的兩個解。

---

## 恍然大悟：組織要開始管理一種新資產——人類判斷力的生產線

技能清單、教育機制、mentorship 保護、Da Vinci 劃線——四件事合起來是一條生產線的維護手冊：**判斷力不是僱來的，是用 pattern 工作當原料、在 stretch opportunities 裡鍛造出來的**。AI 把原料抽走（pattern 工作沒了）、把鍛造爐也拆了（senior 不再帶人），生產線兩頭同時斷。聰明的組織不是阻止 AI，是在自動化的版圖上刻意留白——那些留白處，是判斷力唯一的養成所。

效率最大化的組織，正在最高效地停止生產自己的未來領導人。

---

## 預測三：2030 年，30% 的組織由 AI orchestrate 採購

第三個預測：**到 2030 年，AI 會在三成的組織裡 orchestrate 採購——任務依據獨特強項被分流（triage）給人類或 AI agents**。動詞在這裡換了：前面講的是 AI「做」工作，這裡是 AI「調度」工作——誰該做什麼、什麼時候交棒，由 orchestration 層決定。這是 agentic 故事的完成式。

## 未來的買東西：先跟 orchestrator agent 講話

Multi-agent system 的運作圖像：未來的人類**透過 AI 系統與企業互動**。想買東西？你面對的第一個介面是 **orchestrator agent**——它已被訓練（或連接）在組織的整個 intelligence layer 上：採購政策、程序、品類策略、sourcing 策略、供應商管理策略。你不再查政策、填表單、找對窗口——orchestrator 就是窗口，而且它背後站著整個組織的制度記憶。

## Orchestrator 的兩個職責：釐清需求，調度子 agent

總管的工作分兩段。第一段：**跟人類 requester 對話釐清需求**（要幾個？最低價還是最高品質？lead time 多急？）。第二段：**協調 sub-agents 把需求操作化**：視需求召喚 sourcing agent、negotiations agent、contracting agent，對每個發出 goal prompt、review 它們的產出、按順序串完整條鏈。分工的形狀很特別：orchestrator 不自己做事，它做的是 04 場說人類要去的那件事——judgment 與編排。只是在 pattern 夠清楚的買東西場景裡，連編排都可以是 agent。

## 鏈的終點回到人：human in the loop 不是裝飾

流程的收尾：**回到人類**。人類 review 整段旅程的結果，必要時召喚第三方驗證——例如一個 compliance agent 把全程再查一遍。這個設計呼應了前四場反覆出現的原則（human-in-the-loop 是設計選擇）：在 multi-agent 的世界裡，人的位置不是被擠出去，是被刻意安放在「判斷結果」的位置上。Gartner 相信 2030 年會有組織把這套 at scale 地跑起來。

## 複雜場景的真相：agent 跟人類接力傳棒

簡單買東西是框得很窄的例子；更複雜的場景裡，**流程不會是純 agent 也不會是純人類，是兩者的接力**——agent 跑到某一步，因為需求屬性把棒子交給人類；人類做完判斷，把棒子交回給下一段的 agent。CPO 的新工作是 **orchestrate autonomous procurement at scale**：設計這場接力賽的交棒規則。這直接逼出 operating model 跟 org design 的更新——誰在哪一棒，憑什麼。

## Agent 要正式進 org chart

Ryan 放了一張塞滿小字的架構圖（他自嘲是 eye chart），真正訊息只有一句：**AI models、agents、bots 要在 org chart 跟 operating model 上佔據正式位置，跟人類並列**。輸入端是流程模型、workflow 設計、決策建模（你的業務 ontology），餵進 LLM 為核心的 intelligence layer，連上 intelligent document processing、decision intelligence 等能力，輸出端流向人類、bot、API、未來的 agent。聽起來像技術架構圖，其實是組織圖——當 agent 承擔角色、接目標、接受績效 review，它就是組織設計的對象，不再只是 IT 資產。

## 個人生產力卡在 role design 裡，沒有 scale 到企業

最後一塊拼圖解釋一個數據疑案（05 場那份 1,600 人調查裡、時數省了績效沒動的平線）：**已經規模化部署 AI 的組織，看得到個人層級的生產力改善，但改善沒有 scale 到企業層級**。Ryan 的診斷一句話：**productivity is allowed to remain trapped in individual role design**——生產力被困在個人的角色設計裡。某人快了 30%，但他的角色邊界沒變、上下游沒變、組織沒有任何機制把那 30% 收割成企業的產出。

## Role redesign 四步：這就是創造性破壞的流程圖

解困的方法是**角色的拆解與重組**，四步。一、**evaluate**：盤點現有角色，量每個角色的任務有多少 % 是 innately human（judgment）、多少是 innately AI（pattern）。二、**realign**：把 innately human 的部分抽出來重新組合——也許把 category manager、sourcing manager、supplier manager 三個角色的人類部分合併成一個全新職稱；把 innately AI 的部分剝給 agents、models、copilot。三、**reconstitute**：用拆出來的零件重構角色。四、更新 operating model。Ryan 自己點題：**這就是 economic creative destruction 畫成一張 slide**——新技術摧毀一些工作，並在同一個過程裡創造新的。把生產力從個人轉移到企業，靠的就是這台重組機。

---

## 恍然大悟：orchestration 的本質是把「組織」本身變成可設計的物件

預測三表面講技術（multi-agent platform），骨子裡講組織學：當 agent 進 org chart、當人機接力有交棒規則、當角色能被拆成 innately human 與 innately AI 再重組——**組織結構第一次變成一個可以工程化迭代的物件**，而不是十年動一次的重組手術。05 場的平線之謎在這裡得到完整解答：生產力不會自己從個人流向企業，它需要 role redesign 這台泵——而泵的設計圖，就是這四步。

AI-first 的真正門檻不是部署多少 agent，是組織敢不敢把自己放上手術台。

---

## 員工的恐懼怎麼管：先畫 roadmap，別只談自動化

Q&A 第一題：怎麼管理員工對 AI 投資的恐懼？Ryan 的答案回扣他的「更多人」論證：**先把 procurement 要去哪的 roadmap 講清楚、把願景畫出來**——因為現在組織裡的對話全是「我們要自動化什麼、自動化什麼、自動化什麼」，員工聽到的全是減法。把「節奏加速的世界需要更多 judgment 工作、judgment 工作需要人」的那條線講出來，恐懼才有對沖的依據。這跟 04 場「第一個可見的勝利應該給人」是同一帖藥。

## Direct vs indirect 不是分界線，data availability 才是

有人問 agentic AI 在直接材料採購（戰略尋源、製造 BOM）的應用。Ryan 的回答先糾正問題的座標系：**AI 用得多深，分界不是 direct 或 indirect spend，是 data availability**。資料在哪裡夠好，AI 就在哪裡能用——這跟全場的 data 論述完全一致，採購類別只是表象變數。

## 真有 ROI 的 use case 在哪：合約管理、支出分析、tail spend 談判

落地現況的快照：Ryan 認定「真實、有 tangible ROI」的 use cases 集中在**合約管理、spend analytics、以及 tail spend 的自動談判**（跨 direct/indirect）。還在 piloting 階段的：orchestration、完整 RFX 自動化、端到端 autonomous sourcing。這張快照值得存檔——它是 2026 年中的基準線，對照三個預測的時間表（2027/2030），你可以每年回來校準市場走到哪了。

## Build or buy：判準是 competitive differentiation，跟 make-vs-buy 同構

要自建 AI 工具還是買？先進組織採 dual-pronged——兩條都試。trade-off 的形狀：**build 給你更好的 contextual information**（模型吃你自己的脈絡），但更貴、更難治理；**buy 給你市場側的 contextual 知識**（vendor 從整個市場學來的），但不貼你的做事方式。判準跟傳統 make-vs-buy 同構：**這個 use case 是你的競爭差異化嗎？是就考慮 build；只是效率改善？buy 或 outsource 就好**。

## 流程標準化的價值要用 token economics 算

「流程標準化對訓練 AI 多重要？」Ryan 的回答把問題翻譯成成本：AI 其實能讀極度非結構的資料來源（連 YouTube 都能讀懂），**問題是 token 帳**——模型從爛資料裡擠出意義要燒多少 token？存在一個臨界點，過了之後**用 AI 比僱人還貴**。所以標準化的回報公式很乾淨：流程越標準 → 資料越（半）結構化 → 同一個 use case 的部署成本越低。標準化不是 AI 的前提，是 AI 的折扣券。

## 真正非標準的流程別用 AI——但先確認它不是「沒寫下來的標準」

收尾的問題：非標準流程怎麼辦？Ryan 的答案分兩刀。第一刀：**真正值得非標準處理的情境，就是需要人類判斷的情境**——那是 innately human 的任務，現階段別想用 AI。第二刀更實用：很多所謂的非標準，**其實在某人腦中很標準，只是沒寫在紙上**——又是 tribal knowledge。所以遇到「非標準」先別讓人類接管，先問一句：這是真的無規則可循，還是規則還沒被文件化？兩個答案通向兩條完全不同的路。

---

## 恍然大悟：三個預測是同一個組織的三張 X 光片

回看三個預測：2027 的 20% 照的是**資料**、2030 的新角色照的是**人**、2030 的 orchestration 照的是**結構**——同一個組織、三張 X 光片，而且病灶會互相轉移：資料不齊，agent 進不了門；agent 進不了門，角色拆不動；角色拆不動，orchestration 沒有棋子可調。Q&A 的每一題（標準化、非標準、direct/indirect、build/buy）問的都是「我這張片子上的陰影是什麼」。三張片子都乾淨的組織，才是預測裡那兩成、三成的分子。

AI-first 的第一步不是買模型，是拿起筆。

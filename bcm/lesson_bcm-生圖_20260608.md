# BCM 學習 + codex 生圖 —— 疊代修正紀錄（2026-06-08）

## 每一步到底發生了什麼

### 第 1 段：找「參加 workshop 沒有用」那篇（今天的主題在這就埋下了）

- **當時產出**：User 記得某篇講「參加 workshop 沒有用」，我先 grep 字面「workshop」，發現它只在中性語境出現（Gartner 自己辦 workshop、教你開 workshop 打分），沒人說參加 workshop 沒用。
- **使用者的話**：「想知道有一篇，有提到參加 workshop 沒有用，那份在這嗎」
- **我的解讀**：User 記的是**概念**不是字面詞。只認字面「workshop」會回「找不到」，但概念其實在 02 場——講法不同：「prompt 培訓是技能層，沒有動機 + 易用，技能不會 convert 成 adoption，花在 training 的錢會變沉沒成本」。
- **下一版動作**：給出 02 場那段，標明是「概念對應、不是字面命中」。**事後看：這是今天「字面 vs 意義」大主題的第一次出現——後面 BCM 的 capability 定義照字面讀會卡，是同一個病的放大版。主題其實 bookend 了整天。**

### 第 2 段：5 場 webinar 的 pipeline（04–08，前半天的主體工）

- **當時產出**：User 連丟 5 條 Bizzabo URL（04 Workforce / 05 FinOps / 06 Procurement / 07 IT 2030 / 08 Leading EA）。我每場走 yt-dlp 下載 → qwen-asr 轉錄四格式 → take-note 生 notes.md → spawn sub-agent review 行文 → 注 MOC，背景並行管理下載/轉錄、逐場補 source.md。專案 3 → 8 篇。每篇過結構檢查（H2 數對宣告、恍然大悟收束、標點全形、無中國用語、破折號收斂），review sub-agent 抓的踩線逐條套修。
- **使用者的話**：多為「這隻的也做一下」「下一個呢」式連續投餵，內容上無修正。
- **我的解讀**：流水線執行，User 滿意節奏。這是今天**做對且量大**的一段，lesson 不該因為「沒被糾正」就讓它隱形。
- **下一版動作**：照同一 pipeline 做完 04-08、注 MOC 跨場互鏈、修 01 講者名（ASR 拼 Hope → 官方 Hoeppe）。

### 第 3 段：commit / 網址（我斷言錯遠端）

- **當時產出**：分批 commit（每場一個 feat + 一個 docs 注 MOC + 一個 fix 講者名），準備 push。
- **使用者的話**：「ok, 這有放到 git 嗎」「commit」「網址」「只看到 3 場？」
- **我的解讀**：「網址」那輪我先斷言「repo 應該還沒有遠端」——`git remote -v` 一查，origin 早就設好，是我從「git log 沒顯示 origin」誤推成「沒遠端」。「只看到 3 場」是因為我還沒 push（遠端還是舊狀態）。
- **下一版動作**：老實更正「沒遠端是我講錯」；push 7 個 commit；私有 repo，確認 video.mp4 被 .gitignore 擋住、沒誤入版控。

### 第 4 段：BCM 說明太抽象

- **當時產出**：User 問 BCM 製作重點，我給了一份七條原則的清單（capability 三鐵則、pace layer、enabling…），全是原則陳述。
- **使用者的話**：「你的說明太抽象了，讀一下 /polish-doc，重寫」
- **我的解讀**：正確——我在講原則不是給做法。「太抽象」不是文字毛病，是缺具體 worked example。
- **下一版動作**：整篇改成「拿一家虛構家電廠『鼎電』走七步」，每條規則配真實畫出的框 + 對錯對照。User 回「好得多」。

### 第 5 段：生圖選錯工具（第一次踩 codex-not-html）

- **當時產出**：User 要「照此生最終結果圖片」，我用 HTML + headless Chrome 截圖做 BCM 圖。
- **使用者的話**：「這樣有點亂 你生成圖片要用 codex cli，我記得有在 gen image skill 說明才對，不要用 html 做圖吧」
- **我的解讀**：當下我以為自己選 HTML 是對的（skill 自己寫「dense text 用 HTML 較忠實」）。其實 User 有明確的工具偏好：生圖走 codex。我讀到 skill 那句 caveat 就繞去 HTML，反而違反偏好。
- **下一版動作**：改用 codex-image-gen 生圖；發現它沒被自動觸發 → 修 skill description。

### 第 6 段：skill 沒被觸發

- **當時產出**：上一輪我「手動」想到用 codex，但 skill 沒自己跳出來。
- **使用者的話**：「是有這份技能，但沒被呼叫，幫我更新一下這技能，同時 polish 文件」
- **我的解讀**：正確診斷 = description 兩個病：觸發詞全綁「codex」（「生結果圖片」沒這字配不上）+ description 裡寫「infographic 改用 HTML instead」這句自殺式 caveat 把自己主場往外推。
- **下一版動作**：補通用觸發詞、移除 caveat；polish-doc 雙引擎磨 prose。

### 第 7 段：第一個沒驗證的假設——「畫不出階層」

- **當時產出**：codex 生的鼎電圖是平鋪的，沒有 L1/L2 巢狀。我說「dense structure gpt-image-2 畫不出來，要回 HTML」。
- **使用者的話**：「有層次了，但是基礎單位是對的嗎？例如 招募？」後來更直接：「這應該不對，是你沒寫清楚給 codex 對吧」
- **我的解讀**：當下我把「圖平鋪」賴給模型。User 戳破——我去翻自己的 brief，發現**根本沒寫階層**，還自己把「人才管理」縮成單一個「人才留任」。是我 brief 拍平的，不是模型畫不出。
- **下一版動作**：寫明確要 L1 含 L2 的 brief 重生 → codex 畫出階層。把這個錯當教材寫進 skill 的 Mindset 段「brief 即 spec、別偷懶替換」。

### 第 8 段：單位純度——留任是 outcome 不是能力

- **當時產出**：鼎電圖把「留任、差旅報銷、預測性維護」當同級 capability 並列。
- **使用者的話**：「基礎單位是對的嗎？例如 招募？」
- **我的解讀**：正確質疑。我承認自己混了四種東西：留任是 outcome、差旅報銷是 process、預測性維護是 use case，全不是乾淨 capability。字面是業務名詞 ≠ 是乾淨 capability。
- **下一版動作**：正名（留任→敬業與留才管理、差旅報銷→費用管理、預測性維護→設備維護管理），AI 改釘在能力不釘在結果。

### 第 9 段：Google 那張是不是 BCM——視角問題

- **當時產出**：User 貼 Google Gemini Agent Platform 圖問是不是 BCM。我答「不是，那是 product（how）不是 business capability（what）」，並大談 tier 分層 + what/how。
- **使用者的話**：「分集分層是一部分，但不要過度聚焦，看一下剛剛的 image」接著「所以 是啥，這些感覺像是 Google 的 business capability，沒有嗎」
- **我的解讀**：兩個誤判。① 我化約成「分層 + what/how」兩軸，漏看圖上的 New/GA 狀態徽章（其實＝pace layer 那種疊加層）跟 Build 層的子分組。② 我說「不是 business capability」是站錯視角——站買方看是工具，**站 Google 自己看就是它的業務能力**。
- **下一版動作**：承認 capability vs product 取決於「誰的地圖」；補四副讀法眼鏡（視角/高度/底圖vs疊加層/單位純度）。

### 第 10 段：寫進詞彙表，不是開新檔；這是通病不是 BCM 問題

- **當時產出**：我把四副眼鏡寫成一份獨立的新 md 檔 `bcm-讀法-脫離字面.md`。
- **使用者的話**：「我覺得這個問題比較像是 ai 在生成文字的問題，不光是 BCM 的問題」「你要改的部分應該是詞彙表，而不是做一個 新的 md 文件」
- **我的解讀**：兩個都對。① 字面陷阱是 AI 把概念當字串的通病，BCM 只是例子（呼應 shape-not-string）。② 我又 over-engineer 開新檔；該壓成詞彙表條目。
- **下一版動作**：刪新檔；四副眼鏡壓成 01 詞彙表四條；通病寫進 take-note 的「字面陷阱」原則。

### 第 11 段：第二個假設——「SQLite lock 造成 server error」

- **當時產出**：銀行圖 server error，我說是兩個 codex 並行撞 SQLite lock。User 接著叫我「朽改 sqlite 讓他可以支援」。
- **使用者的話**：「朽改 sqlite 讓他可以支援」
- **我的解讀**：User 照我的（錯）診斷開了工單。我先驗證再動手——`PRAGMA journal_mode` 一查，四個 DB **本來就全是 WAL**（已支援並行），busy_timeout 又是連線層改不了。而且「server error」指向 OpenAI 後端，不是本機 SQLite。我的「SQLite lock」診斷是錯的。
- **下一版動作**：沒動 SQLite（沒東西可改）；改說真因在伺服器端並行。

### 第 12 段：第三個假設——「不能並行打 gpt-image-2」

- **當時產出**：我堅持「等你的 codex 跑完再生，否則並行會撞」。
- **使用者的話**：「為什麼不能多個打gpt-image-2」
- **我的解讀**：又被戳破——我從沒驗過「不能並行」。OpenAI 圖像 API 一般支援並行；而且這 session 的 server error 都「重試就成功」，是暫時性抖動的特徵，不是並行硬牆。
- **下一版動作**：故意不等、並行 fire 銀行圖 → **成功了**。並行假設當場死亡。而且這一 fire 意外露出 codex 的第二條引擎。

### 第 13 段：真發現——codex 兩條渲染路徑

- **當時產出**：並行硬生的銀行圖成功，codex 回報「built-in imagegen attempted, then deterministic local SVG/Pillow rendering」。圖最乾淨、中文零糊、虛線框第一次畫對、還附 .svg + .py。
- **使用者的話**：「更新技能說明，是限制嗎，還是可以成功？」「這應該不是 image-2 生成的, 可能是 svg 換的」
- **我的解讀**：User 要我分清「限制 vs 可主動成功」再寫 skill——不接受我推測。我測：明確叫 codex「render deterministically via SVG/Pillow, do NOT use raster model」→ 它照辦，出 .py + .svg + 乾淨 PNG。**可主動叫成功，不是限制。**
- **下一版動作**：skill 加「Two render paths」段（含觸發法 + 驗證日期 + 兩案例）；修掉「gpt-image-2 always renders」錯句；舊「改用 HTML」改成「叫 codex 確定性繪圖」；記憶 use-codex-not-html 同步升級。

## 共通教訓

1. **「現象 → 機制 → 結論」中，機制那層最會騙人。** 這場連犯三次（階層/SQLite/並行）都是：我用一個聽起來合理的機制解釋現象，然後當事實往下推。共通解藥不是「想得更周全」，是**先做最便宜的那個實測**——翻自己的 brief、跑一行 `PRAGMA`、並行 fire 一張。reason 講得再順，沒有 evidence 那格就是假設。其中最便宜的一種：**輸出缺東西，先查自己的輸入**——圖平鋪先查 brief 有沒有要階層，再怪模型，九成是自己沒寫。

2. **錯誤的診斷會生出錯誤的工單。** User 叫我「改 SQLite」「等並行」，都是照我的錯診斷下的指令。所以給診斷時若沒測過，要主動標「這是假設」，否則對方會拿它當結論去開下一步的工——錯誤就這樣從我這流到行動。

3. **「太抽象」「有點亂」不是文字毛病，是缺具體錨點 / 選錯載體。** 「太抽象」的解是換成一個具體 worked example（鼎電走一遍），不是把句子改漂亮；「有點亂」的解是換工具/版式，不是排版微調。

4. **User 的工具偏好是硬約束，不是我可以用「技術上更好」覆寫的。** 我兩次拿「HTML 對密集文字更忠實」去違反「生圖用 codex」，兩次被打回。偏好優先於我的技術論證——而且這次證明：在偏好框架內（codex 確定性 SVG）反而找到比 HTML 更好的解。

5. **同一個東西是 capability 還是 product，看「這是誰的地圖」。** 判斷框架類概念前先釘視角，否則會像我一樣站錯邊下結論。延伸：定義照字面抄會把人鎖死，要補「相對於誰、哪一層、什麼預設」。

6. **真正推進的不是我哪句分析對，是被推去「測一下」。** 這場每一次前進都來自一個實測，不是一次更聰明的推理。對協作的含義：我該主動把「我猜」變成「我去測」，不要等對方逼。

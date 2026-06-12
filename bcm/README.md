# BCM — 業務能力地圖工作區

> 方法學自 01 場 webinar（Alexander Hoeppe，*Accelerate Your AI Journey With Business Capability Maps*），加上 `bcm-creator` skill 對三家真實公司跑出的範例，跟下載的參考範本。
> BCM 的四副「讀法」眼鏡（視角／高度相對／底圖vs疊加層／單位純度）在 [`../01-ai-journey-business-capability-maps/notes.md`](../01-ai-journey-business-capability-maps/notes.md) 的詞彙表。

## 方法文件

| 檔 | 是什麼 |
|---|---|
| [`bcm-製作重點.md`](./bcm-製作重點.md) | **怎麼畫**。9 步走查（用虛構家電廠鼎電走一遍）。最難的是第 3 步「單位純度」——別把 outcome／process／use case 當能力放進框。 |
| [`bcm-使用與治理.md`](./bcm-使用與治理.md) | **怎麼用、怎麼養**。use case 評估（6 維 agent／技術+資料+整合／Defend-Extend-Upend）、AI readiness、Capability→Value Stream→Process→IT＋Digital Thread、metadata 卡、contextual data readiness、bimodal、update cadence。BCM 是 ongoing governance backbone。 |
| [`lesson_bcm-生圖_20260608.md`](./lesson_bcm-生圖_20260608.md) | 疊代修正紀錄：學 BCM ＋ 生圖那天連犯幾個「沒驗證就斷因果」的假設，怎麼被實測打死。 |

## 真實公司範例（`bcm-creator` 跑出）

每家兩份交付：**輸入功課 HTML**（底圖＝穩定事實：戰略目標 + 能力清單分 value-realizing／enabling）＋ **BCM 圖 PNG**（疊加層＝pace 上色 + AI 釘點）。

| 公司 | 視角 | 功課 HTML | 圖 PNG |
|---|---|---|---|
| TSMC 台積電 | 衝 AI 製程領先 | `tsmc-bcm-input.html` | `tsmc-bcm.png` |
| L'Oréal 萊雅 | AI 個人化／Beauty Tech | `loreal-bcm-input.html` | `loreal-bcm.png` |
| Pandora | 品牌＋手工＋自營零售 | `pandora-bcm-input.html` | `pandora-bcm.png` |
| BASF | 能源困局下的組合重整（Winning Ways） | `basf-bcm-input.html` | `basf-bcm.png` |
| CMoney 全曜財經 | 工具→社群→內容飛輪 × 數據變現 | `cmoney-bcm-input.html` | `cmoney-bcm.png` |
| Netflix | 訂閱規模經濟 × 內容資本配置 | `netflix-bcm-input.html` | `netflix-bcm.png` |
| The New York Times | 訂閱 LTV 飛輪 × 內容護城河 | `nyt-bcm-input.html` | `nyt-bcm.png` |
| Grinding Gear Games（PoE2） | 道德 F2P × live-service 長尾營運 | `poe2-bcm-input.html` | `poe2-bcm.png` |
| The RealReal | 鑑定信任護城河 × 轉盈路徑 | `therealreal-bcm-input.html` | `therealreal-bcm.png` |
| We Are Social | 重建獲利 × 文化創意差異化（社群代理） | `wearesocial-bcm-input.html` | `wearesocial-bcm.png` |
| 工研院 ITRI | 整合跨域創新 × 驗證樞紐（研究法人） | `itri-bcm-input.html` | `itri-bcm.png` |
| Cloudflare | 衝 $5B × 第四幕內容收費市場（分發基建） | `cloudflare-bcm-input.html` | `cloudflare-bcm.png` |
| TollBit | 兩面市場冷啟動 × agentic 基建（內容收費） | `tollbit-bcm-input.html` | `tollbit-bcm.png` |
| The Trade Desk | 危機修復 × 守住中立性（廣告分發 DSP） | `ttd-bcm-input.html` | `ttd-bcm.png` |
| AppLovin | 單引擎全壓 × 開放自助平台（AI 廣告分發） | `applovin-bcm-input.html` | `applovin-bcm.png` |
| ByteDance 字節跳動 | 守住分發現金機 × AI 攀峰（內容分發） | `bytedance-bcm-input.html` | `bytedance-bcm.png` |
| 小紅書 Xiaohongshu | 守住真實感 × 變現追趕（內容分發） | `xiaohongshu-bcm-input.html` | `xiaohongshu-bcm.png` |
| SmartNews | 日本現金機防守 × LLM 重建（內容分發） | `smartnews-bcm-input.html` | `smartnews-bcm.png` |
| OpusClip | 剪輯工具轉自主分發代理（內容分發） | `opusclip-bcm-input.html` | `opusclip-bcm.png` |

每家的 spec：`<公司>-bcm-input.json`（清單輸入）→ `.polished.json`（polish-doc 後，HTML 由它 render）；`<公司>-bcm.json`（圖的結構＋pace）。各家差異化落點不同，方法照各家研究推導、非套版。幾個對照組：We Are Social 的 AI 釘點是「該押但還沒有」（公司實際只有一個 AI 職位）；ITRI 是非營利法人，objectives 用準公共 KPI（技轉／新創／促成投資），AI 釘點只算院方自有動作、不算路過的政策經費。分發產業四連發（Cloudflare／TollBit／TTD／AppLovin）要一起讀：Cloudflare 與 TollBit 的「內容收費市場」橘格財報收入都還是零（押注型橘色），TTD 與 AppLovin 的橘格全是現金引擎（現金型橘色）——同一個 differentiating 色，兩種意思。內容分發四連發（ByteDance／小紅書／SmartNews／OpusClip）全是未上市公司，數字是媒體估計不是審計財報，可信度跟 10-K 組不同級；四張並排的看點是小紅書「社區治理」格的 AI 釘點——唯一一顆防禦性釘點（用 AI 抓 AI 灌水筆記），其他家全是進攻性變現。

## 早期示範（虛構，學方法用）

| 檔 | 是什麼 |
|---|---|
| `xinda-bcm-genimage.png` | 信達數位銀行 BCM（raster，純網銀示範） |
| `dingdian-ai-recruiting-map.png` | 鼎電對外「招募機會地圖」（raster，含公司背景＋疊加層） |
| `dingdian-business-capability-map.png`／`.svg`／`render_dingdian_business_capability_map.py` | 鼎電內部 BCM，走程式繪圖那條路（非 raster），保留當對照 |

## 參考範本（下載的真實 BCM 模板）

| 檔 | 是什麼 | 授權 |
|---|---|---|
| `apqc-pcf-v7.4-cross-industry.pdf` | APQC Process Classification Framework，跨產業 13 大類，畫 BCM 的「點菜單」。 | 免費可再散布，需標出處 |
| `qgea-bcrm.pdf`／`.vsdx`／`qgea-bcrm-definitions.xlsx` | 昆士蘭政府 Business Capability Reference Model。 | CC BY-NC-SA（非商用）|

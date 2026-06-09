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

每家的 spec：`<公司>-bcm-input.json`（清單輸入）→ `.polished.json`（polish-doc 後，HTML 由它 render）；`<公司>-bcm.json`（圖的結構＋pace）。三家差異化落點各不同，方法照各家研究推導、非套版。

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

# Gartner AI Webinars — 筆記庫 + BCM 工作區

Gartner 公開 AI webinar 的逐字稿與知識點筆記（8 場），加上一條從 01 場延伸出來的 Business Capability Map（BCM）工作線。下面用「你可能想問的問題」直接帶你到對的檔案。

**這裡有什麼**
- **8 場 webinar**（`01-`–`08-`）：每場一資料夾，內含 `notes.md`（H2 知識點，最完整）、`source.md`、`transcript.{srt,vtt,txt,json}`。影片太大不進 repo。
- **[`MOC.md`](./MOC.md)** — 8 場總索引（表格 + 按主題找）。
- **[`bcm/`](./bcm/)** — BCM 方法、三家公司實作範例、參考範本。
- **[`01-03-cross-synthesis.md`](./01-03-cross-synthesis.md)** — CIO/CHRO/CCO 三場深度跨場對照。

---

## Q：想快速抓某場的重點，看哪？
進該場資料夾的 `notes.md`。不確定看哪場 → 先到 [`MOC.md`](./MOC.md) 挑。

## Q：8 場分別在講什麼？

| # | 主題 | 一句話 |
|---|---|---|
| 01 | BCM | 用 BCM 把 AI 投資錨在 capability、不是 use case |
| 02 | HR AI | North Star outcome 先於工具；Skills + Motivation + Ease of Use |
| 03 | Comms AI | 逃 efficiency trap，comms 從 cost center 變 strategic partner |
| 04 | Workforce | 讓員工跟得上 AI 的人才轉型 |
| 05 | FinOps | 高價值 AI use case 的成本／價值取捨 |
| 06 | Procurement | AI-first 採購 |
| 07 | IT 2030 | 為 AI 時代重塑 IT |
| 08 | Leading EA | 帶領企業架構（EA）做 AI 轉型 |

講者、標籤、完整索引在 [`MOC.md`](./MOC.md)。

## Q：01–03 為什麼常被綁在一起？
它們是 CIO / CHRO / CCO 三場，**共用同一套 Gartner framework、只換 C-suite 外衣**。跨場對照（同一個 thesis、Value×Feasibility、portfolio 三層、readiness、agent 警告）整理在 [`01-03-cross-synthesis.md`](./01-03-cross-synthesis.md)。

## Q：什麼是 BCM？怎麼自己做一張？
- **概念**：01 場 [`notes.md`](./01-ai-journey-business-capability-maps/notes.md)，含四副讀法眼鏡（視角／高度相對／底圖vs疊加層／單位純度）。
- **怎麼做**：[`bcm/bcm-製作重點.md`](./bcm/bcm-製作重點.md) 的 9 步走查。最難的是第 3 步「單位純度」——別把 outcome／process／use case 當能力放進框。

## Q：BCM 畫完之後怎麼用、怎麼養？
它是 ongoing governance backbone，不是畫完存檔的文件。[`bcm/bcm-使用與治理.md`](./bcm/bcm-使用與治理.md) 涵蓋：把 use case 映射上去（AI Opportunity Radar、6 維 agent 能力、Defend/Extend/Upend、技術+資料源+整合）、AI readiness（contextual）、Capability→Value Stream→Process→IT＋Digital Thread、每能力 metadata 卡、把 bottom-up POC 接回 BCM、每季/半年的 update cadence。

## Q：有做好的 BCM 範例嗎？
`bcm/` 有三家**真實公司**，各一份「輸入功課 HTML」＋一張「BCM 圖」：

| 公司 | 產業 | 視角 | 功課 | 圖 |
|---|---|---|---|---|
| TSMC 台積電 | 半導體代工 | 衝 AI 製程領先 | `bcm/tsmc-bcm-input.html` | `bcm/tsmc-bcm.png` |
| L'Oréal 萊雅 | 美妝 | AI 個人化／Beauty Tech | `bcm/loreal-bcm-input.html` | `bcm/loreal-bcm.png` |
| Pandora | 珠寶手作 | 品牌＋手工＋自營零售 | `bcm/pandora-bcm-input.html` | `bcm/pandora-bcm.png` |

三家差異化落點各不同（製程 vs 個人化 vs 手工藝），方法照各家研究推導、非套版。`bcm/` 自己的索引見 [`bcm/README.md`](./bcm/README.md)。

## Q：BCM 的「功課」跟「圖」差在哪？為何分開？
- **功課 HTML** = 底圖：穩定事實（戰略目標 + 能力清單，分 value-realizing / value-enabling）。
- **圖 PNG** = 疊加層：pace layer 上色 + AI 釘點——隨戰略視角會變的判斷。

分開是因為 pace／AI 是「疊加層」，不是能力的天生屬性（01 場讀法）。

## Q：這些數字可信嗎？
每份功課底部有「資料註記」，標出口徑、估計值、待補，並附來源清單。**內部欄位（owner／系統／KPI／data readiness）非公開、一律標待補**——只有公司自己填得了。

## Q：怎麼生一張新的 BCM？
用 `bcm-creator` skill（在本機 `~/.claude/skills/`，**不在這個 repo**）：釐清 → 研究 → 功課 HTML（含 polish）→ raster 圖。

---

## 結構

```
.
├── 01-ai-journey-business-capability-maps/   # 01–08：每場 notes.md + transcript + source.md
├── 02-hr-ai-stop-funding-features/
├── …  06, 07
├── 08-leading-ea-ai-transformation/
├── MOC.md                      # 8 場總索引
├── 01-03-cross-synthesis.md    # CIO/CHRO/CCO 三場深度對照
└── bcm/                        # BCM 方法、TSMC/L'Oréal/Pandora 範例、參考範本
```

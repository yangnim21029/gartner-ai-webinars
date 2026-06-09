from html import escape
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


W, H = 1600, 1067
OUT_SVG = Path("dingdian-business-capability-map.svg")
OUT_PNG = Path("dingdian-business-capability-map.png")

FONT_CANDIDATES = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]

COLORS = {
    "orange": "#d9701b",
    "gold": "#f5c266",
    "cream": "#fbf4e2",
    "black": "#151515",
    "text": "#202124",
    "muted": "#70757d",
    "tier": "#777d86",
    "line": "#edf0f3",
    "stroke": "#cfd4dc",
    "child_stroke": "#b9bec7",
    "header": "#f1f3f6",
    "white": "#ffffff",
    "ai": "#111111",
}


def font_path():
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError("No CJK-capable system font found.")


FONT_PATH = font_path()


def pil_font(size, weight="regular"):
    return ImageFont.truetype(FONT_PATH, size=size)


FONTS = {
    "title": pil_font(40, "bold"),
    "subtitle": pil_font(21),
    "tier": pil_font(29, "bold"),
    "l1": pil_font(24, "bold"),
    "l2": pil_font(22, "bold"),
    "legend": pil_font(18, "bold"),
    "ai": ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size=14),
}


SVG_STYLE = """
    .bg { fill: #ffffff; }
    .title { font: 800 40px "PingFang TC", "Hiragino Sans GB", "STHeiti", "Microsoft JhengHei", Arial, sans-serif; fill: #151515; }
    .subtitle { font: 500 21px "PingFang TC", "Hiragino Sans GB", "STHeiti", "Microsoft JhengHei", Arial, sans-serif; fill: #70757d; }
    .tier { font: 800 29px "PingFang TC", "Hiragino Sans GB", "STHeiti", "Microsoft JhengHei", Arial, sans-serif; fill: #777d86; }
    .l1-label { font: 800 24px "PingFang TC", "Hiragino Sans GB", "STHeiti", "Microsoft JhengHei", Arial, sans-serif; fill: #24272b; }
    .l2-label { font: 800 22px "PingFang TC", "Hiragino Sans GB", "STHeiti", "Microsoft JhengHei", Arial, sans-serif; fill: #202124; }
    .legend { font: 700 18px "PingFang TC", "Hiragino Sans GB", "STHeiti", "Microsoft JhengHei", Arial, sans-serif; fill: #24272b; }
    .ai-text { font: 800 14px Arial, sans-serif; fill: #ffffff; letter-spacing: 0; }
    .container { fill: #ffffff; stroke: #cfd4dc; stroke-width: 1.4; }
    .header { fill: #f1f3f6; }
    .orange { fill: #d9701b; }
    .gold { fill: #f5c266; }
    .cream { fill: #fbf4e2; }
    .child-stroke { stroke: #b9bec7; stroke-width: 1.2; }
    .dashed { stroke-dasharray: 8 6; stroke-width: 2; }
    .rule { stroke: #edf0f3; stroke-width: 1; }
"""


MAP = [
    {
        "tier": "策略層",
        "tier_xy": (58, 235),
        "containers": [
            {
                "title": "經營治理",
                "box": (335, 145, 1030, 155),
                "children": [
                    ("策略管理", "gold", False, False, (82, 76, 250, 58)),
                    ("治理合規", "gold", False, False, (390, 76, 250, 58)),
                    ("風險管理", "gold", False, False, (698, 76, 250, 58)),
                ],
            }
        ],
    },
    {
        "tier": "核心層",
        "tier_xy": (58, 525),
        "containers": [
            {
                "title": "產品創新",
                "box": (190, 365, 420, 265),
                "children": [
                    ("產品開發", "orange", True, False, (38, 88, 160, 72)),
                    ("工業設計", "orange", True, False, (222, 88, 160, 72)),
                ],
            },
            {
                "title": "需求供應",
                "box": (590, 365, 420, 265),
                "children": [
                    ("需求預測", "orange", True, False, (38, 78, 160, 70)),
                    ("供應鏈管理", "gold", False, False, (222, 78, 160, 70)),
                    ("採購管理", "gold", False, False, (130, 170, 160, 70)),
                ],
            },
            {
                "title": "品質售後",
                "box": (990, 365, 420, 265),
                "children": [
                    ("品質管理", "gold", False, False, (38, 88, 160, 72)),
                    ("售後服務管理", "gold", False, False, (222, 88, 160, 72)),
                ],
            },
        ],
    },
    {
        "tier": "支援層",
        "tier_xy": (58, 825),
        "containers": [
            {
                "title": "人才管理",
                "box": (190, 700, 420, 240),
                "children": [
                    ("人才招募", "cream", False, False, (38, 75, 160, 58)),
                    ("學習發展", "cream", False, False, (222, 75, 160, 58)),
                    ("敬業與留才", "orange", True, False, (38, 152, 160, 58)),
                    ("薪酬管理", "cream", False, False, (222, 152, 160, 58)),
                ],
            },
            {
                "title": "財務管理",
                "box": (590, 700, 420, 240),
                "children": [
                    ("財務會計", "gold", False, False, (38, 82, 160, 62)),
                    ("費用管理", "cream", True, False, (222, 82, 160, 62)),
                    ("資金管理", "gold", False, False, (130, 160, 160, 62)),
                ],
            },
            {
                "title": "設備資料",
                "box": (990, 700, 420, 240),
                "children": [
                    ("設備維護管理", "orange", True, False, (38, 104, 160, 70)),
                    ("資料治理", "cream", False, True, (222, 104, 160, 70)),
                ],
            },
        ],
    },
]


def rounded_rect_svg(x, y, w, h, rx, classes=None, fill=None, stroke=None, dashed=False):
    attrs = [f'x="{x}"', f'y="{y}"', f'width="{w}"', f'height="{h}"', f'rx="{rx}"']
    if classes:
        attrs.append(f'class="{classes}"')
    if fill:
        attrs.append(f'fill="{fill}"')
    if stroke:
        attrs.append(f'stroke="{stroke}"')
    if dashed:
        attrs.append('stroke-dasharray="8 6"')
        attrs.append('stroke-width="2"')
    return f"    <rect {' '.join(attrs)}/>"


def text_svg(text, x, y, cls, anchor="start"):
    return f'    <text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{escape(text)}</text>'


def header_path_svg(w, h=45, r=16):
    return f'    <path class="header" d="M{r} 0H{w-r}Q{w} 0 {w} {r}V{h}H0V{r}Q0 0 {r} 0Z"/>'


def draw_centered(draw, text, box, font, fill):
    x, y, w, h = box
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x + (w - tw) / 2, y + (h - th) / 2 - 1), text, font=font, fill=fill)


def draw_l2_label(draw, text, box, has_ai=False):
    x, y, w, h = box
    if has_ai:
        draw_centered(draw, text, (x, y + 24, w, h - 24), FONTS["l2"], COLORS["text"])
    else:
        draw_centered(draw, text, box, FONTS["l2"], COLORS["text"])


def draw_ai_pill(draw, x, y):
    draw.rounded_rectangle((x, y, x + 32, y + 20), radius=10, fill=COLORS["ai"])
    draw_centered(draw, "AI", (x, y + 1, 32, 18), FONTS["ai"], COLORS["white"])


def draw_dashed_round_rect(draw, xy, radius, fill, outline, width=2, dash=8, gap=6):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)
    # Dashed border approximation: draw dash segments around the straight sides.
    x = x1 + radius
    while x < x2 - radius:
        draw.line((x, y1, min(x + dash, x2 - radius), y1), fill=outline, width=width)
        draw.line((x, y2, min(x + dash, x2 - radius), y2), fill=outline, width=width)
        x += dash + gap
    y = y1 + radius
    while y < y2 - radius:
        draw.line((x1, y, x1, min(y + dash, y2 - radius)), fill=outline, width=width)
        draw.line((x2, y, x2, min(y + dash, y2 - radius)), fill=outline, width=width)
        y += dash + gap
    # Solid corner arcs keep the rounded shape clean at this output size.
    draw.arc((x1, y1, x1 + radius * 2, y1 + radius * 2), 180, 270, fill=outline, width=width)
    draw.arc((x2 - radius * 2, y1, x2, y1 + radius * 2), 270, 360, fill=outline, width=width)
    draw.arc((x1, y2 - radius * 2, x1 + radius * 2, y2), 90, 180, fill=outline, width=width)
    draw.arc((x2 - radius * 2, y2 - radius * 2, x2, y2), 0, 90, fill=outline, width=width)


def generate_svg():
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        '  <title id="title">鼎電 Business Capability Map</title>',
        '  <desc id="desc">自有品牌家電製造商 · pace layer 戰略地位（示範）</desc>',
        "  <defs>",
        "  <style>",
        SVG_STYLE.rstrip(),
        "  </style>",
        "  </defs>",
        "",
        f'  <rect class="bg" x="0" y="0" width="{W}" height="{H}"/>',
        "",
        text_svg("鼎電 Business Capability Map", 62, 64, "title"),
        text_svg("自有品牌家電製造商 · pace layer 戰略地位（示範）", 64, 100, "subtitle"),
        "",
    ]
    for y in [125, 330, 665, 962]:
        lines.append(f'  <line class="rule" x1="62" y1="{y}" x2="1538" y2="{y}"/>')
    lines.append("")

    for tier in MAP:
        tx, ty = tier["tier_xy"]
        lines.append(text_svg(tier["tier"], tx, ty, "tier"))
        for container in tier["containers"]:
            cx, cy, cw, ch = container["box"]
            lines.append(f'  <g transform="translate({cx} {cy})">')
            lines.append(rounded_rect_svg(0, 0, cw, ch, 16, "container"))
            lines.append(header_path_svg(cw))
            lines.append(text_svg(container["title"], cw / 2, 31, "l1-label", "middle"))
            for label, color, ai, dashed, child in container["children"]:
                x, y, w, h = child
                cls = f"{color} child-stroke" + (" dashed" if dashed else "")
                lines.append(f'    <g transform="translate({x} {y})">')
                lines.append(rounded_rect_svg(0, 0, w, h, 11, cls))
                if ai:
                    lines.append(text_svg(label, w / 2, h - 14, "l2-label", "middle"))
                    px, py = w - 43, 10
                    lines.append(f'    <rect x="{px}" y="{py}" width="32" height="20" rx="10" fill="#111111"/>')
                    lines.append(f'    <text class="ai-text" x="{px + 16}" y="{py + 15}" text-anchor="middle">AI</text>')
                else:
                    lines.append(text_svg(label, w / 2, h / 2 + 8, "l2-label", "middle"))
                lines.append("    </g>")
            lines.append("  </g>")
            lines.append("")

    lines.extend(
        [
            '  <g transform="translate(78 1018)">',
            '    <rect class="orange" x="0" y="-20" width="34" height="24" rx="6"/>',
            text_svg("競爭優勢 重押AI", 44, 0, "legend"),
            '    <rect class="gold child-stroke" x="254" y="-20" width="34" height="24" rx="6"/>',
            text_svg("跟上別落後", 298, 0, "legend"),
            '    <rect class="cream child-stroke" x="456" y="-20" width="34" height="24" rx="6"/>',
            text_svg("買現成", 500, 0, "legend"),
            '    <rect class="cream child-stroke dashed" x="620" y="-20" width="34" height="24" rx="6"/>',
            text_svg("養地基 不准砍", 664, 0, "legend"),
            '    <rect class="container" x="860" y="-22" width="48" height="28" rx="8"/>',
            '    <path class="header" d="M868 -22H900Q908 -22 908 -14V-10H860V-14Q860 -22 868 -22Z"/>',
            text_svg("L1 母能力 內含 L2 子能力", 920, 0, "legend"),
            "  </g>",
            "</svg>",
        ]
    )
    OUT_SVG.write_text("\n".join(lines), encoding="utf-8")


def generate_png():
    im = Image.new("RGB", (W, H), COLORS["white"])
    draw = ImageDraw.Draw(im)
    draw.text((62, 24), "鼎電 Business Capability Map", font=FONTS["title"], fill=COLORS["black"])
    draw.text((64, 77), "自有品牌家電製造商 · pace layer 戰略地位（示範）", font=FONTS["subtitle"], fill=COLORS["muted"])

    for y in [125, 330, 665, 962]:
        draw.line((62, y, 1538, y), fill=COLORS["line"], width=1)

    for tier in MAP:
        draw.text(tier["tier_xy"], tier["tier"], font=FONTS["tier"], fill=COLORS["tier"])
        for container in tier["containers"]:
            cx, cy, cw, ch = container["box"]
            draw.rounded_rectangle((cx, cy, cx + cw, cy + ch), radius=16, fill=COLORS["white"], outline=COLORS["stroke"], width=2)
            draw.rounded_rectangle((cx, cy, cx + cw, cy + 52), radius=16, fill=COLORS["header"])
            draw.rectangle((cx, cy + 30, cx + cw, cy + 52), fill=COLORS["header"])
            draw_centered(draw, container["title"], (cx, cy, cw, 45), FONTS["l1"], "#24272b")

            for label, color, ai, dashed, child in container["children"]:
                x, y, w, h = child
                bx, by = cx + x, cy + y
                if dashed:
                    draw_dashed_round_rect(
                        draw,
                        (bx, by, bx + w, by + h),
                        11,
                        COLORS[color],
                        COLORS["child_stroke"],
                        width=2,
                    )
                else:
                    draw.rounded_rectangle(
                        (bx, by, bx + w, by + h),
                        radius=11,
                        fill=COLORS[color],
                        outline=COLORS["child_stroke"],
                        width=1,
                    )
                draw_l2_label(draw, label, (bx, by, w, h), has_ai=ai)
                if ai:
                    draw_ai_pill(draw, bx + w - 43, by + 10)

    lx, ly = 78, 1018
    legend_items = [
        ("orange", False, "競爭優勢 重押AI", 0),
        ("gold", False, "跟上別落後", 254),
        ("cream", False, "買現成", 456),
        ("cream", True, "養地基 不准砍", 620),
    ]
    for color, dashed, label, x in legend_items:
        if dashed:
            draw_dashed_round_rect(draw, (lx + x, ly - 20, lx + x + 34, ly + 4), 6, COLORS[color], COLORS["child_stroke"])
        else:
            draw.rounded_rectangle((lx + x, ly - 20, lx + x + 34, ly + 4), radius=6, fill=COLORS[color], outline=COLORS["child_stroke"] if color != "orange" else None, width=1)
        draw.text((lx + x + 44, ly - 20), label, font=FONTS["legend"], fill="#24272b")

    x = 860
    draw.rounded_rectangle((lx + x, ly - 22, lx + x + 48, ly + 6), radius=8, fill=COLORS["white"], outline=COLORS["stroke"], width=2)
    draw.rounded_rectangle((lx + x, ly - 22, lx + x + 48, ly - 10), radius=8, fill=COLORS["header"])
    draw.rectangle((lx + x, ly - 16, lx + x + 48, ly - 10), fill=COLORS["header"])
    draw.text((lx + x + 60, ly - 20), "L1 母能力 內含 L2 子能力", font=FONTS["legend"], fill="#24272b")

    im.save(OUT_PNG)


if __name__ == "__main__":
    generate_svg()
    generate_png()
    print(OUT_SVG)
    print(OUT_PNG)

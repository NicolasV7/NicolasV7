"""Genera dark_mode.svg y light_mode.svg del perfil (estatico, sin datos externos)."""

ASCII_LABEL = "~ ghost in the shell ~"

ART = [
    '        *=',
    '        *--=+',
    '        *==--=+',
    '         ====--++%* #   ***+*',
    '  *      +=======+====+++++*',
    ' +=====  +=+==---------===+++**+++++++====*',
    ' *+===-=+*+=------------========--------=+',
    '   +========-=----------====+=========+*',
    '    +++====+===-------======++=====++*',
    '     +=+===+::+=========+++++===++*',
    '    *=++++++-:=+++++==++==-++===+#',
    '    +-=++.:+++==+==++==-::=+=+==++=======*',
    '    +==++-.--=+++++++====+++++++=+====+++',
    '    *==++*+:.:-:--=+=+++==++++++++++*',
    '   ##++*****==:....:...--++++++#',
    '   +********##**+=+=-=+*******#',
    '   +=+********########*****###',
    '    *++**************+++++++#',
    '      #**#**********++++++++*',
    '              #***#*++++++==*',
    '                *#   +****++',
    '                      ****',
]

DARK = {
    "bg": "#161b22", "fg": "#c9d1d9", "key": "#ffa657", "value": "#a5d6ff",
    "dots": "#616e7f", "art": "#bc8cff", "accent": "#7ee787",
}
LIGHT = {
    "bg": "#fffefe", "fg": "#24292f", "key": "#953800", "value": "#0a3069",
    "dots": "#6e7781", "art": "#8250df", "accent": "#1a7f37",
}

LINE_W = 60


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def kv(key, value):
    prefix = f". {key}: "
    dots = "." * max(2, LINE_W - len(prefix) - len(value) - 1)
    return [(". ", "cc"), (key, "key"), (": ", "fg"), (dots + " ", "cc"), (value, "value")]


def header(text):
    dashes = "-" + "—" * (LINE_W - len(text) - 3) + "-"
    return [(text, "key"), (" " + dashes, "cc")]


LINES = [
    header("nicolas"),
    kv("OS", "Linux"),
    kv("Role", "Security Researcher"),
    kv("Background", "Full Stack, DevOps"),
    None,
    kv("Languages.Programming", "TypeScript, Python, Java"),
    kv("Languages.Real", "Espanol, English"),
    None,
    header("- Focus"),
    kv("Now", "security research"),
    kv("Interests", "appsec, pentesting, self-hosting"),
    None,
    header("- Contact"),
    kv("LinkedIn", "in/nicolasdlp"),
    kv("Email", "nicolas@delapava.dev"),
]


def render(p):
    width, height = 985, 530
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" font-family="Consolas,Menlo,monospace" '
        f'width="{width}px" height="{height}px" font-size="16px">',
        "<style>",
        f".fg {{fill: {p['fg']};}} .key {{fill: {p['key']};}} .value {{fill: {p['value']};}}",
        f".cc {{fill: {p['dots']};}} .art {{fill: {p['art']};}} .accent {{fill: {p['accent']};}}",
        "text, tspan {white-space: pre;}",
        "</style>",
        f'<rect width="{width}px" height="{height}px" fill="{p["bg"]}" rx="15"/>',
        '<text x="20" y="56" class="art">',
    ]
    for i, row in enumerate(ART):
        out.append(f'<tspan x="20" y="{56 + i * 20}">{esc(row)}</tspan>')
    label_x = 20 + max(0, (44 - len(ASCII_LABEL)) // 2) * 9
    out.append(f'<tspan x="{label_x}" y="{56 + len(ART) * 20 + 10}" class="accent">{esc(ASCII_LABEL)}</tspan>')
    out.append("</text>")
    out.append('<text x="430" y="56" class="fg">')
    y = 56
    for line in LINES:
        if line is not None:
            spans = "".join(f'<tspan class="{cls}">{esc(txt)}</tspan>' for txt, cls in line)
            out.append(f'<tspan x="430" y="{y}">{spans}</tspan>')
        y += 28
    out.append("</text></svg>")
    return "\n".join(out)


if __name__ == "__main__":
    for name, palette in (("dark_mode.svg", DARK), ("light_mode.svg", LIGHT)):
        with open(name, "w", encoding="utf-8") as f:
            f.write(render(palette))
    print("ok")

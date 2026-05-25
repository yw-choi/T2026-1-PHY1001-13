#!/usr/bin/env python3
"""Inject answers with OMML math into midterm docx answer boxes.

Approach: for each subproblem, write LaTeX-flavored markdown, let pandoc
convert to OMML, extract the generated <w:p>...</w:p> blocks, and splice
them into the target cell's answer space.
"""

import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

# Each subproblem: (key, list of markdown paragraphs)
# Each "paragraph" becomes one <w:p> in the target cell after the problem
# statement.  LaTeX math uses $...$ inline form.
ANSWERS = {
    "1(a)": [
        r"**[제1법칙 서술 2점]** 물체에 작용하는 알짜힘이 0이면, 정지한 물체는 계속 정지, 운동하는 물체는 등속직선운동을 유지한다 ($\vec{F}_\text{net} = 0 \Rightarrow \vec{v}$ = 일정).",
        r"**[관성 기준틀 3점]** 제1법칙이 성립하는 기준틀. 즉, 가속하지 않고 등속으로 움직이거나 정지한 기준틀. (가속·회전 기준틀은 $\vec{F}_\text{net}=0$ 인데도 가속하는 것처럼 보이므로 제1법칙이 그대로 성립하지 않음.)",
    ],
    "1(b)": [
        r"$\vec{F}_\text{net} = m\vec{a} \Rightarrow a = F_\text{net}/m$.",
        r"**[2.5점]** 질량 일정, $F \to 2F$: $a' = \dfrac{2F}{m} = 2a$ → 가속도 **2배**.",
        r"**[2.5점]** 힘 일정, $m \to 3m$: $a' = \dfrac{F}{3m} = \dfrac{a}{3}$ → 가속도 **1/3배**.",
    ],
    "1(c)": [
        r"**[제3법칙 1점]** A가 B에 $\vec{F}_{AB}$를 가하면 B도 A에 $\vec{F}_{BA} = -\vec{F}_{AB}$를 가한다 (서로 다른 두 물체에 작용).",
        r"**[쌍 ① 책–지구 중력 2점]** 지구→책 $= m\vec{g}$ (아래) ↔ 책→지구 $= -m\vec{g}$ (위).",
        r"**[쌍 ② 책–테이블 수직항력 2점]** 테이블→책 $= \vec{N}$ (위) ↔ 책→테이블 $= -\vec{N}$ (아래).",
        r"(참고: 책에 작용하는 $m\vec{g}$와 $\vec{N}$은 둘 다 책에 작용하므로 작용-반작용 쌍이 아니라 힘의 평형.)",
    ],
    "2(a)": [
        r"$y(t) = v_0\sin\theta_0 \cdot t - \tfrac{1}{2}gt^2$, $y=0 \Rightarrow$ **[비행시간 3점]** $t_f = \dfrac{2v_0\sin\theta_0}{g}$.",
        r"**[사거리 2점]** $R = v_0\cos\theta_0 \cdot t_f = \dfrac{v_0^2 \sin(2\theta_0)}{g}$.",
    ],
    "2(b)": [
        r"(a)에서 바로: $t(\theta_0) = \dfrac{2v_0\sin\theta_0}{g}$. **[5점]**",
    ],
    "2(c)": [
        r"**[$t_\text{max}$ 2점]** $t(\theta_0) \propto \sin\theta_0$이므로 $\theta_0 = 90°$에서 $t_\text{max} = \dfrac{2v_0}{g}$.",
        r"**[방정식 2점]** $t(\theta_0) = 0.5\, t_\text{max} \Rightarrow \sin\theta_0 = \tfrac{1}{2}$.",
        r"**[해 1점]** 발사각 범위 $0° < \theta_0 \le 90°$에서 $\theta_0 = 30°$.",
    ],
    "2(d)": [
        r"$v^2 = v_x^2 + v_y^2$, $v_x = v_0\cos\theta_0$ (일정), $v_y(t) = v_0\sin\theta_0 - gt$.",
        r"**[최소 조건 3점]** $v_x$가 일정하므로 $v^2$은 $v_y=0$일 때 최소 → **궤적의 최고점**.",
        r"**[물리적 해석 3점]** 중력은 연직 방향으로만 작용 → $v_x$ 보존, $v_y$만 감속(상승)→0→증가(하강). 최고점에서는 수평 성분만 남음.",
        r"**[$v_\text{min}$ 4점]** $\theta_0 = 30°$: $v_\text{min} = v_0\cos 30° = \dfrac{\sqrt{3}}{2}v_0$.",
    ],
    "3(a)": [
        r"**[$\Delta p$ 3점]** 충격량-운동량 정리: $\Delta p = F\Delta t$.",
        r"**[$v$ 3점]** 초기 정지, $\Delta p = mv \Rightarrow v = \dfrac{F\Delta t}{m}$.",
        r"**[$W$ 4점]** 일-운동에너지 정리: $W = \Delta K = \tfrac{1}{2}mv^2 = \dfrac{F^2(\Delta t)^2}{2m}$.",
    ],
    "3(b)": [
        r"운동량 성분 보존 ⇔ 그 방향의 알짜힘 $=0$.",
        r"**[수평면, 수평 1점]** 알짜힘 $= F \neq 0 \Rightarrow$ 보존 ✗.",
        r"**[수평면, 연직 1점]** 중력 $+$ 수직항력 $= 0 \Rightarrow$ 보존 ✓.",
        r"**[경사면 수직항력 2점]** $N = mg\cos\theta$ (경사면에 수직한 방향으로 가속 없음).",
        r"**[경사면, 수평 2점]** 알짜힘 $= -N\sin\theta = -mg\sin\theta\cos\theta \neq 0 \Rightarrow$ 보존 ✗.",
        r"**[경사면, 연직 2점]** 알짜힘 $= N\cos\theta - mg = -mg\sin^2\theta \neq 0 \Rightarrow$ 보존 ✗.",
        r"**[이유 설명 2점]** 경사면의 수직항력이 수평·연직 두 방향 모두에 성분을 가지므로 두 성분 모두 보존되지 않는다.",
    ],
    "3(c)": [
        r"**[진입 직후 2점]** $K_i = \tfrac{1}{2}mv^2 = \dfrac{F^2(\Delta t)^2}{2m}$, $U_i = 0$ (수평면 기준).",
        r"**[정지 순간 2점]** 거리 $d$, 높이 $h = d\sin\theta$: $K_f = 0$, $U_f = mgd\sin\theta$.",
        r"**[에너지 보존 3점]** 마찰 없음, 수직항력은 일을 하지 않음: $\tfrac{1}{2}mv^2 = mgd\sin\theta$.",
        r"**[$d$ 계산 3점]** $d = \dfrac{v^2}{2g\sin\theta} = \dfrac{F^2(\Delta t)^2}{2m^2 g\sin\theta}$. ($U_f = \dfrac{F^2(\Delta t)^2}{2m}$.)",
    ],
    "4(a)": [
        r"**[보존법칙 3점]** 축에 대한 외부 토크 0 (중력·축 수직항력은 축을 지남, 충돌 내력은 상쇄) → **각운동량 보존**.",
        r"**[$L_i$ 2점]** 충돌 전: $L_i = mvR$ (충격 매개변수 $R$).",
        r"**[$I_f$ 3점]** 충돌 후: $I_f = \tfrac{1}{2}MR^2 + mR^2 = \dfrac{(M+2m)R^2}{2}$.",
        r"**[$\omega$ 2점]** $mvR = I_f\omega \Rightarrow \omega = \dfrac{2mv}{(M+2m)R}$.",
    ],
    "4(b)": [
        r"**[$K_i$ 1점]** $K_i = \tfrac{1}{2}mv^2$.",
        r"**[$K_f$ 계산 4점]** $K_f = \tfrac{1}{2}I_f\omega^2 = \tfrac{1}{2}\cdot\dfrac{(M+2m)R^2}{2}\cdot\dfrac{4m^2v^2}{(M+2m)^2R^2} = \dfrac{m^2v^2}{M+2m}$.",
        r"**[비율·부등식 3점]** $\dfrac{K_f}{K_i} = \dfrac{2m}{M+2m} < 1$ ($M>0$이므로 $M+2m > 2m$).",
        r"**[판정 2점]** $K$ 감소 → **비탄성 충돌**. 입자가 원판에 붙으므로 **완전비탄성 충돌**.",
    ],
    "4(c)": [
        r"**[보존량 3점]** 미는 힘은 반지름 방향 → 축에 대한 토크 0 → **각운동량 보존** ($L = mvR$ 유지).",
        r"**[$I(r)$ 3점]** $I(r) = \tfrac{1}{2}MR^2 + mr^2$.",
        r"**[$\omega_f$ 유도 4점]** $L = I(r)\omega_f \Rightarrow \omega_f = \dfrac{mvR}{\tfrac{1}{2}MR^2 + mr^2} = \dfrac{2mvR}{MR^2 + 2mr^2}$.",
    ],
}

ORDER = ["1(a)", "1(b)", "1(c)",
         "2(a)", "2(b)", "2(c)", "2(d)",
         "3(a)", "3(b)", "3(c)",
         "4(a)", "4(b)", "4(c)"]


def md_para_to_wp(md_para: str) -> str:
    """Convert one markdown paragraph (with LaTeX math) to a single <w:p>...</w:p>.

    Uses pandoc to produce a docx, then extracts the first <w:p> from body.
    """
    with tempfile.TemporaryDirectory() as td:
        md_path = Path(td) / "frag.md"
        md_path.write_text(md_para + "\n", encoding="utf-8")
        docx_path = Path(td) / "frag.docx"
        subprocess.run(
            ["pandoc", str(md_path), "-o", str(docx_path)],
            check=True, capture_output=True,
        )
        # unzip
        with zipfile.ZipFile(docx_path) as zf:
            xml = zf.read("word/document.xml").decode("utf-8")
    # Find the first <w:p ...>...</w:p> in body (skip the <w:sectPr>'s parent)
    # pandoc wraps content in <w:body>. We want paragraphs that contain our text.
    # Simplest: find all <w:p>...</w:p> but exclude the last one which is the
    # section properties paragraph (contains <w:sectPr>).
    paras = re.findall(r"<w:p\b[^>]*>.*?</w:p>", xml, flags=re.DOTALL)
    # Keep only paragraphs NOT containing sectPr
    content_paras = [p for p in paras if "<w:sectPr" not in p]
    if not content_paras:
        raise RuntimeError("No content paragraph found in pandoc output")
    out = content_paras[0]
    # Schema-fix pandoc OMML: m:sty is not valid as an element child of m:rPr
    # in strict OOXML math schema. Remove it (variables will render italic,
    # which is the desired math convention).
    out = re.sub(r"<m:sty\s[^/]*/>", "", out)
    # m:nor alone is ok but remove if it leaves empty m:rPr
    out = re.sub(r"<m:rPr>\s*</m:rPr>", "", out)
    # Also strip pandoc's "FirstParagraph" pStyle — not defined in our target
    # document's styles.xml. We'll inherit default paragraph style.
    out = re.sub(
        r'<w:pPr><w:pStyle w:val="FirstParagraph"\s*/></w:pPr>',
        '<w:pPr><w:rPr><w:rFonts w:ascii="Malgun Gothic" w:eastAsia="Malgun Gothic" w:hAnsi="Malgun Gothic"/><w:sz w:val="20"/></w:rPr></w:pPr>',
        out,
    )
    # Add font size 20 to runs (match exam's 10pt style)
    out = re.sub(
        r"<w:r>(\s*<w:t)",
        r'<w:r><w:rPr><w:rFonts w:ascii="Malgun Gothic" w:eastAsia="Malgun Gothic" w:hAnsi="Malgun Gothic"/><w:sz w:val="20"/></w:rPr>\1',
        out,
    )
    out = re.sub(
        r"<w:r><w:rPr><w:b\s*/><w:bCs\s*/></w:rPr>",
        r'<w:r><w:rPr><w:rFonts w:ascii="Malgun Gothic" w:eastAsia="Malgun Gothic" w:hAnsi="Malgun Gothic"/><w:b/><w:bCs/><w:sz w:val="20"/></w:rPr>',
        out,
    )
    return out


def main():
    # Step 0: ensure unpacked dir exists (from unpack.py)
    unpacked = Path("unpacked")
    if not unpacked.exists():
        subprocess.run(
            ["python3",
             "/Users/ywchoi/Library/Application Support/Claude/local-agent-mode-sessions/"
             "skills-plugin/880eb2ab-045b-4cc8-b609-614d27a57292/"
             "12f4f66b-1b8d-49db-8fd9-f91fe04bf07e/skills/docx/scripts/office/unpack.py",
             "midterm.docx", "unpacked/"],
            check=True,
        )

    # Step 1: render each subproblem's paragraphs
    rendered = {}
    for key, paras in ANSWERS.items():
        rendered[key] = [md_para_to_wp(p) for p in paras]
        print(f"  rendered {key}: {len(paras)} paragraphs")

    # Step 2: inject into document.xml
    doc_path = unpacked / "word" / "document.xml"
    xml = doc_path.read_text(encoding="utf-8")

    tr_re = re.compile(r"<w:tr\b[^>]*>.*?</w:tr>", re.DOTALL)

    out = []
    cursor = 0
    row_idx = 0

    for m in tr_re.finditer(xml):
        out.append(xml[cursor : m.start()])
        row = m.group(0)

        if row_idx < len(ORDER):
            key = ORDER[row_idx]
            injected_paras = rendered[key]
            joined = "".join(injected_paras)

            # Strategy: insert answer paragraphs just before the closing </w:tc>.
            # This keeps the problem statement at top and any existing empty
            # paragraphs (placeholder spacing) will sit AFTER the answer — we
            # drop them to remove duplicated blank space.
            tc_close = row.rfind("</w:tc>")
            if tc_close == -1:
                print(f"WARNING: no </w:tc> found in {key}")
                out.append(row)
            else:
                before_close = row[:tc_close]
                after_close = row[tc_close:]
                # Split before_close into <w:p>...</w:p> chunks, strip trailing empty ones
                # using a proper paragraph boundary regex.
                p_iter = list(re.finditer(
                    r"<w:p(?:\s[^>]*)?(?:/>|>.*?</w:p>)",
                    before_close,
                    flags=re.DOTALL,
                ))
                if p_iter:
                    # Remove trailing empty paragraphs
                    last_keep = len(p_iter)
                    for idx in range(len(p_iter) - 1, -1, -1):
                        content = p_iter[idx].group(0)
                        if (
                            "<w:r>" not in content
                            and "<w:r " not in content
                            and "<m:" not in content
                            and "<w:drawing" not in content
                        ):
                            last_keep = idx
                        else:
                            break
                    if last_keep < len(p_iter):
                        cut_pos = p_iter[last_keep].start()
                        before_close = before_close[:cut_pos].rstrip()
                new_row = before_close + "\n          " + joined + "\n        " + after_close
                out.append(new_row)

        else:
            out.append(row)

        cursor = m.end()
        row_idx += 1

    out.append(xml[cursor:])
    new_xml = "".join(out)
    doc_path.write_text(new_xml, encoding="utf-8")
    print(f"Injected {len(ORDER)} cells")


if __name__ == "__main__":
    main()

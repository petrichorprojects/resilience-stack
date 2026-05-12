#!/usr/bin/env python3
"""Build branded fillable PDF for Skill Stack Launch Checklist."""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT
import textwrap

# Petrichor "Clarity Precedes Momentum" brutalist editorial system —
# extracted from Figma Make design system (New Pet Proj Design System, v22).
_HERE = __import__("pathlib").Path(__file__).parent
OUT = str(_HERE / "skill-stack-launch-checklist-generic.pdf")
PETRICHOR_INK = HexColor("#000000")     # pure black, institutional briefing
PETRICHOR_RUST = HexColor("#000000")    # accents stay black — brutalist palette
PETRICHOR_CREAM = HexColor("#F4EFE7")   # warm off-white background
PETRICHOR_GRAY = HexColor("#6E6A63")    # secondary tagline gray
HAIRLINE = HexColor("#1A1A1A")          # 0.5pt hairline rules
PAGE_W, PAGE_H = LETTER
MARGIN = 0.75 * inch
SPINE_X = MARGIN - 0.22 * inch          # spine OUTSIDE content gutter (decorative)
CONTENT_W = PAGE_W - 2 * MARGIN          # usable canvas width
BASELINE = 8                             # 8pt vertical rhythm grid

from reportlab.pdfbase.pdfmetrics import stringWidth

def fits(text, font, size, max_w=None):
    """Measure-or-fail. Returns True if string fits within max_w (default CONTENT_W)."""
    if max_w is None:
        max_w = CONTENT_W
    return stringWidth(text, font, size) <= max_w

def fit_font_size(text, font, target_w, start=56, floor=14):
    """Step font size down until text fits target_w. Floor prevents infinite shrink."""
    size = start
    while size > floor and stringWidth(text, font, size) > target_w:
        size -= 1
    return size

def fill_cream(c):
    c.setFillColor(PETRICHOR_CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

def spine_rule(c):
    # decorative vertical spine — OUTSIDE content gutter, hairline
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.line(SPINE_X, 0.6 * inch, SPINE_X, PAGE_H - 0.4 * inch)

# Auto-fit eyebrow label so it never overflows
EYEBROW_LABEL = "SKILL STACK LAUNCH CHECKLIST"

def new_page(c):
    """Inner page chrome only. Title rendering belongs to section_header()."""
    fill_cream(c)
    # institutional eyebrow — small uppercase, no banner block
    c.setFillColor(PETRICHOR_INK)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN, PAGE_H - 0.5 * inch, "PETRICHOR PROJECTS")
    # eyebrow right — auto-shrink if needed (won't actually overflow at 7.5pt)
    right_text = EYEBROW_LABEL
    right_size = fit_font_size(right_text, "Helvetica", CONTENT_W * 0.6, start=7.5, floor=5)
    c.setFillColor(PETRICHOR_GRAY)
    c.setFont("Helvetica", right_size)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.5 * inch, right_text)
    # hairline horizontal under eyebrow
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_H - 0.6 * inch, PAGE_W - MARGIN, PAGE_H - 0.6 * inch)
    # vertical spine rule (Petrichor architectural element, decorative only)
    spine_rule(c)
    # footer — institutional briefing tone
    c.setFillColor(PETRICHOR_GRAY)
    c.setFont("Helvetica", 7)
    c.drawString(MARGIN, 0.45 * inch, "CC BY 4.0  ·  Petrichor Projects  ·  petrichorgrowth.com")
    c.drawRightString(PAGE_W - MARGIN, 0.45 * inch, f"{c.getPageNumber():02d}")
    # footer hairline
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.line(MARGIN, 0.6 * inch, PAGE_W - MARGIN, 0.6 * inch)

def cb(c, x, y, name):
    c.acroForm.checkbox(name=name, x=x, y=y - 2, size=10,
                        borderColor=PETRICHOR_INK, fillColor=white,
                        textColor=black, forceBorder=True)

def textfield(c, x, y, width, name, height=14, multiline=False):
    c.acroForm.textfield(name=name, x=x, y=y, width=width, height=height,
                         borderColor=PETRICHOR_INK, fillColor=white,
                         textColor=black, forceBorder=True,
                         fontSize=9, fieldFlags="multiline" if multiline else "")

def checkline(c, x, y, name, label, max_width=420):
    cb(c, x, y, name)
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    c.drawString(x + 16, y, label[:140])

def section_header(c, y, num, title):
    # SOLE title authority — brutalist square counter + uppercase title, single layer
    box = 0.32 * inch
    c.setFillColor(PETRICHOR_INK)
    c.rect(MARGIN, y - 4, box, box, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(MARGIN + box/2, y + 4, num.replace("§", ""))
    # auto-fit title in remaining width
    title_x = MARGIN + box + 10
    max_title_w = (PAGE_W - MARGIN) - title_x
    size = fit_font_size(title.upper(), "Helvetica-Bold", max_title_w, start=16, floor=10)
    c.setFillColor(PETRICHOR_INK)
    c.setFont("Helvetica-Bold", size)
    c.drawString(title_x, y + 4, title.upper())
    # hairline under header (architectural element)
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.75)
    c.line(MARGIN, y - 14, MARGIN + 0.6 * inch, y - 14)
    return y - 34

def write_field_label(c, x, y, text):
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(PETRICHOR_INK)
    c.drawString(x, y, text.upper())
    c.setFillColor(black)

def wrap_text(c, text, x, y, max_chars=95):
    c.setFont("Helvetica", 9)
    c.setFillColor(black)
    lines = textwrap.wrap(text, max_chars)
    for line in lines:
        c.drawString(x, y, line)
        y -= 11
    return y

def cover_page(c):
    # Petrichor cover — brutalist editorial, "Federal Reserve briefing"
    fill_cream(c)
    # eyebrow top-left
    c.setFillColor(PETRICHOR_GRAY)
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, PAGE_H - 0.8 * inch, "We build categories.")
    # wordmark — top-right small uppercase
    c.setFillColor(PETRICHOR_INK)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.8 * inch, "PETRICHOR.")
    # hairline under header band
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_H - 0.95 * inch, PAGE_W - MARGIN, PAGE_H - 0.95 * inch)
    # spine rule (vertical architectural element, OUTSIDE content)
    spine_rule(c)
    # MAIN HEADLINE — measure-fit each line. CONTENT_W is the hard constraint.
    headline_lines = ["SKILL STACK", "LAUNCH", "CHECKLIST."]
    # Find largest size where ALL lines fit
    longest = max(headline_lines, key=lambda s: stringWidth(s, "Helvetica-Bold", 100))
    head_size = fit_font_size(longest, "Helvetica-Bold", CONTENT_W, start=72, floor=20)
    line_h = head_size * 0.95  # tight leading, brutalist
    c.setFillColor(PETRICHOR_INK)
    c.setFont("Helvetica-Bold", head_size)
    y_head = PAGE_H - 2.4 * inch
    for line in headline_lines:
        c.drawString(MARGIN, y_head, line)
        y_head -= line_h
    # tagline — "Clarity Precedes Momentum" institutional pull
    y_head -= 0.15 * inch
    c.setFillColor(PETRICHOR_GRAY)
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, y_head, "CLARITY PRECEDES MOMENTUM.")
    # body — brief intro
    y_head -= 0.4 * inch
    c.setFillColor(PETRICHOR_INK)
    c.setFont("Helvetica", 10)
    intro = ("A pre-launch diagnostic for any curated skill, framework, or template stack. "
             "Twelve sections. Ninety-plus checkpoints. Work top-to-bottom. The repository "
             "is not scaffolded until sections one through five are complete.")
    y = wrap_text(c, intro, MARGIN, y_head, max_chars=88)
    y -= 22
    # Engagement details block — institutional briefing form
    c.setFillColor(PETRICHOR_INK)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN, y, "ENGAGEMENT DETAILS")
    y -= 6
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.75)
    c.line(MARGIN, y, MARGIN + 1.6 * inch, y)
    y -= 22
    # Field grid — label column 1.7", field fills remainder cleanly
    label_col_w = 1.7 * inch
    field_x = MARGIN + label_col_w
    field_w = (PAGE_W - MARGIN) - field_x
    for label, fname in [
        ("Stack name", "cover_stack_name"),
        ("Owner / maintainer", "cover_owner"),
        ("Date started", "cover_date_started"),
        ("Target launch date", "cover_target_launch"),
    ]:
        write_field_label(c, MARGIN, y, label)
        textfield(c, field_x, y - 4, field_w, fname)
        y -= 26
    # foot stamp
    y = 0.8 * inch
    c.setFillColor(PETRICHOR_GRAY)
    c.setFont("Helvetica", 7)
    c.drawString(MARGIN, y, "TEMPLATE V.1  ·  RESILIENCE STACK  ·  CC BY 4.0")
    c.drawRightString(PAGE_W - MARGIN, y, "PETRICHORGROWTH.COM")
    c.setStrokeColor(HAIRLINE)
    c.line(MARGIN, y - 0.1 * inch, PAGE_W - MARGIN, y - 0.1 * inch)
    c.showPage()

SECTIONS = [
    ("§1", "Strategy", [
        ("text", "s1_problem", "Problem statement (one sentence). What this stack solves that no curated list covers."),
        ("text", "s1_icp", "ICP (buyer / user). Role plus company stage. Not 'everyone'."),
        ("text", "s1_outcome", "Outcome promise. Concrete deliverable the user walks away with."),
        ("text", "s1_why", "One-sentence 'why this exists' that survives a 10-second skim."),
    ]),
    ("§2", "Packaging Vector", [
        ("cb_group", "s2_model", "Monetization model (select all that apply):",
         ["Free + reputation play",
          "Free OSS + paid Pro (rubrics, templates, slides)",
          "Paid per skill (Gumroad / marketplace)",
          "Productized service ($k+)",
          "Hybrid"]),
        ("text", "s2_gate", "Free / paid gate location (if hybrid)."),
        ("cb_pair", "s2_funnel", "Funnel for existing service?", ["Yes", "No"]),
        ("text", "s2_funnel_path", "If yes: describe upsell path."),
    ]),
    ("§3", "Branding", [
        ("cb_group", "s3_brand_stance", "Brand stance:",
         ["Forward (logo + name dominant)",
          "Subtle (footer + author credit only)",
          "Stealth (no brand)"]),
        ("text", "s3_name_candidates", "Name candidates (list 3-5)."),
        ("cb_group", "s3_style", "Naming style:",
         ["Descriptive (SEO-friendly, generic)",
          "Abstract / rare word (ownable, needs explanation)",
          "Metaphor (memorable, brand-native)"]),
        ("cb_pair", "s3_tone", "Tone:", ["Positive / aspirational", "Problem-framed / urgent"]),
        ("text", "s3_tagline", "Tagline (one sentence, must survive elevator pitch)."),
        ("cb_group", "s3_availability", "Name availability check:",
         ["GitHub org / repo free",
          "npm / PyPI / package registry free",
          "Domain free (optional)",
          "Trademark conflict check (USPTO TESS, EUIPO)"]),
    ]),
    ("§4", "License", [
        ("cb_pair", "s4_commercial", "Commercial use allowed?", ["Yes", "No"]),
        ("cb_pair", "s4_attribution", "Attribution mandatory?", ["Yes", "No"]),
        ("cb_pair", "s4_mixed", "Mixed code + content?",
         ["Yes (dual: code MIT or Apache-2.0 / content CC BY 4.0)", "No (single license)"]),
        ("cb_group", "s4_license", "License selected:",
         ["MIT", "Apache 2.0", "CC BY 4.0", "CC BY-SA 4.0", "CC BY-NC 4.0", "Other"]),
        ("cb_pair", "s4_tm", "Trademark filing (~$350 USPTO)?", ["Filing", "Skipping"]),
        ("cb_group", "s4_done", "Sign-off:", ["LICENSE file written + linked from README"]),
    ]),
    ("§5", "Contributions", [
        ("cb_group", "s5_model", "Contribution model:",
         ["Open (anyone PRs)",
          "Curated (maintainer-only)",
          "Hybrid (open + validator + maintainer veto) — recommended"]),
        ("cb_group", "s5_bar", "Rejection bar documented (paste into CONTRIBUTING.md):",
         ["Required frontmatter fields",
          "Required sections",
          "Min / max length",
          "Required output / deliverable type",
          "Required stance / quality marker"]),
        ("cb_group", "s5_signoff", "Sign-off mechanism:",
         ["CLA (formal, friction)", "DCO (commit sign-off)", "Implicit (PR = agreement)"]),
        ("text", "s5_sla", "Review SLA (days)."),
        ("cb_group", "s5_scope", "Out-of-scope contributions listed explicitly in CONTRIBUTING.md",
         ["Documented"]),
    ]),
    ("§6", "Hosting + Security", [
        ("cb_group", "s6_host", "Source-of-truth host:",
         ["GitHub", "GitLab", "Codeberg", "Other"]),
        ("cb_group", "s6_dist", "Distribution channels:",
         ["GitHub releases / clone", "npm", "PyPI",
          "Homebrew tap", "Marketplace mirror", "curl bash one-liner"]),
        ("cb_pair", "s6_runner", "Hosted runner?", ["No (local-only — zero key risk)", "Yes (flag for API key risk)"]),
        ("cb_pair", "s6_creds", "Runtime credentials needed?", ["No", "Yes (document env vars)"]),
        ("cb_group", "s6_sec", "Security hygiene:",
         [".gitignore blocks .env, *.key, credentials, secrets",
          "GitHub Secret Scanning enabled",
          "No secrets in commit history",
          "Dependencies pinned",
          "npm package signed w/ provenance"]),
    ]),
    ("§7", "Scope + Robustness", [
        ("text", "s7_count", "Launch entry count (honest)."),
        ("cb_group", "s7_positioning", "Positioning matches count?",
         ["Curated (10-25 works)",
          "Awesome (needs 50-100+)",
          "Comprehensive (needs 200+)"]),
        ("text", "s7_v15", "v1.5 expansion roadmap."),
        ("text", "s7_v1_scope", "v1 scope locked — what ships now vs deferred."),
    ]),
    ("§8", "Tech / Format", [
        ("cb_group", "s8_format", "Skill / entry format:",
         ["Markdown", "JSON", "YAML", "TypeScript / JS", "Python", "Mixed"]),
        ("text", "s8_frontmatter", "Required frontmatter fields."),
        ("text", "s8_sections", "Required sections."),
        ("cb_group", "s8_installer", "Installer pattern:",
         ["git clone", "npx <package>", "curl ... | bash", "Package manager", "Marketplace-only"]),
        ("cb_group", "s8_validation", "Validation tooling:",
         ["GitHub Action validates PRs", "Lint rules documented", "Test runner"]),
    ]),
    ("§9", "Repo Scaffold (build checklist)", [
        ("cb_group", "s9_files", "Files committed:",
         ["README.md — branded intro, install, index, license",
          "LICENSE — full text",
          "CONTRIBUTING.md — spec template, rejection bar, PR process",
          "CODE_OF_CONDUCT.md",
          "CONTRIBUTORS.md",
          ".gitignore — secrets + build artifacts blocked",
          ".github/PULL_REQUEST_TEMPLATE.md",
          ".github/workflows/validate-*.yml",
          "bin/<cli> or installer script",
          "install.sh (curl one-liner)",
          "package.json / pyproject.toml",
          "docs/ — methodology, roadmap, FAQ",
          "Entries organized into folders by track / category"]),
    ]),
    ("§10", "Launch", [
        ("cb_group", "s10_channels", "Launch channels (top 3):",
         ["Hacker News (Show HN)", "X / Twitter", "LinkedIn",
          "Reddit", "Product Hunt", "Newsletter", "Direct outreach",
          "Discord / Slack communities"]),
        ("text", "s10_sequence", "Launch order + timing (which first, 24h plan)."),
        ("text", "s10_amplifiers", "Pre-launch ask list — friendlies tagged for amplification."),
        ("cb_group", "s10_copy", "Launch copy drafted:",
         ["Show HN title + body",
          "X thread",
          "LinkedIn carousel / long-form",
          "Newsletter blast"]),
        ("text", "s10_metric", "Success metric for 30 days (stars / installs / signups / leads)."),
        ("text", "s10_pivot", "Failure threshold + pivot plan."),
        ("cb_group", "s10_discovery", "Repo discoverability:",
         ["Repo description filled",
          "Topics added (5-10 tags)",
          "Social preview image uploaded",
          "Pinned to GitHub profile / org",
          "Badges in README"]),
    ]),
    ("§11", "Governance + Long-Term", [
        ("text", "s11_maintainers", "Maintainer count."),
        ("text", "s11_bus", "Bus factor mitigation — co-maintainer or backup named."),
        ("cb_group", "s11_versioning", "Versioning approach:",
         ["Semver", "Calendar versioning", "main is stable"]),
        ("text", "s11_breaking", "Breaking-change policy."),
        ("text", "s11_sunset", "Sunset / transfer plan."),
    ]),
    ("§12", "Quick-Fill 10 (rapid scaffolding)", [
        ("text", "s12_1", "1. Buyer."),
        ("text", "s12_2", "2. Outcome."),
        ("text", "s12_3", "3. Monetization."),
        ("text", "s12_4", "4. Brand stance."),
        ("text", "s12_5", "5. Name + tagline."),
        ("text", "s12_6", "6. License."),
        ("text", "s12_7", "7. Contributions (open / curated / hybrid)."),
        ("text", "s12_8", "8. Host + runner?"),
        ("text", "s12_9", "9. Launch count + v1.5 plan."),
        ("text", "s12_10", "10. Launch channel order."),
    ]),
]

def render_item(c, item, y):
    kind = item[0]
    name = item[1]
    label = item[2]
    if kind == "text":
        write_field_label(c, MARGIN, y, label)
        y -= 18
        textfield(c, MARGIN, y - 30, PAGE_W - 2 * MARGIN, name, height=32, multiline=True)
        y -= 46
    elif kind == "cb_group":
        write_field_label(c, MARGIN, y, label)
        y -= 18
        opts = item[3]
        for i, opt in enumerate(opts):
            checkline(c, MARGIN + 6, y, f"{name}_{i}", opt)
            y -= 16
        y -= 6
    elif kind == "cb_pair":
        write_field_label(c, MARGIN, y, label)
        y -= 18
        opts = item[3]
        x = MARGIN + 6
        for i, opt in enumerate(opts):
            checkline(c, x, y, f"{name}_{i}", opt)
            y -= 16
        y -= 6
    return y

def render_sections(c):
    y = None
    for num, title, items in SECTIONS:
        new_page(c)
        y = PAGE_H - 1.0 * inch
        y = section_header(c, y, num, title)
        for item in items:
            if y < 1.4 * inch:
                c.showPage()
                new_page(c)
                y = PAGE_H - 1.0 * inch
                y = section_header(c, y, num, title + " (cont.)")
            y = render_item(c, item, y)
        c.showPage()

def signoff_page(c):
    new_page(c)
    y = PAGE_H - 1.0 * inch
    y = section_header(c, y, "13", "Sign-Off")
    y -= 6
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    for label in [
        "§1-§5 answered — ready to scaffold",
        "§6-§9 complete — ready to commit + push",
        "§10 complete — ready to launch",
        "§11 complete — ready to sustain",
    ]:
        cb(c, MARGIN, y, f"signoff_{label[:6]}")
        c.drawString(MARGIN + 18, y, label)
        y -= 22
    y -= 16
    for label, fname in [
        ("Date Completed", "signoff_date"),
        ("Stack Name", "signoff_stack"),
        ("Owner Signature", "signoff_owner"),
        ("Petrichor Reviewer", "signoff_reviewer"),
    ]:
        write_field_label(c, MARGIN, y, label)
        textfield(c, MARGIN + 1.7 * inch, y - 4, 4.5 * inch, fname)
        y -= 30
    y -= 20
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(MARGIN, y, "Once signed, return to: phil@petrichorgrowth.com")
    c.showPage()

def main():
    c = canvas.Canvas(OUT, pagesize=LETTER)
    c.setTitle("Skill Stack Launch Checklist — Petrichor Projects")
    c.setAuthor("Petrichor Projects")
    c.setSubject("Reusable diagnostic for launching a skill stack")
    c.setKeywords("petrichor strategy skill stack launch checklist")
    cover_page(c)
    render_sections(c)
    signoff_page(c)
    c.save()
    print(f"Wrote: {OUT}")

if __name__ == "__main__":
    main()

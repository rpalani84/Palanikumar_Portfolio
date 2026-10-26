from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "assets" / "resume.pdf"

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=18 * mm,
    leftMargin=18 * mm,
    topMargin=15 * mm,
    bottomMargin=15 * mm,
    title="Palanikumar R. - Professional Resume",
    author="Palanikumar R.",
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="ResumeName", parent=styles["Title"],
    fontName="Helvetica-Bold", fontSize=21, leading=25,
    alignment=TA_CENTER, textColor=colors.HexColor("#183b59"),
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="ResumeHeadline", parent=styles["Normal"],
    fontSize=10, leading=14, alignment=TA_CENTER,
    textColor=colors.HexColor("#374151"), spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="SectionHeading", parent=styles["Heading2"],
    fontSize=11, leading=14, textColor=colors.HexColor("#183b59"),
    spaceBefore=8, spaceAfter=4, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="ResumeBody", parent=styles["BodyText"],
    fontSize=9, leading=12, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="ResumeBullet", parent=styles["BodyText"],
    fontSize=8.8, leading=11.5, leftIndent=12,
    firstLineIndent=-7, spaceAfter=2,
))

story = []

def para(text, style="ResumeBody"):
    story.append(Paragraph(text, styles[style]))

def section(title):
    para(escape(title), "SectionHeading")
    story.append(HRFlowable(
        width="100%", thickness=0.6,
        color=colors.HexColor("#b7c7d4"), spaceAfter=5
    ))

def bullet(text):
    para("&#8226;&nbsp; " + text, "ResumeBullet")

para("PALANIKUMAR R.", "ResumeName")
para(
    "Senior Technical Lead | Healthcare EDI Specialist | Production &amp; "
    "Quality Coordination | AI Application Developer (Developing Skills)",
    "ResumeHeadline",
)
story.append(Spacer(1, 3))

section("PROFESSIONAL SUMMARY")
para(
    "Healthcare EDI and technical operations professional with more than "
    "22 years of service at Exela Technologies, from October 2001 to "
    "14 August 2024. Progressed through seven designations, from Junior "
    "Processor to Senior Technical Lead. Experienced in healthcare data "
    "formats, configuration, data mapping, production support, delivery "
    "quality, and cross-functional change coordination. Currently developing "
    "practical AI application skills with Python, Streamlit, Ollama, and "
    "locally hosted language models."
)

section("PROFESSIONAL EXPERIENCE")
para("<b>Exela Technologies</b>")
para("<b>Senior Technical Lead (final designation)</b> | October 2001 - 14 August 2024")
para("<b>Career progression:</b> Junior Processor &gt; Processor &gt; "
     "Senior Processor &gt; Data Analyst &gt; Senior Data Analyst &gt; "
     "Technical Lead &gt; Senior Technical Lead")
bullet("Contributed to UnitedHealthcare (UHG) projects and healthcare EDI processes.")
bullet("Worked with EDI configuration, data mapping, requirements-based processing, and delivery practices.")
bullet("Supported Technical Delivery Managers by coordinating discussions and follow-ups for Customer Change Requests (CRs) and Internal Customer Change Requests (ICRs).")
bullet("Coordinated CR/ICR activities across Development, Configuration, Testing, QA, and Production teams; tracked ETAs and followed up on outstanding work against agreed timelines.")
bullet("Supported production stability, delivery quality, and SLA/process compliance.")
bullet("Worked with healthcare formats and outputs including HCFA, UB-04, Superbills, RX, NSF, ANSI, TEXT, XLS, and XML.")

section("TECHNICAL SKILLS")
para("<b>Healthcare:</b> Healthcare EDI operations, configuration, data mapping, healthcare formats, requirements analysis, delivery-process coordination.")
para("<b>Application development:</b> Python, Streamlit, Ollama, locally hosted language models, prompt design, knowledge-base question answering, RAG concepts, document processing, CSV-based storage.")

section("SELECTED PROJECTS")
para("<b>AI Helpdesk Ticket Router</b>")
para("Python, Streamlit, Ollama, local language models, and CSV-based storage. The application is undergoing development and validation; production deployment and measurable business outcomes have not been established.")
para("<b>AI Knowledge Assistant</b>")
para("Development experiment using document ingestion, text chunking, embeddings, and retrieval-based question answering with Python, Streamlit, Ollama, Qwen2.5, and nomic-embed-text. Formal performance benchmarks have not been established.")
para("<b>Portfolio Chat Assistant</b>")
para("Portfolio question-answering application under development and testing, using owner-approved Markdown knowledge and focusing on grounded responses without invented personal or professional details.")

section("EDUCATION")
para("<b>Higher Secondary Certificate (+2)</b> | Government Boys Higher Secondary School | 2001")
para("Subjects: Mathematics and Biology. <b>Highest completed qualification.</b>")
para("<b>B.B.A. studies (not completed)</b> | Madras University | 2003-2006")

section("ADDITIONAL INFORMATION")
para("Developing practical AI application skills through hands-on projects. Public contact details and verified certifications have not been supplied for inclusion.")

doc.build(story)
print(f"Created: {OUTPUT}")
print(f"Size: {OUTPUT.stat().st_size} bytes")

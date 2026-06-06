"""Generate Vineesh W resume PDF."""
from fpdf import FPDF


class ResumePDF(FPDF):
    def header(self):
        pass

    def section_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 30, 30)
        self.cell(0, 8, title.upper(), ln=True)
        self.set_draw_color(34, 211, 238)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, f"  - {text}")
        self.ln(1)


pdf = ResumePDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Heading
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 10, "Vineesh W", ln=True, align="C")

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 6, "Tamil Nadu, India  |  vineeshw1994@gmail.com  |  +91 7598570568  |  github.com/vineeshw1994", ln=True, align="C")
pdf.ln(6)

# Summary
pdf.section_title("Summary")
pdf.body_text(
    "Full-Stack DevOps Engineer with 2.5+ years of experience building scalable web applications "
    "and modern DevOps infrastructure. Strong expertise in Node.js, React, TypeScript, Docker, CI/CD "
    "and cloud platforms (AWS EC2, Digital Ocean). Experience with Python, OpenCV, and integrating "
    "local LLM models via Ollama into production systems. Currently delivering high-throughput "
    "microservices using Kafka, RabbitMQ, Redis, Prometheus & Grafana."
)

# Experience
pdf.section_title("Experience")

pdf.set_font("Helvetica", "B", 10.5)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 6, "Full-Stack DevOps Engineer", ln=True)
pdf.set_font("Helvetica", "I", 9.5)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5, "Entegation Technologies LLC - Allen, Texas, USA (Fully Remote)     Jul 2024 - Present", ln=True)
pdf.ln(2)
for item in [
    "Designed and maintained microservices in Node.js handling millions of daily events via RabbitMQ - improved throughput by 25%.",
    "Built and owned full CI/CD pipelines using GitHub Actions, Docker, Docker Swarm and Traefik - reduced deployment time to under 10 minutes.",
    "Implemented Redis caching and query optimisation in MySQL - reduced API latency by 35-40%.",
    "Set up complete observability stack (Prometheus + Grafana + Glances + Loki) achieving 99.99% uptime.",
    "Integrated local LLM models using Ollama for AI-powered features within production systems.",
]:
    pdf.bullet(item)
pdf.ln(3)

pdf.set_font("Helvetica", "B", 10.5)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 6, "Software Developer", ln=True)
pdf.set_font("Helvetica", "I", 9.5)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5, "Cross Roads - India     Mar 2023 - Apr 2024", ln=True)
pdf.ln(2)
for item in [
    "Built a full-featured e-commerce platform from scratch using React, Node.js, Express, MongoDB and Tailwind CSS.",
    "Implemented user authentication, product catalogue, cart, checkout, order tracking and admin dashboard.",
    "Containerised with Docker and Docker Swarm; introduced GitHub Actions for CI/CD.",
    "Improved Lighthouse performance score from 62 to 94 through code splitting, lazy loading and image optimisation.",
]:
    pdf.bullet(item)
pdf.ln(3)

# Projects
pdf.section_title("Projects")

projects = [
    ("MyCarePedia - Healthcare Booking Platform (uat.mycarepedia.com)", [
        "Developed patient portal for searching and booking doctors using React, Node.js, MySQL.",
        "Built doctor dashboard for profile management, appointment scheduling and patient communication.",
    ]),
    ("Drag-and-Drop Email Template Builder (React.js, Node.js, RabbitMQ, Redis)", [
        "Visual editor for reusable email templates with live preview and bulk sending via RabbitMQ.",
        "Campaign analytics dashboard with open/click tracking powered by Redis + Grafana.",
    ]),
    ("API Rate Limiter & Analytics Service (Node.js)", [
        "Distributed API hitting service with real-time metrics exported to Grafana.",
    ]),
]
for title, bullets in projects:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 5, title)
    pdf.ln(1)
    for b in bullets:
        pdf.bullet(b)
    pdf.ln(2)

# Skills
pdf.section_title("Skills")
skills = [
    "Languages & Frameworks: JavaScript (ES6+), TypeScript, Python, Node.js, Java, Spring Boot, PHP, Next.js, Express.js, React",
    "AI & Computer Vision: OpenCV, Ollama (Local LLM Integration), Model Deployment",
    "Styling: Tailwind CSS, Bootstrap, CSS Modules",
    "Databases: MySQL, MongoDB, Redis",
    "DevOps & Cloud: Docker, Docker Swarm, GitHub Actions, CI/CD, Nginx, Traefik, AWS EC2, Digital Ocean",
    "Message Brokers & Monitoring: Kafka, RabbitMQ, Prometheus, Grafana, Glances, Loki",
    "Tools: Git/GitHub, Postman, VS Code, Linux",
]
for s in skills:
    pdf.bullet(s)
pdf.ln(3)

# Education
pdf.section_title("Education")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "Master of Commerce (M.Com) - Manonmaniam Sundaranar University, India (2017-2019)", ln=True)
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "Bachelor of Commerce (B.Com) - Manonmaniam Sundaranar University, India (2012-2015)", ln=True)

pdf.output("Vineesh_W_Resume.pdf")
print("PDF generated successfully")

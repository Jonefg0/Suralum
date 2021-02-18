from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
w, h = A4
c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
c.drawString(50, h - 50, "¡Hola, mundo!")
x = 50
y = h - 50
c.line(x, y, x + 200, y)

text = c.beginText(50, h - 50)
text.setFont("Times-Roman", 12)
text.textLine("¡Hola, mundo!")
text.textLine("¡Desde ReportLab y Python!")
c.drawText(text)
c.showPage()
c.save()
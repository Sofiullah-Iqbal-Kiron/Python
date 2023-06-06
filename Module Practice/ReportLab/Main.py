from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

# Create a canvas to draw text/graphics and render on the file which is passed as argument.
c = canvas.Canvas("First.pdf", pagesize=A4)
width, height = A4

c.setStrokeColorRGB(0.2, 0.5, 0.3)
c.setFillColorRGB(1, 0, 1)

# Coordinate (0, 0) starts from lower-left corner.
# x - right, y - up
c.drawString(100, 100, 'Kiron Here.')

# Save the current page then page-break.
c.showPage()

# Save on file and close the canvas.
c.save()
print("Success.")

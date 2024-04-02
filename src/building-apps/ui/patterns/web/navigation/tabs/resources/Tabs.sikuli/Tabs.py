from servicestudio import ServiceStudio
from recorder.ScreenRecorder import *

# Demo script should be written below this line

### WAIT FOR SERVICE STUDIO READINESS
wait(Pattern("1578649585153.png").similar(0.70))

### START RECORDER
rec = Recording("Tabs", "tabs")
rec.Start(CaptureAudio=True)

### RUN DEMO

rightClick(Pattern("1580399480976.png").similar(0.70).targetOffset(0,3))
wait(Pattern("1580399482568.png").similar(0.70).targetOffset(15,3)).click()
wait(Pattern("1580399485376.png").similar(0.70).targetOffset(30,5)).click()
wait(Pattern("1580399662163.png").similar(0.70))
type("Tabs")
wait(Pattern("1580400126966.png").similar(0.70))
wait(Pattern("1580400074629.png").similar(0.70).targetOffset(-31,-2)).click()
doubleClick(Pattern("1580399837368.png").similar(0.70).targetOffset(-45,-5))
paste("Details")

doubleClick(Pattern("1580399915259.png").similar(0.70).targetOffset(-2,1))
paste("Price")

doubleClick(Pattern("1580400004619.png").similar(0.70).targetOffset(39,7))
paste("Stock")

click(Pattern("1580400472616.png").similar(0.70).targetOffset(0,-2))

click(Pattern("1580401708921.png").similar(0.70).targetOffset(66,8))
wait(Pattern("1580402417276.png").similar(0.70).targetOffset(-28,1)).click()
wait(Pattern("1580402465876.png").similar(0.70)).click()
type(Key.DELETE)
click(Pattern("1580400477104.png").similar(0.70).targetOffset(98,0))
wait(Pattern("1580400478584.png").similar(0.70).targetOffset(8,8)).click()
type(Key.DELETE)
wait(Pattern("1580402673450.png").similar(0.70).targetOffset(53,48)).click()
wait(Pattern("1580402759211.png").similar(0.70).targetOffset(-62,56)).click()
wait(Pattern("1580402851419.png").similar(0.70).targetOffset(-12,20)).click()
type(Key.DELETE)


dragDrop(Pattern("1580402980211.png").similar(0.70).targetOffset(-1,19), Pattern("1580403065756.png").similar(0.70).targetOffset(8,1))

dragDrop(Pattern("1580403166283.png").similar(0.70).targetOffset(-16,10), Pattern("1580403197228.png").similar(0.70))

dragDrop(Pattern("1580402892656.png").similar(0.70).targetOffset(23,3),Pattern("1580402895480.png").similar(0.70).targetOffset(8,8))
dragDrop(Pattern("1580403579497.png").similar(0.70).targetOffset(-5,1),Pattern("1580403627409.png").similar(0.70).targetOffset(-18,-1))

# Publish and Open in Browser

wait(Pattern("1578677853440.png").similar(0.70)).click()

wait(2)

hover(Pattern("1580299316148.png").similar(0.70).targetOffset(27,3))

wait(3)

wait(Pattern("1580299700683.png").similar(0.70))

wait(2)

click(Pattern("1580299700683.png").similar(0.70).targetOffset(4,3))

# Navigate to the screen and test
wait(4)

wait(Pattern("1580463770343.png").similar(0.70).targetOffset(-6,-37)).click()

wait(Pattern("1580463828238.png").similar(0.70))

click(Pattern("1580463842414.png").similar(0.70).targetOffset(-3,-3))

wait(2)

click(Pattern("1580463887103.png").similar(0.70).targetOffset(67,0))

wait(2)

### STOP RECORDER
rec.Stop()

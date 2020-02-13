from servicestudio import ServiceStudio
from recorder.ScreenRecorder import *

# Demo script should be written below this line

### WAIT FOR SERVICE STUDIO READINESS
wait(Pattern("1578649585153.png").similar(0.70))

### START RECORDER
rec = Recording("Balloon", "balloon")
rec.Start(CaptureAudio=True)
#rec = Recording("Demo","demo")
#rec.Start(CaptureAudio=False, UseGoogleTTS=True)

### RUN DEMO

click(Pattern("1578584182817.png").similar(0.90).targetOffset(38,5))
wait(Pattern("1578584183458.png").similar(0.70).targetOffset(15,0)).click()
wait(Pattern("1578584184570.png").similar(0.70).targetOffset(60,0)).click()
paste("InStockExpression")
dragDrop(Pattern("1578650050495.png").similar(0.70), Pattern("1578650052663.png").similar(0.70).targetOffset(8,15))

wait(Pattern("1578584196065.png").similar(0.90).targetOffset(45,0)).click()

paste("Current Stock")

click(Pattern("1578584200826.png").similar(0.70).targetOffset(75,3))
paste("There are ")

dragDrop(Pattern("1580297298919.png").similar(0.70).targetOffset(0,-5), Pattern("1580297300311.png").similar(0.70).targetOffset(38,18))

click(Pattern("1578650305727.png").similar(0.70).targetOffset(83,3))
paste(" in stock.")
doubleClick(Pattern("1580297433763.png").similar(0.70))

wait(Pattern("1578652198437.png").similar(0.70).targetOffset(30,20)).doubleClick()
type(".")
type(Key.DOWN)
type(Key.ENTER)
type(".")
wait(Pattern("1578652204878.png").similar(0.70).targetOffset(-7,0), 5).doubleClick()
click(Pattern("1578652206302.png").similar(0.80).targetOffset(-7,-2))

click(Pattern("1578653629412.png").similar(0.70).targetOffset(68,-7))
wait(Pattern("1578653633172.png").similar(0.70).targetOffset(49,10), 4).click()
wait(Pattern("1578653634909.png").similar(0.70).targetOffset(0,-7)).click()

# Publish and Open in Browser

wait(Pattern("1578677853440.png").similar(0.70)).click()

wait(2)

hover(Pattern("1580299316148.png").similar(0.70).targetOffset(27,3))

wait(5)

wait(Pattern("1580299700683.png").similar(0.70))

wait(2)

click(Pattern("1580299700683.png").similar(0.70).targetOffset(4,3))

# Navigate to the screen and test
wait(4)

wait(Pattern("1580304104819.png").similar(0.70).targetOffset(-76,13))

hover(Pattern("1578676284061.png").similar(0.70).targetOffset(-21,49))

wait(Pattern("1578676372069.png").similar(0.70))

hover(Pattern("1578676386927.png").similar(0.70).targetOffset(-24,48))

wait(2)

### STOP RECORDER
rec.Stop()
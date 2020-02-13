from servicestudio import ServiceStudio
from recorder.ScreenRecorder import *

# Demo script should be written below this line

### WAIT FOR SERVICE STUDIO READINESS
wait(Pattern("1578649585153.png").similar(0.70))

### START RECORDER
rec = Recording("File Upload", "file-upload")
rec.Start(CaptureAudio=True)

### RUN DEMO

dragDrop(Pattern("1580320668288.png").similar(0.70).targetOffset(8,-5), Pattern("1580320669008.png").similar(0.70).targetOffset(0,60))
wait(Pattern("1580320671944.png").similar(0.90), 5).click()
dragDrop(Pattern("1580320674712.png").similar(0.90).targetOffset(23,0), Pattern("1580320675104.png").similar(0.70).targetOffset(-75,-15))

paste("PictureUpload")

doubleClick(Pattern("1580320686824.png").similar(0.70).targetOffset(15,-2))

dragDrop(Pattern("1580381404800.png").similar(0.70).targetOffset(28,6), Pattern("1580381483764.png").similar(0.70).targetOffset(-1,-40))
wait(Pattern("1580320692753.png").similar(0.70).targetOffset(0,8)).doubleClick()
wait(Pattern("1580320694721.png").similar(0.70).targetOffset(88,8)).click()
wait(Pattern("1580320695792.png").similar(0.70).targetOffset(-1,-31)).click()
wait(Pattern("1580320696713.png").similar(0.70).targetOffset(80,13)).click()
wait(Pattern("1580320698897.png").similar(0.70).targetOffset(15,13)).click()

click(Pattern("1580381903455.png").similar(0.70).targetOffset(63,18))
wait(Pattern("1580381905527.png").similar(0.70).targetOffset(47,8)).click()
wait(Pattern("1580381909039.png").similar(0.70).targetOffset(45,18), 6).click()
paste("PictureUpload.Type")

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

wait(Pattern("1580382518959.png").similar(0.70).targetOffset(-7,-7), 9).click()
wait(Pattern("1580382522039.png").similar(0.70).targetOffset(8,-12), 4).click()

click(Pattern("1580383041687.png").similar(0.70).targetOffset(15,0))
click(Pattern("1580383043303.png").similar(0.70).targetOffset(-7,-5))
click(Pattern("1580383045463.png").similar(0.70).targetOffset(-22,-2))
wait(Pattern("1580383063339.png").similar(0.70))
wait(2)
### STOP RECORDER
rec.Stop()
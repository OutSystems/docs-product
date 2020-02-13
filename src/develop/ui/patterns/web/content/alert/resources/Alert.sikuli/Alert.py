# Add SikuliX path to path, so common modules 
#   (e.g. library) can be loaded properly

if not os.getcwd() in sys.path: sys.path.append(os.getcwd())

import Library
import ServiceStudio
from Recorder import Recording

# Demo script should be written below this line

Settings.MoveMouseDelay = 1.5

### WAIT FOR SERVICE STUDIO TO BE READY
#wait("1574786681252.png")

### START RECORDER
rec = Recording("Alert Pattern Demo", "alert-widget-demo")
rec.Start(CaptureAudio=False, UseGoogleTTS=True)
    
### RUN DEMO
# Demo script should be written below this line
# The wait(...) function will look a specific image

# The click(...) function will move the mouse to the location, and click it

### GO TO THE WIDGETS FILTER

click(Pattern("1574786711402.png").targetOffset(-52,0))

wait(1.5)

### TYPE THE NAME OF THE WIDGET
type("Alert" + Key.ENTER)

wait(1.5)

### DRAG AND DROP THE Alert WIDGET TO THE SCREEN

wait("1574786856423.png")

dragDrop("1574786885629.png",Pattern("1574786950291.png").targetOffset(-41,8))

wait(1.5)

### SET THE Alert TYPE

wait("1574787019318.png")


click(Pattern("1574787019318.png").targetOffset(121,36))

wait("1574787156751.png")

hover(Pattern("1574787156751.png").targetOffset(-53,11))

click(Pattern("1574787215565.png").targetOffset(-44,8))

wait(1.5)

### SET THE Alert TO SHOW THE CLOSE ICON
click(Pattern("1574787291075.png").targetOffset(-35,16))

type("True")

wait(1.5)

### TYPE THE TEXT TO SHOW IN THE Alert WIDGET

click(Pattern("1574787321534.png").targetOffset(-16,7))

type("Friendly reminder, when a request is declined, add a comment with the reason.")
    
wait(1.5)

### PUBLISH AND OPEN IN BROWSER

click("1574787357101.png")

wait(1.5)

hover("1574787424836.png")

wait(5)

wait("1574787501265.png")

click("1574787515076.png")

wait(5)

wait("1574787569808.png")

click("1574787569808.png")

wait(5)

### STOP RECORDER
rec.Stop()

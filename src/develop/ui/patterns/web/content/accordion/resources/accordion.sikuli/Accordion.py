# Add SikuliX path to path, so common modules 
#   (e.g. library) can be loaded properly

if not os.getcwd() in sys.path: sys.path.append(os.getcwd())

import Library
import ServiceStudio
from Recorder import Recording

### WAIT FOR SERVICE STUDIO READINESS
#wait("1574445085711.png")

### START RECORDER
rec = Recording("Sample Demo with Recorder", "sample-demo")
rec.Start(CaptureAudio=False, UseGoogleTTS=True)

### RUN DEMO
# Demo script should be written below this line
# The wait(...) function will look a specific image

# Search for the Accordion pattern
wait(1.5)

click("1574693375974.png")

type("Accordion")

wait(1.5)

# Drag the pattern to the screen

wait("1574696564916.png")

dragDrop("1574696564916.png","1574694866382.png")

wait("1574762012510.png")

# Add Text to the Accordion items

findAll("1574694463006.png")
mm = list(getLastMatches())

click(mm[0])

paste("Where do I enter the promo code?")

wait(0.5)

click(Pattern("1574762573920.png").targetOffset(-42,41))

paste("If you have a promo code you can enter it on the checkout page. Click the validate button, and the order total amount will be updated accordingly.")

wait(0.5)

findAll(Pattern("1574762703741.png").targetOffset(0,-25))

nn = list(getLastMatches())

click(nn[0])

paste("What are the available payment methods?")

wait(0.5)

click(Pattern("1574762895965.png").targetOffset(-5,38))

paste("All order payments can be made by Credit Card or PayPal.")

wait(0.5)

findAll(Pattern("1574762703741.png").targetOffset(0,-25))

pp = list(getLastMatches())

click(pp[0])

paste("What countries do you ship for?")

wait(0.5)

click(Pattern("1574763120245.png").targetOffset(-1,45))

paste("Free shipping is available to US and Canada. Shipping to EU has an additional cost, depending on the total amount of the order.")

wait(1.5)

# Publish and Open in Browser

ServiceStudio.OneClickPublish()

ServiceStudio.OpenInBrowser()

# Navigate to the screen and test

wait("1574697298173.png")

findAll("1574697730803.png")
oo = list(getLastMatches())

click(oo[0])

wait(1.5)

findAll("1574697730803.png")
oo = list(getLastMatches())

click(oo[1])

wait(1.5)

### STOP RECORDER
rec.Stop()

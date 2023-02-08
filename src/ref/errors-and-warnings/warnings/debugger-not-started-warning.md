---
locale: en-us
guid: c311f5c1-54b9-417e-9561-c39db45ac706
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Debugger Not Started Warning

Message
:   `You should set the module Operation property ‘Debug Mode’ in Service Center and republish it so it can be debugged. Debugger was not started.`

Cause
:   Property Debug Mode of the module was not set last time the module was published. The module was opened in the browser but the debugger was not started.

Recommendation
:   In Service Center, go to the module tab Operation and check the property Debug Mode. Afterwards, 1-Click Publish your module before trying to Run it again.

---

Message
:   `This Service Studio debugger version is not compatible with the current Platform Server version. Debugger was not started.`

Cause
:   You are trying to run your module in a Platform Server with a debugger version that is not compatible with Service Studio's. The module was opened in the browser but the debugger was not started.

Recommendation
:   Check with your Service Center administrator to determine what version is being used and to find out which parts of the software must be upgraded so you can debug your module.

---

Message
:   `The debugger could not access your module. It was not started.`

Cause
:   You were running your module but the debugger was not able to access it, so it was not started. However, the Run command proceeded, the browser was opened and a request was done.

Recommendation
:   Check whether the module is executing in the browser instance launched by Service Studio. If it is, try to Run your module again.

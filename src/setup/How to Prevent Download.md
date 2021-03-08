# How do you prevent users from copying text or images?

## How do you prevent users from copying text or images?

## Resolution

### Disable selection
Any content inside a container or other element with the “basic-protect” class will generally not be selectable by users.

This is accomplished with a little bit of CSS:


	.basic-protect * {
	    /* Selection */
	    -webkit-touch-callout: none;
	    -webkit-user-select: none;
	    -khtml-user-select: none;
	    -moz-user-select: none;
	    -ms-user-select: none;
	    user-select: none;
	}

### Disable printing (with notification message)

Any content inside a container or other element with the “basic-protect” will not be displayed when printed and show a message instead.

This is accomplished with a little bit of CSS:


	@media print {
	    .basic-protect::before {
	        content: "Not available for printing. "
	    }
    
	    .basic-protect * {
	      display: none;
	  }
	}

### Disable right-click menu

Prevent access to cut/copy commands from the browser’s context menu.

This is accomplished with a little bit of Javascript:


	/* Disable right-click menu on page */
	document.addEventListener('contextmenu', function(event) { 
	    event.preventDefault()
	});

### Disable print screen screenshots

Prevent the “print screen” button from taking a screenshot of the page when the page has focus. 

Caveat: This only works if the page is in focus AND the user isn’t using a special screenshot tool. In other words, this one is pretty weak. 

This is accomplished with a little bit of Javascript:


	/* Disable print screen button */
	document.addEventListener("keyup", function (event) {
	    var keyCode = event.keyCode ? event.keyCode : event.which;
	    if (keyCode == 44) {
	        stopPrntScr();
	    }
	});

	function stopPrntScr() {
	    var inpFld = document.createElement("input");
	    inpFld.setAttribute("value", ".");
	    inpFld.setAttribute("width", "0");
	    inpFld.style.height = "0px";
	    inpFld.style.width = "0px";
	    inpFld.style.border = "0px";
	    document.body.appendChild(inpFld);
	    inpFld.select();
	    document.execCommand("copy");
	    inpFld.remove(inpFld);
	}
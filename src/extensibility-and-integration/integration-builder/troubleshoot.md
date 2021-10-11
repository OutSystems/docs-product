---
summary: Identify and solve issues that may occur while using Integration Builder.
---
# Troubleshooting Integration Builder

Check the list of possible issues you may face when using Integration Builder and their corresponding solutions.

If you receive an error message, check the [Integration Builder error documentation section](<https://success.outsystems.com/Support/Errors/Integration_Builder_errors>) to learn more about the error and how to solve it.

## Error in "Select Objects" step when creating a Salesforce integration

* **The Salesforce account you used to connect Integration Builder to Salesforce doesn't have permission to see the Salesforce list of objects.**

    Go back to the "Authorize Integration Builder" step and sign into Salesforce with an account that has the App Administrator role.

* **Your OutSystems development environment can't reach the Salesforce API endpoint. This may be due to a temporary connectivity issue, or due to network security configurations.**

    **A)** Check if you can access your Salesforce instance (available at `*.my.salesforce.com`) from a browser on your computer. If Salesforce is not accessible, it can be a Salesforce issue. Open a support ticket with Salesforce.

    **B)** Check if you can access your Salesforce instance from a browser in your OutSystems development environment. Your network configurations may not allow the server to contact the internet, and in this case you can't use Integration Manager.

* **Your development environment can't reach Integration Builder. Integration Manager requires a connection to Integration Builder to create a Salesforce connection.**

    **A)** Open Integration Builder on your browser. If there's an error, it's probably down due to maintenance or technical issues. You can't create Salesforce connections while Integration Builder is unavailable.

    **B)** Check if you can access Integration Builder from a browser in your development environment. Your network configurations may not allow the server to contact the internet, and in this case you can't use Integration Manager.

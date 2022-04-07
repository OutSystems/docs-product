---
locale: en-us
guid: 19f255a3-4d7e-4bf4-91d7-74c191a42399
---

# Options Window

In the Options window, of the [Edit](<intro.md>) menu, you can customize some parameters related to the development in Integration Studio.

## General Tab

Compare files using
:   Path of the application used in the Compare with Template option that checks the differences between the definition of the extension in Integration Studio and the source code files. For more information, see [Compare with Template operation](<../../resources-tree.md>).

    Default value: empty value.

Show "Select default Application Server for new extension" window
:   Indicates whether this window is displayed when you are creating a new extension.

    Default value: checked. 
    
    It is recommended that this option always be checked, since the sooner the developer selects the application server, the less impact it has on the extension development.

## .NET Tab

In this tab you can specify the parameters related to .NET Software Development Kit (SDK) you want to use in .NET extensions.

.NET Integrated Development Environment
:   Path of the .NET IDE (Integrated Development Environment) used for coding the .NET extensions. This parameter is used in the [Edit Source Code](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-code-edit.md>) and [Compile the Extension](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-compile.md>) options.

    Default value: Detected by Integration Studio based on the .NET IDEs installed on your machine (one of the Visual Studio versions/editions supported by OutSystems).  
    Examples:  
    `C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\VCSExpress.exe`  
    `C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\devenv.exe`

.NET Compiler Tool
:   Path of the builder used when the extension is compiled within Integration Studio, during the [verification](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify.md>) of an extension. The .NET Compiler Tool is executed, in the background, through a command line with the options defined below.

    Default value: Detected by Integration Studio based on the .NET Framework versions installed in the current machine and supported by OutSystems.  
    Examples:  
    `C:\Windows\Microsoft.NET\Framework\v2.0.50727\MSBuild.exe`  
    `C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe`

.NET Compiler Tool Options
:   Indicates the compiler options used when the extension is compiled within Integration Studio, during the [verification](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify.md>) of an extension.  
The default compiler options are as follows:

    * `/nologo`: Prevents copyright information from displaying.
    * `/verbosity:minimal`: Specifies that the amount of information to display in the build log should be minimal.
    * `/target:Rebuild`: Cleans and then builds the specified solution or project according to the specified solution configuration.
    * `/property:Configuration=Release`: The solution will be compiled in Release mode, generating the DLLs and EXEs for the current extension.

![](images/tip.gif) For more information about the compiler options, check the [MSDN site](<https://msdn.microsoft.com/en-us/library/ms164311.aspx>).

## Connection Tab

In this tab you can specify the parameters related to the use of proxy authentication in the Platform Server you are connected to.

Use proxy authentication
:   To be used when your proxy requires authentication.

    Default value: un-checked.

    ![](images/tip.gif) If the Platform Server you are trying to connect to has a proxy, then it's mandatory that you set this option; otherwise it won't be possible for Integration Studio to connect to it.

Proxy user
:   User name used in the proxy authentication.

Proxy password
:   Password of the user used in the proxy authentication.

Reset Defaults
:   You can, at any time, restore the default values for these parameters by clicking on the Reset Defaults button.

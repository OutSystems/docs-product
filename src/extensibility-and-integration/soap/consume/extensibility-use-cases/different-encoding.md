---
summary: How to add support for a different character encoding using the SOAP Extensibility API.
---

# Use a different character encoding

In this example scenario we will add support for using a different character encoding in the contents of SOAP requests.

Out of the box, Windows Communication Framework (WCF) — the underlying .NET framework used to make SOAP requests — only supports the following character encodings: UTF-8, UTF-16 and Big Endian Unicode. If you try to use other encodings you will probably face one of the following runtime errors:

    FailedSystem.ServiceModel.ProtocolException: The content type text/xml; 
    charset=ISO-8859-1 of the response message does not match the content
    type of the binding (text/xml; charset=utf-8). If using a custom encoder, 
    be sure that the IsContentTypeSupported method is implemented properly.

Or:

    System.ServiceModel.ProtocolException: There is a problem with the XML 
    that was received from the network. See inner exception for more details. 
    ---> System.Xml.XmlException: The encoding in the declaration 
    'iso-8859-1' does not match the encoding of the document 'utf-8'.

You can add support for other character encodings by implementing a series of helper classes, following the sample code provided by Microsoft in [Custom Message Encoder: Custom Text Encoder](<https://docs.microsoft.com/en-us/dotnet/framework/wcf/samples/custom-message-encoder-custom-text-encoder>).

To add support for other character encodings do the following:

1\. In Integration Studio create an extension and define an action that will be used to define the encoding you wish to use.  

In example below we defined an action in Integration Studio called "SetEncoding", with a "Encoding" input parameter of type Text.

![](<images/is-action-set-encoding.png>)

2\. Click 'Edit Source Code .NET'. In Visual Studio .NET, set the project target framework and add a reference to `System.ServiceModel` and `System.Runtime.Serialization` assemblies.  

3\. Create some helper classes by copying the code presented below and pasting it in the `[yourExtensionName].cs` file, for example below the `Css[yourExtensionName]` class definition.  
Note: For more information on how these classes fit the WCF architecture, check the Microsoft page mentioned above.

```csharp
// required 'using' statements at the beginning of the file
using System.IO;
using System.ServiceModel;
using System.ServiceModel.Channels;
using System.Text;
using System.Xml;

// Custom message encoder that operates both in streaming and buffered mode. 
// It uses the XmlReader and XmlWriter to read and write the messages respectively.
// As opposed to the optimized XML readers and writers of WCF that support only UTF-8, 
// UTF-16 and Big-Endian Unicode encodings, these readers and writers support all 
// .NET platform-supported encodings.

public class CustomTextMessageEncoder : MessageEncoder {

    private CustomTextMessageEncoderFactory factory;
    private XmlWriterSettings writerSettings;
    private string contentType;

    public CustomTextMessageEncoder(CustomTextMessageEncoderFactory factory) {
        this.factory = factory;

        this.writerSettings = new XmlWriterSettings();
        this.writerSettings.Encoding = Encoding.GetEncoding(factory.CharSet);
        this.contentType = string.Format("{0}; charset={1}",
            this.factory.MediaType, this.writerSettings.Encoding.HeaderName);
    }

    public override bool IsContentTypeSupported(string contentType) {
        return base.IsContentTypeSupported(contentType) || contentType == MediaType;
    }

    public override string ContentType {
        get {
            return this.contentType;
        }
    }

    public override string MediaType {
        get {
            return factory.MediaType;
        }
    }

    public override MessageVersion MessageVersion {
        get {
            return this.factory.MessageVersion;
        }
    }

    public override Message ReadMessage(ArraySegment<byte> buffer, BufferManager bufferManager, string contentType) {
        byte[] msgContents = new byte[buffer.Count];
        Array.Copy(buffer.Array, buffer.Offset, msgContents, 0, msgContents.Length);
        bufferManager.ReturnBuffer(buffer.Array);

        MemoryStream stream = new MemoryStream(msgContents);
        return ReadMessage(stream, int.MaxValue);
    }

    public override Message ReadMessage(Stream stream, int maxSizeOfHeaders, string contentType) {
        XmlReader reader = XmlReader.Create(stream);
        return Message.CreateMessage(reader, maxSizeOfHeaders, this.MessageVersion);
    }

    public override ArraySegment<byte> WriteMessage(Message message, int maxMessageSize, BufferManager bufferManager, int messageOffset) {
        MemoryStream stream = new MemoryStream();
        XmlWriter writer = XmlWriter.Create(stream, this.writerSettings);
        message.WriteMessage(writer);
        writer.Close();

        byte[] messageBytes = stream.GetBuffer();
        int messageLength = (int)stream.Position;
        stream.Close();

        int totalLength = messageLength + messageOffset;
        byte[] totalBytes = bufferManager.TakeBuffer(totalLength);
        Array.Copy(messageBytes, 0, totalBytes, messageOffset, messageLength);

        ArraySegment<byte> byteArray = new ArraySegment<byte>(totalBytes, messageOffset, messageLength);
        return byteArray;
    }

    public override void WriteMessage(Message message, Stream stream) {
        XmlWriter writer = XmlWriter.Create(stream, this.writerSettings);
        message.WriteMessage(writer);
        writer.Close();
    }
}


public class CustomTextMessageEncoderFactory : MessageEncoderFactory {

    internal CustomTextMessageEncoderFactory(string mediaType, string charSet,
        MessageVersion version) {
        this.MessageVersion = version;
        this.MediaType = mediaType;
        this.CharSet = charSet;
        this.Encoder = new CustomTextMessageEncoder(this);
    }

    public override MessageEncoder Encoder { get; }
    public override MessageVersion MessageVersion { get; }
    internal string MediaType { get; }
    internal string CharSet { get; }
}


// Binding elements allow the configuration of the WCF run-time stack.
// To use the custom message encoder in a WCF application, a binding element
// is required that creates the message encoder factory with the appropriate 
// settings at the appropriate level in the run-time stack.

public class CustomTextMessageEncodingBindingElement : MessageEncodingBindingElement {

    public override MessageVersion MessageVersion { get; set; }
    public string MediaType { get; set; }
    public string Encoding { get; set; }

    CustomTextMessageEncodingBindingElement(CustomTextMessageEncodingBindingElement binding)
        : this(binding.Encoding, binding.MediaType, binding.MessageVersion) {
    }

    public CustomTextMessageEncodingBindingElement(string encoding, string mediaType,
        MessageVersion messageVersion) {
        this.MessageVersion = messageVersion;
        this.MediaType = mediaType;
        this.Encoding = encoding;
    }

    public CustomTextMessageEncodingBindingElement(string encoding, MessageVersion messageVersion) {
        this.Encoding = encoding;
        this.MessageVersion = messageVersion;
        if (messageVersion.Envelope == EnvelopeVersion.Soap11) {
            this.MediaType = "text/xml";
        } else if (messageVersion.Envelope == EnvelopeVersion.Soap12) {
            this.MediaType = "application/soap+xml";
        } else {
            this.MediaType = "application/xml";
        }
    }

    public override BindingElement Clone() {
        return new CustomTextMessageEncodingBindingElement(this);
    }

    public override MessageEncoderFactory CreateMessageEncoderFactory() {
        return new CustomTextMessageEncoderFactory(MediaType, Encoding, MessageVersion);
    }

    public override IChannelFactory<TChannel> BuildChannelFactory<TChannel>(BindingContext context) {
        if (context == null) {
            throw new ArgumentNullException("context");
        }

        context.BindingParameters.Add(this);
        return context.BuildInnerChannelFactory<TChannel>();
    }
}

```

4\. Add the code below, replacing the `MssSetEncoding` function placeholder that Integration Studio created for you:  

```csharp
// required 'using' statements at the beginning of the file
using System.Linq;
using OutSystems.SOAP.API;

/* ... */

// replace the 'MssSetEncoding' function placeholder with the following code
public void MssSetEncoding(string ssEncoding) {

    ISOAPClient client = SoapRequest.GetCurrentClient();

    // Create a binding based on the one already set-up.
    var customBinding = new CustomBinding(client.Endpoint.Binding);

    // Get the current TextMessageEncodingBindingElement
    // that will be replaced with the custom one defined in a helper class.
    var textEncodingElement = customBinding.Elements.OfType<TextMessageEncodingBindingElement>().Single();

    // Create a new instance of our custom TextMessageEncodingBindingElement 
    // with the correct encoding.
    var customTextEncodingElement = new CustomTextMessageEncodingBindingElement(ssEncoding, client.Endpoint.Binding.MessageVersion);

    // Insert customTextEncodingElement in the correct place.
    // Required to respect the mandatory order of elements in a custom binding: https://docs.microsoft.com/en-us/dotnet/framework/wcf/extending/custom-bindings
    customBinding.Elements.Remove(textEncodingElement);
    customBinding.Elements.Insert(customBinding.Elements.Count - 1, customTextEncodingElement);

    //Replace previous binding with the custom one
    client.Endpoint.Binding = customBinding;
}
```

5\. Quit Visual Studio .NET and, back in Integration Studio, publish the extension by clicking the "1-Click Publish" toolbar icon or by pressing `F5`.

6\. In Service Studio, add a reference to the "SetEncoding" action of your extension in your application module.  

7\. In the flow of the SOAP callback of your SOAP Web Service, i.e. the flow of "OnBeforeRequestAdvanced", drag the "SetEncoding" action to the flow and enter the desired encoding value in the "Encoding" input parameter. 

8\. Publish the application module and test the application, checking that the requests made to the consumed SOAP Web Service are done with the correct encoding and that no runtime errors occur due to encoding mismatch.

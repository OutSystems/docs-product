# PlatformPasswordUtils API

For Platform Version 9.0.99.11. Provides actions for validating and securely storing passwords in the database, compliant with established cryptographic practices

## Summary

Action | Description
---|---
[GenerateSaltedMD5Hash](<#GenerateSaltedMD5Hash>) | Salts the password with a fixed number and hashes it using the MD5 hash algorithm.
[GenerateSaltedSHA512Hash](<#GenerateSaltedSHA512Hash>) | Salts the password with a 32 bytes random number and hashes it using the SHA512 hash algorithm.
[ValidatePassword](<#ValidatePassword>) | Validates a password against the expected salted password hash.

## Actions

### GenerateSaltedMD5Hash { #GenerateSaltedMD5Hash }

Salts the password with a fixed number and hashes it using the MD5 hash algorithm.

*Inputs*

PlainTextPassword
:   Type: Text. Mandatory.  
    The password to salt and hash.  
    

*Outputs*

SaltedMD5HashPassword
:   Type: Text.  
    The password salted and hashed with MD5.  
    

### GenerateSaltedSHA512Hash { #GenerateSaltedSHA512Hash }

Salts the password with a 32 bytes random number and hashes it using the SHA512 hash algorithm.

*Inputs*

PlainTextPassword
:   Type: Text. Mandatory.  
    The password to salt and hash.

*Outputs*

SaltedSHA512HashPassword
:   Type: Text.  
    The password salted and hashed with SHA512.

### ValidatePassword { #ValidatePassword }

Validates a password against the expected salted password hash.

*Inputs*

PlainTextPassword
:   Type: Text. Mandatory.  
    The password in plain text.

SaltedHashedPassword
:   Type: Text. Mandatory.  
    The expected password, salted and hashed.

*Outputs*

IsValid
:   Type: Boolean.  
    Returns true if the password matches the given salted and hashed password.  
    



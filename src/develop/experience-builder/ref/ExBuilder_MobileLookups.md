---
locale: en-us
guid: 20b75e5b-44cc-46b5-8448-8b5b87e9ebf4
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# ExBuilder_MobileLookups

Module with a set of mobile specific lookups.

## Summary

Action | Description
---|---
[GetAgendaEntries](<#GetAgendaEntries>) | Server action that returns a list with the sample information about agenda entries.
[GetAgents](<#GetAgents>) | Server action that returns a list of support agents.
[GetAppointmentSlots](<#GetAppointmentSlots>) | Server action that returns a list of available appointment slot times.
[GetAutoClaims](<#GetAutoClaims>) | Server action that returns a list with information about auto claims.
[GetAutoImagePlaceholders](<#GetAutoImagePlaceholders>) | Server action that returns a list with empty binaries used as placeholders in auto claims.
[GetBankAccounts](<#GetBankAccounts>) | Server action that returns a list with the sample information about bank accounts.
[GetBankCards](<#GetBankCards>) | Server action that returns a list with the sample information about bank cards.
[GetCheckDepositLimit](<#GetCheckDepositLimit>) | Server action that returns the check deposit limit for an account.
[GetClaimDamagedItems](<#GetClaimDamagedItems>) | Server action that returns a list with information about damaged items for claims.
[GetClaimReceipts](<#GetClaimReceipts>) | Server action that returns a list with information about claim receipts.
[GetClaimsData](<#GetClaimsData>) | Server action that returns a list with information about claims.
[GetContactHours](<#GetContactHours>) | Server action that returns a list with the sample information about contact hours.
[GetCountries](<#GetCountries>) | Server action that returns a list of countries.
[GetCoveragesData](<#GetCoveragesData>) | Server action that returns a list with information about coverages.
[GetCreditScore](<#GetCreditScore>) | Server action that returns a credit score for a given loan type.
[GetCurrentIR](<#GetCurrentIR>) | Server action that returns the current IR rate for a loan.
[GetCustomMapMarker](<#GetCustomMapMarker>) | Server action that returns the custom marker URL.
[GetDayTimeHours](<#GetDayTimeHours>) | Server action that returns a list with the sample information about day time (Morning / Afternoon / Night).
[GetDebitCategories](<#GetDebitCategories>) | Server action that returns a list with information about debit categories.
[GetDoctors](<#GetDoctors>) | Server action that returns a list with the sample information about doctors.
[GetDoctorsById](<#GetDoctorsById>) | Server action to get the information about a doctor by a given identifier.
[GetExamTypes](<#GetExamTypes>) | Server action that returns a list with the sample information about exam types.
[GetFamilyMembers](<#GetFamilyMembers>) | Server action that returns a list with the sample information about family members.
[GetFamilyMembersById](<#GetFamilyMembersById>) | Server action to get a Family Members detail info by given id.
[GetFiltersAndSortSampleData](<#GetFiltersAndSortSampleData>) | Server action that returns a list of available filter and sort options.
[GetGenericSupportChat](<#GetGenericSupportChat>) | Server action that returns a list with the sample information about a generic support chat..
[GetHealthcareClaims](<#GetHealthcareClaims>) | Server action that returns a list with information about healthcare claims.
[GetHomeClaims](<#GetHomeClaims>) | Server action that returns a list with information about home claims.
[GetHospitalById](<#GetHospitalById>) | Server action to get the information about a hospital by a given identifier.
[GetHospitals](<#GetHospitals>) | Server action that returns a list with the sample information about hospitals.
[GetHouseLocations](<#GetHouseLocations>) | Server action that returns a list with information about house locations.
[GetIndustries](<#GetIndustries>) | Server action that returns a list with the sample information about industries.
[GetInsurancePartners](<#GetInsurancePartners>) | Server action that returns a list with the sample information about insurance partners.
[GetInsuranceProductsData](<#GetInsuranceProductsData>) | Server action that returns a list with information about products.
[GetInsuredPersonData](<#GetInsuredPersonData>) | Server action that returns a list with information about insured people for healthcare policies.
[GetInvoices](<#GetInvoices>) | Server action that returns a list with the sample information about invoices.
[GetInvolvedPartiesData](<#GetInvolvedPartiesData>) | Server action that returns a list with information about people that were involved in auto claims.
[GetLabResults](<#GetLabResults>) | Server action that returns a list with the sample information about lab results.
[GetLoanPurposes](<#GetLoanPurposes>) | Server action that returns a list with the sample information about loan purposes.
[GetLoans](<#GetLoans>) | Server action that returns a list with the sample information about loans.
[GetMapMarkerImageURL](<#GetMapMarkerImageURL>) | Server action to get the URL for the custom map marker image file.
[GetMedicalRecords](<#GetMedicalRecords>) | Server action that returns a list with the sample information about medical records.
[GetMedication](<#GetMedication>) | Server action that returns a list with the sample information about medications.
[GetMedicationById](<#GetMedicationById>) | Server action to get a Medication detail info by given id.
[GetNotifications](<#GetNotifications>) | Server action that returns a list with the sample information about notifications.
[GetNotificationSettings](<#GetNotificationSettings>) | Server action that returns a list with the sample information about notification settings.
[GetPasscode](<#GetPasscode>) | Server action that returns the passcode value.
[GetPaymentFrequencies](<#GetPaymentFrequencies>) | Server action that returns a list with information about payment frequencies.
[GetPaymentReceipts](<#GetPaymentReceipts>) | Server action that returns a list with information about payment receipts.
[GetPaymentsData](<#GetPaymentsData>) | Server action that returns a list with information about payments.
[GetPDFSampleURL](<#GetPDFSampleURL>) | Server action to get the URL for the sample PDF file.
[GetPeopleImages](<#GetPeopleImages>) | Server action that returns a list with people images. The number of images is controlled by an input.
[GetPillAmountList](<#GetPillAmountList>) | Method that returns the list of available and sort options for Medication.
[GetPolicies](<#GetPolicies>) | Server action that returns a list with the sample information about policies.
[GetPolicyContracts](<#GetPolicyContracts>) | Server action that returns a list with information about policy contracts.
[GetPrescriptions](<#GetPrescriptions>) | Server action that returns a list with the sample information about prescriptions.
[GetPrescriptionsById](<#GetPrescriptionsById>) | Server action to get a Prescription detail info by given id.
[GetPrivacyPolicies](<#GetPrivacyPolicies>) | Server action that returns a list with information about privacy policies.
[GetProductImagesSampleData](<#GetProductImagesSampleData>) | Server action that returns a list with sample images data.
[GetProductsSampleData](<#GetProductsSampleData>) | Server action that returns a list of products.
[GetPromoCodesList](<#GetPromoCodesList>) | Server action that returns all the active promo codes.
[GetSampleImages](<#GetSampleImages>) | Server action that returns a list with sample images. The number of images is controlled by an input.
[GetShipping](<#GetShipping>) | Server action that returns a list of shipping types.
[GetShoppingById](<#GetShoppingById>) | Server action to get the information about a shopping by its identifier.
[GetShoppings](<#GetShoppings>) | Server action that returns a sample list of shoppings.
[GetShoppingsFiltersAndSortSampleData](<#GetShoppingsFiltersAndSortSampleData>) | Server action that returns a list of available filters and sort options applied to shoppings.
[GetSpecialties](<#GetSpecialties>) | Server action that returns a list with the sample information about specialties.
[GetTermsAndConditions](<#GetTermsAndConditions>) | Server action that returns a list with information about privacy policies.
[GetTreatments](<#GetTreatments>) | Server action that returns a list with the sample information about treatments.
[GetVehicleDriversData](<#GetVehicleDriversData>) | Server action that returns a list with information about vehicle drivers.
[GetVehicles](<#GetVehicles>) | Server action that returns a list with information about vehicles

Structure | Description
---|---
[AgendaEntry](<#Structure_AgendaEntry>) | Structure to handle data about the detail of an agenda entry.
[Agent](<#Structure_Agent>) | Structure to handle data about the detail of an agent.
[AppointmentSlot](<#Structure_AppointmentSlot>) | Structure to handle sample data about an appointment slot times.
[AutoClaim](<#Structure_AutoClaim>) | Structure to handle data about the detail of an auto claim.
[BankAccount](<#Structure_BankAccount>) | Structure to handle data about bank accounts.
[BankCard](<#Structure_BankCard>) | Structure to handle data about bank cards.
[BusinessHours](<#Structure_BusinessHours>) | Structure to handle the information about business hours.
[Claim](<#Structure_Claim>) | Structure to handle data about the detail of a claim.
[ClaimDamagedItem](<#Structure_ClaimDamagedItem>) | Structure to handle data about the detail of a claim damaged item.
[ClaimReceipt](<#Structure_ClaimReceipt>) | Structure to handle data about the detail of a claim receipt.
[ContactHours](<#Structure_ContactHours>) | Structure to handle data about the detail of Contact Hours.
[Country](<#Structure_Country>) | Structure to handle the basic information about a country.
[Coverage](<#Structure_Coverage>) | Structure to handle data about the detail of a coverage.
[DayTime](<#Structure_DayTime>) | Structure to handle information about day time hours (Morning / Afternoon / Night).
[Doctor](<#Structure_Doctor>) | Structure to handle information about a doctor.
[ExamType](<#Structure_ExamType>) | Structure to handle information about an exam type.
[FamilyMember](<#Structure_FamilyMember>) | Structure to handle information about a family member.
[FilterAndSort](<#Structure_FilterAndSort>) | Structure to handle filter and Sort options.
[FilterAndSort_Distance](<#Structure_FilterAndSort_Distance>) | Structure to handle filter by distance options.
[FilterAndSort_Price](<#Structure_FilterAndSort_Price>) | Structure to handle filter by price options.
[FilterAndSort_Rating](<#Structure_FilterAndSort_Rating>) | Structure to handle filter by price rating options.
[FilterAndSort_Services](<#Structure_FilterAndSort_Services>) | Structure to handle filter by service structure options.
[FilterAndSort_Sort](<#Structure_FilterAndSort_Sort>) | Struture to handle a list of options about products by a sort type.
[GenericSupportChat](<#Structure_GenericSupportChat>) | Structure to handle data about the detail of a Support generic chat
[Geometry](<#Structure_Geometry>) | Structure to handle the information about coordinates.
[HealthcareClaim](<#Structure_HealthcareClaim>) | Structure to handle data about the detail of a healthcare claim.
[HomeClaim](<#Structure_HomeClaim>) | Structure to handle data about the detail of a home claim.
[Hospital](<#Structure_Hospital>) | Structure to handle information about a hospital.
[HouseLocation](<#Structure_HouseLocation>) | Structure to handle data about the detail of a house location.
[Industry](<#Structure_Industry>) | Structure to handle data about industry.
[InsurancePartner](<#Structure_InsurancePartner>) | Structure to handle information about an insurance partner.
[InsuranceProduct](<#Structure_InsuranceProduct>) | Structure to handle data about the detail of an insurance product.
[InsuredPerson](<#Structure_InsuredPerson>) | Structure to handle data about the detail of an insured person.
[Invoice](<#Structure_Invoice>) | Structure to handle information about an invoice.
[InvolvedParty](<#Structure_InvolvedParty>) | Structure to handle data about the detail of an involved party.
[LabResult](<#Structure_LabResult>) | Structure to handle information about a lab result.
[Loan](<#Structure_Loan>) | Structure to handle data about loans.
[LoanPurpose](<#Structure_LoanPurpose>) | Structure to handle data about loan purposes.
[MedicalRecord](<#Structure_MedicalRecord>) | Structure to handle information about a medical record
[Medication](<#Structure_Medication>) | Structure to handle information about medication.
[Notification](<#Structure_Notification>) | Structure to handle information to handle the notifications.
[NotificationSetting](<#Structure_NotificationSetting>) | Structure to handle data about notification settings.
[PaymentData](<#Structure_PaymentData>) | Structure to handle data about the detail of a payment data.
[PaymentReceipt](<#Structure_PaymentReceipt>) | Structure to handle data about the detail of a payment receipt.
[Policy](<#Structure_Policy>) | Structure to handle data about the detail of a policy.
[PolicyContract](<#Structure_PolicyContract>) | Structure to handle data about the detail of a policy contract.
[Prescription](<#Structure_Prescription>) | Structure to handle information about prescriptions.
[ProductSampleData](<#Structure_ProductSampleData>) | Custom structure for a sample product.
[Shipping](<#Structure_Shipping>) | Structure to handle the basic information about shipping.
[Shopping](<#Structure_Shopping>) | Structure to handle the basic information about a shopping.
[Specialty](<#Structure_Specialty>) | Structure to handle information about a clinical specialty.
[Treatment](<#Structure_Treatment>) | Structure to handle information about treatments.
[Vehicle](<#Structure_Vehicle>) | Structure to handle data about the detail of a vehicle.
[VehicleDriver](<#Structure_VehicleDriver>) | Structure to handle data about the detail of a vehicle driver.

Static Entity | Description
---|---
[AppointmentStatus](<#StaticEntity_AppointmentStatus>) | Static Entity with the appointment status.
[BookingType](<#StaticEntity_BookingType>) | Static Entity with the type of booking when making a new appointment.
[ClaimState](<#StaticEntity_ClaimState>) | 
[DisplayToggleStructure](<#StaticEntity_DisplayToggleStructure>) | Static entity with a set of options to define the apearance structure on the Display_ToggleShow pattern.
[DocumentDataType](<#StaticEntity_DocumentDataType>) | Static Entity with the available document data types.
[FamilialRelation](<#StaticEntity_FamilialRelation>) | Static Entity with the Familial Relations.
[Filter](<#StaticEntity_Filter>) | Static Entity with the filters for Healthcare items.
[FilterTypes](<#StaticEntity_FilterTypes>) | Static entity with the available filter types. It's used in order to enable the filter or sort option.
[FindUsSortTypes](<#StaticEntity_FindUsSortTypes>) | Static Entity with the sorts for Hospital/Clinic items in FindUs screen.
[Gender](<#StaticEntity_Gender>) | Static Entity with the genders enumeration.
[IncidentCauseOfLoss](<#StaticEntity_IncidentCauseOfLoss>) | Static Entity with the possible causes of loss
[InsuranceType](<#StaticEntity_InsuranceType>) | Static Entity with the available types of insurance.
[KeystoreKeys](<#StaticEntity_KeystoreKeys>) | Static Entity with the keys used in the app to set and get values from keystore.
[Language](<#StaticEntity_Language>) | Static Entity with the user languages.
[LoanStatus](<#StaticEntity_LoanStatus>) | Static Entity with the status of a loan.
[LoanType](<#StaticEntity_LoanType>) | Static Entity with the types of a requested loan.
[MedicalActivityType](<#StaticEntity_MedicalActivityType>) | Static Entity with the types of medical activities for healthcare app.
[MedicalArea](<#StaticEntity_MedicalArea>) | Static Entity with the insurance medical areas
[ParticipantType](<#StaticEntity_ParticipantType>) | Static Entity with the insurance claim participant types
[PolicyDetailOptionItem](<#StaticEntity_PolicyDetailOptionItem>) | Static Entity with the options available for the policy details.
[ProductColors](<#StaticEntity_ProductColors>) | Static Entity with the available colors for a product.
[ProductSize](<#StaticEntity_ProductSize>) | Static Entity with the available sizes for a product.
[RecordType](<#StaticEntity_RecordType>) | Static Entity with the type associated with a record.
[Sort](<#StaticEntity_Sort>) | Static Entity with the sorts for Healthcare items.
[SupportTypeGeneric](<#StaticEntity_SupportTypeGeneric>) | Static Entity with the support options.
[SupportTypeInsurance](<#StaticEntity_SupportTypeInsurance>) | Static Entity with the support options for insurance.
[SyncUnits](<#StaticEntity_SyncUnits>) | Static Entity with the available sync units.
[TouchIdErrorMessage](<#StaticEntity_TouchIdErrorMessage>) | Static Entity (id only) with the possible error messages of the touch id plugin.
[TriggerListAction](<#StaticEntity_TriggerListAction>) | Static Entity with the actions to execute on a given list like Filter or Sort.

## Actions

### GetAgendaEntries { #GetAgendaEntries }

Server action that returns a list with the sample information about agenda entries.

*Outputs*

AgendaEntriesList
:   Type: [AgendaEntry](<#Structure_AgendaEntry>) List.  
    Returned list with the sample information about agenda entries.

### GetAgents { #GetAgents }

Server action that returns a list of support agents.

*Outputs*

AgentsDataList
:   Type: [Agent](<#Structure_Agent>) List.  
    Returned list of support agents.

### GetAppointmentSlots { #GetAppointmentSlots }

Server action that returns a list of available appointment slot times.

*Outputs*

AppointmentSlotsList
:   Type: [AppointmentSlot](<#Structure_AppointmentSlot>) List.  
    Server action list with the sample information about appointment slot times.

### GetAutoClaims { #GetAutoClaims }

Server action that returns a list with information about auto claims.

*Outputs*

AutoClaimsDataList
:   Type: [AutoClaim](<#Structure_AutoClaim>) List.  
    Returned list with information about auto claims.

### GetAutoImagePlaceholders { #GetAutoImagePlaceholders }

Server action that returns a list with empty binaries used as placeholders in auto claims.

*Outputs*

AutoImagePlaceholdersList
:   Type: Binary Data List.  
    Returned list with empty binaries used as placeholders in auto claims.

### GetBankAccounts { #GetBankAccounts }

Server action that returns a list with the sample information about bank accounts.

*Outputs*

BankAccountList
:   Type: [BankAccount](<#Structure_BankAccount>) List.  
    Returned list with the sample information about bank accounts

### GetBankCards { #GetBankCards }

Server action that returns a list with the sample information about bank cards.

*Outputs*

BankCardList
:   Type: [BankCard](<#Structure_BankCard>) List.  
    Returned list with the sample information about bank cards

### GetCheckDepositLimit { #GetCheckDepositLimit }

Server action that returns the check deposit limit for an account.

*Outputs*

CheckDepositLimit
:   Type: Integer.  
    Returned check deposit limit value.

### GetClaimDamagedItems { #GetClaimDamagedItems }

Server action that returns a list with information about damaged items for claims.

*Outputs*

DamagedItemsList
:   Type: [ClaimDamagedItem](<#Structure_ClaimDamagedItem>) List.  
    Returned list with information about damaged items for home.

### GetClaimReceipts { #GetClaimReceipts }

Server action that returns a list with information about claim receipts.

*Outputs*

ClaimReceiptsList
:   Type: [ClaimReceipt](<#Structure_ClaimReceipt>) List.  
    Returned list of records with sample data about claim receipts.

### GetClaimsData { #GetClaimsData }

Server action that returns a list with information about claims.

*Outputs*

ClaimsDataList
:   Type: [Claim](<#Structure_Claim>) List.  
    Returned list with information about claims.

### GetContactHours { #GetContactHours }

Server action that returns a list with the sample information about contact hours.

*Outputs*

ContactHoursList
:   Type: [ContactHours](<#Structure_ContactHours>) List.  
    Returned list with the sample information about contact hours.

### GetCountries { #GetCountries }

Server action that returns a list of countries.

*Outputs*

CountryList
:   Type: [Country](<#Structure_Country>) List.  
    Returned list of countries and all the needed info for each one.

### GetCoveragesData { #GetCoveragesData }

Server action that returns a list with information about coverages.

*Outputs*

CoveragesDataList
:   Type: [Coverage](<#Structure_Coverage>) List.  
    Returned list with information about coverages.

### GetCreditScore { #GetCreditScore }

Server action that returns a credit score for a given loan type.

*Inputs*

LoanTypeId
:   Type: mandatory, LoanType Identifier.  
    Input variable with the given loan type identifier.

*Outputs*

CreditScoreNum
:   Type: Integer.  
    Returned numeric value of the credit score.

CreditScoreDescription
:   Type: Text.  
    Returned description of the credit score.

### GetCurrentIR { #GetCurrentIR }

Server action that returns the current IR rate for a loan.

*Outputs*

CurrentInterestRate
:   Type: Decimal.  
    Returned interest rate.

### GetCustomMapMarker { #GetCustomMapMarker }

Server action that returns the custom marker URL.

*Outputs*

MapMarkerURL
:   Type: Text.  
    Returned custom marker URL.

### GetDayTimeHours { #GetDayTimeHours }

Server action that returns a list with the sample information about day time (Morning / Afternoon / Night).

*Outputs*

DayTimeList
:   Type: [DayTime](<#Structure_DayTime>) List.  
    Returned list with the sample information about day time (Morning / Afternoon / Night).

### GetDebitCategories { #GetDebitCategories }

Server action that returns a list with information about debit categories.

*Outputs*

DebitCategories
:   Type: Long Integer, Text List.  
    Returned list with information about debit categories.

### GetDoctors { #GetDoctors }

Server action that returns a list with the sample information about doctors.

*Outputs*

DoctorList
:   Type: [Doctor](<#Structure_Doctor>) List.  
    Returned list with the sample information about doctors.

### GetDoctorsById { #GetDoctorsById }

Server action to get the information about a doctor by a given identifier.

*Inputs*

DoctorId
:   Type: mandatory, Long Integer.  
    Input variable with the doctor unique identifier we'll search for.

*Outputs*

DoctorDetail
:   Type: [Doctor](<#Structure_Doctor>).  
    Returned record with all given doctor information.

### GetExamTypes { #GetExamTypes }

Server action that returns a list with the sample information about exam types.

*Outputs*

ExamTypesList
:   Type: [ExamType](<#Structure_ExamType>) List.  
    Returned list with the sample information about exam types.

### GetFamilyMembers { #GetFamilyMembers }

Server action that returns a list with the sample information about family members.

*Outputs*

FamilyMemberList
:   Type: [FamilyMember](<#Structure_FamilyMember>) List.  
    Returned list with the sample information about family members.

### GetFamilyMembersById { #GetFamilyMembersById }

Server action to get a Family Members detail info by given id.

*Inputs*

MemberId
:   Type: mandatory, Long Integer.  
    Input variable with the member identifier value.

*Outputs*

FamilyMemberDetail
:   Type: [FamilyMember](<#Structure_FamilyMember>).  
    Returned sample information about a given Family Member id

### GetFiltersAndSortSampleData { #GetFiltersAndSortSampleData }

Server action that returns a list of available filter and sort options.

*Outputs*

SortOptions
:   Type: [FilterAndSort](<#Structure_FilterAndSort>).  
    Returned list with sorting options.

### GetGenericSupportChat { #GetGenericSupportChat }

Server action that returns a list with the sample information about a generic support chat..

*Outputs*

GenericSupportChatList
:   Type: [GenericSupportChat](<#Structure_GenericSupportChat>) List.  
    Returned list with the sample information about generic support chat.

### GetHealthcareClaims { #GetHealthcareClaims }

Server action that returns a list with information about healthcare claims.

*Outputs*

HealthcareClaimsList
:   Type: [HealthcareClaim](<#Structure_HealthcareClaim>) List.  
    Returned list with information about healthcare claims.

### GetHomeClaims { #GetHomeClaims }

Server action that returns a list with information about home claims.

*Outputs*

HomeClaimsList
:   Type: [HomeClaim](<#Structure_HomeClaim>) List.  
    Returned list with information about home claims.

### GetHospitalById { #GetHospitalById }

Server action to get the information about a hospital by a given identifier.

*Inputs*

HospitalId
:   Type: mandatory, Long Integer.  
    Input variable with hospital unique identifier we'll search for.

*Outputs*

HospitalDetail
:   Type: [Hospital](<#Structure_Hospital>).  
    Returned record with the sample information about an hospital detail.

### GetHospitals { #GetHospitals }

Server action that returns a list with the sample information about hospitals.

*Outputs*

HospitalsList
:   Type: [Hospital](<#Structure_Hospital>) List.  
    Returned list with the sample information about hospitals.

### GetHouseLocations { #GetHouseLocations }

Server action that returns a list with information about house locations.

*Outputs*

HouseLocationList
:   Type: [HouseLocation](<#Structure_HouseLocation>) List.  
    Returned list with information about house locations.

### GetIndustries { #GetIndustries }

Server action that returns a list with the sample information about industries.

*Outputs*

IndustryList
:   Type: [Industry](<#Structure_Industry>) List.  
    Returned list with the sample information about industries.

### GetInsurancePartners { #GetInsurancePartners }

Server action that returns a list with the sample information about insurance partners.

*Outputs*

InsurancePartnerList
:   Type: [InsurancePartner](<#Structure_InsurancePartner>) List.  
    Returned list with the sample information about insurance partners.

### GetInsuranceProductsData { #GetInsuranceProductsData }

Server action that returns a list with information about products.

*Outputs*

InsuranceProductsDataList
:   Type: [InsuranceProduct](<#Structure_InsuranceProduct>) List.  
    Returned list with information about products.

### GetInsuredPersonData { #GetInsuredPersonData }

Server action that returns a list with information about insured people for healthcare policies.

*Outputs*

InsuredPersonDataList
:   Type: [InsuredPerson](<#Structure_InsuredPerson>) List.  
    Returned a list with information about insured people for healthcare policies.

### GetInvoices { #GetInvoices }

Server action that returns a list with the sample information about invoices.

*Outputs*

InvoicesList
:   Type: [Invoice](<#Structure_Invoice>) List.  
    Returned list with the sample information about invoices.

### GetInvolvedPartiesData { #GetInvolvedPartiesData }

Server action that returns a list with information about people that were involved in auto claims.

*Outputs*

InvolvedPartiesDataList
:   Type: [InvolvedParty](<#Structure_InvolvedParty>) List.  
    Returned list with information about people that were involved in auto claims.

### GetLabResults { #GetLabResults }

Server action that returns a list with the sample information about lab results.

*Outputs*

LabResultList
:   Type: [LabResult](<#Structure_LabResult>) List.  
    Returned list with all the information about lab results.

### GetLoanPurposes { #GetLoanPurposes }

Server action that returns a list with the sample information about loan purposes.

*Outputs*

LoanPurposeList
:   Type: [LoanPurpose](<#Structure_LoanPurpose>) List.  
    Returned list with the sample information about loan purposes.

### GetLoans { #GetLoans }

Server action that returns a list with the sample information about loans.

*Outputs*

LoanList
:   Type: [Loan](<#Structure_Loan>) List.  
    Returned list with the sample information about loans

### GetMapMarkerImageURL { #GetMapMarkerImageURL }

Server action to get the URL for the custom map marker image file.

*Outputs*

FileURL
:   Type: Text.  
    Returned URL for the sample PDF file.

### GetMedicalRecords { #GetMedicalRecords }

Server action that returns a list with the sample information about medical records.

*Outputs*

MedicalRecordList
:   Type: [MedicalRecord](<#Structure_MedicalRecord>) List.  
    Returned list with the sample information about medical records.

### GetMedication { #GetMedication }

Server action that returns a list with the sample information about medications.

*Outputs*

MedicationList
:   Type: [Medication](<#Structure_Medication>) List.  
    Returned list with the sample information about medications.

### GetMedicationById { #GetMedicationById }

Server action to get a Medication detail info by given id.

*Inputs*

MedicationId
:   Type: mandatory, Long Integer.  
    Input variable with the medication identifier to be fetched.

*Outputs*

MedicationDetail
:   Type: [Medication](<#Structure_Medication>).  
    Returned sample information about a given medication id.

### GetNotifications { #GetNotifications }

Server action that returns a list with the sample information about notifications.

*Outputs*

NotificationList
:   Type: [Notification](<#Structure_Notification>) List.  
    Returned list with the sample information about notifications.

### GetNotificationSettings { #GetNotificationSettings }

Server action that returns a list with the sample information about notification settings.

*Outputs*

NotificationSettingsList
:   Type: [NotificationSetting](<#Structure_NotificationSetting>) List.  
    Returned list with the sample information about notification settings.

### GetPasscode { #GetPasscode }

Server action that returns the passcode value.

*Outputs*

Passcode
:   Type: Integer.  
    Returned passcode value.

### GetPaymentFrequencies { #GetPaymentFrequencies }

Server action that returns a list with information about payment frequencies.

*Outputs*

PaymentFrequencies
:   Type: Long Integer, Text List.  
    Returned list with information about payment frequencies.

### GetPaymentReceipts { #GetPaymentReceipts }

Server action that returns a list with information about payment receipts.

*Outputs*

PaymentReceiptsList
:   Type: [PaymentReceipt](<#Structure_PaymentReceipt>) List.  
    Returned list with information about payment receipts.

### GetPaymentsData { #GetPaymentsData }

Server action that returns a list with information about payments.

*Outputs*

PaymentsDataList
:   Type: [PaymentData](<#Structure_PaymentData>) List.  
    Returned list with information about payments.

### GetPDFSampleURL { #GetPDFSampleURL }

Server action to get the URL for the sample PDF file.

*Outputs*

FileURL
:   Type: Text.  
    Returned URL for the sample PDF file.

### GetPeopleImages { #GetPeopleImages }

Server action that returns a list with people images. The number of images is controlled by an input.

*Inputs*

NumberOfImages
:   Type: mandatory, Integer.  
    Input variable Number of images to return.

*Outputs*

PeopleImagesList
:   Type: Binary Data List.  
    Returned list with people images.

### GetPillAmountList { #GetPillAmountList }

Method that returns the list of available and sort options for Medication.

*Outputs*

PillAmounts
:   Type: Integer, Text List.  
    Returned list of the available pill amounts for the medication filters.

### GetPolicies { #GetPolicies }

Server action that returns a list with the sample information about policies.

*Outputs*

PolicyList
:   Type: [Policy](<#Structure_Policy>) List.  
    Returned list with the sample information about policies

### GetPolicyContracts { #GetPolicyContracts }

Server action that returns a list with information about policy contracts.

*Outputs*

PolicyContractsList
:   Type: [PolicyContract](<#Structure_PolicyContract>) List.  
    Returned list with information about policy contracts.

### GetPrescriptions { #GetPrescriptions }

Server action that returns a list with the sample information about prescriptions.

*Outputs*

PrescriptionsList
:   Type: [Prescription](<#Structure_Prescription>) List.  
    Returned list with the sample information about prescriptions.

### GetPrescriptionsById { #GetPrescriptionsById }

Server action to get a Prescription detail info by given id.

*Inputs*

PrescriptionId
:   Type: mandatory, Long Integer.  
    Input variable with the prescription identifier to be fetched.

*Outputs*

PrescriptionDetail
:   Type: [Prescription](<#Structure_Prescription>).  
    Returned sample information about a given prescription id.

### GetPrivacyPolicies { #GetPrivacyPolicies }

Server action that returns a list with information about privacy policies.

*Outputs*

PrivacyPolicyList
:   Type: Text, Text, Text, Boolean, Boolean, Boolean, Long Integer List.  
    Returned list with information about privacy policies.

### GetProductImagesSampleData { #GetProductImagesSampleData }

Server action that returns a list with sample images data.

*Inputs*

NumberOfImages
:   Type: optional, Integer.  
    Input variable to specify how many images to be fetched from the database.

*Outputs*

ImagesList
:   Type: Binary Data List.  
    Returned list of images from the database.

### GetProductsSampleData { #GetProductsSampleData }

Server action that returns a list of products.

*Inputs*

NumberOfProducts
:   Type: mandatory, Integer.  
    Input variable to specify how many products to be fetched from the database.

*Outputs*

ProductsList
:   Type: [ProductSampleData](<#Structure_ProductSampleData>) List.  
    Returned list of products.

### GetPromoCodesList { #GetPromoCodesList }

Server action that returns all the active promo codes.

*Outputs*

PromoCodesList
:   Type: Text, Decimal List.  
    Returned list of all the active promo codes.

### GetSampleImages { #GetSampleImages }

Server action that returns a list with sample images. The number of images is controlled by an input.

*Inputs*

NumberOfImages
:   Type: mandatory, Integer.  
    Input variable with the number of images to return.

*Outputs*

ImagesList
:   Type: Binary Data List.  
    Returned list with sample images.

### GetShipping { #GetShipping }

Server action that returns a list of shipping types.

*Outputs*

Shipping
:   Type: [Shipping](<#Structure_Shipping>) List.  
    Returned list of shipping types.

### GetShoppingById { #GetShoppingById }

Server action to get the information about a shopping by its identifier.

*Inputs*

ShoppingId
:   Type: mandatory, Long Integer.  
    Input variable with the shopping unique identifier to which we'll get the information.

*Outputs*

ShoppingInfo
:   Type: [Shopping](<#Structure_Shopping>).  
    Record returned with the information about a shopping based on the given identifier.

### GetShoppings { #GetShoppings }

Server action that returns a sample list of shoppings.

*Outputs*

ShoppingsList
:   Type: [Shopping](<#Structure_Shopping>) List.  
    List of Shoppings and all the needed info for each one.

### GetShoppingsFiltersAndSortSampleData { #GetShoppingsFiltersAndSortSampleData }

Server action that returns a list of available filters and sort options applied to shoppings.

*Outputs*

SortOptions
:   Type: [FilterAndSort](<#Structure_FilterAndSort>).  
    Returned list of available filters and sort options applied to shoppings.

### GetSpecialties { #GetSpecialties }

Server action that returns a list with the sample information about specialties.

*Outputs*

SpecialtiesList
:   Type: [Specialty](<#Structure_Specialty>) List.  
    Returned list with the sample information about specialties.

### GetTermsAndConditions { #GetTermsAndConditions }

Server action that returns a list with information about privacy policies.

*Outputs*

TermsAndConditions
:   Type: Text, Text, Text.  
    Returned information about privacy policies.

### GetTreatments { #GetTreatments }

Server action that returns a list with the sample information about treatments.

*Outputs*

TreatmentsList
:   Type: [Treatment](<#Structure_Treatment>) List.  
    Returned list with the sample information about treatments.

### GetVehicleDriversData { #GetVehicleDriversData }

Server action that returns a list with information about vehicle drivers.

*Outputs*

VehicleDriversDataList
:   Type: [VehicleDriver](<#Structure_VehicleDriver>) List.  
    Returned list with information about vehicle drivers.

### GetVehicles { #GetVehicles }

Server action that returns a list with information about vehicles

*Outputs*

VehiclesList
:   Type: [Vehicle](<#Structure_Vehicle>) List.  
    Returned list with information about vehicles


## Structures

### AgendaEntry { #Structure_AgendaEntry }

Structure to handle data about the detail of an agenda entry.

*Attributes*

Id
:   Type: Long Integer.  
    Agenda unique identifier.

SpecialtyId
:   Type: Text.  
    Indicates the specialty id.

Hours
:   Type: Time.  
    Indicates the appointment time.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

DateTime
:   Type: Date Time.  
    Indicates the generated datetime.

FamilyMemberId
:   Type: Long Integer.  
    Indicates the related patient id.

DoctorId
:   Type: Long Integer.  
    Indicates the related doctor id.

InsurancePartnerId
:   Type: Long Integer.  
    Indicates the related insurance id.

HospitalId
:   Type: Long Integer.  
    Indicates the related hospital id.

MedicalRecordId
:   Type: Long Integer.  
    Identifier of the related medical record.

BookingTypeId
:   Type: BookingType Identifier.  
    Identifier of the booking type.

Status
:   Type: AppointmentStatus Identifier.  
    Indicates the status for the current appointment.

ExamTypeId
:   Type: Long Integer.  
    Identifier of the related Exam Type.

### Agent { #Structure_Agent }

Structure to handle data about the detail of an agent.

*Attributes*

Id
:   Type: Long Integer.  
    Agent unique identifier.

Name
:   Type: Text.  
    Indicates the agent's name.

PhoneNumber
:   Type: Phone Number.  
    Indicates the agent's phone number.

Email
:   Type: Email.  
    Indicates the agent's email.

### AppointmentSlot { #Structure_AppointmentSlot }

Structure to handle sample data about an appointment slot times.

*Attributes*

Id
:   Type: Long Integer.  
    Appointment slot unique identifier.

SpecialtyId
:   Type: Long Integer.  
    Indicates the related specialty id.

Hours
:   Type: Time.  
    Indicates the appointment time.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

DateTime
:   Type: Date Time.  
    Indicates the generated datetime.

DoctorId
:   Type: Long Integer.  
    Identifier of the related doctor.

HospitalId
:   Type: Long Integer.  
    Indicates the id of the hospital where the appointment will occur.

ExamTypeId
:   Type: Long Integer.  
    Indicates the exam type that can be taken in this slot.

### AutoClaim { #Structure_AutoClaim }

Structure to handle data about the detail of an auto claim.

*Attributes*

ClaimId
:   Type: Long Integer.  
    Related claim unique identifier.

Location
:   Type: Text.  
    Indicates the location of the auto claim.

### BankAccount { #Structure_BankAccount }

Structure to handle data about bank accounts.

*Attributes*

Id
:   Type: Long Integer.  
    Bank account unique indentifier.

AccountName
:   Type: Text.  
    Indicates the name of the account.

AccountNumber
:   Type: Text.  
    Indicates the number of the account.

AccountStatus
:   Type: Text.  
    Indicates the status of the account.

Balance
:   Type: Decimal (0, 0).  
    Indicates the balance of the account.

BankAddress
:   Type: Text.  
    Indicates the address of the bank of the account.

RoutingNumber
:   Type: Text.  
    Indicates the routing number of the account.

SwiftBICCode
:   Type: Text.  
    Indicates the swift BIC Code of the account.

### BankCard { #Structure_BankCard }

Structure to handle data about bank cards.

*Attributes*

Id
:   Type: Long Integer.  
    Bank card unique indentifier.

AccountId
:   Type: Long Integer.  
    Related bank account unique indentifier.

CardName
:   Type: Text.  
    Indicates the name of the card.

IsCancelled
:   Type: Boolean.  
    Indicates if the card is cancelled.

IsLocked
:   Type: Boolean.  
    Indicates if the card is locked.

Last4Digits
:   Type: Text.  
    Indicates the last 4 digits of the card.

### BusinessHours { #Structure_BusinessHours }

Structure to handle the information about business hours.

*Attributes*

WeekDays
:   Type: Text.  
    Indacates business hours during the week days.

Saturday
:   Type: Text.  
    Indacates business hours on Saturday.

Sunday
:   Type: Text.  
    Indacates business hours on Sunday.

### Claim { #Structure_Claim }

Structure to handle data about the detail of a claim.

*Attributes*

Id
:   Type: Long Integer.  
    Claim unique identifier.

Hour
:   Type: Time.  
    Indicates the claim time

AccountId
:   Type: Long Integer.  
    Indicates the related account identifier.

Description
:   Type: Text.  
    Indicates the claim's descripton.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

CreatedOn
:   Type: Date.  
    Indicates the date when the claim was created.

IsActive
:   Type: Boolean.  
    Indicates if the claim is active.

PolicyId
:   Type: Long Integer.  
    Indicates the related policy identifier.

ReferenceNumber
:   Type: Integer.  
    Indicates the claim's reference number.

ClaimStateId
:   Type: ClaimState Identifier.  
    Indicates the related claim state.

InsuranceTypeId
:   Type: InsuranceType Identifier.  
    Indicates the related insurance type.

### ClaimDamagedItem { #Structure_ClaimDamagedItem }

Structure to handle data about the detail of a claim damaged item.

*Attributes*

ClaimId
:   Type: Long Integer.  
    Indicates the related claim unique identifier.

Name
:   Type: Text.  
    Indicates the name of the damaged item.

### ClaimReceipt { #Structure_ClaimReceipt }

Structure to handle data about the detail of a claim receipt.

*Attributes*

Id
:   Type: Integer.  
    Claim receipt unique identifier.

Name
:   Type: Text.  
    Indicates the receipt's name.

ClaimId
:   Type: Long Integer.  
    Indicates related claim identfier.

FilePathURL
:   Type: Text.  
    Indicates the receipt's file path.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

CreatedOn
:   Type: Date.  
    Indicates the date when the claim receipt was created.

MimeType
:   Type: Text.  
    Indicates the receipt's mimetype.

### ContactHours { #Structure_ContactHours }

Structure to handle data about the detail of Contact Hours.

*Attributes*

Id
:   Type: Long Integer.  
    Contact hours unique indentifier.

HourFrom
:   Type: Time.  
    Indicates start hour of the contact hours.

HourTo
:   Type: Time.  
    Indicates end hour of the contact hours.

Label
:   Type: Text.  
    Indicates the preference label.

### Country { #Structure_Country }

Structure to handle the basic information about a country.

*Attributes*

Name
:   Type: Text.  
    Indicates the country name.

Code
:   Type: Text.  
    Indicates the country code.

DialCode
:   Type: Text.  
    Indicates the country phone dial-code.

Flag
:   Type: Text.  
    Country flag.

### Coverage { #Structure_Coverage }

Structure to handle data about the detail of a coverage.

*Attributes*

Id
:   Type: Long Integer.  
    Coverage unique identifier.

Name
:   Type: Text.  
    Indicates the coverage's name.

Description
:   Type: Text.  
    Indicates the coverage's description.

AdditionalDescription
:   Type: Text.  
    Aditional description for the coverage.

PolicyId
:   Type: Long Integer.  
    Indicates related policy identifier.

Price
:   Type: Currency.  
    Indicates coverage's price.

### DayTime { #Structure_DayTime }

Structure to handle information about day time hours (Morning / Afternoon / Night).

*Attributes*

Id
:   Type: Long Integer.  
    Day time unique identifier.

Name
:   Type: Text.  
    Indicates the day designation.

StartHour
:   Type: Integer.  
    Indicates the start hour of the period.

StopHour
:   Type: Integer.  
    Indicates the stop hour of the period.

NameHours
:   Type: Text.  
    Indicates the day time designation.

### Doctor { #Structure_Doctor }

Structure to handle information about a doctor.

*Attributes*

Id
:   Type: Long Integer.  
    Doctor unique identifier.

Title
:   Type: Text.  
    Indicates the doctor's title. Usually displayed as &quot;Doc&quot; or &quot;Prof&quot;.

Name
:   Type: Text.  
    Indicates the doctor's name.

Specialty
:   Type: Text.  
    Indicates the doctor's specialty.

PhotoURL
:   Type: Text.  
    Indicates the URL for the doctor's photo.

### ExamType { #Structure_ExamType }

Structure to handle information about an exam type.

*Attributes*

Id
:   Type: Long Integer.  
    Exam type unique identifier.

Name
:   Type: Text.  
    Indicates the exam type name.

### FamilyMember { #Structure_FamilyMember }

Structure to handle information about a family member.

*Attributes*

Id
:   Type: Long Integer.  
    Family member unique identifier.

Name
:   Type: Text.  
    Indicates the family member name.

FullName
:   Type: Text.  
    Indicates the family member full name.

FamilialRelation
:   Type: Text.  
    Indicates the family member familial relation.

PhotoURL
:   Type: Text.  
    Indicates the URL for the customer's family member photo.

IdCard
:   Type: Long Integer.  
    Indicates the ID Card number of the family member.

IsPolicyMainHolder
:   Type: Boolean.  
    Indicates if the family member is the policy's main holder.

IsProcessFinished
:   Type: Boolean.  
    Indicates if the family member's process is finished.

PlanAccess
:   Type: Text.  
    Indicates the coverage plan that this family member can access.

Address
:   Type: Text.  
    Indicates the address of the family member.

AllowFaceId
:   Type: Boolean.  
    Indicates if this family member can use Face ID.

PhoneNumber
:   Type: Phone Number.  
    Indicates the phone number of the family member.

Email
:   Type: Email.  
    Indicates the email of the family member.

Gender
:   Type: Text.  
    Indicates the gender of the family member.

Language
:   Type: Text.  
    Indicates the language of the family member.

Birthdate
:   Type: Date.  
    Indicates the birthdate of the family member.

MobileNumber
:   Type: Phone Number.  
    Indicates the mobile number of the family member.

### FilterAndSort { #Structure_FilterAndSort }

Structure to handle filter and Sort options.

*Attributes*

Price
:   Type: [FilterAndSort_Price](<#Structure_FilterAndSort_Price>) List.  
    Structure to handle data about possible filter options by price

Rating
:   Type: [FilterAndSort_Rating](<#Structure_FilterAndSort_Rating>) List.  
    Structure to handle data about possible filter options by rating.

Distance
:   Type: [FilterAndSort_Distance](<#Structure_FilterAndSort_Distance>) List.  
    Structure to handle data about possible filter options by distance.

Service
:   Type: [FilterAndSort_Services](<#Structure_FilterAndSort_Services>) List.  
    Structure to handle data about possible filter options by service.

Sort
:   Type: [FilterAndSort_Sort](<#Structure_FilterAndSort_Sort>) List.  
    Structure to handle data about possible filter options by sort type.

### FilterAndSort_Distance { #Structure_FilterAndSort_Distance }

Structure to handle filter by distance options.

*Attributes*

Label
:   Type: Text.  
    Filter label.

MaxDistance
:   Type: Decimal (0, 0).  
    Indicates distance value applied.

IsSelected
:   Type: Boolean.  
    Indicates if the sort option is selected.

### FilterAndSort_Price { #Structure_FilterAndSort_Price }

Structure to handle filter by price options.

*Attributes*

Label
:   Type: Text.  
    Filter label.

MinValue
:   Type: Integer.  
    Indicates the minimum filter value. Applies to price or rating filters.

MaxValue
:   Type: Integer.  
    Indicates the max filter value. Applies to price or rating filters.

IsSelected
:   Type: Boolean.  
    Indicates if the sort option is selected.

### FilterAndSort_Rating { #Structure_FilterAndSort_Rating }

Structure to handle filter by price rating options.

*Attributes*

Label
:   Type: Text.  
    Filter label.

Value
:   Type: Integer.  
    Indicates the rating value applied.

IsSelected
:   Type: Boolean.  
    Indicates if the sort option is selected.

### FilterAndSort_Services { #Structure_FilterAndSort_Services }

Structure to handle filter by service structure options.

*Attributes*

Label
:   Type: Text.  
    Filter label.

Service
:   Type: Text.  
    Indicates the service value.

IsSelected
:   Type: Boolean.  
    Indicates if the sort option is selected.

### FilterAndSort_Sort { #Structure_FilterAndSort_Sort }

Struture to handle a list of options about products by a sort type.

*Attributes*

Label
:   Type: Text.  
    Sort label.

SortBy
:   Type: Text.  
    Indicates the sorting option. Product can be sorted by &quot;ProductPrice&quot;, &quot;ProductRating&quot; or &quot;Distance&quot;.

IsAscending
:   Type: Boolean.  
    Indicates if Is ascending, the sort will apply an ascending sort option.

IsSelected
:   Type: Boolean.  
    Indicates if if the sort option is selected.

### GenericSupportChat { #Structure_GenericSupportChat }

Structure to handle data about the detail of a Support generic chat

*Attributes*

Id
:   Type: Long Integer.  
    Support chat unique identifier.

Position
:   Type: Text.  
    Indicates the role of the person

FirstName
:   Type: Text.  
    Indicates the first name of the person

LastName
:   Type: Text.  
    Indicates the last name of the person

PhotoURL
:   Type: Text.  
    Indicates the Url for the person's picture

DaysToAdd
:   Type: Integer.  
    Number of days to add to current date

Message
:   Type: Text.  
    Message written by the person

### Geometry { #Structure_Geometry }

Structure to handle the information about coordinates.

*Attributes*

Type
:   Type: Text.  
    Represents the geometry type.

Latitude
:   Type: Decimal (0, 0).  
    Indacates GPS Latitude coordinate value.

Longitude
:   Type: Decimal (0, 0).  
    Indacates GPS Longitude coordinate value.

### HealthcareClaim { #Structure_HealthcareClaim }

Structure to handle data about the detail of a healthcare claim.

*Attributes*

ClaimId
:   Type: Long Integer.  
    Indicates related claim unique identfier.

Amount
:   Type: Currency.  
    Indicates the amount on the healthcare claim.

MedicalAreaId
:   Type: MedicalArea Identifier.  
    Indicates related medical area identifier.

### HomeClaim { #Structure_HomeClaim }

Structure to handle data about the detail of a home claim.

*Attributes*

ClaimId
:   Type: Long Integer.  
    Related claim unique identfier.

CauseOfLossId
:   Type: IncidentCauseOfLoss Identifier.  
    Indicates the related cause of loss identifier.

### Hospital { #Structure_Hospital }

Structure to handle information about a hospital.

*Attributes*

Id
:   Type: Long Integer.  
    Hospital unique identifier.

Name
:   Type: Text.  
    Indicates the hospital name.

Address
:   Type: Text.  
    Indicates the hospital address.

Geometry
:   Type: [Geometry](<#Structure_Geometry>).  
    Record to handle the hospital coordinates.

Phone
:   Type: Phone Number.  
    Indicates the hospital phone number.

Website
:   Type: Text.  
    Indicates the hospital website url.

Distance
:   Type: Decimal (0, 0).  
    Indicates the distance to the Hospital or Clinic.

Rating
:   Type: Integer.  
    Indicates the hospital rating from 1 to 5 stars.

BusinessHours
:   Type: [BusinessHours](<#Structure_BusinessHours>).  
    Record to handle the business hours for a hospital.

IsHospital
:   Type: Boolean.  
    Indicates if the item is a hospital (true) or a clinic (false).

SpecialtyId
:   Type: Long Integer.  
    Identifier of the specialty related to this hospital.

InsuranceId
:   Type: Long Integer.  
    Identifier of the insurance partner related to this hospital.

IsEmergencyService
:   Type: Boolean.  
    Indicates if the item has a 24/7 emergency service (true) or not (false).

IsOpen
:   Type: Boolean.  
    Indicates if the item is open (true) or not (false).

### HouseLocation { #Structure_HouseLocation }

Structure to handle data about the detail of a house location.

*Attributes*

Id
:   Type: Long Integer.  
    House location unique identfier.

Location
:   Type: Text.  
    Indicates the location of the house.

HasDwellingCoverage
:   Type: Boolean.  
    Indicates if the house has dwelling coverage.

HasOtherStructures
:   Type: Boolean.  
    Indicates if the house has other structures.

SecureAmount
:   Type: Currency.  
    Indicates the house location's secure amount.

Type
:   Type: Text.  
    Indicates the house's type.

PolicyId
:   Type: Long Integer.  
    Indicates the related policy.

### Industry { #Structure_Industry }

Structure to handle data about industry.

*Attributes*

Id
:   Type: Integer.  
    Industry unique identifier.

Name
:   Type: Text.  
    Indicates the industry name.

### InsurancePartner { #Structure_InsurancePartner }

Structure to handle information about an insurance partner.

*Attributes*

Id
:   Type: Long Integer.  
    Insurance partner unique identifier.

Name
:   Type: Text.  
    Indicates the insurance partner name.

### InsuranceProduct { #Structure_InsuranceProduct }

Structure to handle data about the detail of an insurance product.

*Attributes*

Id
:   Type: Integer.  
    Insurance product unique identfier.

Name
:   Type: Text.  
    Indicates the insurance product's name.

InsuranceTypeId
:   Type: InsuranceType Identifier.  
    Indicates the related insurance type identifier.

Description
:   Type: Text.  
    Indicates the insurance product's description.

Price
:   Type: Currency.  
    Indicates the insurance product's price.

### InsuredPerson { #Structure_InsuredPerson }

Structure to handle data about the detail of an insured person.

*Attributes*

Id
:   Type: Long Integer.  
    Insured person unique identfier.

Birthdate
:   Type: Date Time.  
    Indicates the insured person's birthdate.

FullName
:   Type: Text.  
    Indicates the insured person's full name.

DoctorPhoneNumber
:   Type: Phone Number.  
    Indicates the insured person's doctor phone number.

HolderType
:   Type: Text.  
    Indicates the insured person's holder type.

IdentityCard
:   Type: Text.  
    Indicates the insured person's identity card.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

InitialDate
:   Type: Date.  
    Indicates the insured person's initial date.

Name
:   Type: Text.  
    Indicates the insured person's name.

Number
:   Type: Text.  
    Indicates the insured person's number.

PolicyId
:   Type: Long Integer.  
    Indicates related policy identifier.

TransferAccountNumber
:   Type: Integer.  
    Indicates the insured person's transfer account number.

### Invoice { #Structure_Invoice }

Structure to handle information about an invoice.

*Attributes*

Id
:   Type: Long Integer.  
    Invoice unique identifier.

Name
:   Type: Text.  
    Indicates the invoice name.

Amount
:   Type: Currency.  
    Indicates the invoice amount.

Date
:   Type: Date.  
    Indicates the invoice date.

DaysToAdd
:   Type: Integer.  
    Indicates the days to add to the current date to get the invoice date.

IsPaid
:   Type: Boolean.  
    Indicates if the invoice is paid.

UserId
:   Type: Long Integer.  
    Identifier of the related user.

FilePathURL
:   Type: Text.  
    Indicates the URL of the invoice so it can be displayed.

MimeType
:   Type: Text.  
    Indicates the mimetype of the invoice available in the file path.

### InvolvedParty { #Structure_InvolvedParty }

Structure to handle data about the detail of an involved party.

*Attributes*

Id
:   Type: Long Integer.  
    Involved party unique identfier.

ClaimId
:   Type: Long Integer.  
    Indicates related claim identifier.

Name
:   Type: Text.  
    Indicates involved party's name.

Contact
:   Type: Text.  
    Indicates involved party's contact.

ParticipantType
:   Type: ParticipantType Identifier.  
    Indicates related participant type identifier.

PlateNumber
:   Type: Text.  
    Indicates involved party's plate number.

### LabResult { #Structure_LabResult }

Structure to handle information about a lab result.

*Attributes*

Id
:   Type: Long Integer.  
    Lab Result unique identifier.

DaysToAdd
:   Type: Integer.  
    Indicates the days to add to the current date to get the lab result date.

Date
:   Type: Date Time.  
    Indicates the invoice date.

DoctorId
:   Type: Long Integer.  
    Identifier of the related doctor.

HospitalId
:   Type: Long Integer.  
    Identifier of the related hospital.

IsUnread
:   Type: Boolean.  
    Indicates if the lab result is unread.

MedicalRecordId
:   Type: Long Integer.  
    Identifier of the related medical record.

SpecialtyId
:   Type: Long Integer.  
    Identifier of the related specialty.

UserId
:   Type: Long Integer.  
    Identifier of the related user.

FilePathURL
:   Type: Text.  
    Indicates the URL of the lab result so it can be displayed.

MimeType
:   Type: Text.  
    Indicates the mimetype of the lab result available in the file path.

InvoiceId
:   Type: Long Integer.  
    Identifier of the related invoice.

ExamTypeId
:   Type: Long Integer.  
    Identifier of the related Exam Type.

### Loan { #Structure_Loan }

Structure to handle data about loans.

*Attributes*

Id
:   Type: Long Integer.  
    Loan unique identifier.

LoanStatusId
:   Type: LoanStatus Identifier.  
    Indicates the status of the loan.

LoanTypeId
:   Type: LoanType Identifier.  
    Indicates the type of loan.

AccountId
:   Type: Long Integer.  
    Indicates the account for the loan.

LoanAmount
:   Type: Currency.  
    Indicates the total amount of the loan.

LoanTermMonths
:   Type: Integer.  
    Indicates the term of the loan in months.

RemainingAmount
:   Type: Currency.  
    Indicates the remaining amount for the loan.

RemainingTermMonths
:   Type: Integer.  
    Indicates the remaining months for the loan.

APRPercentage
:   Type: Decimal (0, 0).  
    Indicates the APR percentage for the loan.

MonthlyPayment
:   Type: Currency.  
    Indicates the loan's monthly payment.

AmountPaid
:   Type: Currency.  
    Indicates the amount of the loan already paid.

HasLifeInsurance
:   Type: Boolean.  
    Indicates if the loan has the life insurance option selected.

DaysToAdd
:   Type: Integer.  
    Indicates the days to add to the issue date to obtain the generated issue date.

IssueDate
:   Type: Date.  
    Indicates the issue date of the loan.

BusinessName
:   Type: Text.  
    Indicates the name of the business that took the loan.

BusinessIdentificationNumber
:   Type: Integer.  
    Indicates the identification number of the business that took the loan.

BusinessIndustryId
:   Type: Integer.  
    Indicates the industry of the business that took the loan.

BusinessYearlyRevenue
:   Type: Currency.  
    Indicates the yearly revenue of the business that took the loan.

BusinessAddress
:   Type: Text.  
    Indicates the address of the business that took the loan.

LoanPurposeId
:   Type: Long Integer.  
    Indicates the loan's purpose.

### LoanPurpose { #Structure_LoanPurpose }

Structure to handle data about loan purposes.

*Attributes*

Id
:   Type: Integer.  
    Loan purpose unique identifier.

Name
:   Type: Text.  
    Indicates the loan purpose name.

### MedicalRecord { #Structure_MedicalRecord }

Structure to handle information about a medical record

*Attributes*

Id
:   Type: Long Integer.  
    Medical Record unique identifier.

DaysToAdd
:   Type: Integer.  
    Indicates the days to add to the current date to get the medical record date.

Date
:   Type: Date Time.  
    Indicates the medical record date.

DoctorId
:   Type: Long Integer.  
    Identifier of the related doctor.

HospitalId
:   Type: Long Integer.  
    Identifier of the related hospital.

IsUnread
:   Type: Boolean.  
    Indicates if the medical record is unread.

Name
:   Type: Text.  
    Indicates the medical record name.

SpecialtyId
:   Type: Long Integer.  
    Identifier of the related specialty.

UserId
:   Type: Long Integer.  
    Identifier of the related user.

BookingTypeId
:   Type: BookingType Identifier.  
    Identifier of the booking type.

InvoiceId
:   Type: Long Integer.  
    Identifier of the related invoice.

### Medication { #Structure_Medication }

Structure to handle information about medication.

*Attributes*

Id
:   Type: Long Integer.  
    Medication unique identifier.

Name
:   Type: Text.  
    Indicates the medication name.

DetailedName
:   Type: Text.  
    Indicates the medication complete name.

### Notification { #Structure_Notification }

Structure to handle information to handle the notifications.

*Attributes*

Id
:   Type: Long Integer.  
    Notification unique identifier.

FamilyMemberId
:   Type: Long Integer.  
    Indicates the related notification family member identifier.

PrescriptionId
:   Type: Long Integer.  
    Indicates the prescription identifier related to the notification.

Title
:   Type: Text.  
    Indicates the notification title.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

Time
:   Type: Time.  
    Indicates the notification date.

Description
:   Type: Text.  
    Indicates the notification description.

IsUnread
:   Type: Boolean.  
    Indicates if the notification was unread.

DateTime
:   Type: Date Time.  
    Indicates the generated notification datetime.

AppointmentId
:   Type: Long Integer.  
    Indentifier of the appointment corresponding this notification (if there is one).

### NotificationSetting { #Structure_NotificationSetting }

Structure to handle data about notification settings.

*Attributes*

Id
:   Type: Long Integer.  
    Indacates the notification settings option unique indentifier.

Label
:   Type: Text.  
    Indicates the notification setting option label.

IsEnabled
:   Type: Boolean.  
    Indicates if the notification setting is enabled.

Tags
:   Type: Text.  
    Notification tags.

RecordType
:   Type: RecordType Identifier.  
    Indacates type of notification

### PaymentData { #Structure_PaymentData }

Structure to handle data about the detail of a payment data.

*Attributes*

Id
:   Type: Long Integer.  
    Payment data unique identfier.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

CreatedOn
:   Type: Date.  
    Indicates when the payment data was created.

Description
:   Type: Text.  
    Indicates payment data description.

AccountId
:   Type: Long Integer.  
    Indicates related account identifier.

PolicyId
:   Type: Long Integer.  
    Indictates related policy identifier.

IsPaid
:   Type: Boolean.  
    Indicates if the payment is paid.

Price
:   Type: Currency.  
    Indicates the payment price.

TotalPrice
:   Type: Currency.  
    Indicates the payment's total price.

RecipientName
:   Type: Text.  
    Indicates the payment's recipient name.

FilePathURL
:   Type: Text.  
    Indicates payment data filepath.

MimeType
:   Type: Text.  
    Indicates payment data mime type.

### PaymentReceipt { #Structure_PaymentReceipt }

Structure to handle data about the detail of a payment receipt.

*Attributes*

Id
:   Type: Long Integer.  
    Payment receipt unique identifier.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

CreatedOn
:   Type: Date.  
    Indicates when the receipt was created.

Name
:   Type: Text.  
    Indicates receipt's name.

PaymentId
:   Type: Long Integer.  
    Indicates related payment identifier.

FilePathURL
:   Type: Text.  
    Indicates the receipt's file path.

MimeType
:   Type: Text.  
    Indicates the receipt's mime type.

### Policy { #Structure_Policy }

Structure to handle data about the detail of a policy.

*Attributes*

Id
:   Type: Integer.  
    Policy unique identifier.

AccountId
:   Type: Integer.  
    Related account identifier.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

ContractDueDate
:   Type: Date.  
    Indicates the policy's contract due date.

InsuranceCompanyName
:   Type: Text.  
    Indicates the policy's insurance company name.

IsActive
:   Type: Boolean.  
    Indicates if the policy is active.

Name
:   Type: Text.  
    Indicates the policy's name.

Number
:   Type: Text.  
    Indicates the policy's number.

InsuranceType
:   Type: InsuranceType Identifier.  
    Indicates related insurance type.

### PolicyContract { #Structure_PolicyContract }

Structure to handle data about the detail of a policy contract.

*Attributes*

Id
:   Type: Integer.  
    Policy contract unique identfier.

Name
:   Type: Text.  
    Indicates policy contract name.

PolicyId
:   Type: Long Integer.  
    Indicates related policy identifier.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

CreatedOn
:   Type: Date.  
    Indicates the date when the policy contract was created.

FilePathURL
:   Type: Text.  
    Indicates policy contract file path.

MimeType
:   Type: Text.  
    Indicates policy contract mimetype

### Prescription { #Structure_Prescription }

Structure to handle information about prescriptions.

*Attributes*

Id
:   Type: Long Integer.  
    Prescription unique identifier.

MedicationId
:   Type: Long Integer.  
    Indicates the related prescription medication identifier.

FamilyMemberId
:   Type: Long Integer.  
    Indicates the related prescription family member identifier.

Code
:   Type: Text.  
    Indicates prescription code.

QrCodeUrl
:   Type: Text.  
    Indicates the QrCode URL path.

PrescribedDate
:   Type: Date Time.  
    Indicates prescription date.

ExpirationDate
:   Type: Date Time.  
    Indicates prescription expiration date.

IsOrdered
:   Type: Boolean.  
    Indicates if the prescription has been ordered.

NeedsRenewal
:   Type: Boolean.  
    Indicates if the prescription need to be renewal.

DoctorId
:   Type: Long Integer.  
    Identifier of the doctor that has prescribed it.

DoctorNotes
:   Type: Text.  
    Indicates the doctor notes text.

PrescribedDaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated prescription date.

ExpirationDaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated expiration date.

PillsAmount
:   Type: Long Integer.  
    Indicates the number of pills prescribed.

### ProductSampleData { #Structure_ProductSampleData }

Custom structure for a sample product.

*Attributes*

ProductId
:   Type: Long Integer.  
    Product unique identifier.

ProductImagesList
:   Type: [Binary Data](<#Structure_Binary Data>) List.  
    List with product images.

ProductName
:   Type: Text.  
    Indicates the product name.

ProductColorId
:   Type: Sample_Color Identifier.  
    Related product color identifier.

ProductSizeId
:   Type: Sample_Size Identifier.  
    Related product size identifier.

ProductShortDescription
:   Type: Text.  
    Indicates product short description. Displayed when product is on a list.

ProductDescription
:   Type: Text.  
    Indicates a details description of the product.

ProductPrice
:   Type: Decimal (0, 0).  
    Indicates product's price.

ProductDiscount
:   Type: Currency.  
    Indicates product's available discount.

ProductIsFavorite
:   Type: Boolean.  
    Indicates if the product is favorite, the product will be displayed on the FavoriteProductsList screen.

ProductRating
:   Type: Integer.  
    Indicates product's rating, given by the users.

ProductStock
:   Type: Integer.  
    Indicates product's available stock.

IsNewProduct
:   Type: Boolean.  
    Indicates if this product is a new one.

IsMostPopular
:   Type: Boolean.  
    Indicates if the product is one of the most popular one.

StoreId
:   Type: Integer.  
    Related store identifier.

### Shipping { #Structure_Shipping }

Structure to handle the basic information about shipping.

*Attributes*

Id
:   Type: Long Integer.  
    Shipping unique identifier.

Info
:   Type: Text.  
    Indicates shipping information.

Price
:   Type: Currency.  
    Indicates shipping price.

TimeToDelivery
:   Type: Integer.  
    Indicates shipping delivery time.

Type
:   Type: Text.  
    Indicates shipping type.

### Shopping { #Structure_Shopping }

Structure to handle the basic information about a shopping.

*Attributes*

Id
:   Type: Long Integer.  
    Shopping unique identifier.

Name
:   Type: Text.  
    Indicates the shopping name.

Address1
:   Type: Text.  
    Indicates the shopping address 1st part.

Address2
:   Type: Text.  
    Indicates the shopping address 2nd part.

Phone
:   Type: Phone Number.  
    Indicates the shopping phone number.

Website
:   Type: Text.  
    Indicates the shopping Website URL.

BusinessHours
:   Type: [BusinessHours](<#Structure_BusinessHours>).  
    Record to handle the business hours for the shopping.

OpeningHour
:   Type: Integer.  
    Today's opening hours of the shopping.

ClosingHour
:   Type: Integer.  
    Today's closing hours of the shopping.

Geometry
:   Type: [Geometry](<#Structure_Geometry>).  
    Record to handle the shopping coordinates.

Distance
:   Type: Decimal (0, 0).  
    Indicates the shopping distance value.

Rating
:   Type: Integer.  
    Indicates the shopping rate value.

Services
:   Type: Text.  
    List of services provided by the shopping, comma separated.

IsOpen
:   Type: Boolean.  
    Indicates if the shopping open right now.

IsOpenLate
:   Type: Boolean.  
    Indicates if the shopping open after a certain hour.

### Specialty { #Structure_Specialty }

Structure to handle information about a clinical specialty.

*Attributes*

Id
:   Type: Long Integer.  
    Specialty unique identifier.

Name
:   Type: Text.  
    Indicates the specialty name.

### Treatment { #Structure_Treatment }

Structure to handle information about treatments.

*Attributes*

Id
:   Type: Long Integer.  
    Treatment unique identifier.

FamilyMemberId
:   Type: Long Integer.  
    Indicates the related treatment family member identifier.

PrescriptionId
:   Type: Long Integer.  
    Indicates the related treatment prescription identifier.

MedicationId
:   Type: Long Integer.  
    Indicates the related treatment medication identifier.

Dosage
:   Type: Long Integer.  
    Indicates the medication intake dosage.

Schedule
:   Type: Text.  
    Indicates the schedule of the treatment.

Duration
:   Type: Text.  
    Indicates the durantion of the treatment.

PillsLeft
:   Type: Long Integer.  
    Indicates the number of pills left in the treatment.

WasTaken
:   Type: Boolean.  
    Indicates the if the medication was taken (true) or not (false).

WasSkipped
:   Type: Boolean.  
    Indicates the if the medication was skipped (true) or not (false).

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

Hours
:   Type: Time.  
    Indicates the treatment hours.

TreatmentDate
:   Type: Date Time.  
    Indicates the generated treatment datetime.

Frequency
:   Type: Text.  
    Indicates the taken frequency.

### Vehicle { #Structure_Vehicle }

Structure to handle data about the detail of a vehicle.

*Attributes*

Id
:   Type: Long Integer.  
    Vehicle unique identfier.

CarName
:   Type: Text.  
    Indicates the vehicle's name.

ExtraCoverage
:   Type: Currency.  
    Indicates the vehicle's coverage.

LicensePlateNumber
:   Type: Text.  
    Indicates the vehicle's license plate number.

VehicleType
:   Type: Text.  
    Indicates the vehicle's type.

PolicyId
:   Type: Long Integer.  
    Indicates the related policy identifier.

### VehicleDriver { #Structure_VehicleDriver }

Structure to handle data about the detail of a vehicle driver.

*Attributes*

Id
:   Type: Long Integer.  
    Vehicle driver unique identifier.

VehicleId
:   Type: Long Integer.  
    Indicates the related vehicle.

Name
:   Type: Text.  
    Indicates the driver's name.

Birthdate
:   Type: Date Time.  
    Indicates the driver's birthdate.

DaysToAdd
:   Type: Integer.  
    Indicates the number of days to add to the generated date.

LicenseDate
:   Type: Date.  
    Indicates the driver's license date.

LicenseNumber
:   Type: Text.  
    Indicates the driver's license number.


## Static Entities

### AppointmentStatus { #StaticEntity_AppointmentStatus }

Static Entity with the appointment status.

*Attributes*

Id
:   Type: Text (50).  
    Appointment status identifier.

*Records*

* Attended
* Confirmed
* NotAttended
* Pending

### BookingType { #StaticEntity_BookingType }

Static Entity with the type of booking when making a new appointment.

*Attributes*

Id
:   Type: Text (50).  
    Booking type identifier.

Label
:   Type: Text (50).  
    Booking type label.

*Records*

* HospitalStay
* Exam
* Appointment

### ClaimState { #StaticEntity_ClaimState }



*Attributes*

Id
:   Type: Text (50).  
    

*Records*

* Approved
* Closed
* Submitted

### DisplayToggleStructure { #StaticEntity_DisplayToggleStructure }

Static entity with a set of options to define the apearance structure on the Display_ToggleShow pattern.

*Attributes*

Label
:   Type: Text (50).  
    

*Records*

* ReverseRows
* Inline

### DocumentDataType { #StaticEntity_DocumentDataType }

Static Entity with the available document data types.

*Attributes*

IconName
:   Type: Text (50).  
    Represents the icon name.

Label
:   Type: Text (50).  
    Data type label to display.

Order
:   Type: Integer.  
    Represents the order of the data type.

IsActive
:   Type: Boolean.  
    Indicates if the datatype is active or not.

*Records*

* word
* pdf
* image
* video
* excel
* other
* powerpoint
* zip

### FamilialRelation { #StaticEntity_FamilialRelation }

Static Entity with the Familial Relations.

*Attributes*

Id
:   Type: Text (50).  
    Familial Relation Identifier

*Records*

* Daughter
* Son
* Mother
* Father

### Filter { #StaticEntity_Filter }

Static Entity with the filters for Healthcare items.

*Attributes*

Id
:   Type: Text (50).  
    Filter identifier

*Records*

* Hospital
* EndDate
* StartDate
* Specialty
* PillsLeft
* NeedsRenewal
* Medication
* Doctor

### FilterTypes { #StaticEntity_FilterTypes }

Static entity with the available filter types. It's used in order to enable the filter or sort option.

*Attributes*

Label
:   Type: Text (50).  
    

*Records*

* PriceAndRating
* Sort

### FindUsSortTypes { #StaticEntity_FindUsSortTypes }

Static Entity with the sorts for Hospital/Clinic items in FindUs screen.

*Attributes*

Id
:   Type: Text (50).  
    Sort identifier

IsActive
:   Type: Boolean.  
    Indicates if the record is active or not.

*Records*

* AlphabeticOrder
* Abandoned_OpenNow
* ShortestDistance
* Abandoned_EmergencyService
* BestRating

### Gender { #StaticEntity_Gender }

Static Entity with the genders enumeration.

*Attributes*

Id
:   Type: Text (50).  
    Gender identifier

*Records*

* Male
* Female

### IncidentCauseOfLoss { #StaticEntity_IncidentCauseOfLoss }

Static Entity with the possible causes of loss

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the Cause of Loss

*Records*

* Sinkholecollapse
* Fire
* Civilcommotion
* Vandalism
* Smoke
* Explosion
* Lightning
* Volcanicaction
* Riot
* Hail
* Windstorm
* Vehicles
* Aircraft
* Sprinklerleakage

### InsuranceType { #StaticEntity_InsuranceType }

Static Entity with the available types of insurance.

*Attributes*

Id
:   Type: Text (50).  
    

*Records*

* Home
* Auto
* Healthcare

### KeystoreKeys { #StaticEntity_KeystoreKeys }

Static Entity with the keys used in the app to set and get values from keystore.

*Attributes*

Id
:   Type: Text (50).  
    Kesytore key identifier.

*Records*

* Password
* Pattern
* CurrentUserIdentifier
* Passcode
* KeyStore
* BiometricsSignature

### Language { #StaticEntity_Language }

Static Entity with the user languages.

*Attributes*

Id
:   Type: Text (50).  
    Language identifier

*Records*

* Portuguese
* French
* English

### LoanStatus { #StaticEntity_LoanStatus }

Static Entity with the status of a loan.

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the loan status.

*Records*

* Closed
* PendingApproval
* Running

### LoanType { #StaticEntity_LoanType }

Static Entity with the types of a requested loan.

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the loan type.

*Records*

* Personal
* Business

### MedicalActivityType { #StaticEntity_MedicalActivityType }

Static Entity with the types of medical activities for healthcare app.

*Attributes*

Id
:   Type: Text (50).  
    Medical activity identifier.

*Records*

* MedicalRecords
* LabResults
* Invoices

### MedicalArea { #StaticEntity_MedicalArea }

Static Entity with the insurance medical areas

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the Medical Area

*Records*

* Hospitalservices
* Contactlenses
* Physicalexamination
* Therapy
* Psychiatriccare
* Laboratoryfees
* Oxygenequipment
* Psychologist
* Surgery
* Longtermcar
* Eyeexaminations
* Xray
* Wheelchair
* MedicalBills

### ParticipantType { #StaticEntity_ParticipantType }

Static Entity with the insurance claim participant types

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the Participant Type

*Records*

* Other
* Passenger
* Driver

### PolicyDetailOptionItem { #StaticEntity_PolicyDetailOptionItem }

Static Entity with the options available for the policy details.

*Attributes*

Id
:   Type: Integer.  
    Identifier of the policy detail option.

*Records*

* Coverage
* Claims
* Info
* Documentation

### ProductColors { #StaticEntity_ProductColors }

Static Entity with the available colors for a product.

*Attributes*

Id
:   Type: Text (50).  
    Product color identifier.

*Records*

* Blue
* Yellow
* Red
* Orange
* White
* Purple
* Gray
* Black
* Green

### ProductSize { #StaticEntity_ProductSize }

Static Entity with the available sizes for a product.

*Attributes*

Id
:   Type: Integer.  
    Product size identifier.

*Records*

* L
* S
* XL
* XXL
* XS
* M

### RecordType { #StaticEntity_RecordType }

Static Entity with the type associated with a record.

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the record type

*Records*

* Generic
* Banking

### Sort { #StaticEntity_Sort }

Static Entity with the sorts for Healthcare items.

*Attributes*

Id
:   Type: Text (50).  
    Sort identifier

*Records*

* UnreadFirst
* MostRecent
* Oldest

### SupportTypeGeneric { #StaticEntity_SupportTypeGeneric }

Static Entity with the support options.

*Attributes*

Id
:   Type: Integer.  
    Identifier of the support type.

*Records*

* CallAgent
* FindUs
* EmailUs
* CallMe
* ChatWithUs

### SupportTypeInsurance { #StaticEntity_SupportTypeInsurance }

Static Entity with the support options for insurance.

*Attributes*

Id
:   Type: Integer.  
    Identifier of the support type.

*Records*

* EmailUs
* ChatWithUs
* CallMe
* CallAgent

### SyncUnits { #StaticEntity_SyncUnits }

Static Entity with the available sync units.

*Attributes*

Code
:   Type: Text (50).  
    Syncronization unit Code.

*Records*

* SitePropertiesInsurance
* SiteProperties

### TouchIdErrorMessage { #StaticEntity_TouchIdErrorMessage }

Static Entity (id only) with the possible error messages of the touch id plugin.

*Attributes*

Id
:   Type: Text (50).  
    Identifier of the touch ID error message.

*Records*

* Unknown
* IOS_UserCancelledOperation
* IOS_ExceedFailedAtempts
* Unavailable
* Android_UserCancelledOperation
* Android_ExceedFailedAttempts

### TriggerListAction { #StaticEntity_TriggerListAction }

Static Entity with the actions to execute on a given list like Filter or Sort.

*Attributes*

Id
:   Type: Integer.  
    Action trigger identifier.

*Records*

* Sort
* Filter

______________________________________________________________
_QR CODE is a registered trademark of Denso Wave Incorporated._

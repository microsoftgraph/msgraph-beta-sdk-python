from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance, agreement_acceptance, approval, app_consent_request, app_role_assignment, assigned_license, assigned_plan, authentication, authorization_info, calendar, calendar_group, chat, cloud_p_c, contact, contact_folder, custom_security_attribute_value, device, device_enrollment_configuration, device_key, device_management_troubleshooting_event, directory_object, drive, employee_org_data, event, extension, group, inference_classification, information_protection, item_insights, license_assignment_state, license_details, mailbox_settings, mail_folder, managed_app_registration, managed_device, message, mobile_app_intent_and_state, mobile_app_troubleshooting_event, notification, object_identity, onenote, online_meeting, on_premises_extension_attributes, on_premises_provisioning_error, outlook_user, o_auth2_permission_grant, password_profile, person, planner_user, presence, profile, profile_photo, provisioned_plan, scoped_role_membership, service_principal, service_provisioning_error, sign_in_activity, site, team, todo, usage_right, user_activity, user_analytics, user_print, user_settings, user_teamwork, windows_information_protection_device_registration
    from .security import security

from . import directory_object

class User(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new User and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.user"
        # A freeform text entry field for the user to describe themselves. Returned only on $select.
        self._about_me: Optional[str] = None
        # true if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter (eq, ne, not, and in).
        self._account_enabled: Optional[bool] = None
        # The activities property
        self._activities: Optional[List[user_activity.UserActivity]] = None
        # Sets the age group of the user. Allowed values: null, Minor, NotAdult and Adult. Refer to the legal age group property definitions for further information. Supports $filter (eq, ne, not, and in).
        self._age_group: Optional[str] = None
        # The user's terms of use acceptance statuses. Read-only. Nullable.
        self._agreement_acceptances: Optional[List[agreement_acceptance.AgreementAcceptance]] = None
        # The analytics property
        self._analytics: Optional[user_analytics.UserAnalytics] = None
        # The appConsentRequestsForApproval property
        self._app_consent_requests_for_approval: Optional[List[app_consent_request.AppConsentRequest]] = None
        # The appRoleAssignedResources property
        self._app_role_assigned_resources: Optional[List[service_principal.ServicePrincipal]] = None
        # Represents the app roles a user has been granted for an application. Supports $expand.
        self._app_role_assignments: Optional[List[app_role_assignment.AppRoleAssignment]] = None
        # The approvals property
        self._approvals: Optional[List[approval.Approval]] = None
        # The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate directly-assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly-assigned and inherited licenses. Not nullable. Supports $filter (eq, not, /$count eq 0, /$count ne 0).
        self._assigned_licenses: Optional[List[assigned_license.AssignedLicense]] = None
        # The plans that are assigned to the user. Read-only. Not nullable.Supports $filter (eq and not).
        self._assigned_plans: Optional[List[assigned_plan.AssignedPlan]] = None
        # The authentication property
        self._authentication: Optional[authentication.Authentication] = None
        # Identifiers that can be used to identify and authenticate a user in non-Azure AD environments. This property can be used to store identifiers for smartcard-based certificates that a user uses for access to on-premises Active Directory deployments or for federated access. It can also be used to store the Subject Alternate Name (SAN) that's associated with a Common Access Card (CAC). Nullable.Supports $filter (eq and startsWith).
        self._authorization_info: Optional[authorization_info.AuthorizationInfo] = None
        # The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Returned only on $select.
        self._birthday: Optional[datetime] = None
        # The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced from on-premises directory. Supports $filter (eq, not, ge, le, startsWith).
        self._business_phones: Optional[List[str]] = None
        # The user's primary calendar. Read-only.
        self._calendar: Optional[calendar.Calendar] = None
        # The user's calendar groups. Read-only. Nullable.
        self._calendar_groups: Optional[List[calendar_group.CalendarGroup]] = None
        # The calendar view for the calendar. Read-only. Nullable.
        self._calendar_view: Optional[List[event.Event]] = None
        # The user's calendars. Read-only. Nullable.
        self._calendars: Optional[List[calendar.Calendar]] = None
        # The chats property
        self._chats: Optional[List[chat.Chat]] = None
        # The city in which the user is located. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._city: Optional[str] = None
        # The cloudPCs property
        self._cloud_p_cs: Optional[List[cloud_p_c.CloudPC]] = None
        # The company name which the user is associated. This property can be useful for describing the company that an external user comes from. The maximum length is 64 characters.Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._company_name: Optional[str] = None
        # Sets whether consent has been obtained for minors. Allowed values: null, Granted, Denied and NotRequired. Refer to the legal age group property definitions for further information. Supports $filter (eq, ne, not, and in).
        self._consent_provided_for_minor: Optional[str] = None
        # The user's contacts folders. Read-only. Nullable.
        self._contact_folders: Optional[List[contact_folder.ContactFolder]] = None
        # The user's contacts. Read-only. Nullable.
        self._contacts: Optional[List[contact.Contact]] = None
        # The country/region in which the user is located; for example, US or UK. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._country: Optional[str] = None
        # The date and time the user was created, in ISO 8601 format and in UTC time. The value cannot be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Azure AD. Property is null for some users created before June 2018 and on-premises users that were synced to Azure AD before June 2018. Read-only. Supports $filter (eq, ne, not , ge, le, in).
        self._created_date_time: Optional[datetime] = None
        # Directory objects that were created by the user. Read-only. Nullable.
        self._created_objects: Optional[List[directory_object.DirectoryObject]] = None
        # Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by an external user signing up through a link that is part of a user flow (SelfServiceSignUp).  Read-only.Supports $filter (eq, ne, not, and in).
        self._creation_type: Optional[str] = None
        # An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Returned only on $select. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive.
        self._custom_security_attributes: Optional[custom_security_attribute_value.CustomSecurityAttributeValue] = None
        # The name for the department in which the user works. Maximum length is 64 characters.Supports $filter (eq, ne, not , ge, le, in, and eq on null values).
        self._department: Optional[str] = None
        # Get enrollment configurations targeted to the user
        self._device_enrollment_configurations: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None
        # The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.
        self._device_enrollment_limit: Optional[int] = None
        # The deviceKeys property
        self._device_keys: Optional[List[device_key.DeviceKey]] = None
        # The list of troubleshooting events for this user.
        self._device_management_troubleshooting_events: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None
        # The devices property
        self._devices: Optional[List[device.Device]] = None
        # The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.
        self._direct_reports: Optional[List[directory_object.DirectoryObject]] = None
        # The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Maximum length is 256 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderBy, and $search.
        self._display_name: Optional[str] = None
        # The user's OneDrive. Read-only.
        self._drive: Optional[drive.Drive] = None
        # A collection of drives available for this user. Read-only.
        self._drives: Optional[List[drive.Drive]] = None
        # The date and time when the user was hired or will start work in case of a future hire. Supports $filter (eq, ne, not , ge, le, in).
        self._employee_hire_date: Optional[datetime] = None
        # The employee identifier assigned to the user by the organization. The maximum length is 16 characters.Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        self._employee_id: Optional[str] = None
        # The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs one of the following Azure AD roles: Lifecycle Workflows Administrator, Global Reader, or Global Administrator. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user.
        self._employee_leave_date_time: Optional[datetime] = None
        # Represents organization data (e.g. division and costCenter) associated with a user. Supports $filter (eq, ne, not , ge, le, in).
        self._employee_org_data: Optional[employee_org_data.EmployeeOrgData] = None
        # Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Supports $filter (eq, ne, not , ge, le, in, startsWith).
        self._employee_type: Optional[str] = None
        # The user's events. Default is to show events under the Default Calendar. Read-only. Nullable.
        self._events: Optional[List[event.Event]] = None
        # The collection of open extensions defined for the user. Supports $expand. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Supports $filter (eq, ne, not , in).
        self._external_user_state: Optional[str] = None
        # Shows the timestamp for the latest change to the externalUserState property. Supports $filter (eq, ne, not , in).
        self._external_user_state_change_date_time: Optional[str] = None
        # The fax number of the user. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        self._fax_number: Optional[str] = None
        # The followedSites property
        self._followed_sites: Optional[List[site.Site]] = None
        # The given name (first name) of the user. Maximum length is 64 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        self._given_name: Optional[str] = None
        # The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Returned only on $select.  Note: This property is specific to SharePoint Online. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.
        self._hire_date: Optional[datetime] = None
        # Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Supports $filter (eq) including on null values, only where the signInType is not userPrincipalName.
        self._identities: Optional[List[object_identity.ObjectIdentity]] = None
        # The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Supports $filter (eq, not, ge, le, startsWith).
        self._im_addresses: Optional[List[str]] = None
        # Relevance classification of the user's messages based on explicit designations which override inferred relevance or importance.
        self._inference_classification: Optional[inference_classification.InferenceClassification] = None
        # Identifies the info segments assigned to the user.  Supports $filter (eq, not, ge, le, startsWith).
        self._info_catalogs: Optional[List[str]] = None
        # The informationProtection property
        self._information_protection: Optional[information_protection.InformationProtection] = None
        # The insights property
        self._insights: Optional[item_insights.ItemInsights] = None
        # A list for the user to describe their interests. Returned only on $select.
        self._interests: Optional[List[str]] = None
        # The isManagementRestricted property
        self._is_management_restricted: Optional[bool] = None
        # Do not use – reserved for future use.
        self._is_resource_account: Optional[bool] = None
        # The user's job title. Maximum length is 128 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        self._job_title: Optional[str] = None
        # The joinedGroups property
        self._joined_groups: Optional[List[group.Group]] = None
        # The Microsoft Teams teams that the user is a member of. Read-only. Nullable.
        self._joined_teams: Optional[List[team.Team]] = None
        # The time when this Azure AD user last changed their password or when their password was created, , whichever date the latest action was performed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Returned only on $select.
        self._last_password_change_date_time: Optional[datetime] = None
        # Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult and Adult. Refer to the legal age group property definitions for further information. Returned only on $select.
        self._legal_age_group_classification: Optional[str] = None
        # State of license assignments for this user. Also indicates licenses that are directly-assigned and those that the user has inherited through group memberships. Read-only. Returned only on $select.
        self._license_assignment_states: Optional[List[license_assignment_state.LicenseAssignmentState]] = None
        # The licenseDetails property
        self._license_details: Optional[List[license_details.LicenseDetails]] = None
        # The SMTP address for the user, for example, admin@contoso.com. Changes to this property will also update the user's proxyAddresses collection to include the value as an SMTP address. This property cannot contain accent characters.  NOTE: We do not recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead.  Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).
        self._mail: Optional[str] = None
        # The user's mail folders. Read-only. Nullable.
        self._mail_folders: Optional[List[mail_folder.MailFolder]] = None
        # The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._mail_nickname: Optional[str] = None
        # Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. For more information, see User preferences for languages and regional formats. Returned only on $select.
        self._mailbox_settings: Optional[mailbox_settings.MailboxSettings] = None
        # Zero or more managed app registrations that belong to the user.
        self._managed_app_registrations: Optional[List[managed_app_registration.ManagedAppRegistration]] = None
        # The managed devices associated with the user.
        self._managed_devices: Optional[List[managed_device.ManagedDevice]] = None
        # The user or contact that is this user's manager. Read-only. (HTTP Methods: GET, PUT, DELETE.). Supports $expand.
        self._manager: Optional[directory_object.DirectoryObject] = None
        # The groups, directory roles and administrative units that the user is a member of. Read-only. Nullable. Supports $expand.
        self._member_of: Optional[List[directory_object.DirectoryObject]] = None
        # The messages in a mailbox or folder. Read-only. Nullable.
        self._messages: Optional[List[message.Message]] = None
        # The list of troubleshooting events for this user.
        self._mobile_app_intent_and_states: Optional[List[mobile_app_intent_and_state.MobileAppIntentAndState]] = None
        # The list of mobile app troubleshooting events for this user.
        self._mobile_app_troubleshooting_events: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]] = None
        # The primary cellular telephone number for the user. Read-only for users synced from on-premises directory.  Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._mobile_phone: Optional[str] = None
        # The URL for the user's personal site. Returned only on $select.
        self._my_site: Optional[str] = None
        # The notifications property
        self._notifications: Optional[List[notification.Notification]] = None
        # The oauth2PermissionGrants property
        self._oauth2_permission_grants: Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]] = None
        # The office location in the user's place of business. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._office_location: Optional[str] = None
        # Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.
        self._on_premises_distinguished_name: Optional[str] = None
        # Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.
        self._on_premises_domain_name: Optional[str] = None
        # Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Supports $filter (eq, ne, not, in).
        self._on_premises_extension_attributes: Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes] = None
        # This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user's userPrincipalName (UPN) property. Note: The $ and _ characters cannot be used when specifying this property. Supports $filter (eq, ne, not, ge, le, in).
        self._on_premises_immutable_id: Optional[str] = None
        # Indicates the last time at which the object was synced with the on-premises directory; for example: '2013-02-16T03:04:54Z'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, in).
        self._on_premises_last_sync_date_time: Optional[datetime] = None
        # Errors when using Microsoft synchronization product during provisioning.  Supports $filter (eq, not, ge, le).
        self._on_premises_provisioning_errors: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]] = None
        # Contains the on-premises sAMAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        self._on_premises_sam_account_name: Optional[str] = None
        # Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Supports $filter (eq including on null values).
        self._on_premises_security_identifier: Optional[str] = None
        # true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Azure Active Directory (Azure AD). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        self._on_premises_sync_enabled: Optional[bool] = None
        # Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        self._on_premises_user_principal_name: Optional[str] = None
        # The onenote property
        self._onenote: Optional[onenote.Onenote] = None
        # The onlineMeetings property
        self._online_meetings: Optional[List[online_meeting.OnlineMeeting]] = None
        # A list of additional email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com'].NOTE: This property cannot contain accent characters.Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).
        self._other_mails: Optional[List[str]] = None
        # Selective Outlook services available to the user. Read-only. Nullable.
        self._outlook: Optional[outlook_user.OutlookUser] = None
        # Devices that are owned by the user. Read-only. Nullable. Supports $expand.
        self._owned_devices: Optional[List[directory_object.DirectoryObject]] = None
        # Directory objects that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        self._owned_objects: Optional[List[directory_object.DirectoryObject]] = None
        # Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two may be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. For more information on the default password policies, see Azure AD pasword policies. Supports $filter (ne, not, and eq on null values).
        self._password_policies: Optional[str] = None
        # Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Supports $filter (eq, ne, not, in, and eq on null values).
        self._password_profile: Optional[password_profile.PasswordProfile] = None
        # A list for the user to enumerate their past projects. Returned only on $select.
        self._past_projects: Optional[List[str]] = None
        # Navigation property to get list of access reviews pending approval by reviewer.
        self._pending_access_review_instances: Optional[List[access_review_instance.AccessReviewInstance]] = None
        # Read-only. The most relevant people to the user. The collection is ordered by their relevance to the user, which is determined by the user's communication, collaboration and business relationships. A person is an aggregation of information from across mail, contacts and social networks.
        self._people: Optional[List[person.Person]] = None
        # The user's profile photo. Read-only.
        self._photo: Optional[profile_photo.ProfilePhoto] = None
        # The photos property
        self._photos: Optional[List[profile_photo.ProfilePhoto]] = None
        # Selective Planner services available to the user. Read-only. Nullable.
        self._planner: Optional[planner_user.PlannerUser] = None
        # The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._postal_code: Optional[str] = None
        # The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.
        self._preferred_data_location: Optional[str] = None
        # The preferred language for the user. Should follow ISO 639-1 Code; for example en-US. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._preferred_language: Optional[str] = None
        # The preferred name for the user. Not Supported. This attribute returns an empty string.Returned only on $select.
        self._preferred_name: Optional[str] = None
        # The presence property
        self._presence: Optional[presence.Presence] = None
        # The print property
        self._print: Optional[user_print.UserPrint] = None
        # Represents properties that are descriptive of a user in a tenant.
        self._profile: Optional[profile.Profile] = None
        # The plans that are provisioned for the user. Read-only. Not nullable. Supports $filter (eq, not, ge, le).
        self._provisioned_plans: Optional[List[provisioned_plan.ProvisionedPlan]] = None
        # For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property will also update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address while those prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of ten unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
        self._proxy_addresses: Optional[List[str]] = None
        # Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use invalidateAllRefreshTokens to reset.
        self._refresh_tokens_valid_from_date_time: Optional[datetime] = None
        # Devices that are registered for the user. Read-only. Nullable. Supports $expand.
        self._registered_devices: Optional[List[directory_object.DirectoryObject]] = None
        # A list for the user to enumerate their responsibilities. Returned only on $select.
        self._responsibilities: Optional[List[str]] = None
        # A list for the user to enumerate the schools they have attended. Returned only on $select.
        self._schools: Optional[List[str]] = None
        # The scoped-role administrative unit memberships for this user. Read-only. Nullable.
        self._scoped_role_member_of: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None
        # The security property
        self._security: Optional[security.Security] = None
        # Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).
        self._security_identifier: Optional[str] = None
        # The serviceProvisioningErrors property
        self._service_provisioning_errors: Optional[List[service_provisioning_error.ServiceProvisioningError]] = None
        # The settings property
        self._settings: Optional[user_settings.UserSettings] = None
        # Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.
        self._show_in_address_list: Optional[bool] = None
        # Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Returned only on $select. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note:  Details for this property require an Azure AD Premium P1/P2 license and the AuditLog.Read.All permission.When you specify $select=signInActivity or $filter=signInActivity while listing users, the maximum page size is 120 users. Requests with $top set higher than 120 will return pages with up to 120 users.This property is not returned for a user who has never signed in or last signed in before April 2020.
        self._sign_in_activity: Optional[sign_in_activity.SignInActivity] = None
        # Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset.
        self._sign_in_sessions_valid_from_date_time: Optional[datetime] = None
        # A list for the user to enumerate their skills. Returned only on $select.
        self._skills: Optional[List[str]] = None
        # The state or province in the user's address. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._state: Optional[str] = None
        # The street address of the user's place of business. Maximum length is 1024 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._street_address: Optional[str] = None
        # The user's surname (family name or last name). Maximum length is 64 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._surname: Optional[str] = None
        # A container for Microsoft Teams features available for the user. Read-only. Nullable.
        self._teamwork: Optional[user_teamwork.UserTeamwork] = None
        # Represents the To Do services available to a user.
        self._todo: Optional[todo.Todo] = None
        # The groups, including nested groups, and directory roles that a user is a member of. Nullable.
        self._transitive_member_of: Optional[List[directory_object.DirectoryObject]] = None
        # The transitive reports for a user. Read-only.
        self._transitive_reports: Optional[List[directory_object.DirectoryObject]] = None
        # A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: US, JP, and GB. Not nullable. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._usage_location: Optional[str] = None
        # Represents the usage rights a user has been granted.
        self._usage_rights: Optional[List[usage_right.UsageRight]] = None
        # The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property cannot contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderBy.
        self._user_principal_name: Optional[str] = None
        # A String value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for member and guest users, see What are the default user permissions in Azure Active Directory?
        self._user_type: Optional[str] = None
        # Zero or more WIP device registrations that belong to the user.
        self._windows_information_protection_device_registrations: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]] = None
    
    @property
    def about_me(self,) -> Optional[str]:
        """
        Gets the aboutMe property value. A freeform text entry field for the user to describe themselves. Returned only on $select.
        Returns: Optional[str]
        """
        return self._about_me
    
    @about_me.setter
    def about_me(self,value: Optional[str] = None) -> None:
        """
        Sets the aboutMe property value. A freeform text entry field for the user to describe themselves. Returned only on $select.
        Args:
            value: Value to set for the about_me property.
        """
        self._about_me = value
    
    @property
    def account_enabled(self,) -> Optional[bool]:
        """
        Gets the accountEnabled property value. true if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter (eq, ne, not, and in).
        Returns: Optional[bool]
        """
        return self._account_enabled
    
    @account_enabled.setter
    def account_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountEnabled property value. true if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter (eq, ne, not, and in).
        Args:
            value: Value to set for the account_enabled property.
        """
        self._account_enabled = value
    
    @property
    def activities(self,) -> Optional[List[user_activity.UserActivity]]:
        """
        Gets the activities property value. The activities property
        Returns: Optional[List[user_activity.UserActivity]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[user_activity.UserActivity]] = None) -> None:
        """
        Sets the activities property value. The activities property
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
    @property
    def age_group(self,) -> Optional[str]:
        """
        Gets the ageGroup property value. Sets the age group of the user. Allowed values: null, Minor, NotAdult and Adult. Refer to the legal age group property definitions for further information. Supports $filter (eq, ne, not, and in).
        Returns: Optional[str]
        """
        return self._age_group
    
    @age_group.setter
    def age_group(self,value: Optional[str] = None) -> None:
        """
        Sets the ageGroup property value. Sets the age group of the user. Allowed values: null, Minor, NotAdult and Adult. Refer to the legal age group property definitions for further information. Supports $filter (eq, ne, not, and in).
        Args:
            value: Value to set for the age_group property.
        """
        self._age_group = value
    
    @property
    def agreement_acceptances(self,) -> Optional[List[agreement_acceptance.AgreementAcceptance]]:
        """
        Gets the agreementAcceptances property value. The user's terms of use acceptance statuses. Read-only. Nullable.
        Returns: Optional[List[agreement_acceptance.AgreementAcceptance]]
        """
        return self._agreement_acceptances
    
    @agreement_acceptances.setter
    def agreement_acceptances(self,value: Optional[List[agreement_acceptance.AgreementAcceptance]] = None) -> None:
        """
        Sets the agreementAcceptances property value. The user's terms of use acceptance statuses. Read-only. Nullable.
        Args:
            value: Value to set for the agreement_acceptances property.
        """
        self._agreement_acceptances = value
    
    @property
    def analytics(self,) -> Optional[user_analytics.UserAnalytics]:
        """
        Gets the analytics property value. The analytics property
        Returns: Optional[user_analytics.UserAnalytics]
        """
        return self._analytics
    
    @analytics.setter
    def analytics(self,value: Optional[user_analytics.UserAnalytics] = None) -> None:
        """
        Sets the analytics property value. The analytics property
        Args:
            value: Value to set for the analytics property.
        """
        self._analytics = value
    
    @property
    def app_consent_requests_for_approval(self,) -> Optional[List[app_consent_request.AppConsentRequest]]:
        """
        Gets the appConsentRequestsForApproval property value. The appConsentRequestsForApproval property
        Returns: Optional[List[app_consent_request.AppConsentRequest]]
        """
        return self._app_consent_requests_for_approval
    
    @app_consent_requests_for_approval.setter
    def app_consent_requests_for_approval(self,value: Optional[List[app_consent_request.AppConsentRequest]] = None) -> None:
        """
        Sets the appConsentRequestsForApproval property value. The appConsentRequestsForApproval property
        Args:
            value: Value to set for the app_consent_requests_for_approval property.
        """
        self._app_consent_requests_for_approval = value
    
    @property
    def app_role_assigned_resources(self,) -> Optional[List[service_principal.ServicePrincipal]]:
        """
        Gets the appRoleAssignedResources property value. The appRoleAssignedResources property
        Returns: Optional[List[service_principal.ServicePrincipal]]
        """
        return self._app_role_assigned_resources
    
    @app_role_assigned_resources.setter
    def app_role_assigned_resources(self,value: Optional[List[service_principal.ServicePrincipal]] = None) -> None:
        """
        Sets the appRoleAssignedResources property value. The appRoleAssignedResources property
        Args:
            value: Value to set for the app_role_assigned_resources property.
        """
        self._app_role_assigned_resources = value
    
    @property
    def app_role_assignments(self,) -> Optional[List[app_role_assignment.AppRoleAssignment]]:
        """
        Gets the appRoleAssignments property value. Represents the app roles a user has been granted for an application. Supports $expand.
        Returns: Optional[List[app_role_assignment.AppRoleAssignment]]
        """
        return self._app_role_assignments
    
    @app_role_assignments.setter
    def app_role_assignments(self,value: Optional[List[app_role_assignment.AppRoleAssignment]] = None) -> None:
        """
        Sets the appRoleAssignments property value. Represents the app roles a user has been granted for an application. Supports $expand.
        Args:
            value: Value to set for the app_role_assignments property.
        """
        self._app_role_assignments = value
    
    @property
    def approvals(self,) -> Optional[List[approval.Approval]]:
        """
        Gets the approvals property value. The approvals property
        Returns: Optional[List[approval.Approval]]
        """
        return self._approvals
    
    @approvals.setter
    def approvals(self,value: Optional[List[approval.Approval]] = None) -> None:
        """
        Sets the approvals property value. The approvals property
        Args:
            value: Value to set for the approvals property.
        """
        self._approvals = value
    
    @property
    def assigned_licenses(self,) -> Optional[List[assigned_license.AssignedLicense]]:
        """
        Gets the assignedLicenses property value. The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate directly-assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly-assigned and inherited licenses. Not nullable. Supports $filter (eq, not, /$count eq 0, /$count ne 0).
        Returns: Optional[List[assigned_license.AssignedLicense]]
        """
        return self._assigned_licenses
    
    @assigned_licenses.setter
    def assigned_licenses(self,value: Optional[List[assigned_license.AssignedLicense]] = None) -> None:
        """
        Sets the assignedLicenses property value. The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate directly-assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly-assigned and inherited licenses. Not nullable. Supports $filter (eq, not, /$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the assigned_licenses property.
        """
        self._assigned_licenses = value
    
    @property
    def assigned_plans(self,) -> Optional[List[assigned_plan.AssignedPlan]]:
        """
        Gets the assignedPlans property value. The plans that are assigned to the user. Read-only. Not nullable.Supports $filter (eq and not).
        Returns: Optional[List[assigned_plan.AssignedPlan]]
        """
        return self._assigned_plans
    
    @assigned_plans.setter
    def assigned_plans(self,value: Optional[List[assigned_plan.AssignedPlan]] = None) -> None:
        """
        Sets the assignedPlans property value. The plans that are assigned to the user. Read-only. Not nullable.Supports $filter (eq and not).
        Args:
            value: Value to set for the assigned_plans property.
        """
        self._assigned_plans = value
    
    @property
    def authentication(self,) -> Optional[authentication.Authentication]:
        """
        Gets the authentication property value. The authentication property
        Returns: Optional[authentication.Authentication]
        """
        return self._authentication
    
    @authentication.setter
    def authentication(self,value: Optional[authentication.Authentication] = None) -> None:
        """
        Sets the authentication property value. The authentication property
        Args:
            value: Value to set for the authentication property.
        """
        self._authentication = value
    
    @property
    def authorization_info(self,) -> Optional[authorization_info.AuthorizationInfo]:
        """
        Gets the authorizationInfo property value. Identifiers that can be used to identify and authenticate a user in non-Azure AD environments. This property can be used to store identifiers for smartcard-based certificates that a user uses for access to on-premises Active Directory deployments or for federated access. It can also be used to store the Subject Alternate Name (SAN) that's associated with a Common Access Card (CAC). Nullable.Supports $filter (eq and startsWith).
        Returns: Optional[authorization_info.AuthorizationInfo]
        """
        return self._authorization_info
    
    @authorization_info.setter
    def authorization_info(self,value: Optional[authorization_info.AuthorizationInfo] = None) -> None:
        """
        Sets the authorizationInfo property value. Identifiers that can be used to identify and authenticate a user in non-Azure AD environments. This property can be used to store identifiers for smartcard-based certificates that a user uses for access to on-premises Active Directory deployments or for federated access. It can also be used to store the Subject Alternate Name (SAN) that's associated with a Common Access Card (CAC). Nullable.Supports $filter (eq and startsWith).
        Args:
            value: Value to set for the authorization_info property.
        """
        self._authorization_info = value
    
    @property
    def birthday(self,) -> Optional[datetime]:
        """
        Gets the birthday property value. The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Returned only on $select.
        Returns: Optional[datetime]
        """
        return self._birthday
    
    @birthday.setter
    def birthday(self,value: Optional[datetime] = None) -> None:
        """
        Sets the birthday property value. The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Returned only on $select.
        Args:
            value: Value to set for the birthday property.
        """
        self._birthday = value
    
    @property
    def business_phones(self,) -> Optional[List[str]]:
        """
        Gets the businessPhones property value. The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced from on-premises directory. Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._business_phones
    
    @business_phones.setter
    def business_phones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the businessPhones property value. The telephone numbers for the user. Only one number can be set for this property. Read-only for users synced from on-premises directory. Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the business_phones property.
        """
        self._business_phones = value
    
    @property
    def calendar(self,) -> Optional[calendar.Calendar]:
        """
        Gets the calendar property value. The user's primary calendar. Read-only.
        Returns: Optional[calendar.Calendar]
        """
        return self._calendar
    
    @calendar.setter
    def calendar(self,value: Optional[calendar.Calendar] = None) -> None:
        """
        Sets the calendar property value. The user's primary calendar. Read-only.
        Args:
            value: Value to set for the calendar property.
        """
        self._calendar = value
    
    @property
    def calendar_groups(self,) -> Optional[List[calendar_group.CalendarGroup]]:
        """
        Gets the calendarGroups property value. The user's calendar groups. Read-only. Nullable.
        Returns: Optional[List[calendar_group.CalendarGroup]]
        """
        return self._calendar_groups
    
    @calendar_groups.setter
    def calendar_groups(self,value: Optional[List[calendar_group.CalendarGroup]] = None) -> None:
        """
        Sets the calendarGroups property value. The user's calendar groups. Read-only. Nullable.
        Args:
            value: Value to set for the calendar_groups property.
        """
        self._calendar_groups = value
    
    @property
    def calendar_view(self,) -> Optional[List[event.Event]]:
        """
        Gets the calendarView property value. The calendar view for the calendar. Read-only. Nullable.
        Returns: Optional[List[event.Event]]
        """
        return self._calendar_view
    
    @calendar_view.setter
    def calendar_view(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the calendarView property value. The calendar view for the calendar. Read-only. Nullable.
        Args:
            value: Value to set for the calendar_view property.
        """
        self._calendar_view = value
    
    @property
    def calendars(self,) -> Optional[List[calendar.Calendar]]:
        """
        Gets the calendars property value. The user's calendars. Read-only. Nullable.
        Returns: Optional[List[calendar.Calendar]]
        """
        return self._calendars
    
    @calendars.setter
    def calendars(self,value: Optional[List[calendar.Calendar]] = None) -> None:
        """
        Sets the calendars property value. The user's calendars. Read-only. Nullable.
        Args:
            value: Value to set for the calendars property.
        """
        self._calendars = value
    
    @property
    def chats(self,) -> Optional[List[chat.Chat]]:
        """
        Gets the chats property value. The chats property
        Returns: Optional[List[chat.Chat]]
        """
        return self._chats
    
    @chats.setter
    def chats(self,value: Optional[List[chat.Chat]] = None) -> None:
        """
        Sets the chats property value. The chats property
        Args:
            value: Value to set for the chats property.
        """
        self._chats = value
    
    @property
    def city(self,) -> Optional[str]:
        """
        Gets the city property value. The city in which the user is located. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. The city in which the user is located. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    @property
    def cloud_p_cs(self,) -> Optional[List[cloud_p_c.CloudPC]]:
        """
        Gets the cloudPCs property value. The cloudPCs property
        Returns: Optional[List[cloud_p_c.CloudPC]]
        """
        return self._cloud_p_cs
    
    @cloud_p_cs.setter
    def cloud_p_cs(self,value: Optional[List[cloud_p_c.CloudPC]] = None) -> None:
        """
        Sets the cloudPCs property value. The cloudPCs property
        Args:
            value: Value to set for the cloud_p_cs property.
        """
        self._cloud_p_cs = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The company name which the user is associated. This property can be useful for describing the company that an external user comes from. The maximum length is 64 characters.Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The company name which the user is associated. This property can be useful for describing the company that an external user comes from. The maximum length is 64 characters.Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the company_name property.
        """
        self._company_name = value
    
    @property
    def consent_provided_for_minor(self,) -> Optional[str]:
        """
        Gets the consentProvidedForMinor property value. Sets whether consent has been obtained for minors. Allowed values: null, Granted, Denied and NotRequired. Refer to the legal age group property definitions for further information. Supports $filter (eq, ne, not, and in).
        Returns: Optional[str]
        """
        return self._consent_provided_for_minor
    
    @consent_provided_for_minor.setter
    def consent_provided_for_minor(self,value: Optional[str] = None) -> None:
        """
        Sets the consentProvidedForMinor property value. Sets whether consent has been obtained for minors. Allowed values: null, Granted, Denied and NotRequired. Refer to the legal age group property definitions for further information. Supports $filter (eq, ne, not, and in).
        Args:
            value: Value to set for the consent_provided_for_minor property.
        """
        self._consent_provided_for_minor = value
    
    @property
    def contact_folders(self,) -> Optional[List[contact_folder.ContactFolder]]:
        """
        Gets the contactFolders property value. The user's contacts folders. Read-only. Nullable.
        Returns: Optional[List[contact_folder.ContactFolder]]
        """
        return self._contact_folders
    
    @contact_folders.setter
    def contact_folders(self,value: Optional[List[contact_folder.ContactFolder]] = None) -> None:
        """
        Sets the contactFolders property value. The user's contacts folders. Read-only. Nullable.
        Args:
            value: Value to set for the contact_folders property.
        """
        self._contact_folders = value
    
    @property
    def contacts(self,) -> Optional[List[contact.Contact]]:
        """
        Gets the contacts property value. The user's contacts. Read-only. Nullable.
        Returns: Optional[List[contact.Contact]]
        """
        return self._contacts
    
    @contacts.setter
    def contacts(self,value: Optional[List[contact.Contact]] = None) -> None:
        """
        Sets the contacts property value. The user's contacts. Read-only. Nullable.
        Args:
            value: Value to set for the contacts property.
        """
        self._contacts = value
    
    @property
    def country(self,) -> Optional[str]:
        """
        Gets the country property value. The country/region in which the user is located; for example, US or UK. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._country
    
    @country.setter
    def country(self,value: Optional[str] = None) -> None:
        """
        Sets the country property value. The country/region in which the user is located; for example, US or UK. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the country property.
        """
        self._country = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the user was created, in ISO 8601 format and in UTC time. The value cannot be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Azure AD. Property is null for some users created before June 2018 and on-premises users that were synced to Azure AD before June 2018. Read-only. Supports $filter (eq, ne, not , ge, le, in).
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the user was created, in ISO 8601 format and in UTC time. The value cannot be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Azure AD. Property is null for some users created before June 2018 and on-premises users that were synced to Azure AD before June 2018. Read-only. Supports $filter (eq, ne, not , ge, le, in).
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @property
    def created_objects(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the createdObjects property value. Directory objects that were created by the user. Read-only. Nullable.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._created_objects
    
    @created_objects.setter
    def created_objects(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the createdObjects property value. Directory objects that were created by the user. Read-only. Nullable.
        Args:
            value: Value to set for the created_objects property.
        """
        self._created_objects = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> User:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: User
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return User()
    
    @property
    def creation_type(self,) -> Optional[str]:
        """
        Gets the creationType property value. Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by an external user signing up through a link that is part of a user flow (SelfServiceSignUp).  Read-only.Supports $filter (eq, ne, not, and in).
        Returns: Optional[str]
        """
        return self._creation_type
    
    @creation_type.setter
    def creation_type(self,value: Optional[str] = None) -> None:
        """
        Sets the creationType property value. Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by an external user signing up through a link that is part of a user flow (SelfServiceSignUp).  Read-only.Supports $filter (eq, ne, not, and in).
        Args:
            value: Value to set for the creation_type property.
        """
        self._creation_type = value
    
    @property
    def custom_security_attributes(self,) -> Optional[custom_security_attribute_value.CustomSecurityAttributeValue]:
        """
        Gets the customSecurityAttributes property value. An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Returned only on $select. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive.
        Returns: Optional[custom_security_attribute_value.CustomSecurityAttributeValue]
        """
        return self._custom_security_attributes
    
    @custom_security_attributes.setter
    def custom_security_attributes(self,value: Optional[custom_security_attribute_value.CustomSecurityAttributeValue] = None) -> None:
        """
        Sets the customSecurityAttributes property value. An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Returned only on $select. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive.
        Args:
            value: Value to set for the custom_security_attributes property.
        """
        self._custom_security_attributes = value
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. The name for the department in which the user works. Maximum length is 64 characters.Supports $filter (eq, ne, not , ge, le, in, and eq on null values).
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. The name for the department in which the user works. Maximum length is 64 characters.Supports $filter (eq, ne, not , ge, le, in, and eq on null values).
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def device_enrollment_configurations(self,) -> Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]]:
        """
        Gets the deviceEnrollmentConfigurations property value. Get enrollment configurations targeted to the user
        Returns: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]]
        """
        return self._device_enrollment_configurations
    
    @device_enrollment_configurations.setter
    def device_enrollment_configurations(self,value: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None) -> None:
        """
        Sets the deviceEnrollmentConfigurations property value. Get enrollment configurations targeted to the user
        Args:
            value: Value to set for the device_enrollment_configurations property.
        """
        self._device_enrollment_configurations = value
    
    @property
    def device_enrollment_limit(self,) -> Optional[int]:
        """
        Gets the deviceEnrollmentLimit property value. The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.
        Returns: Optional[int]
        """
        return self._device_enrollment_limit
    
    @device_enrollment_limit.setter
    def device_enrollment_limit(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceEnrollmentLimit property value. The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.
        Args:
            value: Value to set for the device_enrollment_limit property.
        """
        self._device_enrollment_limit = value
    
    @property
    def device_keys(self,) -> Optional[List[device_key.DeviceKey]]:
        """
        Gets the deviceKeys property value. The deviceKeys property
        Returns: Optional[List[device_key.DeviceKey]]
        """
        return self._device_keys
    
    @device_keys.setter
    def device_keys(self,value: Optional[List[device_key.DeviceKey]] = None) -> None:
        """
        Sets the deviceKeys property value. The deviceKeys property
        Args:
            value: Value to set for the device_keys property.
        """
        self._device_keys = value
    
    @property
    def device_management_troubleshooting_events(self,) -> Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]]:
        """
        Gets the deviceManagementTroubleshootingEvents property value. The list of troubleshooting events for this user.
        Returns: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]]
        """
        return self._device_management_troubleshooting_events
    
    @device_management_troubleshooting_events.setter
    def device_management_troubleshooting_events(self,value: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None) -> None:
        """
        Sets the deviceManagementTroubleshootingEvents property value. The list of troubleshooting events for this user.
        Args:
            value: Value to set for the device_management_troubleshooting_events property.
        """
        self._device_management_troubleshooting_events = value
    
    @property
    def devices(self,) -> Optional[List[device.Device]]:
        """
        Gets the devices property value. The devices property
        Returns: Optional[List[device.Device]]
        """
        return self._devices
    
    @devices.setter
    def devices(self,value: Optional[List[device.Device]] = None) -> None:
        """
        Sets the devices property value. The devices property
        Args:
            value: Value to set for the devices property.
        """
        self._devices = value
    
    @property
    def direct_reports(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the directReports property value. The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._direct_reports
    
    @direct_reports.setter
    def direct_reports(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the directReports property value. The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the direct_reports property.
        """
        self._direct_reports = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Maximum length is 256 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderBy, and $search.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Maximum length is 256 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderBy, and $search.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def drive(self,) -> Optional[drive.Drive]:
        """
        Gets the drive property value. The user's OneDrive. Read-only.
        Returns: Optional[drive.Drive]
        """
        return self._drive
    
    @drive.setter
    def drive(self,value: Optional[drive.Drive] = None) -> None:
        """
        Sets the drive property value. The user's OneDrive. Read-only.
        Args:
            value: Value to set for the drive property.
        """
        self._drive = value
    
    @property
    def drives(self,) -> Optional[List[drive.Drive]]:
        """
        Gets the drives property value. A collection of drives available for this user. Read-only.
        Returns: Optional[List[drive.Drive]]
        """
        return self._drives
    
    @drives.setter
    def drives(self,value: Optional[List[drive.Drive]] = None) -> None:
        """
        Sets the drives property value. A collection of drives available for this user. Read-only.
        Args:
            value: Value to set for the drives property.
        """
        self._drives = value
    
    @property
    def employee_hire_date(self,) -> Optional[datetime]:
        """
        Gets the employeeHireDate property value. The date and time when the user was hired or will start work in case of a future hire. Supports $filter (eq, ne, not , ge, le, in).
        Returns: Optional[datetime]
        """
        return self._employee_hire_date
    
    @employee_hire_date.setter
    def employee_hire_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the employeeHireDate property value. The date and time when the user was hired or will start work in case of a future hire. Supports $filter (eq, ne, not , ge, le, in).
        Args:
            value: Value to set for the employee_hire_date property.
        """
        self._employee_hire_date = value
    
    @property
    def employee_id(self,) -> Optional[str]:
        """
        Gets the employeeId property value. The employee identifier assigned to the user by the organization. The maximum length is 16 characters.Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._employee_id
    
    @employee_id.setter
    def employee_id(self,value: Optional[str] = None) -> None:
        """
        Sets the employeeId property value. The employee identifier assigned to the user by the organization. The maximum length is 16 characters.Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the employee_id property.
        """
        self._employee_id = value
    
    @property
    def employee_leave_date_time(self,) -> Optional[datetime]:
        """
        Gets the employeeLeaveDateTime property value. The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs one of the following Azure AD roles: Lifecycle Workflows Administrator, Global Reader, or Global Administrator. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user.
        Returns: Optional[datetime]
        """
        return self._employee_leave_date_time
    
    @employee_leave_date_time.setter
    def employee_leave_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the employeeLeaveDateTime property value. The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs one of the following Azure AD roles: Lifecycle Workflows Administrator, Global Reader, or Global Administrator. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user.
        Args:
            value: Value to set for the employee_leave_date_time property.
        """
        self._employee_leave_date_time = value
    
    @property
    def employee_org_data(self,) -> Optional[employee_org_data.EmployeeOrgData]:
        """
        Gets the employeeOrgData property value. Represents organization data (e.g. division and costCenter) associated with a user. Supports $filter (eq, ne, not , ge, le, in).
        Returns: Optional[employee_org_data.EmployeeOrgData]
        """
        return self._employee_org_data
    
    @employee_org_data.setter
    def employee_org_data(self,value: Optional[employee_org_data.EmployeeOrgData] = None) -> None:
        """
        Sets the employeeOrgData property value. Represents organization data (e.g. division and costCenter) associated with a user. Supports $filter (eq, ne, not , ge, le, in).
        Args:
            value: Value to set for the employee_org_data property.
        """
        self._employee_org_data = value
    
    @property
    def employee_type(self,) -> Optional[str]:
        """
        Gets the employeeType property value. Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Supports $filter (eq, ne, not , ge, le, in, startsWith).
        Returns: Optional[str]
        """
        return self._employee_type
    
    @employee_type.setter
    def employee_type(self,value: Optional[str] = None) -> None:
        """
        Sets the employeeType property value. Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Supports $filter (eq, ne, not , ge, le, in, startsWith).
        Args:
            value: Value to set for the employee_type property.
        """
        self._employee_type = value
    
    @property
    def events(self,) -> Optional[List[event.Event]]:
        """
        Gets the events property value. The user's events. Default is to show events under the Default Calendar. Read-only. Nullable.
        Returns: Optional[List[event.Event]]
        """
        return self._events
    
    @events.setter
    def events(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the events property value. The user's events. Default is to show events under the Default Calendar. Read-only. Nullable.
        Args:
            value: Value to set for the events property.
        """
        self._events = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the user. Supports $expand. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the user. Supports $expand. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    @property
    def external_user_state(self,) -> Optional[str]:
        """
        Gets the externalUserState property value. For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Supports $filter (eq, ne, not , in).
        Returns: Optional[str]
        """
        return self._external_user_state
    
    @external_user_state.setter
    def external_user_state(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUserState property value. For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Supports $filter (eq, ne, not , in).
        Args:
            value: Value to set for the external_user_state property.
        """
        self._external_user_state = value
    
    @property
    def external_user_state_change_date_time(self,) -> Optional[str]:
        """
        Gets the externalUserStateChangeDateTime property value. Shows the timestamp for the latest change to the externalUserState property. Supports $filter (eq, ne, not , in).
        Returns: Optional[str]
        """
        return self._external_user_state_change_date_time
    
    @external_user_state_change_date_time.setter
    def external_user_state_change_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUserStateChangeDateTime property value. Shows the timestamp for the latest change to the externalUserState property. Supports $filter (eq, ne, not , in).
        Args:
            value: Value to set for the external_user_state_change_date_time property.
        """
        self._external_user_state_change_date_time = value
    
    @property
    def fax_number(self,) -> Optional[str]:
        """
        Gets the faxNumber property value. The fax number of the user. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._fax_number
    
    @fax_number.setter
    def fax_number(self,value: Optional[str] = None) -> None:
        """
        Sets the faxNumber property value. The fax number of the user. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the fax_number property.
        """
        self._fax_number = value
    
    @property
    def followed_sites(self,) -> Optional[List[site.Site]]:
        """
        Gets the followedSites property value. The followedSites property
        Returns: Optional[List[site.Site]]
        """
        return self._followed_sites
    
    @followed_sites.setter
    def followed_sites(self,value: Optional[List[site.Site]] = None) -> None:
        """
        Sets the followedSites property value. The followedSites property
        Args:
            value: Value to set for the followed_sites property.
        """
        self._followed_sites = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance, agreement_acceptance, approval, app_consent_request, app_role_assignment, assigned_license, assigned_plan, authentication, authorization_info, calendar, calendar_group, chat, cloud_p_c, contact, contact_folder, custom_security_attribute_value, device, device_enrollment_configuration, device_key, device_management_troubleshooting_event, directory_object, drive, employee_org_data, event, extension, group, inference_classification, information_protection, item_insights, license_assignment_state, license_details, mailbox_settings, mail_folder, managed_app_registration, managed_device, message, mobile_app_intent_and_state, mobile_app_troubleshooting_event, notification, object_identity, onenote, online_meeting, on_premises_extension_attributes, on_premises_provisioning_error, outlook_user, o_auth2_permission_grant, password_profile, person, planner_user, presence, profile, profile_photo, provisioned_plan, scoped_role_membership, service_principal, service_provisioning_error, sign_in_activity, site, team, todo, usage_right, user_activity, user_analytics, user_print, user_settings, user_teamwork, windows_information_protection_device_registration
        from .security import security

        fields: Dict[str, Callable[[Any], None]] = {
            "aboutMe": lambda n : setattr(self, 'about_me', n.get_str_value()),
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(user_activity.UserActivity)),
            "ageGroup": lambda n : setattr(self, 'age_group', n.get_str_value()),
            "agreementAcceptances": lambda n : setattr(self, 'agreement_acceptances', n.get_collection_of_object_values(agreement_acceptance.AgreementAcceptance)),
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(user_analytics.UserAnalytics)),
            "approvals": lambda n : setattr(self, 'approvals', n.get_collection_of_object_values(approval.Approval)),
            "appConsentRequestsForApproval": lambda n : setattr(self, 'app_consent_requests_for_approval', n.get_collection_of_object_values(app_consent_request.AppConsentRequest)),
            "appRoleAssignedResources": lambda n : setattr(self, 'app_role_assigned_resources', n.get_collection_of_object_values(service_principal.ServicePrincipal)),
            "appRoleAssignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(app_role_assignment.AppRoleAssignment)),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(assigned_license.AssignedLicense)),
            "assignedPlans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(assigned_plan.AssignedPlan)),
            "authentication": lambda n : setattr(self, 'authentication', n.get_object_value(authentication.Authentication)),
            "authorizationInfo": lambda n : setattr(self, 'authorization_info', n.get_object_value(authorization_info.AuthorizationInfo)),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "businessPhones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(calendar.Calendar)),
            "calendars": lambda n : setattr(self, 'calendars', n.get_collection_of_object_values(calendar.Calendar)),
            "calendarGroups": lambda n : setattr(self, 'calendar_groups', n.get_collection_of_object_values(calendar_group.CalendarGroup)),
            "calendarView": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(event.Event)),
            "chats": lambda n : setattr(self, 'chats', n.get_collection_of_object_values(chat.Chat)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "cloudPCs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(cloud_p_c.CloudPC)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "consentProvidedForMinor": lambda n : setattr(self, 'consent_provided_for_minor', n.get_str_value()),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(contact.Contact)),
            "contactFolders": lambda n : setattr(self, 'contact_folders', n.get_collection_of_object_values(contact_folder.ContactFolder)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdObjects": lambda n : setattr(self, 'created_objects', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "creationType": lambda n : setattr(self, 'creation_type', n.get_str_value()),
            "customSecurityAttributes": lambda n : setattr(self, 'custom_security_attributes', n.get_object_value(custom_security_attribute_value.CustomSecurityAttributeValue)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "devices": lambda n : setattr(self, 'devices', n.get_collection_of_object_values(device.Device)),
            "deviceEnrollmentConfigurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(device_enrollment_configuration.DeviceEnrollmentConfiguration)),
            "deviceEnrollmentLimit": lambda n : setattr(self, 'device_enrollment_limit', n.get_int_value()),
            "deviceKeys": lambda n : setattr(self, 'device_keys', n.get_collection_of_object_values(device_key.DeviceKey)),
            "deviceManagementTroubleshootingEvents": lambda n : setattr(self, 'device_management_troubleshooting_events', n.get_collection_of_object_values(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent)),
            "directReports": lambda n : setattr(self, 'direct_reports', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(drive.Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(drive.Drive)),
            "employeeHireDate": lambda n : setattr(self, 'employee_hire_date', n.get_datetime_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_str_value()),
            "employeeLeaveDateTime": lambda n : setattr(self, 'employee_leave_date_time', n.get_datetime_value()),
            "employeeOrgData": lambda n : setattr(self, 'employee_org_data', n.get_object_value(employee_org_data.EmployeeOrgData)),
            "employeeType": lambda n : setattr(self, 'employee_type', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(event.Event)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "externalUserState": lambda n : setattr(self, 'external_user_state', n.get_str_value()),
            "externalUserStateChangeDateTime": lambda n : setattr(self, 'external_user_state_change_date_time', n.get_str_value()),
            "faxNumber": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "followedSites": lambda n : setattr(self, 'followed_sites', n.get_collection_of_object_values(site.Site)),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "hireDate": lambda n : setattr(self, 'hire_date', n.get_datetime_value()),
            "identities": lambda n : setattr(self, 'identities', n.get_collection_of_object_values(object_identity.ObjectIdentity)),
            "imAddresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "inferenceClassification": lambda n : setattr(self, 'inference_classification', n.get_object_value(inference_classification.InferenceClassification)),
            "informationProtection": lambda n : setattr(self, 'information_protection', n.get_object_value(information_protection.InformationProtection)),
            "infoCatalogs": lambda n : setattr(self, 'info_catalogs', n.get_collection_of_primitive_values(str)),
            "insights": lambda n : setattr(self, 'insights', n.get_object_value(item_insights.ItemInsights)),
            "interests": lambda n : setattr(self, 'interests', n.get_collection_of_primitive_values(str)),
            "isManagementRestricted": lambda n : setattr(self, 'is_management_restricted', n.get_bool_value()),
            "isResourceAccount": lambda n : setattr(self, 'is_resource_account', n.get_bool_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "joinedGroups": lambda n : setattr(self, 'joined_groups', n.get_collection_of_object_values(group.Group)),
            "joinedTeams": lambda n : setattr(self, 'joined_teams', n.get_collection_of_object_values(team.Team)),
            "lastPasswordChangeDateTime": lambda n : setattr(self, 'last_password_change_date_time', n.get_datetime_value()),
            "legalAgeGroupClassification": lambda n : setattr(self, 'legal_age_group_classification', n.get_str_value()),
            "licenseAssignmentStates": lambda n : setattr(self, 'license_assignment_states', n.get_collection_of_object_values(license_assignment_state.LicenseAssignmentState)),
            "licenseDetails": lambda n : setattr(self, 'license_details', n.get_collection_of_object_values(license_details.LicenseDetails)),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailboxSettings": lambda n : setattr(self, 'mailbox_settings', n.get_object_value(mailbox_settings.MailboxSettings)),
            "mailFolders": lambda n : setattr(self, 'mail_folders', n.get_collection_of_object_values(mail_folder.MailFolder)),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "managedAppRegistrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(managed_app_registration.ManagedAppRegistration)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(directory_object.DirectoryObject)),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(message.Message)),
            "mobileAppIntentAndStates": lambda n : setattr(self, 'mobile_app_intent_and_states', n.get_collection_of_object_values(mobile_app_intent_and_state.MobileAppIntentAndState)),
            "mobileAppTroubleshootingEvents": lambda n : setattr(self, 'mobile_app_troubleshooting_events', n.get_collection_of_object_values(mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent)),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "mySite": lambda n : setattr(self, 'my_site', n.get_str_value()),
            "notifications": lambda n : setattr(self, 'notifications', n.get_collection_of_object_values(notification.Notification)),
            "oauth2PermissionGrants": lambda n : setattr(self, 'oauth2_permission_grants', n.get_collection_of_object_values(o_auth2_permission_grant.OAuth2PermissionGrant)),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(onenote.Onenote)),
            "onlineMeetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(online_meeting.OnlineMeeting)),
            "onPremisesDistinguishedName": lambda n : setattr(self, 'on_premises_distinguished_name', n.get_str_value()),
            "onPremisesDomainName": lambda n : setattr(self, 'on_premises_domain_name', n.get_str_value()),
            "onPremisesExtensionAttributes": lambda n : setattr(self, 'on_premises_extension_attributes', n.get_object_value(on_premises_extension_attributes.OnPremisesExtensionAttributes)),
            "onPremisesImmutableId": lambda n : setattr(self, 'on_premises_immutable_id', n.get_str_value()),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesProvisioningErrors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(on_premises_provisioning_error.OnPremisesProvisioningError)),
            "onPremisesSamAccountName": lambda n : setattr(self, 'on_premises_sam_account_name', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "onPremisesUserPrincipalName": lambda n : setattr(self, 'on_premises_user_principal_name', n.get_str_value()),
            "otherMails": lambda n : setattr(self, 'other_mails', n.get_collection_of_primitive_values(str)),
            "outlook": lambda n : setattr(self, 'outlook', n.get_object_value(outlook_user.OutlookUser)),
            "ownedDevices": lambda n : setattr(self, 'owned_devices', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "ownedObjects": lambda n : setattr(self, 'owned_objects', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "passwordPolicies": lambda n : setattr(self, 'password_policies', n.get_str_value()),
            "passwordProfile": lambda n : setattr(self, 'password_profile', n.get_object_value(password_profile.PasswordProfile)),
            "pastProjects": lambda n : setattr(self, 'past_projects', n.get_collection_of_primitive_values(str)),
            "pendingAccessReviewInstances": lambda n : setattr(self, 'pending_access_review_instances', n.get_collection_of_object_values(access_review_instance.AccessReviewInstance)),
            "people": lambda n : setattr(self, 'people', n.get_collection_of_object_values(person.Person)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(profile_photo.ProfilePhoto)),
            "photos": lambda n : setattr(self, 'photos', n.get_collection_of_object_values(profile_photo.ProfilePhoto)),
            "planner": lambda n : setattr(self, 'planner', n.get_object_value(planner_user.PlannerUser)),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "preferredDataLocation": lambda n : setattr(self, 'preferred_data_location', n.get_str_value()),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "preferredName": lambda n : setattr(self, 'preferred_name', n.get_str_value()),
            "presence": lambda n : setattr(self, 'presence', n.get_object_value(presence.Presence)),
            "print": lambda n : setattr(self, 'print', n.get_object_value(user_print.UserPrint)),
            "profile": lambda n : setattr(self, 'profile', n.get_object_value(profile.Profile)),
            "provisionedPlans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(provisioned_plan.ProvisionedPlan)),
            "proxyAddresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "refreshTokensValidFromDateTime": lambda n : setattr(self, 'refresh_tokens_valid_from_date_time', n.get_datetime_value()),
            "registeredDevices": lambda n : setattr(self, 'registered_devices', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "responsibilities": lambda n : setattr(self, 'responsibilities', n.get_collection_of_primitive_values(str)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_primitive_values(str)),
            "scopedRoleMemberOf": lambda n : setattr(self, 'scoped_role_member_of', n.get_collection_of_object_values(scoped_role_membership.ScopedRoleMembership)),
            "security": lambda n : setattr(self, 'security', n.get_object_value(security.Security)),
            "securityIdentifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
            "serviceProvisioningErrors": lambda n : setattr(self, 'service_provisioning_errors', n.get_collection_of_object_values(service_provisioning_error.ServiceProvisioningError)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(user_settings.UserSettings)),
            "showInAddressList": lambda n : setattr(self, 'show_in_address_list', n.get_bool_value()),
            "signInActivity": lambda n : setattr(self, 'sign_in_activity', n.get_object_value(sign_in_activity.SignInActivity)),
            "signInSessionsValidFromDateTime": lambda n : setattr(self, 'sign_in_sessions_valid_from_date_time', n.get_datetime_value()),
            "skills": lambda n : setattr(self, 'skills', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "streetAddress": lambda n : setattr(self, 'street_address', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "teamwork": lambda n : setattr(self, 'teamwork', n.get_object_value(user_teamwork.UserTeamwork)),
            "todo": lambda n : setattr(self, 'todo', n.get_object_value(todo.Todo)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "transitiveReports": lambda n : setattr(self, 'transitive_reports', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "usageLocation": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "usageRights": lambda n : setattr(self, 'usage_rights', n.get_collection_of_object_values(usage_right.UsageRight)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_str_value()),
            "windowsInformationProtectionDeviceRegistrations": lambda n : setattr(self, 'windows_information_protection_device_registrations', n.get_collection_of_object_values(windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The given name (first name) of the user. Maximum length is 64 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The given name (first name) of the user. Maximum length is 64 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the given_name property.
        """
        self._given_name = value
    
    @property
    def hire_date(self,) -> Optional[datetime]:
        """
        Gets the hireDate property value. The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Returned only on $select.  Note: This property is specific to SharePoint Online. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.
        Returns: Optional[datetime]
        """
        return self._hire_date
    
    @hire_date.setter
    def hire_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the hireDate property value. The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Returned only on $select.  Note: This property is specific to SharePoint Online. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.
        Args:
            value: Value to set for the hire_date property.
        """
        self._hire_date = value
    
    @property
    def identities(self,) -> Optional[List[object_identity.ObjectIdentity]]:
        """
        Gets the identities property value. Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Supports $filter (eq) including on null values, only where the signInType is not userPrincipalName.
        Returns: Optional[List[object_identity.ObjectIdentity]]
        """
        return self._identities
    
    @identities.setter
    def identities(self,value: Optional[List[object_identity.ObjectIdentity]] = None) -> None:
        """
        Sets the identities property value. Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Supports $filter (eq) including on null values, only where the signInType is not userPrincipalName.
        Args:
            value: Value to set for the identities property.
        """
        self._identities = value
    
    @property
    def im_addresses(self,) -> Optional[List[str]]:
        """
        Gets the imAddresses property value. The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._im_addresses
    
    @im_addresses.setter
    def im_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the imAddresses property value. The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the im_addresses property.
        """
        self._im_addresses = value
    
    @property
    def inference_classification(self,) -> Optional[inference_classification.InferenceClassification]:
        """
        Gets the inferenceClassification property value. Relevance classification of the user's messages based on explicit designations which override inferred relevance or importance.
        Returns: Optional[inference_classification.InferenceClassification]
        """
        return self._inference_classification
    
    @inference_classification.setter
    def inference_classification(self,value: Optional[inference_classification.InferenceClassification] = None) -> None:
        """
        Sets the inferenceClassification property value. Relevance classification of the user's messages based on explicit designations which override inferred relevance or importance.
        Args:
            value: Value to set for the inference_classification property.
        """
        self._inference_classification = value
    
    @property
    def info_catalogs(self,) -> Optional[List[str]]:
        """
        Gets the infoCatalogs property value. Identifies the info segments assigned to the user.  Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._info_catalogs
    
    @info_catalogs.setter
    def info_catalogs(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the infoCatalogs property value. Identifies the info segments assigned to the user.  Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the info_catalogs property.
        """
        self._info_catalogs = value
    
    @property
    def information_protection(self,) -> Optional[information_protection.InformationProtection]:
        """
        Gets the informationProtection property value. The informationProtection property
        Returns: Optional[information_protection.InformationProtection]
        """
        return self._information_protection
    
    @information_protection.setter
    def information_protection(self,value: Optional[information_protection.InformationProtection] = None) -> None:
        """
        Sets the informationProtection property value. The informationProtection property
        Args:
            value: Value to set for the information_protection property.
        """
        self._information_protection = value
    
    @property
    def insights(self,) -> Optional[item_insights.ItemInsights]:
        """
        Gets the insights property value. The insights property
        Returns: Optional[item_insights.ItemInsights]
        """
        return self._insights
    
    @insights.setter
    def insights(self,value: Optional[item_insights.ItemInsights] = None) -> None:
        """
        Sets the insights property value. The insights property
        Args:
            value: Value to set for the insights property.
        """
        self._insights = value
    
    @property
    def interests(self,) -> Optional[List[str]]:
        """
        Gets the interests property value. A list for the user to describe their interests. Returned only on $select.
        Returns: Optional[List[str]]
        """
        return self._interests
    
    @interests.setter
    def interests(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the interests property value. A list for the user to describe their interests. Returned only on $select.
        Args:
            value: Value to set for the interests property.
        """
        self._interests = value
    
    @property
    def is_management_restricted(self,) -> Optional[bool]:
        """
        Gets the isManagementRestricted property value. The isManagementRestricted property
        Returns: Optional[bool]
        """
        return self._is_management_restricted
    
    @is_management_restricted.setter
    def is_management_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManagementRestricted property value. The isManagementRestricted property
        Args:
            value: Value to set for the is_management_restricted property.
        """
        self._is_management_restricted = value
    
    @property
    def is_resource_account(self,) -> Optional[bool]:
        """
        Gets the isResourceAccount property value. Do not use – reserved for future use.
        Returns: Optional[bool]
        """
        return self._is_resource_account
    
    @is_resource_account.setter
    def is_resource_account(self,value: Optional[bool] = None) -> None:
        """
        Sets the isResourceAccount property value. Do not use – reserved for future use.
        Args:
            value: Value to set for the is_resource_account property.
        """
        self._is_resource_account = value
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. The user's job title. Maximum length is 128 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. The user's job title. Maximum length is 128 characters. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the job_title property.
        """
        self._job_title = value
    
    @property
    def joined_groups(self,) -> Optional[List[group.Group]]:
        """
        Gets the joinedGroups property value. The joinedGroups property
        Returns: Optional[List[group.Group]]
        """
        return self._joined_groups
    
    @joined_groups.setter
    def joined_groups(self,value: Optional[List[group.Group]] = None) -> None:
        """
        Sets the joinedGroups property value. The joinedGroups property
        Args:
            value: Value to set for the joined_groups property.
        """
        self._joined_groups = value
    
    @property
    def joined_teams(self,) -> Optional[List[team.Team]]:
        """
        Gets the joinedTeams property value. The Microsoft Teams teams that the user is a member of. Read-only. Nullable.
        Returns: Optional[List[team.Team]]
        """
        return self._joined_teams
    
    @joined_teams.setter
    def joined_teams(self,value: Optional[List[team.Team]] = None) -> None:
        """
        Sets the joinedTeams property value. The Microsoft Teams teams that the user is a member of. Read-only. Nullable.
        Args:
            value: Value to set for the joined_teams property.
        """
        self._joined_teams = value
    
    @property
    def last_password_change_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastPasswordChangeDateTime property value. The time when this Azure AD user last changed their password or when their password was created, , whichever date the latest action was performed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Returned only on $select.
        Returns: Optional[datetime]
        """
        return self._last_password_change_date_time
    
    @last_password_change_date_time.setter
    def last_password_change_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastPasswordChangeDateTime property value. The time when this Azure AD user last changed their password or when their password was created, , whichever date the latest action was performed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Returned only on $select.
        Args:
            value: Value to set for the last_password_change_date_time property.
        """
        self._last_password_change_date_time = value
    
    @property
    def legal_age_group_classification(self,) -> Optional[str]:
        """
        Gets the legalAgeGroupClassification property value. Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult and Adult. Refer to the legal age group property definitions for further information. Returned only on $select.
        Returns: Optional[str]
        """
        return self._legal_age_group_classification
    
    @legal_age_group_classification.setter
    def legal_age_group_classification(self,value: Optional[str] = None) -> None:
        """
        Sets the legalAgeGroupClassification property value. Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult and Adult. Refer to the legal age group property definitions for further information. Returned only on $select.
        Args:
            value: Value to set for the legal_age_group_classification property.
        """
        self._legal_age_group_classification = value
    
    @property
    def license_assignment_states(self,) -> Optional[List[license_assignment_state.LicenseAssignmentState]]:
        """
        Gets the licenseAssignmentStates property value. State of license assignments for this user. Also indicates licenses that are directly-assigned and those that the user has inherited through group memberships. Read-only. Returned only on $select.
        Returns: Optional[List[license_assignment_state.LicenseAssignmentState]]
        """
        return self._license_assignment_states
    
    @license_assignment_states.setter
    def license_assignment_states(self,value: Optional[List[license_assignment_state.LicenseAssignmentState]] = None) -> None:
        """
        Sets the licenseAssignmentStates property value. State of license assignments for this user. Also indicates licenses that are directly-assigned and those that the user has inherited through group memberships. Read-only. Returned only on $select.
        Args:
            value: Value to set for the license_assignment_states property.
        """
        self._license_assignment_states = value
    
    @property
    def license_details(self,) -> Optional[List[license_details.LicenseDetails]]:
        """
        Gets the licenseDetails property value. The licenseDetails property
        Returns: Optional[List[license_details.LicenseDetails]]
        """
        return self._license_details
    
    @license_details.setter
    def license_details(self,value: Optional[List[license_details.LicenseDetails]] = None) -> None:
        """
        Sets the licenseDetails property value. The licenseDetails property
        Args:
            value: Value to set for the license_details property.
        """
        self._license_details = value
    
    @property
    def mail(self,) -> Optional[str]:
        """
        Gets the mail property value. The SMTP address for the user, for example, admin@contoso.com. Changes to this property will also update the user's proxyAddresses collection to include the value as an SMTP address. This property cannot contain accent characters.  NOTE: We do not recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead.  Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._mail
    
    @mail.setter
    def mail(self,value: Optional[str] = None) -> None:
        """
        Sets the mail property value. The SMTP address for the user, for example, admin@contoso.com. Changes to this property will also update the user's proxyAddresses collection to include the value as an SMTP address. This property cannot contain accent characters.  NOTE: We do not recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead.  Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).
        Args:
            value: Value to set for the mail property.
        """
        self._mail = value
    
    @property
    def mail_folders(self,) -> Optional[List[mail_folder.MailFolder]]:
        """
        Gets the mailFolders property value. The user's mail folders. Read-only. Nullable.
        Returns: Optional[List[mail_folder.MailFolder]]
        """
        return self._mail_folders
    
    @mail_folders.setter
    def mail_folders(self,value: Optional[List[mail_folder.MailFolder]] = None) -> None:
        """
        Sets the mailFolders property value. The user's mail folders. Read-only. Nullable.
        Args:
            value: Value to set for the mail_folders property.
        """
        self._mail_folders = value
    
    @property
    def mail_nickname(self,) -> Optional[str]:
        """
        Gets the mailNickname property value. The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._mail_nickname
    
    @mail_nickname.setter
    def mail_nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the mailNickname property value. The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the mail_nickname property.
        """
        self._mail_nickname = value
    
    @property
    def mailbox_settings(self,) -> Optional[mailbox_settings.MailboxSettings]:
        """
        Gets the mailboxSettings property value. Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. For more information, see User preferences for languages and regional formats. Returned only on $select.
        Returns: Optional[mailbox_settings.MailboxSettings]
        """
        return self._mailbox_settings
    
    @mailbox_settings.setter
    def mailbox_settings(self,value: Optional[mailbox_settings.MailboxSettings] = None) -> None:
        """
        Sets the mailboxSettings property value. Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. For more information, see User preferences for languages and regional formats. Returned only on $select.
        Args:
            value: Value to set for the mailbox_settings property.
        """
        self._mailbox_settings = value
    
    @property
    def managed_app_registrations(self,) -> Optional[List[managed_app_registration.ManagedAppRegistration]]:
        """
        Gets the managedAppRegistrations property value. Zero or more managed app registrations that belong to the user.
        Returns: Optional[List[managed_app_registration.ManagedAppRegistration]]
        """
        return self._managed_app_registrations
    
    @managed_app_registrations.setter
    def managed_app_registrations(self,value: Optional[List[managed_app_registration.ManagedAppRegistration]] = None) -> None:
        """
        Sets the managedAppRegistrations property value. Zero or more managed app registrations that belong to the user.
        Args:
            value: Value to set for the managed_app_registrations property.
        """
        self._managed_app_registrations = value
    
    @property
    def managed_devices(self,) -> Optional[List[managed_device.ManagedDevice]]:
        """
        Gets the managedDevices property value. The managed devices associated with the user.
        Returns: Optional[List[managed_device.ManagedDevice]]
        """
        return self._managed_devices
    
    @managed_devices.setter
    def managed_devices(self,value: Optional[List[managed_device.ManagedDevice]] = None) -> None:
        """
        Sets the managedDevices property value. The managed devices associated with the user.
        Args:
            value: Value to set for the managed_devices property.
        """
        self._managed_devices = value
    
    @property
    def manager(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the manager property value. The user or contact that is this user's manager. Read-only. (HTTP Methods: GET, PUT, DELETE.). Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._manager
    
    @manager.setter
    def manager(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the manager property value. The user or contact that is this user's manager. Read-only. (HTTP Methods: GET, PUT, DELETE.). Supports $expand.
        Args:
            value: Value to set for the manager property.
        """
        self._manager = value
    
    @property
    def member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the memberOf property value. The groups, directory roles and administrative units that the user is a member of. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the memberOf property value. The groups, directory roles and administrative units that the user is a member of. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the member_of property.
        """
        self._member_of = value
    
    @property
    def messages(self,) -> Optional[List[message.Message]]:
        """
        Gets the messages property value. The messages in a mailbox or folder. Read-only. Nullable.
        Returns: Optional[List[message.Message]]
        """
        return self._messages
    
    @messages.setter
    def messages(self,value: Optional[List[message.Message]] = None) -> None:
        """
        Sets the messages property value. The messages in a mailbox or folder. Read-only. Nullable.
        Args:
            value: Value to set for the messages property.
        """
        self._messages = value
    
    @property
    def mobile_app_intent_and_states(self,) -> Optional[List[mobile_app_intent_and_state.MobileAppIntentAndState]]:
        """
        Gets the mobileAppIntentAndStates property value. The list of troubleshooting events for this user.
        Returns: Optional[List[mobile_app_intent_and_state.MobileAppIntentAndState]]
        """
        return self._mobile_app_intent_and_states
    
    @mobile_app_intent_and_states.setter
    def mobile_app_intent_and_states(self,value: Optional[List[mobile_app_intent_and_state.MobileAppIntentAndState]] = None) -> None:
        """
        Sets the mobileAppIntentAndStates property value. The list of troubleshooting events for this user.
        Args:
            value: Value to set for the mobile_app_intent_and_states property.
        """
        self._mobile_app_intent_and_states = value
    
    @property
    def mobile_app_troubleshooting_events(self,) -> Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]]:
        """
        Gets the mobileAppTroubleshootingEvents property value. The list of mobile app troubleshooting events for this user.
        Returns: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]]
        """
        return self._mobile_app_troubleshooting_events
    
    @mobile_app_troubleshooting_events.setter
    def mobile_app_troubleshooting_events(self,value: Optional[List[mobile_app_troubleshooting_event.MobileAppTroubleshootingEvent]] = None) -> None:
        """
        Sets the mobileAppTroubleshootingEvents property value. The list of mobile app troubleshooting events for this user.
        Args:
            value: Value to set for the mobile_app_troubleshooting_events property.
        """
        self._mobile_app_troubleshooting_events = value
    
    @property
    def mobile_phone(self,) -> Optional[str]:
        """
        Gets the mobilePhone property value. The primary cellular telephone number for the user. Read-only for users synced from on-premises directory.  Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._mobile_phone
    
    @mobile_phone.setter
    def mobile_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the mobilePhone property value. The primary cellular telephone number for the user. Read-only for users synced from on-premises directory.  Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the mobile_phone property.
        """
        self._mobile_phone = value
    
    @property
    def my_site(self,) -> Optional[str]:
        """
        Gets the mySite property value. The URL for the user's personal site. Returned only on $select.
        Returns: Optional[str]
        """
        return self._my_site
    
    @my_site.setter
    def my_site(self,value: Optional[str] = None) -> None:
        """
        Sets the mySite property value. The URL for the user's personal site. Returned only on $select.
        Args:
            value: Value to set for the my_site property.
        """
        self._my_site = value
    
    @property
    def notifications(self,) -> Optional[List[notification.Notification]]:
        """
        Gets the notifications property value. The notifications property
        Returns: Optional[List[notification.Notification]]
        """
        return self._notifications
    
    @notifications.setter
    def notifications(self,value: Optional[List[notification.Notification]] = None) -> None:
        """
        Sets the notifications property value. The notifications property
        Args:
            value: Value to set for the notifications property.
        """
        self._notifications = value
    
    @property
    def oauth2_permission_grants(self,) -> Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]]:
        """
        Gets the oauth2PermissionGrants property value. The oauth2PermissionGrants property
        Returns: Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]]
        """
        return self._oauth2_permission_grants
    
    @oauth2_permission_grants.setter
    def oauth2_permission_grants(self,value: Optional[List[o_auth2_permission_grant.OAuth2PermissionGrant]] = None) -> None:
        """
        Sets the oauth2PermissionGrants property value. The oauth2PermissionGrants property
        Args:
            value: Value to set for the oauth2_permission_grants property.
        """
        self._oauth2_permission_grants = value
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. The office location in the user's place of business. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. The office location in the user's place of business. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the office_location property.
        """
        self._office_location = value
    
    @property
    def on_premises_distinguished_name(self,) -> Optional[str]:
        """
        Gets the onPremisesDistinguishedName property value. Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.
        Returns: Optional[str]
        """
        return self._on_premises_distinguished_name
    
    @on_premises_distinguished_name.setter
    def on_premises_distinguished_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesDistinguishedName property value. Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.
        Args:
            value: Value to set for the on_premises_distinguished_name property.
        """
        self._on_premises_distinguished_name = value
    
    @property
    def on_premises_domain_name(self,) -> Optional[str]:
        """
        Gets the onPremisesDomainName property value. Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.
        Returns: Optional[str]
        """
        return self._on_premises_domain_name
    
    @on_premises_domain_name.setter
    def on_premises_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesDomainName property value. Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only.
        Args:
            value: Value to set for the on_premises_domain_name property.
        """
        self._on_premises_domain_name = value
    
    @property
    def on_premises_extension_attributes(self,) -> Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes]:
        """
        Gets the onPremisesExtensionAttributes property value. Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Supports $filter (eq, ne, not, in).
        Returns: Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes]
        """
        return self._on_premises_extension_attributes
    
    @on_premises_extension_attributes.setter
    def on_premises_extension_attributes(self,value: Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes] = None) -> None:
        """
        Sets the onPremisesExtensionAttributes property value. Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Supports $filter (eq, ne, not, in).
        Args:
            value: Value to set for the on_premises_extension_attributes property.
        """
        self._on_premises_extension_attributes = value
    
    @property
    def on_premises_immutable_id(self,) -> Optional[str]:
        """
        Gets the onPremisesImmutableId property value. This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user's userPrincipalName (UPN) property. Note: The $ and _ characters cannot be used when specifying this property. Supports $filter (eq, ne, not, ge, le, in).
        Returns: Optional[str]
        """
        return self._on_premises_immutable_id
    
    @on_premises_immutable_id.setter
    def on_premises_immutable_id(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesImmutableId property value. This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user's userPrincipalName (UPN) property. Note: The $ and _ characters cannot be used when specifying this property. Supports $filter (eq, ne, not, ge, le, in).
        Args:
            value: Value to set for the on_premises_immutable_id property.
        """
        self._on_premises_immutable_id = value
    
    @property
    def on_premises_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the onPremisesLastSyncDateTime property value. Indicates the last time at which the object was synced with the on-premises directory; for example: '2013-02-16T03:04:54Z'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Returns: Optional[datetime]
        """
        return self._on_premises_last_sync_date_time
    
    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onPremisesLastSyncDateTime property value. Indicates the last time at which the object was synced with the on-premises directory; for example: '2013-02-16T03:04:54Z'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Args:
            value: Value to set for the on_premises_last_sync_date_time property.
        """
        self._on_premises_last_sync_date_time = value
    
    @property
    def on_premises_provisioning_errors(self,) -> Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]]:
        """
        Gets the onPremisesProvisioningErrors property value. Errors when using Microsoft synchronization product during provisioning.  Supports $filter (eq, not, ge, le).
        Returns: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]]
        """
        return self._on_premises_provisioning_errors
    
    @on_premises_provisioning_errors.setter
    def on_premises_provisioning_errors(self,value: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]] = None) -> None:
        """
        Sets the onPremisesProvisioningErrors property value. Errors when using Microsoft synchronization product during provisioning.  Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the on_premises_provisioning_errors property.
        """
        self._on_premises_provisioning_errors = value
    
    @property
    def on_premises_sam_account_name(self,) -> Optional[str]:
        """
        Gets the onPremisesSamAccountName property value. Contains the on-premises sAMAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        Returns: Optional[str]
        """
        return self._on_premises_sam_account_name
    
    @on_premises_sam_account_name.setter
    def on_premises_sam_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSamAccountName property value. Contains the on-premises sAMAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        Args:
            value: Value to set for the on_premises_sam_account_name property.
        """
        self._on_premises_sam_account_name = value
    
    @property
    def on_premises_security_identifier(self,) -> Optional[str]:
        """
        Gets the onPremisesSecurityIdentifier property value. Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Supports $filter (eq including on null values).
        Returns: Optional[str]
        """
        return self._on_premises_security_identifier
    
    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSecurityIdentifier property value. Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Supports $filter (eq including on null values).
        Args:
            value: Value to set for the on_premises_security_identifier property.
        """
        self._on_premises_security_identifier = value
    
    @property
    def on_premises_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the onPremisesSyncEnabled property value. true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Azure Active Directory (Azure AD). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Returns: Optional[bool]
        """
        return self._on_premises_sync_enabled
    
    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onPremisesSyncEnabled property value. true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Azure Active Directory (Azure AD). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Args:
            value: Value to set for the on_premises_sync_enabled property.
        """
        self._on_premises_sync_enabled = value
    
    @property
    def on_premises_user_principal_name(self,) -> Optional[str]:
        """
        Gets the onPremisesUserPrincipalName property value. Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        Returns: Optional[str]
        """
        return self._on_premises_user_principal_name
    
    @on_premises_user_principal_name.setter
    def on_premises_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesUserPrincipalName property value. Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        Args:
            value: Value to set for the on_premises_user_principal_name property.
        """
        self._on_premises_user_principal_name = value
    
    @property
    def onenote(self,) -> Optional[onenote.Onenote]:
        """
        Gets the onenote property value. The onenote property
        Returns: Optional[onenote.Onenote]
        """
        return self._onenote
    
    @onenote.setter
    def onenote(self,value: Optional[onenote.Onenote] = None) -> None:
        """
        Sets the onenote property value. The onenote property
        Args:
            value: Value to set for the onenote property.
        """
        self._onenote = value
    
    @property
    def online_meetings(self,) -> Optional[List[online_meeting.OnlineMeeting]]:
        """
        Gets the onlineMeetings property value. The onlineMeetings property
        Returns: Optional[List[online_meeting.OnlineMeeting]]
        """
        return self._online_meetings
    
    @online_meetings.setter
    def online_meetings(self,value: Optional[List[online_meeting.OnlineMeeting]] = None) -> None:
        """
        Sets the onlineMeetings property value. The onlineMeetings property
        Args:
            value: Value to set for the online_meetings property.
        """
        self._online_meetings = value
    
    @property
    def other_mails(self,) -> Optional[List[str]]:
        """
        Gets the otherMails property value. A list of additional email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com'].NOTE: This property cannot contain accent characters.Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).
        Returns: Optional[List[str]]
        """
        return self._other_mails
    
    @other_mails.setter
    def other_mails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the otherMails property value. A list of additional email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com'].NOTE: This property cannot contain accent characters.Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the other_mails property.
        """
        self._other_mails = value
    
    @property
    def outlook(self,) -> Optional[outlook_user.OutlookUser]:
        """
        Gets the outlook property value. Selective Outlook services available to the user. Read-only. Nullable.
        Returns: Optional[outlook_user.OutlookUser]
        """
        return self._outlook
    
    @outlook.setter
    def outlook(self,value: Optional[outlook_user.OutlookUser] = None) -> None:
        """
        Sets the outlook property value. Selective Outlook services available to the user. Read-only. Nullable.
        Args:
            value: Value to set for the outlook property.
        """
        self._outlook = value
    
    @property
    def owned_devices(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the ownedDevices property value. Devices that are owned by the user. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owned_devices
    
    @owned_devices.setter
    def owned_devices(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the ownedDevices property value. Devices that are owned by the user. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the owned_devices property.
        """
        self._owned_devices = value
    
    @property
    def owned_objects(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the ownedObjects property value. Directory objects that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owned_objects
    
    @owned_objects.setter
    def owned_objects(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the ownedObjects property value. Directory objects that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Args:
            value: Value to set for the owned_objects property.
        """
        self._owned_objects = value
    
    @property
    def password_policies(self,) -> Optional[str]:
        """
        Gets the passwordPolicies property value. Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two may be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. For more information on the default password policies, see Azure AD pasword policies. Supports $filter (ne, not, and eq on null values).
        Returns: Optional[str]
        """
        return self._password_policies
    
    @password_policies.setter
    def password_policies(self,value: Optional[str] = None) -> None:
        """
        Sets the passwordPolicies property value. Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two may be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. For more information on the default password policies, see Azure AD pasword policies. Supports $filter (ne, not, and eq on null values).
        Args:
            value: Value to set for the password_policies property.
        """
        self._password_policies = value
    
    @property
    def password_profile(self,) -> Optional[password_profile.PasswordProfile]:
        """
        Gets the passwordProfile property value. Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Supports $filter (eq, ne, not, in, and eq on null values).
        Returns: Optional[password_profile.PasswordProfile]
        """
        return self._password_profile
    
    @password_profile.setter
    def password_profile(self,value: Optional[password_profile.PasswordProfile] = None) -> None:
        """
        Sets the passwordProfile property value. Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Supports $filter (eq, ne, not, in, and eq on null values).
        Args:
            value: Value to set for the password_profile property.
        """
        self._password_profile = value
    
    @property
    def past_projects(self,) -> Optional[List[str]]:
        """
        Gets the pastProjects property value. A list for the user to enumerate their past projects. Returned only on $select.
        Returns: Optional[List[str]]
        """
        return self._past_projects
    
    @past_projects.setter
    def past_projects(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the pastProjects property value. A list for the user to enumerate their past projects. Returned only on $select.
        Args:
            value: Value to set for the past_projects property.
        """
        self._past_projects = value
    
    @property
    def pending_access_review_instances(self,) -> Optional[List[access_review_instance.AccessReviewInstance]]:
        """
        Gets the pendingAccessReviewInstances property value. Navigation property to get list of access reviews pending approval by reviewer.
        Returns: Optional[List[access_review_instance.AccessReviewInstance]]
        """
        return self._pending_access_review_instances
    
    @pending_access_review_instances.setter
    def pending_access_review_instances(self,value: Optional[List[access_review_instance.AccessReviewInstance]] = None) -> None:
        """
        Sets the pendingAccessReviewInstances property value. Navigation property to get list of access reviews pending approval by reviewer.
        Args:
            value: Value to set for the pending_access_review_instances property.
        """
        self._pending_access_review_instances = value
    
    @property
    def people(self,) -> Optional[List[person.Person]]:
        """
        Gets the people property value. Read-only. The most relevant people to the user. The collection is ordered by their relevance to the user, which is determined by the user's communication, collaboration and business relationships. A person is an aggregation of information from across mail, contacts and social networks.
        Returns: Optional[List[person.Person]]
        """
        return self._people
    
    @people.setter
    def people(self,value: Optional[List[person.Person]] = None) -> None:
        """
        Sets the people property value. Read-only. The most relevant people to the user. The collection is ordered by their relevance to the user, which is determined by the user's communication, collaboration and business relationships. A person is an aggregation of information from across mail, contacts and social networks.
        Args:
            value: Value to set for the people property.
        """
        self._people = value
    
    @property
    def photo(self,) -> Optional[profile_photo.ProfilePhoto]:
        """
        Gets the photo property value. The user's profile photo. Read-only.
        Returns: Optional[profile_photo.ProfilePhoto]
        """
        return self._photo
    
    @photo.setter
    def photo(self,value: Optional[profile_photo.ProfilePhoto] = None) -> None:
        """
        Sets the photo property value. The user's profile photo. Read-only.
        Args:
            value: Value to set for the photo property.
        """
        self._photo = value
    
    @property
    def photos(self,) -> Optional[List[profile_photo.ProfilePhoto]]:
        """
        Gets the photos property value. The photos property
        Returns: Optional[List[profile_photo.ProfilePhoto]]
        """
        return self._photos
    
    @photos.setter
    def photos(self,value: Optional[List[profile_photo.ProfilePhoto]] = None) -> None:
        """
        Sets the photos property value. The photos property
        Args:
            value: Value to set for the photos property.
        """
        self._photos = value
    
    @property
    def planner(self,) -> Optional[planner_user.PlannerUser]:
        """
        Gets the planner property value. Selective Planner services available to the user. Read-only. Nullable.
        Returns: Optional[planner_user.PlannerUser]
        """
        return self._planner
    
    @planner.setter
    def planner(self,value: Optional[planner_user.PlannerUser] = None) -> None:
        """
        Sets the planner property value. Selective Planner services available to the user. Read-only. Nullable.
        Args:
            value: Value to set for the planner property.
        """
        self._planner = value
    
    @property
    def postal_code(self,) -> Optional[str]:
        """
        Gets the postalCode property value. The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self,value: Optional[str] = None) -> None:
        """
        Sets the postalCode property value. The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the postal_code property.
        """
        self._postal_code = value
    
    @property
    def preferred_data_location(self,) -> Optional[str]:
        """
        Gets the preferredDataLocation property value. The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.
        Returns: Optional[str]
        """
        return self._preferred_data_location
    
    @preferred_data_location.setter
    def preferred_data_location(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredDataLocation property value. The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.
        Args:
            value: Value to set for the preferred_data_location property.
        """
        self._preferred_data_location = value
    
    @property
    def preferred_language(self,) -> Optional[str]:
        """
        Gets the preferredLanguage property value. The preferred language for the user. Should follow ISO 639-1 Code; for example en-US. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._preferred_language
    
    @preferred_language.setter
    def preferred_language(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredLanguage property value. The preferred language for the user. Should follow ISO 639-1 Code; for example en-US. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the preferred_language property.
        """
        self._preferred_language = value
    
    @property
    def preferred_name(self,) -> Optional[str]:
        """
        Gets the preferredName property value. The preferred name for the user. Not Supported. This attribute returns an empty string.Returned only on $select.
        Returns: Optional[str]
        """
        return self._preferred_name
    
    @preferred_name.setter
    def preferred_name(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredName property value. The preferred name for the user. Not Supported. This attribute returns an empty string.Returned only on $select.
        Args:
            value: Value to set for the preferred_name property.
        """
        self._preferred_name = value
    
    @property
    def presence(self,) -> Optional[presence.Presence]:
        """
        Gets the presence property value. The presence property
        Returns: Optional[presence.Presence]
        """
        return self._presence
    
    @presence.setter
    def presence(self,value: Optional[presence.Presence] = None) -> None:
        """
        Sets the presence property value. The presence property
        Args:
            value: Value to set for the presence property.
        """
        self._presence = value
    
    @property
    def print(self,) -> Optional[user_print.UserPrint]:
        """
        Gets the print property value. The print property
        Returns: Optional[user_print.UserPrint]
        """
        return self._print
    
    @print.setter
    def print(self,value: Optional[user_print.UserPrint] = None) -> None:
        """
        Sets the print property value. The print property
        Args:
            value: Value to set for the print property.
        """
        self._print = value
    
    @property
    def profile(self,) -> Optional[profile.Profile]:
        """
        Gets the profile property value. Represents properties that are descriptive of a user in a tenant.
        Returns: Optional[profile.Profile]
        """
        return self._profile
    
    @profile.setter
    def profile(self,value: Optional[profile.Profile] = None) -> None:
        """
        Sets the profile property value. Represents properties that are descriptive of a user in a tenant.
        Args:
            value: Value to set for the profile property.
        """
        self._profile = value
    
    @property
    def provisioned_plans(self,) -> Optional[List[provisioned_plan.ProvisionedPlan]]:
        """
        Gets the provisionedPlans property value. The plans that are provisioned for the user. Read-only. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[provisioned_plan.ProvisionedPlan]]
        """
        return self._provisioned_plans
    
    @provisioned_plans.setter
    def provisioned_plans(self,value: Optional[List[provisioned_plan.ProvisionedPlan]] = None) -> None:
        """
        Sets the provisionedPlans property value. The plans that are provisioned for the user. Read-only. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the provisioned_plans property.
        """
        self._provisioned_plans = value
    
    @property
    def proxy_addresses(self,) -> Optional[List[str]]:
        """
        Gets the proxyAddresses property value. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property will also update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address while those prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of ten unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
        Returns: Optional[List[str]]
        """
        return self._proxy_addresses
    
    @proxy_addresses.setter
    def proxy_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the proxyAddresses property value. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property will also update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address while those prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of ten unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the proxy_addresses property.
        """
        self._proxy_addresses = value
    
    @property
    def refresh_tokens_valid_from_date_time(self,) -> Optional[datetime]:
        """
        Gets the refreshTokensValidFromDateTime property value. Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use invalidateAllRefreshTokens to reset.
        Returns: Optional[datetime]
        """
        return self._refresh_tokens_valid_from_date_time
    
    @refresh_tokens_valid_from_date_time.setter
    def refresh_tokens_valid_from_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the refreshTokensValidFromDateTime property value. Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use invalidateAllRefreshTokens to reset.
        Args:
            value: Value to set for the refresh_tokens_valid_from_date_time property.
        """
        self._refresh_tokens_valid_from_date_time = value
    
    @property
    def registered_devices(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the registeredDevices property value. Devices that are registered for the user. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._registered_devices
    
    @registered_devices.setter
    def registered_devices(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the registeredDevices property value. Devices that are registered for the user. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the registered_devices property.
        """
        self._registered_devices = value
    
    @property
    def responsibilities(self,) -> Optional[List[str]]:
        """
        Gets the responsibilities property value. A list for the user to enumerate their responsibilities. Returned only on $select.
        Returns: Optional[List[str]]
        """
        return self._responsibilities
    
    @responsibilities.setter
    def responsibilities(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the responsibilities property value. A list for the user to enumerate their responsibilities. Returned only on $select.
        Args:
            value: Value to set for the responsibilities property.
        """
        self._responsibilities = value
    
    @property
    def schools(self,) -> Optional[List[str]]:
        """
        Gets the schools property value. A list for the user to enumerate the schools they have attended. Returned only on $select.
        Returns: Optional[List[str]]
        """
        return self._schools
    
    @schools.setter
    def schools(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the schools property value. A list for the user to enumerate the schools they have attended. Returned only on $select.
        Args:
            value: Value to set for the schools property.
        """
        self._schools = value
    
    @property
    def scoped_role_member_of(self,) -> Optional[List[scoped_role_membership.ScopedRoleMembership]]:
        """
        Gets the scopedRoleMemberOf property value. The scoped-role administrative unit memberships for this user. Read-only. Nullable.
        Returns: Optional[List[scoped_role_membership.ScopedRoleMembership]]
        """
        return self._scoped_role_member_of
    
    @scoped_role_member_of.setter
    def scoped_role_member_of(self,value: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None) -> None:
        """
        Sets the scopedRoleMemberOf property value. The scoped-role administrative unit memberships for this user. Read-only. Nullable.
        Args:
            value: Value to set for the scoped_role_member_of property.
        """
        self._scoped_role_member_of = value
    
    @property
    def security(self,) -> Optional[security.Security]:
        """
        Gets the security property value. The security property
        Returns: Optional[security.Security]
        """
        return self._security
    
    @security.setter
    def security(self,value: Optional[security.Security] = None) -> None:
        """
        Sets the security property value. The security property
        Args:
            value: Value to set for the security property.
        """
        self._security = value
    
    @property
    def security_identifier(self,) -> Optional[str]:
        """
        Gets the securityIdentifier property value. Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).
        Returns: Optional[str]
        """
        return self._security_identifier
    
    @security_identifier.setter
    def security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the securityIdentifier property value. Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the security_identifier property.
        """
        self._security_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("aboutMe", self.about_me)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_str_value("ageGroup", self.age_group)
        writer.write_collection_of_object_values("agreementAcceptances", self.agreement_acceptances)
        writer.write_object_value("analytics", self.analytics)
        writer.write_collection_of_object_values("approvals", self.approvals)
        writer.write_collection_of_object_values("appConsentRequestsForApproval", self.app_consent_requests_for_approval)
        writer.write_collection_of_object_values("appRoleAssignedResources", self.app_role_assigned_resources)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_collection_of_object_values("assignedPlans", self.assigned_plans)
        writer.write_object_value("authentication", self.authentication)
        writer.write_object_value("authorizationInfo", self.authorization_info)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_collection_of_primitive_values("businessPhones", self.business_phones)
        writer.write_object_value("calendar", self.calendar)
        writer.write_collection_of_object_values("calendars", self.calendars)
        writer.write_collection_of_object_values("calendarGroups", self.calendar_groups)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_collection_of_object_values("chats", self.chats)
        writer.write_str_value("city", self.city)
        writer.write_collection_of_object_values("cloudPCs", self.cloud_p_cs)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("consentProvidedForMinor", self.consent_provided_for_minor)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_collection_of_object_values("contactFolders", self.contact_folders)
        writer.write_str_value("country", self.country)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("createdObjects", self.created_objects)
        writer.write_str_value("creationType", self.creation_type)
        writer.write_object_value("customSecurityAttributes", self.custom_security_attributes)
        writer.write_str_value("department", self.department)
        writer.write_collection_of_object_values("devices", self.devices)
        writer.write_collection_of_object_values("deviceEnrollmentConfigurations", self.device_enrollment_configurations)
        writer.write_int_value("deviceEnrollmentLimit", self.device_enrollment_limit)
        writer.write_collection_of_object_values("deviceKeys", self.device_keys)
        writer.write_collection_of_object_values("deviceManagementTroubleshootingEvents", self.device_management_troubleshooting_events)
        writer.write_collection_of_object_values("directReports", self.direct_reports)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_datetime_value("employeeHireDate", self.employee_hire_date)
        writer.write_str_value("employeeId", self.employee_id)
        writer.write_datetime_value("employeeLeaveDateTime", self.employee_leave_date_time)
        writer.write_object_value("employeeOrgData", self.employee_org_data)
        writer.write_str_value("employeeType", self.employee_type)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("externalUserState", self.external_user_state)
        writer.write_str_value("externalUserStateChangeDateTime", self.external_user_state_change_date_time)
        writer.write_str_value("faxNumber", self.fax_number)
        writer.write_collection_of_object_values("followedSites", self.followed_sites)
        writer.write_str_value("givenName", self.given_name)
        writer.write_datetime_value("hireDate", self.hire_date)
        writer.write_collection_of_object_values("identities", self.identities)
        writer.write_collection_of_primitive_values("imAddresses", self.im_addresses)
        writer.write_object_value("inferenceClassification", self.inference_classification)
        writer.write_object_value("informationProtection", self.information_protection)
        writer.write_collection_of_primitive_values("infoCatalogs", self.info_catalogs)
        writer.write_object_value("insights", self.insights)
        writer.write_collection_of_primitive_values("interests", self.interests)
        writer.write_bool_value("isManagementRestricted", self.is_management_restricted)
        writer.write_bool_value("isResourceAccount", self.is_resource_account)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_collection_of_object_values("joinedGroups", self.joined_groups)
        writer.write_collection_of_object_values("joinedTeams", self.joined_teams)
        writer.write_datetime_value("lastPasswordChangeDateTime", self.last_password_change_date_time)
        writer.write_str_value("legalAgeGroupClassification", self.legal_age_group_classification)
        writer.write_collection_of_object_values("licenseAssignmentStates", self.license_assignment_states)
        writer.write_collection_of_object_values("licenseDetails", self.license_details)
        writer.write_str_value("mail", self.mail)
        writer.write_object_value("mailboxSettings", self.mailbox_settings)
        writer.write_collection_of_object_values("mailFolders", self.mail_folders)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_collection_of_object_values("managedAppRegistrations", self.managed_app_registrations)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_collection_of_object_values("mobileAppIntentAndStates", self.mobile_app_intent_and_states)
        writer.write_collection_of_object_values("mobileAppTroubleshootingEvents", self.mobile_app_troubleshooting_events)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("mySite", self.my_site)
        writer.write_collection_of_object_values("notifications", self.notifications)
        writer.write_collection_of_object_values("oauth2PermissionGrants", self.oauth2_permission_grants)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_str_value("onPremisesDistinguishedName", self.on_premises_distinguished_name)
        writer.write_str_value("onPremisesDomainName", self.on_premises_domain_name)
        writer.write_object_value("onPremisesExtensionAttributes", self.on_premises_extension_attributes)
        writer.write_str_value("onPremisesImmutableId", self.on_premises_immutable_id)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_collection_of_object_values("onPremisesProvisioningErrors", self.on_premises_provisioning_errors)
        writer.write_str_value("onPremisesSamAccountName", self.on_premises_sam_account_name)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_str_value("onPremisesUserPrincipalName", self.on_premises_user_principal_name)
        writer.write_collection_of_primitive_values("otherMails", self.other_mails)
        writer.write_object_value("outlook", self.outlook)
        writer.write_collection_of_object_values("ownedDevices", self.owned_devices)
        writer.write_collection_of_object_values("ownedObjects", self.owned_objects)
        writer.write_str_value("passwordPolicies", self.password_policies)
        writer.write_object_value("passwordProfile", self.password_profile)
        writer.write_collection_of_primitive_values("pastProjects", self.past_projects)
        writer.write_collection_of_object_values("pendingAccessReviewInstances", self.pending_access_review_instances)
        writer.write_collection_of_object_values("people", self.people)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("photos", self.photos)
        writer.write_object_value("planner", self.planner)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("preferredDataLocation", self.preferred_data_location)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_str_value("preferredName", self.preferred_name)
        writer.write_object_value("presence", self.presence)
        writer.write_object_value("print", self.print)
        writer.write_object_value("profile", self.profile)
        writer.write_collection_of_object_values("provisionedPlans", self.provisioned_plans)
        writer.write_collection_of_primitive_values("proxyAddresses", self.proxy_addresses)
        writer.write_datetime_value("refreshTokensValidFromDateTime", self.refresh_tokens_valid_from_date_time)
        writer.write_collection_of_object_values("registeredDevices", self.registered_devices)
        writer.write_collection_of_primitive_values("responsibilities", self.responsibilities)
        writer.write_collection_of_primitive_values("schools", self.schools)
        writer.write_collection_of_object_values("scopedRoleMemberOf", self.scoped_role_member_of)
        writer.write_object_value("security", self.security)
        writer.write_str_value("securityIdentifier", self.security_identifier)
        writer.write_collection_of_object_values("serviceProvisioningErrors", self.service_provisioning_errors)
        writer.write_object_value("settings", self.settings)
        writer.write_bool_value("showInAddressList", self.show_in_address_list)
        writer.write_object_value("signInActivity", self.sign_in_activity)
        writer.write_datetime_value("signInSessionsValidFromDateTime", self.sign_in_sessions_valid_from_date_time)
        writer.write_collection_of_primitive_values("skills", self.skills)
        writer.write_str_value("state", self.state)
        writer.write_str_value("streetAddress", self.street_address)
        writer.write_str_value("surname", self.surname)
        writer.write_object_value("teamwork", self.teamwork)
        writer.write_object_value("todo", self.todo)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_collection_of_object_values("transitiveReports", self.transitive_reports)
        writer.write_str_value("usageLocation", self.usage_location)
        writer.write_collection_of_object_values("usageRights", self.usage_rights)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userType", self.user_type)
        writer.write_collection_of_object_values("windowsInformationProtectionDeviceRegistrations", self.windows_information_protection_device_registrations)
    
    @property
    def service_provisioning_errors(self,) -> Optional[List[service_provisioning_error.ServiceProvisioningError]]:
        """
        Gets the serviceProvisioningErrors property value. The serviceProvisioningErrors property
        Returns: Optional[List[service_provisioning_error.ServiceProvisioningError]]
        """
        return self._service_provisioning_errors
    
    @service_provisioning_errors.setter
    def service_provisioning_errors(self,value: Optional[List[service_provisioning_error.ServiceProvisioningError]] = None) -> None:
        """
        Sets the serviceProvisioningErrors property value. The serviceProvisioningErrors property
        Args:
            value: Value to set for the service_provisioning_errors property.
        """
        self._service_provisioning_errors = value
    
    @property
    def settings(self,) -> Optional[user_settings.UserSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[user_settings.UserSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[user_settings.UserSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def show_in_address_list(self,) -> Optional[bool]:
        """
        Gets the showInAddressList property value. Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.
        Returns: Optional[bool]
        """
        return self._show_in_address_list
    
    @show_in_address_list.setter
    def show_in_address_list(self,value: Optional[bool] = None) -> None:
        """
        Sets the showInAddressList property value. Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.
        Args:
            value: Value to set for the show_in_address_list property.
        """
        self._show_in_address_list = value
    
    @property
    def sign_in_activity(self,) -> Optional[sign_in_activity.SignInActivity]:
        """
        Gets the signInActivity property value. Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Returned only on $select. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note:  Details for this property require an Azure AD Premium P1/P2 license and the AuditLog.Read.All permission.When you specify $select=signInActivity or $filter=signInActivity while listing users, the maximum page size is 120 users. Requests with $top set higher than 120 will return pages with up to 120 users.This property is not returned for a user who has never signed in or last signed in before April 2020.
        Returns: Optional[sign_in_activity.SignInActivity]
        """
        return self._sign_in_activity
    
    @sign_in_activity.setter
    def sign_in_activity(self,value: Optional[sign_in_activity.SignInActivity] = None) -> None:
        """
        Sets the signInActivity property value. Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Returned only on $select. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note:  Details for this property require an Azure AD Premium P1/P2 license and the AuditLog.Read.All permission.When you specify $select=signInActivity or $filter=signInActivity while listing users, the maximum page size is 120 users. Requests with $top set higher than 120 will return pages with up to 120 users.This property is not returned for a user who has never signed in or last signed in before April 2020.
        Args:
            value: Value to set for the sign_in_activity property.
        """
        self._sign_in_activity = value
    
    @property
    def sign_in_sessions_valid_from_date_time(self,) -> Optional[datetime]:
        """
        Gets the signInSessionsValidFromDateTime property value. Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset.
        Returns: Optional[datetime]
        """
        return self._sign_in_sessions_valid_from_date_time
    
    @sign_in_sessions_valid_from_date_time.setter
    def sign_in_sessions_valid_from_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the signInSessionsValidFromDateTime property value. Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications will get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application will need to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset.
        Args:
            value: Value to set for the sign_in_sessions_valid_from_date_time property.
        """
        self._sign_in_sessions_valid_from_date_time = value
    
    @property
    def skills(self,) -> Optional[List[str]]:
        """
        Gets the skills property value. A list for the user to enumerate their skills. Returned only on $select.
        Returns: Optional[List[str]]
        """
        return self._skills
    
    @skills.setter
    def skills(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the skills property value. A list for the user to enumerate their skills. Returned only on $select.
        Args:
            value: Value to set for the skills property.
        """
        self._skills = value
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state or province in the user's address. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state or province in the user's address. Maximum length is 128 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def street_address(self,) -> Optional[str]:
        """
        Gets the streetAddress property value. The street address of the user's place of business. Maximum length is 1024 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._street_address
    
    @street_address.setter
    def street_address(self,value: Optional[str] = None) -> None:
        """
        Sets the streetAddress property value. The street address of the user's place of business. Maximum length is 1024 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the street_address property.
        """
        self._street_address = value
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The user's surname (family name or last name). Maximum length is 64 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The user's surname (family name or last name). Maximum length is 64 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def teamwork(self,) -> Optional[user_teamwork.UserTeamwork]:
        """
        Gets the teamwork property value. A container for Microsoft Teams features available for the user. Read-only. Nullable.
        Returns: Optional[user_teamwork.UserTeamwork]
        """
        return self._teamwork
    
    @teamwork.setter
    def teamwork(self,value: Optional[user_teamwork.UserTeamwork] = None) -> None:
        """
        Sets the teamwork property value. A container for Microsoft Teams features available for the user. Read-only. Nullable.
        Args:
            value: Value to set for the teamwork property.
        """
        self._teamwork = value
    
    @property
    def todo(self,) -> Optional[todo.Todo]:
        """
        Gets the todo property value. Represents the To Do services available to a user.
        Returns: Optional[todo.Todo]
        """
        return self._todo
    
    @todo.setter
    def todo(self,value: Optional[todo.Todo] = None) -> None:
        """
        Sets the todo property value. Represents the To Do services available to a user.
        Args:
            value: Value to set for the todo property.
        """
        self._todo = value
    
    @property
    def transitive_member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMemberOf property value. The groups, including nested groups, and directory roles that a user is a member of. Nullable.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_member_of
    
    @transitive_member_of.setter
    def transitive_member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMemberOf property value. The groups, including nested groups, and directory roles that a user is a member of. Nullable.
        Args:
            value: Value to set for the transitive_member_of property.
        """
        self._transitive_member_of = value
    
    @property
    def transitive_reports(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveReports property value. The transitive reports for a user. Read-only.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_reports
    
    @transitive_reports.setter
    def transitive_reports(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveReports property value. The transitive reports for a user. Read-only.
        Args:
            value: Value to set for the transitive_reports property.
        """
        self._transitive_reports = value
    
    @property
    def usage_location(self,) -> Optional[str]:
        """
        Gets the usageLocation property value. A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: US, JP, and GB. Not nullable. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._usage_location
    
    @usage_location.setter
    def usage_location(self,value: Optional[str] = None) -> None:
        """
        Sets the usageLocation property value. A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: US, JP, and GB. Not nullable. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the usage_location property.
        """
        self._usage_location = value
    
    @property
    def usage_rights(self,) -> Optional[List[usage_right.UsageRight]]:
        """
        Gets the usageRights property value. Represents the usage rights a user has been granted.
        Returns: Optional[List[usage_right.UsageRight]]
        """
        return self._usage_rights
    
    @usage_rights.setter
    def usage_rights(self,value: Optional[List[usage_right.UsageRight]] = None) -> None:
        """
        Sets the usageRights property value. Represents the usage rights a user has been granted.
        Args:
            value: Value to set for the usage_rights property.
        """
        self._usage_rights = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property cannot contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderBy.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property cannot contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderBy.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def user_type(self,) -> Optional[str]:
        """
        Gets the userType property value. A String value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for member and guest users, see What are the default user permissions in Azure Active Directory?
        Returns: Optional[str]
        """
        return self._user_type
    
    @user_type.setter
    def user_type(self,value: Optional[str] = None) -> None:
        """
        Sets the userType property value. A String value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for member and guest users, see What are the default user permissions in Azure Active Directory?
        Args:
            value: Value to set for the user_type property.
        """
        self._user_type = value
    
    @property
    def windows_information_protection_device_registrations(self,) -> Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]]:
        """
        Gets the windowsInformationProtectionDeviceRegistrations property value. Zero or more WIP device registrations that belong to the user.
        Returns: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]]
        """
        return self._windows_information_protection_device_registrations
    
    @windows_information_protection_device_registrations.setter
    def windows_information_protection_device_registrations(self,value: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]] = None) -> None:
        """
        Sets the windowsInformationProtectionDeviceRegistrations property value. Zero or more WIP device registrations that belong to the user.
        Args:
            value: Value to set for the windows_information_protection_device_registrations property.
        """
        self._windows_information_protection_device_registrations = value
    


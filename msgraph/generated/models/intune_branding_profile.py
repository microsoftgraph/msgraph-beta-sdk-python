from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

company_portal_blocked_action = lazy_import('msgraph.generated.models.company_portal_blocked_action')
enrollment_availability_options = lazy_import('msgraph.generated.models.enrollment_availability_options')
entity = lazy_import('msgraph.generated.models.entity')
intune_branding_profile_assignment = lazy_import('msgraph.generated.models.intune_branding_profile_assignment')
mime_content = lazy_import('msgraph.generated.models.mime_content')
rgb_color = lazy_import('msgraph.generated.models.rgb_color')

class IntuneBrandingProfile(entity.Entity):
    """
    This entity contains data which is used in customizing the tenant level appearance of the Company Portal applications as well as the end user web portal.
    """
    @property
    def assignments(self,) -> Optional[List[intune_branding_profile_assignment.IntuneBrandingProfileAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the branding profile
        Returns: Optional[List[intune_branding_profile_assignment.IntuneBrandingProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[intune_branding_profile_assignment.IntuneBrandingProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the branding profile
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def company_portal_blocked_actions(self,) -> Optional[List[company_portal_blocked_action.CompanyPortalBlockedAction]]:
        """
        Gets the companyPortalBlockedActions property value. Collection of blocked actions on the company portal as per platform and device ownership types.
        Returns: Optional[List[company_portal_blocked_action.CompanyPortalBlockedAction]]
        """
        return self._company_portal_blocked_actions
    
    @company_portal_blocked_actions.setter
    def company_portal_blocked_actions(self,value: Optional[List[company_portal_blocked_action.CompanyPortalBlockedAction]] = None) -> None:
        """
        Sets the companyPortalBlockedActions property value. Collection of blocked actions on the company portal as per platform and device ownership types.
        Args:
            value: Value to set for the companyPortalBlockedActions property.
        """
        self._company_portal_blocked_actions = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new intuneBrandingProfile and sets the default values.
        """
        super().__init__()
        # The list of group assignments for the branding profile
        self._assignments: Optional[List[intune_branding_profile_assignment.IntuneBrandingProfileAssignment]] = None
        # Collection of blocked actions on the company portal as per platform and device ownership types.
        self._company_portal_blocked_actions: Optional[List[company_portal_blocked_action.CompanyPortalBlockedAction]] = None
        # E-mail address of the person/organization responsible for IT support
        self._contact_i_t_email_address: Optional[str] = None
        # Name of the person/organization responsible for IT support
        self._contact_i_t_name: Optional[str] = None
        # Text comments regarding the person/organization responsible for IT support
        self._contact_i_t_notes: Optional[str] = None
        # Phone number of the person/organization responsible for IT support
        self._contact_i_t_phone_number: Optional[str] = None
        # Time when the BrandingProfile was created
        self._created_date_time: Optional[datetime] = None
        # Text comments regarding what the admin has access to on the device
        self._custom_can_see_privacy_message: Optional[str] = None
        # Text comments regarding what the admin doesn't have access to on the device
        self._custom_cant_see_privacy_message: Optional[str] = None
        # Text comments regarding what the admin doesn't have access to on the device
        self._custom_privacy_message: Optional[str] = None
        # Applies to telemetry sent from all clients to the Intune service. When disabled, all proactive troubleshooting and issue warnings within the client are turned off, and telemetry settings appear inactive or hidden to the device user.
        self._disable_client_telemetry: Optional[bool] = None
        # Company/organization name that is displayed to end users
        self._display_name: Optional[str] = None
        # Options available for enrollment flow customization
        self._enrollment_availability: Optional[enrollment_availability_options.EnrollmentAvailabilityOptions] = None
        # Boolean that represents whether the profile is used as default or not
        self._is_default_profile: Optional[bool] = None
        # Boolean that represents whether the adminsistrator has disabled the 'Factory Reset' action on corporate owned devices.
        self._is_factory_reset_disabled: Optional[bool] = None
        # Boolean that represents whether the adminsistrator has disabled the 'Remove Device' action on corporate owned devices.
        self._is_remove_device_disabled: Optional[bool] = None
        # Customized image displayed in Company Portal apps landing page
        self._landing_page_customized_image: Optional[mime_content.MimeContent] = None
        # Time when the BrandingProfile was last modified
        self._last_modified_date_time: Optional[datetime] = None
        # Logo image displayed in Company Portal apps which have a light background behind the logo
        self._light_background_logo: Optional[mime_content.MimeContent] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Display name of the company/organization’s IT helpdesk site
        self._online_support_site_name: Optional[str] = None
        # URL to the company/organization’s IT helpdesk site
        self._online_support_site_url: Optional[str] = None
        # URL to the company/organization’s privacy policy
        self._privacy_url: Optional[str] = None
        # Description of the profile
        self._profile_description: Optional[str] = None
        # Name of the profile
        self._profile_name: Optional[str] = None
        # List of scope tags assigned to the branding profile
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Boolean that indicates if a push notification is sent to users when their device ownership type changes from personal to corporate
        self._send_device_ownership_change_push_notification: Optional[bool] = None
        # Boolean that indicates if AzureAD Enterprise Apps will be shown in Company Portal
        self._show_azure_a_d_enterprise_apps: Optional[bool] = None
        # Boolean that indicates if Configuration Manager Apps will be shown in Company Portal
        self._show_configuration_manager_apps: Optional[bool] = None
        # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image or not
        self._show_display_name_next_to_logo: Optional[bool] = None
        # Boolean that represents whether the administrator-supplied logo images are shown or not
        self._show_logo: Optional[bool] = None
        # Boolean that indicates if Office WebApps will be shown in Company Portal
        self._show_office_web_apps: Optional[bool] = None
        # Primary theme color used in the Company Portal applications and web portal
        self._theme_color: Optional[rgb_color.RgbColor] = None
        # Logo image displayed in Company Portal apps which have a theme color background behind the logo
        self._theme_color_logo: Optional[mime_content.MimeContent] = None
    
    @property
    def contact_i_t_email_address(self,) -> Optional[str]:
        """
        Gets the contactITEmailAddress property value. E-mail address of the person/organization responsible for IT support
        Returns: Optional[str]
        """
        return self._contact_i_t_email_address
    
    @contact_i_t_email_address.setter
    def contact_i_t_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITEmailAddress property value. E-mail address of the person/organization responsible for IT support
        Args:
            value: Value to set for the contactITEmailAddress property.
        """
        self._contact_i_t_email_address = value
    
    @property
    def contact_i_t_name(self,) -> Optional[str]:
        """
        Gets the contactITName property value. Name of the person/organization responsible for IT support
        Returns: Optional[str]
        """
        return self._contact_i_t_name
    
    @contact_i_t_name.setter
    def contact_i_t_name(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITName property value. Name of the person/organization responsible for IT support
        Args:
            value: Value to set for the contactITName property.
        """
        self._contact_i_t_name = value
    
    @property
    def contact_i_t_notes(self,) -> Optional[str]:
        """
        Gets the contactITNotes property value. Text comments regarding the person/organization responsible for IT support
        Returns: Optional[str]
        """
        return self._contact_i_t_notes
    
    @contact_i_t_notes.setter
    def contact_i_t_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITNotes property value. Text comments regarding the person/organization responsible for IT support
        Args:
            value: Value to set for the contactITNotes property.
        """
        self._contact_i_t_notes = value
    
    @property
    def contact_i_t_phone_number(self,) -> Optional[str]:
        """
        Gets the contactITPhoneNumber property value. Phone number of the person/organization responsible for IT support
        Returns: Optional[str]
        """
        return self._contact_i_t_phone_number
    
    @contact_i_t_phone_number.setter
    def contact_i_t_phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITPhoneNumber property value. Phone number of the person/organization responsible for IT support
        Args:
            value: Value to set for the contactITPhoneNumber property.
        """
        self._contact_i_t_phone_number = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time when the BrandingProfile was created
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time when the BrandingProfile was created
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IntuneBrandingProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IntuneBrandingProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IntuneBrandingProfile()
    
    @property
    def custom_can_see_privacy_message(self,) -> Optional[str]:
        """
        Gets the customCanSeePrivacyMessage property value. Text comments regarding what the admin has access to on the device
        Returns: Optional[str]
        """
        return self._custom_can_see_privacy_message
    
    @custom_can_see_privacy_message.setter
    def custom_can_see_privacy_message(self,value: Optional[str] = None) -> None:
        """
        Sets the customCanSeePrivacyMessage property value. Text comments regarding what the admin has access to on the device
        Args:
            value: Value to set for the customCanSeePrivacyMessage property.
        """
        self._custom_can_see_privacy_message = value
    
    @property
    def custom_cant_see_privacy_message(self,) -> Optional[str]:
        """
        Gets the customCantSeePrivacyMessage property value. Text comments regarding what the admin doesn't have access to on the device
        Returns: Optional[str]
        """
        return self._custom_cant_see_privacy_message
    
    @custom_cant_see_privacy_message.setter
    def custom_cant_see_privacy_message(self,value: Optional[str] = None) -> None:
        """
        Sets the customCantSeePrivacyMessage property value. Text comments regarding what the admin doesn't have access to on the device
        Args:
            value: Value to set for the customCantSeePrivacyMessage property.
        """
        self._custom_cant_see_privacy_message = value
    
    @property
    def custom_privacy_message(self,) -> Optional[str]:
        """
        Gets the customPrivacyMessage property value. Text comments regarding what the admin doesn't have access to on the device
        Returns: Optional[str]
        """
        return self._custom_privacy_message
    
    @custom_privacy_message.setter
    def custom_privacy_message(self,value: Optional[str] = None) -> None:
        """
        Sets the customPrivacyMessage property value. Text comments regarding what the admin doesn't have access to on the device
        Args:
            value: Value to set for the customPrivacyMessage property.
        """
        self._custom_privacy_message = value
    
    @property
    def disable_client_telemetry(self,) -> Optional[bool]:
        """
        Gets the disableClientTelemetry property value. Applies to telemetry sent from all clients to the Intune service. When disabled, all proactive troubleshooting and issue warnings within the client are turned off, and telemetry settings appear inactive or hidden to the device user.
        Returns: Optional[bool]
        """
        return self._disable_client_telemetry
    
    @disable_client_telemetry.setter
    def disable_client_telemetry(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableClientTelemetry property value. Applies to telemetry sent from all clients to the Intune service. When disabled, all proactive troubleshooting and issue warnings within the client are turned off, and telemetry settings appear inactive or hidden to the device user.
        Args:
            value: Value to set for the disableClientTelemetry property.
        """
        self._disable_client_telemetry = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Company/organization name that is displayed to end users
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Company/organization name that is displayed to end users
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enrollment_availability(self,) -> Optional[enrollment_availability_options.EnrollmentAvailabilityOptions]:
        """
        Gets the enrollmentAvailability property value. Options available for enrollment flow customization
        Returns: Optional[enrollment_availability_options.EnrollmentAvailabilityOptions]
        """
        return self._enrollment_availability
    
    @enrollment_availability.setter
    def enrollment_availability(self,value: Optional[enrollment_availability_options.EnrollmentAvailabilityOptions] = None) -> None:
        """
        Sets the enrollmentAvailability property value. Options available for enrollment flow customization
        Args:
            value: Value to set for the enrollmentAvailability property.
        """
        self._enrollment_availability = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(intune_branding_profile_assignment.IntuneBrandingProfileAssignment)),
            "company_portal_blocked_actions": lambda n : setattr(self, 'company_portal_blocked_actions', n.get_collection_of_object_values(company_portal_blocked_action.CompanyPortalBlockedAction)),
            "contact_i_t_email_address": lambda n : setattr(self, 'contact_i_t_email_address', n.get_str_value()),
            "contact_i_t_name": lambda n : setattr(self, 'contact_i_t_name', n.get_str_value()),
            "contact_i_t_notes": lambda n : setattr(self, 'contact_i_t_notes', n.get_str_value()),
            "contact_i_t_phone_number": lambda n : setattr(self, 'contact_i_t_phone_number', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custom_can_see_privacy_message": lambda n : setattr(self, 'custom_can_see_privacy_message', n.get_str_value()),
            "custom_cant_see_privacy_message": lambda n : setattr(self, 'custom_cant_see_privacy_message', n.get_str_value()),
            "custom_privacy_message": lambda n : setattr(self, 'custom_privacy_message', n.get_str_value()),
            "disable_client_telemetry": lambda n : setattr(self, 'disable_client_telemetry', n.get_bool_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollment_availability": lambda n : setattr(self, 'enrollment_availability', n.get_enum_value(enrollment_availability_options.EnrollmentAvailabilityOptions)),
            "is_default_profile": lambda n : setattr(self, 'is_default_profile', n.get_bool_value()),
            "is_factory_reset_disabled": lambda n : setattr(self, 'is_factory_reset_disabled', n.get_bool_value()),
            "is_remove_device_disabled": lambda n : setattr(self, 'is_remove_device_disabled', n.get_bool_value()),
            "landing_page_customized_image": lambda n : setattr(self, 'landing_page_customized_image', n.get_object_value(mime_content.MimeContent)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "light_background_logo": lambda n : setattr(self, 'light_background_logo', n.get_object_value(mime_content.MimeContent)),
            "online_support_site_name": lambda n : setattr(self, 'online_support_site_name', n.get_str_value()),
            "online_support_site_url": lambda n : setattr(self, 'online_support_site_url', n.get_str_value()),
            "privacy_url": lambda n : setattr(self, 'privacy_url', n.get_str_value()),
            "profile_description": lambda n : setattr(self, 'profile_description', n.get_str_value()),
            "profile_name": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "send_device_ownership_change_push_notification": lambda n : setattr(self, 'send_device_ownership_change_push_notification', n.get_bool_value()),
            "show_azure_a_d_enterprise_apps": lambda n : setattr(self, 'show_azure_a_d_enterprise_apps', n.get_bool_value()),
            "show_configuration_manager_apps": lambda n : setattr(self, 'show_configuration_manager_apps', n.get_bool_value()),
            "show_display_name_next_to_logo": lambda n : setattr(self, 'show_display_name_next_to_logo', n.get_bool_value()),
            "show_logo": lambda n : setattr(self, 'show_logo', n.get_bool_value()),
            "show_office_web_apps": lambda n : setattr(self, 'show_office_web_apps', n.get_bool_value()),
            "theme_color": lambda n : setattr(self, 'theme_color', n.get_object_value(rgb_color.RgbColor)),
            "theme_color_logo": lambda n : setattr(self, 'theme_color_logo', n.get_object_value(mime_content.MimeContent)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default_profile(self,) -> Optional[bool]:
        """
        Gets the isDefaultProfile property value. Boolean that represents whether the profile is used as default or not
        Returns: Optional[bool]
        """
        return self._is_default_profile
    
    @is_default_profile.setter
    def is_default_profile(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultProfile property value. Boolean that represents whether the profile is used as default or not
        Args:
            value: Value to set for the isDefaultProfile property.
        """
        self._is_default_profile = value
    
    @property
    def is_factory_reset_disabled(self,) -> Optional[bool]:
        """
        Gets the isFactoryResetDisabled property value. Boolean that represents whether the adminsistrator has disabled the 'Factory Reset' action on corporate owned devices.
        Returns: Optional[bool]
        """
        return self._is_factory_reset_disabled
    
    @is_factory_reset_disabled.setter
    def is_factory_reset_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFactoryResetDisabled property value. Boolean that represents whether the adminsistrator has disabled the 'Factory Reset' action on corporate owned devices.
        Args:
            value: Value to set for the isFactoryResetDisabled property.
        """
        self._is_factory_reset_disabled = value
    
    @property
    def is_remove_device_disabled(self,) -> Optional[bool]:
        """
        Gets the isRemoveDeviceDisabled property value. Boolean that represents whether the adminsistrator has disabled the 'Remove Device' action on corporate owned devices.
        Returns: Optional[bool]
        """
        return self._is_remove_device_disabled
    
    @is_remove_device_disabled.setter
    def is_remove_device_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRemoveDeviceDisabled property value. Boolean that represents whether the adminsistrator has disabled the 'Remove Device' action on corporate owned devices.
        Args:
            value: Value to set for the isRemoveDeviceDisabled property.
        """
        self._is_remove_device_disabled = value
    
    @property
    def landing_page_customized_image(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the landingPageCustomizedImage property value. Customized image displayed in Company Portal apps landing page
        Returns: Optional[mime_content.MimeContent]
        """
        return self._landing_page_customized_image
    
    @landing_page_customized_image.setter
    def landing_page_customized_image(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the landingPageCustomizedImage property value. Customized image displayed in Company Portal apps landing page
        Args:
            value: Value to set for the landingPageCustomizedImage property.
        """
        self._landing_page_customized_image = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Time when the BrandingProfile was last modified
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Time when the BrandingProfile was last modified
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def light_background_logo(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the lightBackgroundLogo property value. Logo image displayed in Company Portal apps which have a light background behind the logo
        Returns: Optional[mime_content.MimeContent]
        """
        return self._light_background_logo
    
    @light_background_logo.setter
    def light_background_logo(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the lightBackgroundLogo property value. Logo image displayed in Company Portal apps which have a light background behind the logo
        Args:
            value: Value to set for the lightBackgroundLogo property.
        """
        self._light_background_logo = value
    
    @property
    def online_support_site_name(self,) -> Optional[str]:
        """
        Gets the onlineSupportSiteName property value. Display name of the company/organization’s IT helpdesk site
        Returns: Optional[str]
        """
        return self._online_support_site_name
    
    @online_support_site_name.setter
    def online_support_site_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onlineSupportSiteName property value. Display name of the company/organization’s IT helpdesk site
        Args:
            value: Value to set for the onlineSupportSiteName property.
        """
        self._online_support_site_name = value
    
    @property
    def online_support_site_url(self,) -> Optional[str]:
        """
        Gets the onlineSupportSiteUrl property value. URL to the company/organization’s IT helpdesk site
        Returns: Optional[str]
        """
        return self._online_support_site_url
    
    @online_support_site_url.setter
    def online_support_site_url(self,value: Optional[str] = None) -> None:
        """
        Sets the onlineSupportSiteUrl property value. URL to the company/organization’s IT helpdesk site
        Args:
            value: Value to set for the onlineSupportSiteUrl property.
        """
        self._online_support_site_url = value
    
    @property
    def privacy_url(self,) -> Optional[str]:
        """
        Gets the privacyUrl property value. URL to the company/organization’s privacy policy
        Returns: Optional[str]
        """
        return self._privacy_url
    
    @privacy_url.setter
    def privacy_url(self,value: Optional[str] = None) -> None:
        """
        Sets the privacyUrl property value. URL to the company/organization’s privacy policy
        Args:
            value: Value to set for the privacyUrl property.
        """
        self._privacy_url = value
    
    @property
    def profile_description(self,) -> Optional[str]:
        """
        Gets the profileDescription property value. Description of the profile
        Returns: Optional[str]
        """
        return self._profile_description
    
    @profile_description.setter
    def profile_description(self,value: Optional[str] = None) -> None:
        """
        Sets the profileDescription property value. Description of the profile
        Args:
            value: Value to set for the profileDescription property.
        """
        self._profile_description = value
    
    @property
    def profile_name(self,) -> Optional[str]:
        """
        Gets the profileName property value. Name of the profile
        Returns: Optional[str]
        """
        return self._profile_name
    
    @profile_name.setter
    def profile_name(self,value: Optional[str] = None) -> None:
        """
        Sets the profileName property value. Name of the profile
        Args:
            value: Value to set for the profileName property.
        """
        self._profile_name = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of scope tags assigned to the branding profile
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of scope tags assigned to the branding profile
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    @property
    def send_device_ownership_change_push_notification(self,) -> Optional[bool]:
        """
        Gets the sendDeviceOwnershipChangePushNotification property value. Boolean that indicates if a push notification is sent to users when their device ownership type changes from personal to corporate
        Returns: Optional[bool]
        """
        return self._send_device_ownership_change_push_notification
    
    @send_device_ownership_change_push_notification.setter
    def send_device_ownership_change_push_notification(self,value: Optional[bool] = None) -> None:
        """
        Sets the sendDeviceOwnershipChangePushNotification property value. Boolean that indicates if a push notification is sent to users when their device ownership type changes from personal to corporate
        Args:
            value: Value to set for the sendDeviceOwnershipChangePushNotification property.
        """
        self._send_device_ownership_change_push_notification = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("companyPortalBlockedActions", self.company_portal_blocked_actions)
        writer.write_str_value("contactITEmailAddress", self.contact_i_t_email_address)
        writer.write_str_value("contactITName", self.contact_i_t_name)
        writer.write_str_value("contactITNotes", self.contact_i_t_notes)
        writer.write_str_value("contactITPhoneNumber", self.contact_i_t_phone_number)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("customCanSeePrivacyMessage", self.custom_can_see_privacy_message)
        writer.write_str_value("customCantSeePrivacyMessage", self.custom_cant_see_privacy_message)
        writer.write_str_value("customPrivacyMessage", self.custom_privacy_message)
        writer.write_bool_value("disableClientTelemetry", self.disable_client_telemetry)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("enrollmentAvailability", self.enrollment_availability)
        writer.write_bool_value("isDefaultProfile", self.is_default_profile)
        writer.write_bool_value("isFactoryResetDisabled", self.is_factory_reset_disabled)
        writer.write_bool_value("isRemoveDeviceDisabled", self.is_remove_device_disabled)
        writer.write_object_value("landingPageCustomizedImage", self.landing_page_customized_image)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("lightBackgroundLogo", self.light_background_logo)
        writer.write_str_value("onlineSupportSiteName", self.online_support_site_name)
        writer.write_str_value("onlineSupportSiteUrl", self.online_support_site_url)
        writer.write_str_value("privacyUrl", self.privacy_url)
        writer.write_str_value("profileDescription", self.profile_description)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("sendDeviceOwnershipChangePushNotification", self.send_device_ownership_change_push_notification)
        writer.write_bool_value("showAzureADEnterpriseApps", self.show_azure_a_d_enterprise_apps)
        writer.write_bool_value("showConfigurationManagerApps", self.show_configuration_manager_apps)
        writer.write_bool_value("showDisplayNameNextToLogo", self.show_display_name_next_to_logo)
        writer.write_bool_value("showLogo", self.show_logo)
        writer.write_bool_value("showOfficeWebApps", self.show_office_web_apps)
        writer.write_object_value("themeColor", self.theme_color)
        writer.write_object_value("themeColorLogo", self.theme_color_logo)
    
    @property
    def show_azure_a_d_enterprise_apps(self,) -> Optional[bool]:
        """
        Gets the showAzureADEnterpriseApps property value. Boolean that indicates if AzureAD Enterprise Apps will be shown in Company Portal
        Returns: Optional[bool]
        """
        return self._show_azure_a_d_enterprise_apps
    
    @show_azure_a_d_enterprise_apps.setter
    def show_azure_a_d_enterprise_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the showAzureADEnterpriseApps property value. Boolean that indicates if AzureAD Enterprise Apps will be shown in Company Portal
        Args:
            value: Value to set for the showAzureADEnterpriseApps property.
        """
        self._show_azure_a_d_enterprise_apps = value
    
    @property
    def show_configuration_manager_apps(self,) -> Optional[bool]:
        """
        Gets the showConfigurationManagerApps property value. Boolean that indicates if Configuration Manager Apps will be shown in Company Portal
        Returns: Optional[bool]
        """
        return self._show_configuration_manager_apps
    
    @show_configuration_manager_apps.setter
    def show_configuration_manager_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the showConfigurationManagerApps property value. Boolean that indicates if Configuration Manager Apps will be shown in Company Portal
        Args:
            value: Value to set for the showConfigurationManagerApps property.
        """
        self._show_configuration_manager_apps = value
    
    @property
    def show_display_name_next_to_logo(self,) -> Optional[bool]:
        """
        Gets the showDisplayNameNextToLogo property value. Boolean that represents whether the administrator-supplied display name will be shown next to the logo image or not
        Returns: Optional[bool]
        """
        return self._show_display_name_next_to_logo
    
    @show_display_name_next_to_logo.setter
    def show_display_name_next_to_logo(self,value: Optional[bool] = None) -> None:
        """
        Sets the showDisplayNameNextToLogo property value. Boolean that represents whether the administrator-supplied display name will be shown next to the logo image or not
        Args:
            value: Value to set for the showDisplayNameNextToLogo property.
        """
        self._show_display_name_next_to_logo = value
    
    @property
    def show_logo(self,) -> Optional[bool]:
        """
        Gets the showLogo property value. Boolean that represents whether the administrator-supplied logo images are shown or not
        Returns: Optional[bool]
        """
        return self._show_logo
    
    @show_logo.setter
    def show_logo(self,value: Optional[bool] = None) -> None:
        """
        Sets the showLogo property value. Boolean that represents whether the administrator-supplied logo images are shown or not
        Args:
            value: Value to set for the showLogo property.
        """
        self._show_logo = value
    
    @property
    def show_office_web_apps(self,) -> Optional[bool]:
        """
        Gets the showOfficeWebApps property value. Boolean that indicates if Office WebApps will be shown in Company Portal
        Returns: Optional[bool]
        """
        return self._show_office_web_apps
    
    @show_office_web_apps.setter
    def show_office_web_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the showOfficeWebApps property value. Boolean that indicates if Office WebApps will be shown in Company Portal
        Args:
            value: Value to set for the showOfficeWebApps property.
        """
        self._show_office_web_apps = value
    
    @property
    def theme_color(self,) -> Optional[rgb_color.RgbColor]:
        """
        Gets the themeColor property value. Primary theme color used in the Company Portal applications and web portal
        Returns: Optional[rgb_color.RgbColor]
        """
        return self._theme_color
    
    @theme_color.setter
    def theme_color(self,value: Optional[rgb_color.RgbColor] = None) -> None:
        """
        Sets the themeColor property value. Primary theme color used in the Company Portal applications and web portal
        Args:
            value: Value to set for the themeColor property.
        """
        self._theme_color = value
    
    @property
    def theme_color_logo(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the themeColorLogo property value. Logo image displayed in Company Portal apps which have a theme color background behind the logo
        Returns: Optional[mime_content.MimeContent]
        """
        return self._theme_color_logo
    
    @theme_color_logo.setter
    def theme_color_logo(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the themeColorLogo property value. Logo image displayed in Company Portal apps which have a theme color background behind the logo
        Args:
            value: Value to set for the themeColorLogo property.
        """
        self._theme_color_logo = value
    


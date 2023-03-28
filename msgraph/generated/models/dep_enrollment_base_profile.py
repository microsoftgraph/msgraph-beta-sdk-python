from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dep_i_o_s_enrollment_profile, dep_mac_o_s_enrollment_profile, enrollment_profile

from . import enrollment_profile

class DepEnrollmentBaseProfile(enrollment_profile.EnrollmentProfile):
    def __init__(self,) -> None:
        """
        Instantiates a new DepEnrollmentBaseProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.depEnrollmentBaseProfile"
        # Indicates if Apple id setup pane is disabled
        self._apple_id_disabled: Optional[bool] = None
        # Indicates if Apple pay setup pane is disabled
        self._apple_pay_disabled: Optional[bool] = None
        # URL for setup assistant login
        self._configuration_web_url: Optional[bool] = None
        # Sets a literal or name pattern.
        self._device_name_template: Optional[str] = None
        # Indicates if diagnostics setup pane is disabled
        self._diagnostics_disabled: Optional[bool] = None
        # Indicates if displaytone setup screen is disabled
        self._display_tone_setup_disabled: Optional[bool] = None
        # enabledSkipKeys contains all the enabled skip keys as strings
        self._enabled_skip_keys: Optional[List[str]] = None
        # Indicates if this is the default profile
        self._is_default: Optional[bool] = None
        # Indicates if the profile is mandatory
        self._is_mandatory: Optional[bool] = None
        # Indicates if Location service setup pane is disabled
        self._location_disabled: Optional[bool] = None
        # Indicates if privacy screen is disabled
        self._privacy_pane_disabled: Optional[bool] = None
        # Indicates if the profile removal option is disabled
        self._profile_removal_disabled: Optional[bool] = None
        # Indicates if Restore setup pane is blocked
        self._restore_blocked: Optional[bool] = None
        # Indicates if screen timeout setup is disabled
        self._screen_time_screen_disabled: Optional[bool] = None
        # Indicates if siri setup pane is disabled
        self._siri_disabled: Optional[bool] = None
        # Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
        self._supervised_mode_enabled: Optional[bool] = None
        # Support department information
        self._support_department: Optional[str] = None
        # Support phone number
        self._support_phone_number: Optional[str] = None
        # Indicates if 'Terms and Conditions' setup pane is disabled
        self._terms_and_conditions_disabled: Optional[bool] = None
        # Indicates if touch id setup pane is disabled
        self._touch_id_disabled: Optional[bool] = None
    
    @property
    def apple_id_disabled(self,) -> Optional[bool]:
        """
        Gets the appleIdDisabled property value. Indicates if Apple id setup pane is disabled
        Returns: Optional[bool]
        """
        return self._apple_id_disabled
    
    @apple_id_disabled.setter
    def apple_id_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleIdDisabled property value. Indicates if Apple id setup pane is disabled
        Args:
            value: Value to set for the apple_id_disabled property.
        """
        self._apple_id_disabled = value
    
    @property
    def apple_pay_disabled(self,) -> Optional[bool]:
        """
        Gets the applePayDisabled property value. Indicates if Apple pay setup pane is disabled
        Returns: Optional[bool]
        """
        return self._apple_pay_disabled
    
    @apple_pay_disabled.setter
    def apple_pay_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the applePayDisabled property value. Indicates if Apple pay setup pane is disabled
        Args:
            value: Value to set for the apple_pay_disabled property.
        """
        self._apple_pay_disabled = value
    
    @property
    def configuration_web_url(self,) -> Optional[bool]:
        """
        Gets the configurationWebUrl property value. URL for setup assistant login
        Returns: Optional[bool]
        """
        return self._configuration_web_url
    
    @configuration_web_url.setter
    def configuration_web_url(self,value: Optional[bool] = None) -> None:
        """
        Sets the configurationWebUrl property value. URL for setup assistant login
        Args:
            value: Value to set for the configuration_web_url property.
        """
        self._configuration_web_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DepEnrollmentBaseProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DepEnrollmentBaseProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.depIOSEnrollmentProfile":
                from . import dep_i_o_s_enrollment_profile

                return dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile()
            if mapping_value == "#microsoft.graph.depMacOSEnrollmentProfile":
                from . import dep_mac_o_s_enrollment_profile

                return dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile()
        return DepEnrollmentBaseProfile()
    
    @property
    def device_name_template(self,) -> Optional[str]:
        """
        Gets the deviceNameTemplate property value. Sets a literal or name pattern.
        Returns: Optional[str]
        """
        return self._device_name_template
    
    @device_name_template.setter
    def device_name_template(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceNameTemplate property value. Sets a literal or name pattern.
        Args:
            value: Value to set for the device_name_template property.
        """
        self._device_name_template = value
    
    @property
    def diagnostics_disabled(self,) -> Optional[bool]:
        """
        Gets the diagnosticsDisabled property value. Indicates if diagnostics setup pane is disabled
        Returns: Optional[bool]
        """
        return self._diagnostics_disabled
    
    @diagnostics_disabled.setter
    def diagnostics_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticsDisabled property value. Indicates if diagnostics setup pane is disabled
        Args:
            value: Value to set for the diagnostics_disabled property.
        """
        self._diagnostics_disabled = value
    
    @property
    def display_tone_setup_disabled(self,) -> Optional[bool]:
        """
        Gets the displayToneSetupDisabled property value. Indicates if displaytone setup screen is disabled
        Returns: Optional[bool]
        """
        return self._display_tone_setup_disabled
    
    @display_tone_setup_disabled.setter
    def display_tone_setup_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the displayToneSetupDisabled property value. Indicates if displaytone setup screen is disabled
        Args:
            value: Value to set for the display_tone_setup_disabled property.
        """
        self._display_tone_setup_disabled = value
    
    @property
    def enabled_skip_keys(self,) -> Optional[List[str]]:
        """
        Gets the enabledSkipKeys property value. enabledSkipKeys contains all the enabled skip keys as strings
        Returns: Optional[List[str]]
        """
        return self._enabled_skip_keys
    
    @enabled_skip_keys.setter
    def enabled_skip_keys(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enabledSkipKeys property value. enabledSkipKeys contains all the enabled skip keys as strings
        Args:
            value: Value to set for the enabled_skip_keys property.
        """
        self._enabled_skip_keys = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import dep_i_o_s_enrollment_profile, dep_mac_o_s_enrollment_profile, enrollment_profile

        fields: Dict[str, Callable[[Any], None]] = {
            "appleIdDisabled": lambda n : setattr(self, 'apple_id_disabled', n.get_bool_value()),
            "applePayDisabled": lambda n : setattr(self, 'apple_pay_disabled', n.get_bool_value()),
            "configurationWebUrl": lambda n : setattr(self, 'configuration_web_url', n.get_bool_value()),
            "deviceNameTemplate": lambda n : setattr(self, 'device_name_template', n.get_str_value()),
            "diagnosticsDisabled": lambda n : setattr(self, 'diagnostics_disabled', n.get_bool_value()),
            "displayToneSetupDisabled": lambda n : setattr(self, 'display_tone_setup_disabled', n.get_bool_value()),
            "enabledSkipKeys": lambda n : setattr(self, 'enabled_skip_keys', n.get_collection_of_primitive_values(str)),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isMandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
            "locationDisabled": lambda n : setattr(self, 'location_disabled', n.get_bool_value()),
            "privacyPaneDisabled": lambda n : setattr(self, 'privacy_pane_disabled', n.get_bool_value()),
            "profileRemovalDisabled": lambda n : setattr(self, 'profile_removal_disabled', n.get_bool_value()),
            "restoreBlocked": lambda n : setattr(self, 'restore_blocked', n.get_bool_value()),
            "screenTimeScreenDisabled": lambda n : setattr(self, 'screen_time_screen_disabled', n.get_bool_value()),
            "siriDisabled": lambda n : setattr(self, 'siri_disabled', n.get_bool_value()),
            "supervisedModeEnabled": lambda n : setattr(self, 'supervised_mode_enabled', n.get_bool_value()),
            "supportDepartment": lambda n : setattr(self, 'support_department', n.get_str_value()),
            "supportPhoneNumber": lambda n : setattr(self, 'support_phone_number', n.get_str_value()),
            "termsAndConditionsDisabled": lambda n : setattr(self, 'terms_and_conditions_disabled', n.get_bool_value()),
            "touchIdDisabled": lambda n : setattr(self, 'touch_id_disabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates if this is the default profile
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates if this is the default profile
        Args:
            value: Value to set for the is_default property.
        """
        self._is_default = value
    
    @property
    def is_mandatory(self,) -> Optional[bool]:
        """
        Gets the isMandatory property value. Indicates if the profile is mandatory
        Returns: Optional[bool]
        """
        return self._is_mandatory
    
    @is_mandatory.setter
    def is_mandatory(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMandatory property value. Indicates if the profile is mandatory
        Args:
            value: Value to set for the is_mandatory property.
        """
        self._is_mandatory = value
    
    @property
    def location_disabled(self,) -> Optional[bool]:
        """
        Gets the locationDisabled property value. Indicates if Location service setup pane is disabled
        Returns: Optional[bool]
        """
        return self._location_disabled
    
    @location_disabled.setter
    def location_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the locationDisabled property value. Indicates if Location service setup pane is disabled
        Args:
            value: Value to set for the location_disabled property.
        """
        self._location_disabled = value
    
    @property
    def privacy_pane_disabled(self,) -> Optional[bool]:
        """
        Gets the privacyPaneDisabled property value. Indicates if privacy screen is disabled
        Returns: Optional[bool]
        """
        return self._privacy_pane_disabled
    
    @privacy_pane_disabled.setter
    def privacy_pane_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the privacyPaneDisabled property value. Indicates if privacy screen is disabled
        Args:
            value: Value to set for the privacy_pane_disabled property.
        """
        self._privacy_pane_disabled = value
    
    @property
    def profile_removal_disabled(self,) -> Optional[bool]:
        """
        Gets the profileRemovalDisabled property value. Indicates if the profile removal option is disabled
        Returns: Optional[bool]
        """
        return self._profile_removal_disabled
    
    @profile_removal_disabled.setter
    def profile_removal_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the profileRemovalDisabled property value. Indicates if the profile removal option is disabled
        Args:
            value: Value to set for the profile_removal_disabled property.
        """
        self._profile_removal_disabled = value
    
    @property
    def restore_blocked(self,) -> Optional[bool]:
        """
        Gets the restoreBlocked property value. Indicates if Restore setup pane is blocked
        Returns: Optional[bool]
        """
        return self._restore_blocked
    
    @restore_blocked.setter
    def restore_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the restoreBlocked property value. Indicates if Restore setup pane is blocked
        Args:
            value: Value to set for the restore_blocked property.
        """
        self._restore_blocked = value
    
    @property
    def screen_time_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the screenTimeScreenDisabled property value. Indicates if screen timeout setup is disabled
        Returns: Optional[bool]
        """
        return self._screen_time_screen_disabled
    
    @screen_time_screen_disabled.setter
    def screen_time_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenTimeScreenDisabled property value. Indicates if screen timeout setup is disabled
        Args:
            value: Value to set for the screen_time_screen_disabled property.
        """
        self._screen_time_screen_disabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("appleIdDisabled", self.apple_id_disabled)
        writer.write_bool_value("applePayDisabled", self.apple_pay_disabled)
        writer.write_bool_value("configurationWebUrl", self.configuration_web_url)
        writer.write_str_value("deviceNameTemplate", self.device_name_template)
        writer.write_bool_value("diagnosticsDisabled", self.diagnostics_disabled)
        writer.write_bool_value("displayToneSetupDisabled", self.display_tone_setup_disabled)
        writer.write_collection_of_primitive_values("enabledSkipKeys", self.enabled_skip_keys)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isMandatory", self.is_mandatory)
        writer.write_bool_value("locationDisabled", self.location_disabled)
        writer.write_bool_value("privacyPaneDisabled", self.privacy_pane_disabled)
        writer.write_bool_value("profileRemovalDisabled", self.profile_removal_disabled)
        writer.write_bool_value("restoreBlocked", self.restore_blocked)
        writer.write_bool_value("screenTimeScreenDisabled", self.screen_time_screen_disabled)
        writer.write_bool_value("siriDisabled", self.siri_disabled)
        writer.write_bool_value("supervisedModeEnabled", self.supervised_mode_enabled)
        writer.write_str_value("supportDepartment", self.support_department)
        writer.write_str_value("supportPhoneNumber", self.support_phone_number)
        writer.write_bool_value("termsAndConditionsDisabled", self.terms_and_conditions_disabled)
        writer.write_bool_value("touchIdDisabled", self.touch_id_disabled)
    
    @property
    def siri_disabled(self,) -> Optional[bool]:
        """
        Gets the siriDisabled property value. Indicates if siri setup pane is disabled
        Returns: Optional[bool]
        """
        return self._siri_disabled
    
    @siri_disabled.setter
    def siri_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriDisabled property value. Indicates if siri setup pane is disabled
        Args:
            value: Value to set for the siri_disabled property.
        """
        self._siri_disabled = value
    
    @property
    def supervised_mode_enabled(self,) -> Optional[bool]:
        """
        Gets the supervisedModeEnabled property value. Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
        Returns: Optional[bool]
        """
        return self._supervised_mode_enabled
    
    @supervised_mode_enabled.setter
    def supervised_mode_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the supervisedModeEnabled property value. Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
        Args:
            value: Value to set for the supervised_mode_enabled property.
        """
        self._supervised_mode_enabled = value
    
    @property
    def support_department(self,) -> Optional[str]:
        """
        Gets the supportDepartment property value. Support department information
        Returns: Optional[str]
        """
        return self._support_department
    
    @support_department.setter
    def support_department(self,value: Optional[str] = None) -> None:
        """
        Sets the supportDepartment property value. Support department information
        Args:
            value: Value to set for the support_department property.
        """
        self._support_department = value
    
    @property
    def support_phone_number(self,) -> Optional[str]:
        """
        Gets the supportPhoneNumber property value. Support phone number
        Returns: Optional[str]
        """
        return self._support_phone_number
    
    @support_phone_number.setter
    def support_phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the supportPhoneNumber property value. Support phone number
        Args:
            value: Value to set for the support_phone_number property.
        """
        self._support_phone_number = value
    
    @property
    def terms_and_conditions_disabled(self,) -> Optional[bool]:
        """
        Gets the termsAndConditionsDisabled property value. Indicates if 'Terms and Conditions' setup pane is disabled
        Returns: Optional[bool]
        """
        return self._terms_and_conditions_disabled
    
    @terms_and_conditions_disabled.setter
    def terms_and_conditions_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the termsAndConditionsDisabled property value. Indicates if 'Terms and Conditions' setup pane is disabled
        Args:
            value: Value to set for the terms_and_conditions_disabled property.
        """
        self._terms_and_conditions_disabled = value
    
    @property
    def touch_id_disabled(self,) -> Optional[bool]:
        """
        Gets the touchIdDisabled property value. Indicates if touch id setup pane is disabled
        Returns: Optional[bool]
        """
        return self._touch_id_disabled
    
    @touch_id_disabled.setter
    def touch_id_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the touchIdDisabled property value. Indicates if touch id setup pane is disabled
        Args:
            value: Value to set for the touch_id_disabled property.
        """
        self._touch_id_disabled = value
    


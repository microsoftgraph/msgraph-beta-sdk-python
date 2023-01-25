from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class EnrollmentProfile(entity.Entity):
    @property
    def configuration_endpoint_url(self,) -> Optional[str]:
        """
        Gets the configurationEndpointUrl property value. Configuration endpoint url to use for Enrollment
        Returns: Optional[str]
        """
        return self._configuration_endpoint_url
    
    @configuration_endpoint_url.setter
    def configuration_endpoint_url(self,value: Optional[str] = None) -> None:
        """
        Sets the configurationEndpointUrl property value. Configuration endpoint url to use for Enrollment
        Args:
            value: Value to set for the configurationEndpointUrl property.
        """
        self._configuration_endpoint_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new enrollmentProfile and sets the default values.
        """
        super().__init__()
        # Configuration endpoint url to use for Enrollment
        self._configuration_endpoint_url: Optional[str] = None
        # Description of the profile
        self._description: Optional[str] = None
        # Name of the profile
        self._display_name: Optional[str] = None
        # Indicates to authenticate with Apple Setup Assistant instead of Company Portal.
        self._enable_authentication_via_company_portal: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates that Company Portal is required on setup assistant enrolled devices
        self._require_company_portal_on_setup_assistant_enrolled_devices: Optional[bool] = None
        # Indicates if the profile requires user authentication
        self._requires_user_authentication: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EnrollmentProfile()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the profile
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the profile
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the profile
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the profile
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enable_authentication_via_company_portal(self,) -> Optional[bool]:
        """
        Gets the enableAuthenticationViaCompanyPortal property value. Indicates to authenticate with Apple Setup Assistant instead of Company Portal.
        Returns: Optional[bool]
        """
        return self._enable_authentication_via_company_portal
    
    @enable_authentication_via_company_portal.setter
    def enable_authentication_via_company_portal(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableAuthenticationViaCompanyPortal property value. Indicates to authenticate with Apple Setup Assistant instead of Company Portal.
        Args:
            value: Value to set for the enableAuthenticationViaCompanyPortal property.
        """
        self._enable_authentication_via_company_portal = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration_endpoint_url": lambda n : setattr(self, 'configuration_endpoint_url', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enable_authentication_via_company_portal": lambda n : setattr(self, 'enable_authentication_via_company_portal', n.get_bool_value()),
            "require_company_portal_on_setup_assistant_enrolled_devices": lambda n : setattr(self, 'require_company_portal_on_setup_assistant_enrolled_devices', n.get_bool_value()),
            "requires_user_authentication": lambda n : setattr(self, 'requires_user_authentication', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def require_company_portal_on_setup_assistant_enrolled_devices(self,) -> Optional[bool]:
        """
        Gets the requireCompanyPortalOnSetupAssistantEnrolledDevices property value. Indicates that Company Portal is required on setup assistant enrolled devices
        Returns: Optional[bool]
        """
        return self._require_company_portal_on_setup_assistant_enrolled_devices
    
    @require_company_portal_on_setup_assistant_enrolled_devices.setter
    def require_company_portal_on_setup_assistant_enrolled_devices(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireCompanyPortalOnSetupAssistantEnrolledDevices property value. Indicates that Company Portal is required on setup assistant enrolled devices
        Args:
            value: Value to set for the requireCompanyPortalOnSetupAssistantEnrolledDevices property.
        """
        self._require_company_portal_on_setup_assistant_enrolled_devices = value
    
    @property
    def requires_user_authentication(self,) -> Optional[bool]:
        """
        Gets the requiresUserAuthentication property value. Indicates if the profile requires user authentication
        Returns: Optional[bool]
        """
        return self._requires_user_authentication
    
    @requires_user_authentication.setter
    def requires_user_authentication(self,value: Optional[bool] = None) -> None:
        """
        Sets the requiresUserAuthentication property value. Indicates if the profile requires user authentication
        Args:
            value: Value to set for the requiresUserAuthentication property.
        """
        self._requires_user_authentication = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("configurationEndpointUrl", self.configuration_endpoint_url)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enableAuthenticationViaCompanyPortal", self.enable_authentication_via_company_portal)
        writer.write_bool_value("requireCompanyPortalOnSetupAssistantEnrolledDevices", self.require_company_portal_on_setup_assistant_enrolled_devices)
        writer.write_bool_value("requiresUserAuthentication", self.requires_user_authentication)
    


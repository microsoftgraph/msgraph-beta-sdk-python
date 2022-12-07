from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

azure_a_d_registration_policy = lazy_import('msgraph.generated.models.azure_a_d_registration_policy')
azure_ad_join_policy = lazy_import('msgraph.generated.models.azure_ad_join_policy')
entity = lazy_import('msgraph.generated.models.entity')
multi_factor_auth_configuration = lazy_import('msgraph.generated.models.multi_factor_auth_configuration')

class DeviceRegistrationPolicy(entity.Entity):
    @property
    def azure_a_d_join(self,) -> Optional[azure_ad_join_policy.AzureAdJoinPolicy]:
        """
        Gets the azureADJoin property value. Specifies the authorization policy for controlling registration of new devices using Azure AD Join within your organization. Required. For more information, see What is a device identity?.
        Returns: Optional[azure_ad_join_policy.AzureAdJoinPolicy]
        """
        return self._azure_a_d_join
    
    @azure_a_d_join.setter
    def azure_a_d_join(self,value: Optional[azure_ad_join_policy.AzureAdJoinPolicy] = None) -> None:
        """
        Sets the azureADJoin property value. Specifies the authorization policy for controlling registration of new devices using Azure AD Join within your organization. Required. For more information, see What is a device identity?.
        Args:
            value: Value to set for the azureADJoin property.
        """
        self._azure_a_d_join = value
    
    @property
    def azure_a_d_registration(self,) -> Optional[azure_a_d_registration_policy.AzureADRegistrationPolicy]:
        """
        Gets the azureADRegistration property value. Specifies the authorization policy for controlling registration of new devices using Azure AD registered within your organization. Required. For more information, see What is a device identity?.
        Returns: Optional[azure_a_d_registration_policy.AzureADRegistrationPolicy]
        """
        return self._azure_a_d_registration
    
    @azure_a_d_registration.setter
    def azure_a_d_registration(self,value: Optional[azure_a_d_registration_policy.AzureADRegistrationPolicy] = None) -> None:
        """
        Sets the azureADRegistration property value. Specifies the authorization policy for controlling registration of new devices using Azure AD registered within your organization. Required. For more information, see What is a device identity?.
        Args:
            value: Value to set for the azureADRegistration property.
        """
        self._azure_a_d_registration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceRegistrationPolicy and sets the default values.
        """
        super().__init__()
        # Specifies the authorization policy for controlling registration of new devices using Azure AD Join within your organization. Required. For more information, see What is a device identity?.
        self._azure_a_d_join: Optional[azure_ad_join_policy.AzureAdJoinPolicy] = None
        # Specifies the authorization policy for controlling registration of new devices using Azure AD registered within your organization. Required. For more information, see What is a device identity?.
        self._azure_a_d_registration: Optional[azure_a_d_registration_policy.AzureADRegistrationPolicy] = None
        # The description of the device registration policy. It is always set to Tenant-wide policy that manages intial provisioning controls using quota restrictions, additional authentication and authorization checks. Read-only.
        self._description: Optional[str] = None
        # The name of the device registration policy. It is always set to Device Registration Policy. Read-only.
        self._display_name: Optional[str] = None
        # The multiFactorAuthConfiguration property
        self._multi_factor_auth_configuration: Optional[multi_factor_auth_configuration.MultiFactorAuthConfiguration] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the maximum number of devices that a user can have within your organization before blocking new device registrations. The default value is set to 50. If this property is not specified during the policy update operation, it is automatically reset to 0 to indicate that users are not allowed to join any devices.
        self._user_device_quota: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceRegistrationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceRegistrationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceRegistrationPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the device registration policy. It is always set to Tenant-wide policy that manages intial provisioning controls using quota restrictions, additional authentication and authorization checks. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the device registration policy. It is always set to Tenant-wide policy that manages intial provisioning controls using quota restrictions, additional authentication and authorization checks. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the device registration policy. It is always set to Device Registration Policy. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the device registration policy. It is always set to Device Registration Policy. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_a_d_join": lambda n : setattr(self, 'azure_a_d_join', n.get_object_value(azure_ad_join_policy.AzureAdJoinPolicy)),
            "azure_a_d_registration": lambda n : setattr(self, 'azure_a_d_registration', n.get_object_value(azure_a_d_registration_policy.AzureADRegistrationPolicy)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "multi_factor_auth_configuration": lambda n : setattr(self, 'multi_factor_auth_configuration', n.get_enum_value(multi_factor_auth_configuration.MultiFactorAuthConfiguration)),
            "user_device_quota": lambda n : setattr(self, 'user_device_quota', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def multi_factor_auth_configuration(self,) -> Optional[multi_factor_auth_configuration.MultiFactorAuthConfiguration]:
        """
        Gets the multiFactorAuthConfiguration property value. The multiFactorAuthConfiguration property
        Returns: Optional[multi_factor_auth_configuration.MultiFactorAuthConfiguration]
        """
        return self._multi_factor_auth_configuration
    
    @multi_factor_auth_configuration.setter
    def multi_factor_auth_configuration(self,value: Optional[multi_factor_auth_configuration.MultiFactorAuthConfiguration] = None) -> None:
        """
        Sets the multiFactorAuthConfiguration property value. The multiFactorAuthConfiguration property
        Args:
            value: Value to set for the multiFactorAuthConfiguration property.
        """
        self._multi_factor_auth_configuration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("azureADJoin", self.azure_a_d_join)
        writer.write_object_value("azureADRegistration", self.azure_a_d_registration)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("multiFactorAuthConfiguration", self.multi_factor_auth_configuration)
        writer.write_int_value("userDeviceQuota", self.user_device_quota)
    
    @property
    def user_device_quota(self,) -> Optional[int]:
        """
        Gets the userDeviceQuota property value. Specifies the maximum number of devices that a user can have within your organization before blocking new device registrations. The default value is set to 50. If this property is not specified during the policy update operation, it is automatically reset to 0 to indicate that users are not allowed to join any devices.
        Returns: Optional[int]
        """
        return self._user_device_quota
    
    @user_device_quota.setter
    def user_device_quota(self,value: Optional[int] = None) -> None:
        """
        Sets the userDeviceQuota property value. Specifies the maximum number of devices that a user can have within your organization before blocking new device registrations. The default value is set to 50. If this property is not specified during the policy update operation, it is automatically reset to 0 to indicate that users are not allowed to join any devices.
        Args:
            value: Value to set for the userDeviceQuota property.
        """
        self._user_device_quota = value
    


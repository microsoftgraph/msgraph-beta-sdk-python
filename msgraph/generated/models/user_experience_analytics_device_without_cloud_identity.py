from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class UserExperienceAnalyticsDeviceWithoutCloudIdentity(entity.Entity):
    """
    The user experience analytics Device without Cloud Identity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsDeviceWithoutCloudIdentity and sets the default values.
        """
        super().__init__()
        # Azure Active Directory Device Id
        self._azure_ad_device_id: Optional[str] = None
        # The tenant attach device's name.
        self._device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def azure_ad_device_id(self,) -> Optional[str]:
        """
        Gets the azureAdDeviceId property value. Azure Active Directory Device Id
        Returns: Optional[str]
        """
        return self._azure_ad_device_id
    
    @azure_ad_device_id.setter
    def azure_ad_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdDeviceId property value. Azure Active Directory Device Id
        Args:
            value: Value to set for the azure_ad_device_id property.
        """
        self._azure_ad_device_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceWithoutCloudIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceWithoutCloudIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceWithoutCloudIdentity()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The tenant attach device's name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The tenant attach device's name.
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureAdDeviceId", self.azure_ad_device_id)
        writer.write_str_value("deviceName", self.device_name)
    


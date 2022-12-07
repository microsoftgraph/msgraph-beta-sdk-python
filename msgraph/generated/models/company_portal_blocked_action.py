from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

company_portal_action = lazy_import('msgraph.generated.models.company_portal_action')
device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')
owner_type = lazy_import('msgraph.generated.models.owner_type')

class CompanyPortalBlockedAction(AdditionalDataHolder, Parsable):
    """
    Blocked actions on the company portal as per platform and device ownership types
    """
    @property
    def action(self,) -> Optional[company_portal_action.CompanyPortalAction]:
        """
        Gets the action property value. Action on a device that can be executed in the Company Portal
        Returns: Optional[company_portal_action.CompanyPortalAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[company_portal_action.CompanyPortalAction] = None) -> None:
        """
        Sets the action property value. Action on a device that can be executed in the Company Portal
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new companyPortalBlockedAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Action on a device that can be executed in the Company Portal
        self._action: Optional[company_portal_action.CompanyPortalAction] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Owner type of device.
        self._owner_type: Optional[owner_type.OwnerType] = None
        # Supported platform types.
        self._platform: Optional[device_platform_type.DevicePlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CompanyPortalBlockedAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CompanyPortalBlockedAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CompanyPortalBlockedAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(company_portal_action.CompanyPortalAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owner_type": lambda n : setattr(self, 'owner_type', n.get_enum_value(owner_type.OwnerType)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def owner_type(self,) -> Optional[owner_type.OwnerType]:
        """
        Gets the ownerType property value. Owner type of device.
        Returns: Optional[owner_type.OwnerType]
        """
        return self._owner_type
    
    @owner_type.setter
    def owner_type(self,value: Optional[owner_type.OwnerType] = None) -> None:
        """
        Sets the ownerType property value. Owner type of device.
        Args:
            value: Value to set for the ownerType property.
        """
        self._owner_type = value
    
    @property
    def platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the platform property value. Supported platform types.
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the platform property value. Supported platform types.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_portal_action import CompanyPortalAction
    from .device_platform_type import DevicePlatformType
    from .owner_type import OwnerType

@dataclass
class CompanyPortalBlockedAction(AdditionalDataHolder, BackedModel, Parsable):
    """
    Blocked actions on the company portal as per platform and device ownership types
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Action on a device that can be executed in the Company Portal
    action: Optional[CompanyPortalAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[OwnerType] = None
    # Supported platform types.
    platform: Optional[DevicePlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanyPortalBlockedAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanyPortalBlockedAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompanyPortalBlockedAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .company_portal_action import CompanyPortalAction
        from .device_platform_type import DevicePlatformType
        from .owner_type import OwnerType

        from .company_portal_action import CompanyPortalAction
        from .device_platform_type import DevicePlatformType
        from .owner_type import OwnerType

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(CompanyPortalAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(OwnerType)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(DevicePlatformType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_additional_data_value(self.additional_data)
    


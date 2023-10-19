from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .rbac_application import RbacApplication
    from .rbac_application_multiple import RbacApplicationMultiple
    from .unified_rbac_application import UnifiedRbacApplication

@dataclass
class RoleManagement(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The cloudPC property
    cloud_p_c: Optional[RbacApplicationMultiple] = None
    # The RbacApplication for Device Management
    device_management: Optional[RbacApplicationMultiple] = None
    # The directory property
    directory: Optional[RbacApplication] = None
    # The enterpriseApps property
    enterprise_apps: Optional[List[RbacApplication]] = None
    # The RbacApplication for Entitlement Management
    entitlement_management: Optional[RbacApplication] = None
    # The exchange property
    exchange: Optional[UnifiedRbacApplication] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RoleManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .rbac_application import RbacApplication
        from .rbac_application_multiple import RbacApplicationMultiple
        from .unified_rbac_application import UnifiedRbacApplication

        from .rbac_application import RbacApplication
        from .rbac_application_multiple import RbacApplicationMultiple
        from .unified_rbac_application import UnifiedRbacApplication

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPC": lambda n : setattr(self, 'cloud_p_c', n.get_object_value(RbacApplicationMultiple)),
            "deviceManagement": lambda n : setattr(self, 'device_management', n.get_object_value(RbacApplicationMultiple)),
            "directory": lambda n : setattr(self, 'directory', n.get_object_value(RbacApplication)),
            "enterpriseApps": lambda n : setattr(self, 'enterprise_apps', n.get_collection_of_object_values(RbacApplication)),
            "entitlementManagement": lambda n : setattr(self, 'entitlement_management', n.get_object_value(RbacApplication)),
            "exchange": lambda n : setattr(self, 'exchange', n.get_object_value(UnifiedRbacApplication)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("cloudPC", self.cloud_p_c)
        writer.write_object_value("deviceManagement", self.device_management)
        writer.write_object_value("directory", self.directory)
        writer.write_collection_of_object_values("enterpriseApps", self.enterprise_apps)
        writer.write_object_value("entitlementManagement", self.entitlement_management)
        writer.write_object_value("exchange", self.exchange)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


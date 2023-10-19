from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .management_category import ManagementCategory

@dataclass
class ManagementTemplateDetailedInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The category property
    category: Optional[ManagementCategory] = None
    # The display name for the management template. Required. Read-only.
    display_name: Optional[str] = None
    # The unique identifier for the management template. Required. Read-only.
    management_template_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The version property
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateDetailedInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateDetailedInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateDetailedInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .management_category import ManagementCategory

        from .management_category import ManagementCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ManagementCategory)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "managementTemplateId": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    


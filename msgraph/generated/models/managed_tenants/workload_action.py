from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .setting import Setting
    from .workload_action_category import WorkloadActionCategory

@dataclass
class WorkloadAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The unique identifier for the workload action. Required. Read-only.
    action_id: Optional[str] = None
    # The category for the workload action. Possible values are: automated, manual, unknownFutureValue. Optional. Read-only.
    category: Optional[WorkloadActionCategory] = None
    # The description for the workload action. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the workload action. Optional. Read-only.
    display_name: Optional[str] = None
    # The licenses property
    licenses: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The service associated with workload action. Optional. Read-only.
    service: Optional[str] = None
    # The collection of settings associated with the workload action. Optional. Read-only.
    settings: Optional[List[Setting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkloadAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkloadAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .setting import Setting
        from .workload_action_category import WorkloadActionCategory

        from .setting import Setting
        from .workload_action_category import WorkloadActionCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(WorkloadActionCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "licenses": lambda n : setattr(self, 'licenses', n.get_collection_of_primitive_values(str)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(Setting)),
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
        writer.write_str_value("actionId", self.action_id)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("licenses", self.licenses)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("service", self.service)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_additional_data_value(self.additional_data)
    


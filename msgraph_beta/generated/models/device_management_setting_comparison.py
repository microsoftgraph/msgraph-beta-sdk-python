from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_comparison_result import DeviceManagementComparisonResult

@dataclass
class DeviceManagementSettingComparison(AdditionalDataHolder, BackedModel, Parsable):
    """
    Entity representing setting comparison result
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Setting comparison result type
    comparison_result: Optional[DeviceManagementComparisonResult] = None
    # JSON representation of current intent (or) template setting's value
    current_value_json: Optional[str] = None
    # The ID of the setting definition for this instance
    definition_id: Optional[str] = None
    # The setting's display name
    display_name: Optional[str] = None
    # The setting ID
    id: Optional[str] = None
    # JSON representation of new template setting's value
    new_value_json: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingComparison:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingComparison
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettingComparison()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_comparison_result import DeviceManagementComparisonResult

        from .device_management_comparison_result import DeviceManagementComparisonResult

        fields: Dict[str, Callable[[Any], None]] = {
            "comparisonResult": lambda n : setattr(self, 'comparison_result', n.get_enum_value(DeviceManagementComparisonResult)),
            "currentValueJson": lambda n : setattr(self, 'current_value_json', n.get_str_value()),
            "definitionId": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "newValueJson": lambda n : setattr(self, 'new_value_json', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("comparisonResult", self.comparison_result)
        writer.write_str_value("currentValueJson", self.current_value_json)
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("newValueJson", self.new_value_json)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


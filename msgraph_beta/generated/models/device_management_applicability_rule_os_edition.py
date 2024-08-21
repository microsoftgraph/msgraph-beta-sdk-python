from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_applicability_rule_type import DeviceManagementApplicabilityRuleType
    from .windows10_edition_type import Windows10EditionType

@dataclass
class DeviceManagementApplicabilityRuleOsEdition(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Name for object.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Applicability rule OS edition type.
    os_edition_types: Optional[List[Windows10EditionType]] = None
    # Supported Applicability rule types for Device Configuration
    rule_type: Optional[DeviceManagementApplicabilityRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementApplicabilityRuleOsEdition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementApplicabilityRuleOsEdition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementApplicabilityRuleOsEdition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_applicability_rule_type import DeviceManagementApplicabilityRuleType
        from .windows10_edition_type import Windows10EditionType

        from .device_management_applicability_rule_type import DeviceManagementApplicabilityRuleType
        from .windows10_edition_type import Windows10EditionType

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osEditionTypes": lambda n : setattr(self, 'os_edition_types', n.get_collection_of_enum_values(Windows10EditionType)),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(DeviceManagementApplicabilityRuleType)),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_enum_values("osEditionTypes", self.os_edition_types)
        writer.write_enum_value("ruleType", self.rule_type)
        writer.write_additional_data_value(self.additional_data)
    


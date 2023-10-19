from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_mode import ApplicationMode
    from .label_action_base import LabelActionBase

@dataclass
class MatchingLabel(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The applicationMode property
    application_mode: Optional[ApplicationMode] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The isEndpointProtectionEnabled property
    is_endpoint_protection_enabled: Optional[bool] = None
    # The labelActions property
    label_actions: Optional[List[LabelActionBase]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyTip property
    policy_tip: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # The toolTip property
    tool_tip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MatchingLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MatchingLabel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MatchingLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .application_mode import ApplicationMode
        from .label_action_base import LabelActionBase

        from .application_mode import ApplicationMode
        from .label_action_base import LabelActionBase

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationMode": lambda n : setattr(self, 'application_mode', n.get_enum_value(ApplicationMode)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isEndpointProtectionEnabled": lambda n : setattr(self, 'is_endpoint_protection_enabled', n.get_bool_value()),
            "labelActions": lambda n : setattr(self, 'label_actions', n.get_collection_of_object_values(LabelActionBase)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyTip": lambda n : setattr(self, 'policy_tip', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "toolTip": lambda n : setattr(self, 'tool_tip', n.get_str_value()),
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
        writer.write_enum_value("applicationMode", self.application_mode)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isEndpointProtectionEnabled", self.is_endpoint_protection_enabled)
        writer.write_collection_of_object_values("labelActions", self.label_actions)
        writer.write_str_value("name", self.name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("policyTip", self.policy_tip)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("toolTip", self.tool_tip)
        writer.write_additional_data_value(self.additional_data)
    


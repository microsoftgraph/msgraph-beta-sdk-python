from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_source, information_protection_action

from . import information_protection_action

@dataclass
class ApplyLabelAction(information_protection_action.InformationProtectionAction):
    odata_type = "#microsoft.graph.security.applyLabelAction"
    # The actionSource property
    action_source: Optional[action_source.ActionSource] = None
    # The collection of actions that should be implemented by the caller.
    actions: Optional[List[information_protection_action.InformationProtectionAction]] = None
    # If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
    responsible_sensitive_type_ids: Optional[List[str]] = None
    # The sensitivityLabelId property
    sensitivity_label_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyLabelAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplyLabelAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApplyLabelAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_source, information_protection_action

        from . import action_source, information_protection_action

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(action_source.ActionSource)),
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(information_protection_action.InformationProtectionAction)),
            "responsibleSensitiveTypeIds": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelId": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("actionSource", self.action_source)
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_collection_of_primitive_values("responsibleSensitiveTypeIds", self.responsible_sensitive_type_ids)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
    


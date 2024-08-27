from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_source import ActionSource
    from .information_protection_action import InformationProtectionAction

from .information_protection_action import InformationProtectionAction

@dataclass
class ApplyLabelAction(InformationProtectionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.applyLabelAction"
    # The actionSource property
    action_source: Optional[ActionSource] = None
    # The collection of actions that should be implemented by the caller.
    actions: Optional[List[InformationProtectionAction]] = None
    # If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
    responsible_sensitive_type_ids: Optional[List[str]] = None
    # The sensitivityLabelId property
    sensitivity_label_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplyLabelAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplyLabelAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplyLabelAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action_source import ActionSource
        from .information_protection_action import InformationProtectionAction

        from .action_source import ActionSource
        from .information_protection_action import InformationProtectionAction

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(ActionSource)),
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(InformationProtectionAction)),
            "responsibleSensitiveTypeIds": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelId": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("actionSource", self.action_source)
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_collection_of_primitive_values("responsibleSensitiveTypeIds", self.responsible_sensitive_type_ids)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
    


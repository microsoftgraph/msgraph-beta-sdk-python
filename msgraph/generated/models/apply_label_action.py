from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import action_source, information_protection_action, label_details

from . import information_protection_action

@dataclass
class ApplyLabelAction(information_protection_action.InformationProtectionAction):
    odata_type = "#microsoft.graph.applyLabelAction"
    # The actionSource property
    action_source: Optional[action_source.ActionSource] = None
    # The collection of specific actions that should be taken by the consuming application to label the document. See  informationProtectionAction for the full list.
    actions: Optional[List[information_protection_action.InformationProtectionAction]] = None
    # Object that describes the details of the label to apply.
    label: Optional[label_details.LabelDetails] = None
    # If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
    responsible_sensitive_type_ids: Optional[List[UUID]] = None
    
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
        from . import action_source, information_protection_action, label_details

        from . import action_source, information_protection_action, label_details

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(action_source.ActionSource)),
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(information_protection_action.InformationProtectionAction)),
            "label": lambda n : setattr(self, 'label', n.get_object_value(label_details.LabelDetails)),
            "responsibleSensitiveTypeIds": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_object_value("label", self.label)
        writer.write_collection_of_primitive_values("responsibleSensitiveTypeIds", self.responsible_sensitive_type_ids)
    


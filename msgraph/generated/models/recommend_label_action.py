from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .action_source import ActionSource
    from .information_protection_action import InformationProtectionAction
    from .label_details import LabelDetails

from .information_protection_action import InformationProtectionAction

@dataclass
class RecommendLabelAction(InformationProtectionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.recommendLabelAction"
    # The actionSource property
    action_source: Optional[ActionSource] = None
    # Actions to take if the label is accepted by the user.
    actions: Optional[List[InformationProtectionAction]] = None
    # The label that is being recommended.
    label: Optional[LabelDetails] = None
    # The sensitive information type GUIDs that caused the recommendation to be given.
    responsible_sensitive_type_ids: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecommendLabelAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecommendLabelAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RecommendLabelAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action_source import ActionSource
        from .information_protection_action import InformationProtectionAction
        from .label_details import LabelDetails

        from .action_source import ActionSource
        from .information_protection_action import InformationProtectionAction
        from .label_details import LabelDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(ActionSource)),
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(InformationProtectionAction)),
            "label": lambda n : setattr(self, 'label', n.get_object_value(LabelDetails)),
            "responsibleSensitiveTypeIds": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(UUID)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("actionSource", self.action_source)
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_object_value("label", self.label)
        writer.write_collection_of_primitive_values("responsibleSensitiveTypeIds", self.responsible_sensitive_type_ids)
    


from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import action_source, information_protection_action, label_details

from . import information_protection_action

class ApplyLabelAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new ApplyLabelAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.applyLabelAction"
        # The actionSource property
        self._action_source: Optional[action_source.ActionSource] = None
        # The collection of specific actions that should be taken by the consuming application to label the document. See  informationProtectionAction for the full list.
        self._actions: Optional[List[information_protection_action.InformationProtectionAction]] = None
        # Object that describes the details of the label to apply.
        self._label: Optional[label_details.LabelDetails] = None
        # If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
        self._responsible_sensitive_type_ids: Optional[List[UUID]] = None
    
    @property
    def action_source(self,) -> Optional[action_source.ActionSource]:
        """
        Gets the actionSource property value. The actionSource property
        Returns: Optional[action_source.ActionSource]
        """
        return self._action_source
    
    @action_source.setter
    def action_source(self,value: Optional[action_source.ActionSource] = None) -> None:
        """
        Sets the actionSource property value. The actionSource property
        Args:
            value: Value to set for the action_source property.
        """
        self._action_source = value
    
    @property
    def actions(self,) -> Optional[List[information_protection_action.InformationProtectionAction]]:
        """
        Gets the actions property value. The collection of specific actions that should be taken by the consuming application to label the document. See  informationProtectionAction for the full list.
        Returns: Optional[List[information_protection_action.InformationProtectionAction]]
        """
        return self._actions
    
    @actions.setter
    def actions(self,value: Optional[List[information_protection_action.InformationProtectionAction]] = None) -> None:
        """
        Sets the actions property value. The collection of specific actions that should be taken by the consuming application to label the document. See  informationProtectionAction for the full list.
        Args:
            value: Value to set for the actions property.
        """
        self._actions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyLabelAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplyLabelAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplyLabelAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_source, information_protection_action, label_details

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(information_protection_action.InformationProtectionAction)),
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(action_source.ActionSource)),
            "label": lambda n : setattr(self, 'label', n.get_object_value(label_details.LabelDetails)),
            "responsibleSensitiveTypeIds": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(UUID)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def label(self,) -> Optional[label_details.LabelDetails]:
        """
        Gets the label property value. Object that describes the details of the label to apply.
        Returns: Optional[label_details.LabelDetails]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[label_details.LabelDetails] = None) -> None:
        """
        Sets the label property value. Object that describes the details of the label to apply.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def responsible_sensitive_type_ids(self,) -> Optional[List[UUID]]:
        """
        Gets the responsibleSensitiveTypeIds property value. If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
        Returns: Optional[List[UUID]]
        """
        return self._responsible_sensitive_type_ids
    
    @responsible_sensitive_type_ids.setter
    def responsible_sensitive_type_ids(self,value: Optional[List[UUID]] = None) -> None:
        """
        Sets the responsibleSensitiveTypeIds property value. If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
        Args:
            value: Value to set for the responsible_sensitive_type_ids property.
        """
        self._responsible_sensitive_type_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_enum_value("actionSource", self.action_source)
        writer.write_object_value("label", self.label)
        writer.write_collection_of_primitive_values("responsibleSensitiveTypeIds", self.responsible_sensitive_type_ids)
    


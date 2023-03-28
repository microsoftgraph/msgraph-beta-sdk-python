from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_source, information_protection_action

from . import information_protection_action

class RecommendLabelAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new RecommendLabelAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.recommendLabelAction"
        # The actionSource property
        self._action_source: Optional[action_source.ActionSource] = None
        # Actions to take if the label is accepted by the user.
        self._actions: Optional[List[information_protection_action.InformationProtectionAction]] = None
        # The sensitive information type GUIDs that caused the recommendation to be given.
        self._responsible_sensitive_type_ids: Optional[List[str]] = None
        # The sensitivityLabelId property
        self._sensitivity_label_id: Optional[str] = None
    
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
        Gets the actions property value. Actions to take if the label is accepted by the user.
        Returns: Optional[List[information_protection_action.InformationProtectionAction]]
        """
        return self._actions
    
    @actions.setter
    def actions(self,value: Optional[List[information_protection_action.InformationProtectionAction]] = None) -> None:
        """
        Sets the actions property value. Actions to take if the label is accepted by the user.
        Args:
            value: Value to set for the actions property.
        """
        self._actions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecommendLabelAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecommendLabelAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecommendLabelAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_source, information_protection_action

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(information_protection_action.InformationProtectionAction)),
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(action_source.ActionSource)),
            "responsibleSensitiveTypeIds": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelId": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def responsible_sensitive_type_ids(self,) -> Optional[List[str]]:
        """
        Gets the responsibleSensitiveTypeIds property value. The sensitive information type GUIDs that caused the recommendation to be given.
        Returns: Optional[List[str]]
        """
        return self._responsible_sensitive_type_ids
    
    @responsible_sensitive_type_ids.setter
    def responsible_sensitive_type_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the responsibleSensitiveTypeIds property value. The sensitive information type GUIDs that caused the recommendation to be given.
        Args:
            value: Value to set for the responsible_sensitive_type_ids property.
        """
        self._responsible_sensitive_type_ids = value
    
    @property
    def sensitivity_label_id(self,) -> Optional[str]:
        """
        Gets the sensitivityLabelId property value. The sensitivityLabelId property
        Returns: Optional[str]
        """
        return self._sensitivity_label_id
    
    @sensitivity_label_id.setter
    def sensitivity_label_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sensitivityLabelId property value. The sensitivityLabelId property
        Args:
            value: Value to set for the sensitivity_label_id property.
        """
        self._sensitivity_label_id = value
    
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
        writer.write_collection_of_primitive_values("responsibleSensitiveTypeIds", self.responsible_sensitive_type_ids)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
    


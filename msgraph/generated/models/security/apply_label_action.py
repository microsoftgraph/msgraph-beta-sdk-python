from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_source = lazy_import('msgraph.generated.models.security.action_source')
information_protection_action = lazy_import('msgraph.generated.models.security.information_protection_action')

class ApplyLabelAction(information_protection_action.InformationProtectionAction):
    @property
    def actions(self,) -> Optional[List[information_protection_action.InformationProtectionAction]]:
        """
        Gets the actions property value. The collection of actions that should be implemented by the caller.
        Returns: Optional[List[information_protection_action.InformationProtectionAction]]
        """
        return self._actions
    
    @actions.setter
    def actions(self,value: Optional[List[information_protection_action.InformationProtectionAction]] = None) -> None:
        """
        Sets the actions property value. The collection of actions that should be implemented by the caller.
        Args:
            value: Value to set for the actions property.
        """
        self._actions = value
    
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
            value: Value to set for the actionSource property.
        """
        self._action_source = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ApplyLabelAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.applyLabelAction"
        # The collection of actions that should be implemented by the caller.
        self._actions: Optional[List[information_protection_action.InformationProtectionAction]] = None
        # The actionSource property
        self._action_source: Optional[action_source.ActionSource] = None
        # If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
        self._responsible_sensitive_type_ids: Optional[List[str]] = None
        # The sensitivityLabelId property
        self._sensitivity_label_id: Optional[str] = None
    
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
        fields = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(information_protection_action.InformationProtectionAction)),
            "action_source": lambda n : setattr(self, 'action_source', n.get_enum_value(action_source.ActionSource)),
            "responsible_sensitive_type_ids": lambda n : setattr(self, 'responsible_sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "sensitivity_label_id": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def responsible_sensitive_type_ids(self,) -> Optional[List[str]]:
        """
        Gets the responsibleSensitiveTypeIds property value. If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
        Returns: Optional[List[str]]
        """
        return self._responsible_sensitive_type_ids
    
    @responsible_sensitive_type_ids.setter
    def responsible_sensitive_type_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the responsibleSensitiveTypeIds property value. If the label was the result of an automatic classification, supply the list of sensitive info type GUIDs that resulted in the returned label.
        Args:
            value: Value to set for the responsibleSensitiveTypeIds property.
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
            value: Value to set for the sensitivityLabelId property.
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
    


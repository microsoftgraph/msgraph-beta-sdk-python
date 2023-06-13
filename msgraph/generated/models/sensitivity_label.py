from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_mode, auto_labeling, entity, label_action_base, label_policy, sensitivity_label_target

from . import entity

@dataclass
class SensitivityLabel(entity.Entity):
    # The applicableTo property
    applicable_to: Optional[sensitivity_label_target.SensitivityLabelTarget] = None
    # The applicationMode property
    application_mode: Optional[application_mode.ApplicationMode] = None
    # The assignedPolicies property
    assigned_policies: Optional[List[label_policy.LabelPolicy]] = None
    # The autoLabeling property
    auto_labeling: Optional[auto_labeling.AutoLabeling] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The isDefault property
    is_default: Optional[bool] = None
    # The isEndpointProtectionEnabled property
    is_endpoint_protection_enabled: Optional[bool] = None
    # The labelActions property
    label_actions: Optional[List[label_action_base.LabelActionBase]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # The sublabels property
    sublabels: Optional[List[SensitivityLabel]] = None
    # The toolTip property
    tool_tip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitivityLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitivityLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_mode, auto_labeling, entity, label_action_base, label_policy, sensitivity_label_target

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableTo": lambda n : setattr(self, 'applicable_to', n.get_enum_value(sensitivity_label_target.SensitivityLabelTarget)),
            "applicationMode": lambda n : setattr(self, 'application_mode', n.get_enum_value(application_mode.ApplicationMode)),
            "assignedPolicies": lambda n : setattr(self, 'assigned_policies', n.get_collection_of_object_values(label_policy.LabelPolicy)),
            "autoLabeling": lambda n : setattr(self, 'auto_labeling', n.get_object_value(auto_labeling.AutoLabeling)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isEndpointProtectionEnabled": lambda n : setattr(self, 'is_endpoint_protection_enabled', n.get_bool_value()),
            "labelActions": lambda n : setattr(self, 'label_actions', n.get_collection_of_object_values(label_action_base.LabelActionBase)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sublabels": lambda n : setattr(self, 'sublabels', n.get_collection_of_object_values(SensitivityLabel)),
            "toolTip": lambda n : setattr(self, 'tool_tip', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("applicableTo", self.applicable_to)
        writer.write_enum_value("applicationMode", self.application_mode)
        writer.write_collection_of_object_values("assignedPolicies", self.assigned_policies)
        writer.write_object_value("autoLabeling", self.auto_labeling)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isEndpointProtectionEnabled", self.is_endpoint_protection_enabled)
        writer.write_collection_of_object_values("labelActions", self.label_actions)
        writer.write_str_value("name", self.name)
        writer.write_int_value("priority", self.priority)
        writer.write_collection_of_object_values("sublabels", self.sublabels)
        writer.write_str_value("toolTip", self.tool_tip)
    


from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_mode import ApplicationMode
    from .auto_labeling import AutoLabeling
    from .entity import Entity
    from .label_action_base import LabelActionBase
    from .label_action_source import LabelActionSource
    from .label_policy import LabelPolicy
    from .sensitivity_label_target import SensitivityLabelTarget
    from .usage_rights_included import UsageRightsIncluded

from .entity import Entity

@dataclass
class SensitivityLabel(Entity, Parsable):
    # The actionSource property
    action_source: Optional[LabelActionSource] = None
    # The applicableTo property
    applicable_to: Optional[SensitivityLabelTarget] = None
    # The applicationMode property
    application_mode: Optional[ApplicationMode] = None
    # The assignedPolicies property
    assigned_policies: Optional[list[LabelPolicy]] = None
    # The autoLabeling property
    auto_labeling: Optional[AutoLabeling] = None
    # The autoTooltip property
    auto_tooltip: Optional[str] = None
    # The color property
    color: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The isDefault property
    is_default: Optional[bool] = None
    # The isEnabled property
    is_enabled: Optional[bool] = None
    # The isEndpointProtectionEnabled property
    is_endpoint_protection_enabled: Optional[bool] = None
    # The isScopedToUser property
    is_scoped_to_user: Optional[bool] = None
    # The labelActions property
    label_actions: Optional[list[LabelActionBase]] = None
    # The locale property
    locale: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # The rights property
    rights: Optional[UsageRightsIncluded] = None
    # The sublabels property
    sublabels: Optional[list[SensitivityLabel]] = None
    # The toolTip property
    tool_tip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensitivityLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityLabel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensitivityLabel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_mode import ApplicationMode
        from .auto_labeling import AutoLabeling
        from .entity import Entity
        from .label_action_base import LabelActionBase
        from .label_action_source import LabelActionSource
        from .label_policy import LabelPolicy
        from .sensitivity_label_target import SensitivityLabelTarget
        from .usage_rights_included import UsageRightsIncluded

        from .application_mode import ApplicationMode
        from .auto_labeling import AutoLabeling
        from .entity import Entity
        from .label_action_base import LabelActionBase
        from .label_action_source import LabelActionSource
        from .label_policy import LabelPolicy
        from .sensitivity_label_target import SensitivityLabelTarget
        from .usage_rights_included import UsageRightsIncluded

        fields: dict[str, Callable[[Any], None]] = {
            "actionSource": lambda n : setattr(self, 'action_source', n.get_enum_value(LabelActionSource)),
            "applicableTo": lambda n : setattr(self, 'applicable_to', n.get_collection_of_enum_values(SensitivityLabelTarget)),
            "applicationMode": lambda n : setattr(self, 'application_mode', n.get_enum_value(ApplicationMode)),
            "assignedPolicies": lambda n : setattr(self, 'assigned_policies', n.get_collection_of_object_values(LabelPolicy)),
            "autoLabeling": lambda n : setattr(self, 'auto_labeling', n.get_object_value(AutoLabeling)),
            "autoTooltip": lambda n : setattr(self, 'auto_tooltip', n.get_str_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isEndpointProtectionEnabled": lambda n : setattr(self, 'is_endpoint_protection_enabled', n.get_bool_value()),
            "isScopedToUser": lambda n : setattr(self, 'is_scoped_to_user', n.get_bool_value()),
            "labelActions": lambda n : setattr(self, 'label_actions', n.get_collection_of_object_values(LabelActionBase)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "rights": lambda n : setattr(self, 'rights', n.get_object_value(UsageRightsIncluded)),
            "sublabels": lambda n : setattr(self, 'sublabels', n.get_collection_of_object_values(SensitivityLabel)),
            "toolTip": lambda n : setattr(self, 'tool_tip', n.get_str_value()),
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
        writer.write_enum_value("applicableTo", self.applicable_to)
        writer.write_enum_value("applicationMode", self.application_mode)
        writer.write_collection_of_object_values("assignedPolicies", self.assigned_policies)
        writer.write_object_value("autoLabeling", self.auto_labeling)
        writer.write_str_value("autoTooltip", self.auto_tooltip)
        writer.write_str_value("color", self.color)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isEndpointProtectionEnabled", self.is_endpoint_protection_enabled)
        writer.write_bool_value("isScopedToUser", self.is_scoped_to_user)
        writer.write_collection_of_object_values("labelActions", self.label_actions)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("name", self.name)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("rights", self.rights)
        writer.write_collection_of_object_values("sublabels", self.sublabels)
        writer.write_str_value("toolTip", self.tool_tip)
    


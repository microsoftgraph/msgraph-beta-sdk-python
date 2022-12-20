from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_mode = lazy_import('msgraph.generated.models.application_mode')
auto_labeling = lazy_import('msgraph.generated.models.auto_labeling')
entity = lazy_import('msgraph.generated.models.entity')
label_action_base = lazy_import('msgraph.generated.models.label_action_base')
label_policy = lazy_import('msgraph.generated.models.label_policy')
sensitivity_label_target = lazy_import('msgraph.generated.models.sensitivity_label_target')

class SensitivityLabel(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def applicable_to(self,) -> Optional[sensitivity_label_target.SensitivityLabelTarget]:
        """
        Gets the applicableTo property value. The applicableTo property
        Returns: Optional[sensitivity_label_target.SensitivityLabelTarget]
        """
        return self._applicable_to
    
    @applicable_to.setter
    def applicable_to(self,value: Optional[sensitivity_label_target.SensitivityLabelTarget] = None) -> None:
        """
        Sets the applicableTo property value. The applicableTo property
        Args:
            value: Value to set for the applicableTo property.
        """
        self._applicable_to = value
    
    @property
    def application_mode(self,) -> Optional[application_mode.ApplicationMode]:
        """
        Gets the applicationMode property value. The applicationMode property
        Returns: Optional[application_mode.ApplicationMode]
        """
        return self._application_mode
    
    @application_mode.setter
    def application_mode(self,value: Optional[application_mode.ApplicationMode] = None) -> None:
        """
        Sets the applicationMode property value. The applicationMode property
        Args:
            value: Value to set for the applicationMode property.
        """
        self._application_mode = value
    
    @property
    def assigned_policies(self,) -> Optional[List[label_policy.LabelPolicy]]:
        """
        Gets the assignedPolicies property value. The assignedPolicies property
        Returns: Optional[List[label_policy.LabelPolicy]]
        """
        return self._assigned_policies
    
    @assigned_policies.setter
    def assigned_policies(self,value: Optional[List[label_policy.LabelPolicy]] = None) -> None:
        """
        Sets the assignedPolicies property value. The assignedPolicies property
        Args:
            value: Value to set for the assignedPolicies property.
        """
        self._assigned_policies = value
    
    @property
    def auto_labeling(self,) -> Optional[auto_labeling.AutoLabeling]:
        """
        Gets the autoLabeling property value. The autoLabeling property
        Returns: Optional[auto_labeling.AutoLabeling]
        """
        return self._auto_labeling
    
    @auto_labeling.setter
    def auto_labeling(self,value: Optional[auto_labeling.AutoLabeling] = None) -> None:
        """
        Sets the autoLabeling property value. The autoLabeling property
        Args:
            value: Value to set for the autoLabeling property.
        """
        self._auto_labeling = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sensitivityLabel and sets the default values.
        """
        super().__init__()
        # The applicableTo property
        self._applicable_to: Optional[sensitivity_label_target.SensitivityLabelTarget] = None
        # The applicationMode property
        self._application_mode: Optional[application_mode.ApplicationMode] = None
        # The assignedPolicies property
        self._assigned_policies: Optional[List[label_policy.LabelPolicy]] = None
        # The autoLabeling property
        self._auto_labeling: Optional[auto_labeling.AutoLabeling] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The isDefault property
        self._is_default: Optional[bool] = None
        # The isEndpointProtectionEnabled property
        self._is_endpoint_protection_enabled: Optional[bool] = None
        # The labelActions property
        self._label_actions: Optional[List[label_action_base.LabelActionBase]] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The priority property
        self._priority: Optional[int] = None
        # The sublabels property
        self._sublabels: Optional[List[SensitivityLabel]] = None
        # The toolTip property
        self._tool_tip: Optional[str] = None
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_to": lambda n : setattr(self, 'applicable_to', n.get_enum_value(sensitivity_label_target.SensitivityLabelTarget)),
            "application_mode": lambda n : setattr(self, 'application_mode', n.get_enum_value(application_mode.ApplicationMode)),
            "assigned_policies": lambda n : setattr(self, 'assigned_policies', n.get_collection_of_object_values(label_policy.LabelPolicy)),
            "auto_labeling": lambda n : setattr(self, 'auto_labeling', n.get_object_value(auto_labeling.AutoLabeling)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_endpoint_protection_enabled": lambda n : setattr(self, 'is_endpoint_protection_enabled', n.get_bool_value()),
            "label_actions": lambda n : setattr(self, 'label_actions', n.get_collection_of_object_values(label_action_base.LabelActionBase)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sublabels": lambda n : setattr(self, 'sublabels', n.get_collection_of_object_values(SensitivityLabel)),
            "tool_tip": lambda n : setattr(self, 'tool_tip', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. The isDefault property
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. The isDefault property
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_endpoint_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the isEndpointProtectionEnabled property value. The isEndpointProtectionEnabled property
        Returns: Optional[bool]
        """
        return self._is_endpoint_protection_enabled
    
    @is_endpoint_protection_enabled.setter
    def is_endpoint_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEndpointProtectionEnabled property value. The isEndpointProtectionEnabled property
        Args:
            value: Value to set for the isEndpointProtectionEnabled property.
        """
        self._is_endpoint_protection_enabled = value
    
    @property
    def label_actions(self,) -> Optional[List[label_action_base.LabelActionBase]]:
        """
        Gets the labelActions property value. The labelActions property
        Returns: Optional[List[label_action_base.LabelActionBase]]
        """
        return self._label_actions
    
    @label_actions.setter
    def label_actions(self,value: Optional[List[label_action_base.LabelActionBase]] = None) -> None:
        """
        Sets the labelActions property value. The labelActions property
        Args:
            value: Value to set for the labelActions property.
        """
        self._label_actions = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority property
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
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
    
    @property
    def sublabels(self,) -> Optional[List[SensitivityLabel]]:
        """
        Gets the sublabels property value. The sublabels property
        Returns: Optional[List[SensitivityLabel]]
        """
        return self._sublabels
    
    @sublabels.setter
    def sublabels(self,value: Optional[List[SensitivityLabel]] = None) -> None:
        """
        Sets the sublabels property value. The sublabels property
        Args:
            value: Value to set for the sublabels property.
        """
        self._sublabels = value
    
    @property
    def tool_tip(self,) -> Optional[str]:
        """
        Gets the toolTip property value. The toolTip property
        Returns: Optional[str]
        """
        return self._tool_tip
    
    @tool_tip.setter
    def tool_tip(self,value: Optional[str] = None) -> None:
        """
        Sets the toolTip property value. The toolTip property
        Args:
            value: Value to set for the toolTip property.
        """
        self._tool_tip = value
    


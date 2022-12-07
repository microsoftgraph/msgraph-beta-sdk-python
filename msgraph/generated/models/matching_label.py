from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_mode = lazy_import('msgraph.generated.models.application_mode')
label_action_base = lazy_import('msgraph.generated.models.label_action_base')

class MatchingLabel(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new matchingLabel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The applicationMode property
        self._application_mode: Optional[application_mode.ApplicationMode] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The id property
        self._id: Optional[str] = None
        # The isEndpointProtectionEnabled property
        self._is_endpoint_protection_enabled: Optional[bool] = None
        # The labelActions property
        self._label_actions: Optional[List[label_action_base.LabelActionBase]] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The policyTip property
        self._policy_tip: Optional[str] = None
        # The priority property
        self._priority: Optional[int] = None
        # The toolTip property
        self._tool_tip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MatchingLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MatchingLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MatchingLabel()
    
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
            "application_mode": lambda n : setattr(self, 'application_mode', n.get_enum_value(application_mode.ApplicationMode)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_endpoint_protection_enabled": lambda n : setattr(self, 'is_endpoint_protection_enabled', n.get_bool_value()),
            "label_actions": lambda n : setattr(self, 'label_actions', n.get_collection_of_object_values(label_action_base.LabelActionBase)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policy_tip": lambda n : setattr(self, 'policy_tip', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "tool_tip": lambda n : setattr(self, 'tool_tip', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def policy_tip(self,) -> Optional[str]:
        """
        Gets the policyTip property value. The policyTip property
        Returns: Optional[str]
        """
        return self._policy_tip
    
    @policy_tip.setter
    def policy_tip(self,value: Optional[str] = None) -> None:
        """
        Sets the policyTip property value. The policyTip property
        Args:
            value: Value to set for the policyTip property.
        """
        self._policy_tip = value
    
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
        writer.write_enum_value("applicationMode", self.application_mode)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isEndpointProtectionEnabled", self.is_endpoint_protection_enabled)
        writer.write_collection_of_object_values("labelActions", self.label_actions)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyTip", self.policy_tip)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("toolTip", self.tool_tip)
        writer.write_additional_data_value(self.additional_data)
    
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
    


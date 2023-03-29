from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_flow_settings, entity, governance_policy

from . import entity

class GovernancePolicyTemplate(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new governancePolicyTemplate and sets the default values.
        """
        super().__init__()
        # The displayName property
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policy property
        self._policy: Optional[governance_policy.GovernancePolicy] = None
        # The settings property
        self._settings: Optional[business_flow_settings.BusinessFlowSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernancePolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernancePolicyTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernancePolicyTemplate()
    
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
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_flow_settings, entity, governance_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(governance_policy.GovernancePolicy)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(business_flow_settings.BusinessFlowSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policy(self,) -> Optional[governance_policy.GovernancePolicy]:
        """
        Gets the policy property value. The policy property
        Returns: Optional[governance_policy.GovernancePolicy]
        """
        return self._policy
    
    @policy.setter
    def policy(self,value: Optional[governance_policy.GovernancePolicy] = None) -> None:
        """
        Sets the policy property value. The policy property
        Args:
            value: Value to set for the policy property.
        """
        self._policy = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("policy", self.policy)
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[business_flow_settings.BusinessFlowSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[business_flow_settings.BusinessFlowSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[business_flow_settings.BusinessFlowSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    


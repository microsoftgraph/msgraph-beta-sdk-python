from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_set_item = lazy_import('msgraph.generated.models.policy_set_item')

class EnrollmentRestrictionsConfigurationPolicySetItem(policy_set_item.PolicySetItem):
    def __init__(self,) -> None:
        """
        Instantiates a new EnrollmentRestrictionsConfigurationPolicySetItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem"
        # Limit of the EnrollmentRestrictionsConfigurationPolicySetItem.
        self._limit: Optional[int] = None
        # Priority of the EnrollmentRestrictionsConfigurationPolicySetItem.
        self._priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EnrollmentRestrictionsConfigurationPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EnrollmentRestrictionsConfigurationPolicySetItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EnrollmentRestrictionsConfigurationPolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def limit(self,) -> Optional[int]:
        """
        Gets the limit property value. Limit of the EnrollmentRestrictionsConfigurationPolicySetItem.
        Returns: Optional[int]
        """
        return self._limit
    
    @limit.setter
    def limit(self,value: Optional[int] = None) -> None:
        """
        Sets the limit property value. Limit of the EnrollmentRestrictionsConfigurationPolicySetItem.
        Args:
            value: Value to set for the limit property.
        """
        self._limit = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Priority of the EnrollmentRestrictionsConfigurationPolicySetItem.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Priority of the EnrollmentRestrictionsConfigurationPolicySetItem.
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
        writer.write_int_value("limit", self.limit)
        writer.write_int_value("priority", self.priority)
    


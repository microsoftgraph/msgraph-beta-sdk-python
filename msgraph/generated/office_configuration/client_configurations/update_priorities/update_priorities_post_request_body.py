from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UpdatePrioritiesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updatePrioritiesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The officeConfigurationPolicyIds property
        self._office_configuration_policy_ids: Optional[List[str]] = None
        # The officeConfigurationPriorities property
        self._office_configuration_priorities: Optional[List[int]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePrioritiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePrioritiesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdatePrioritiesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "officeConfigurationPolicyIds": lambda n : setattr(self, 'office_configuration_policy_ids', n.get_collection_of_primitive_values(str)),
            "officeConfigurationPriorities": lambda n : setattr(self, 'office_configuration_priorities', n.get_collection_of_primitive_values(int)),
        }
        return fields
    
    @property
    def office_configuration_policy_ids(self,) -> Optional[List[str]]:
        """
        Gets the officeConfigurationPolicyIds property value. The officeConfigurationPolicyIds property
        Returns: Optional[List[str]]
        """
        return self._office_configuration_policy_ids
    
    @office_configuration_policy_ids.setter
    def office_configuration_policy_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the officeConfigurationPolicyIds property value. The officeConfigurationPolicyIds property
        Args:
            value: Value to set for the office_configuration_policy_ids property.
        """
        self._office_configuration_policy_ids = value
    
    @property
    def office_configuration_priorities(self,) -> Optional[List[int]]:
        """
        Gets the officeConfigurationPriorities property value. The officeConfigurationPriorities property
        Returns: Optional[List[int]]
        """
        return self._office_configuration_priorities
    
    @office_configuration_priorities.setter
    def office_configuration_priorities(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the officeConfigurationPriorities property value. The officeConfigurationPriorities property
        Args:
            value: Value to set for the office_configuration_priorities property.
        """
        self._office_configuration_priorities = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("officeConfigurationPolicyIds", self.office_configuration_policy_ids)
        writer.write_collection_of_primitive_values("officeConfigurationPriorities", self.office_configuration_priorities)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class GetPolicySetsPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new getPolicySetsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The policySetIds property
        self._policy_set_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetPolicySetsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetPolicySetsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetPolicySetsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "policy_set_ids": lambda n : setattr(self, 'policy_set_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def policy_set_ids(self,) -> Optional[List[str]]:
        """
        Gets the policySetIds property value. The policySetIds property
        Returns: Optional[List[str]]
        """
        return self._policy_set_ids
    
    @policy_set_ids.setter
    def policy_set_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the policySetIds property value. The policySetIds property
        Args:
            value: Value to set for the policySetIds property.
        """
        self._policy_set_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("policySetIds", self.policy_set_ids)
        writer.write_additional_data_value(self.additional_data)
    


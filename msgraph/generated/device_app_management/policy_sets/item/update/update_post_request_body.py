from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_set_assignment = lazy_import('msgraph.generated.models.policy_set_assignment')
policy_set_item = lazy_import('msgraph.generated.models.policy_set_item')

class UpdatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the update method.
    """
    @property
    def added_policy_set_items(self,) -> Optional[List[policy_set_item.PolicySetItem]]:
        """
        Gets the addedPolicySetItems property value. The addedPolicySetItems property
        Returns: Optional[List[policy_set_item.PolicySetItem]]
        """
        return self._added_policy_set_items
    
    @added_policy_set_items.setter
    def added_policy_set_items(self,value: Optional[List[policy_set_item.PolicySetItem]] = None) -> None:
        """
        Sets the addedPolicySetItems property value. The addedPolicySetItems property
        Args:
            value: Value to set for the addedPolicySetItems property.
        """
        self._added_policy_set_items = value
    
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
    def assignments(self,) -> Optional[List[policy_set_assignment.PolicySetAssignment]]:
        """
        Gets the assignments property value. The assignments property
        Returns: Optional[List[policy_set_assignment.PolicySetAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[policy_set_assignment.PolicySetAssignment]] = None) -> None:
        """
        Sets the assignments property value. The assignments property
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The addedPolicySetItems property
        self._added_policy_set_items: Optional[List[policy_set_item.PolicySetItem]] = None
        # The assignments property
        self._assignments: Optional[List[policy_set_assignment.PolicySetAssignment]] = None
        # The deletedPolicySetItems property
        self._deleted_policy_set_items: Optional[List[str]] = None
        # The updatedPolicySetItems property
        self._updated_policy_set_items: Optional[List[policy_set_item.PolicySetItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdatePostRequestBody()
    
    @property
    def deleted_policy_set_items(self,) -> Optional[List[str]]:
        """
        Gets the deletedPolicySetItems property value. The deletedPolicySetItems property
        Returns: Optional[List[str]]
        """
        return self._deleted_policy_set_items
    
    @deleted_policy_set_items.setter
    def deleted_policy_set_items(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deletedPolicySetItems property value. The deletedPolicySetItems property
        Args:
            value: Value to set for the deletedPolicySetItems property.
        """
        self._deleted_policy_set_items = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "added_policy_set_items": lambda n : setattr(self, 'added_policy_set_items', n.get_collection_of_object_values(policy_set_item.PolicySetItem)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(policy_set_assignment.PolicySetAssignment)),
            "deleted_policy_set_items": lambda n : setattr(self, 'deleted_policy_set_items', n.get_collection_of_primitive_values(str)),
            "updated_policy_set_items": lambda n : setattr(self, 'updated_policy_set_items', n.get_collection_of_object_values(policy_set_item.PolicySetItem)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("addedPolicySetItems", self.added_policy_set_items)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_primitive_values("deletedPolicySetItems", self.deleted_policy_set_items)
        writer.write_collection_of_object_values("updatedPolicySetItems", self.updated_policy_set_items)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def updated_policy_set_items(self,) -> Optional[List[policy_set_item.PolicySetItem]]:
        """
        Gets the updatedPolicySetItems property value. The updatedPolicySetItems property
        Returns: Optional[List[policy_set_item.PolicySetItem]]
        """
        return self._updated_policy_set_items
    
    @updated_policy_set_items.setter
    def updated_policy_set_items(self,value: Optional[List[policy_set_item.PolicySetItem]] = None) -> None:
        """
        Sets the updatedPolicySetItems property value. The updatedPolicySetItems property
        Args:
            value: Value to set for the updatedPolicySetItems property.
        """
        self._updated_policy_set_items = value
    


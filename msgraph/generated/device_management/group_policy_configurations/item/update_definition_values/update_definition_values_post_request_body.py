from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import group_policy_definition_value

class UpdateDefinitionValuesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updateDefinitionValuesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The added property
        self._added: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None
        # The deletedIds property
        self._deleted_ids: Optional[List[str]] = None
        # The updated property
        self._updated: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None
    
    @property
    def added(self,) -> Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]]:
        """
        Gets the added property value. The added property
        Returns: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]]
        """
        return self._added
    
    @added.setter
    def added(self,value: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None) -> None:
        """
        Sets the added property value. The added property
        Args:
            value: Value to set for the added property.
        """
        self._added = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateDefinitionValuesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateDefinitionValuesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateDefinitionValuesPostRequestBody()
    
    @property
    def deleted_ids(self,) -> Optional[List[str]]:
        """
        Gets the deletedIds property value. The deletedIds property
        Returns: Optional[List[str]]
        """
        return self._deleted_ids
    
    @deleted_ids.setter
    def deleted_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deletedIds property value. The deletedIds property
        Args:
            value: Value to set for the deleted_ids property.
        """
        self._deleted_ids = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import group_policy_definition_value

        fields: Dict[str, Callable[[Any], None]] = {
            "added": lambda n : setattr(self, 'added', n.get_collection_of_object_values(group_policy_definition_value.GroupPolicyDefinitionValue)),
            "deletedIds": lambda n : setattr(self, 'deleted_ids', n.get_collection_of_primitive_values(str)),
            "updated": lambda n : setattr(self, 'updated', n.get_collection_of_object_values(group_policy_definition_value.GroupPolicyDefinitionValue)),
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
        writer.write_collection_of_object_values("added", self.added)
        writer.write_collection_of_primitive_values("deletedIds", self.deleted_ids)
        writer.write_collection_of_object_values("updated", self.updated)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def updated(self,) -> Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]]:
        """
        Gets the updated property value. The updated property
        Returns: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]]
        """
        return self._updated
    
    @updated.setter
    def updated(self,value: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None) -> None:
        """
        Sets the updated property value. The updated property
        Args:
            value: Value to set for the updated property.
        """
        self._updated = value
    


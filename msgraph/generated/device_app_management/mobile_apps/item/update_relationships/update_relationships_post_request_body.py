from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_relationship = lazy_import('msgraph.generated.models.mobile_app_relationship')

class UpdateRelationshipsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateRelationships method.
    """
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
        Instantiates a new updateRelationshipsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The relationships property
        self._relationships: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateRelationshipsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateRelationshipsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateRelationshipsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "relationships": lambda n : setattr(self, 'relationships', n.get_collection_of_object_values(mobile_app_relationship.MobileAppRelationship)),
        }
        return fields
    
    @property
    def relationships(self,) -> Optional[List[mobile_app_relationship.MobileAppRelationship]]:
        """
        Gets the relationships property value. The relationships property
        Returns: Optional[List[mobile_app_relationship.MobileAppRelationship]]
        """
        return self._relationships
    
    @relationships.setter
    def relationships(self,value: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None) -> None:
        """
        Sets the relationships property value. The relationships property
        Args:
            value: Value to set for the relationships property.
        """
        self._relationships = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("relationships", self.relationships)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

tag = lazy_import('msgraph.generated.models.ediscovery.tag')

class ApplyTagsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the applyTags method.
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
        Instantiates a new applyTagsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The tagsToAdd property
        self._tags_to_add: Optional[List[tag.Tag]] = None
        # The tagsToRemove property
        self._tags_to_remove: Optional[List[tag.Tag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyTagsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplyTagsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplyTagsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "tags_to_add": lambda n : setattr(self, 'tags_to_add', n.get_collection_of_object_values(tag.Tag)),
            "tags_to_remove": lambda n : setattr(self, 'tags_to_remove', n.get_collection_of_object_values(tag.Tag)),
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
        writer.write_collection_of_object_values("tagsToAdd", self.tags_to_add)
        writer.write_collection_of_object_values("tagsToRemove", self.tags_to_remove)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tags_to_add(self,) -> Optional[List[tag.Tag]]:
        """
        Gets the tagsToAdd property value. The tagsToAdd property
        Returns: Optional[List[tag.Tag]]
        """
        return self._tags_to_add
    
    @tags_to_add.setter
    def tags_to_add(self,value: Optional[List[tag.Tag]] = None) -> None:
        """
        Sets the tagsToAdd property value. The tagsToAdd property
        Args:
            value: Value to set for the tagsToAdd property.
        """
        self._tags_to_add = value
    
    @property
    def tags_to_remove(self,) -> Optional[List[tag.Tag]]:
        """
        Gets the tagsToRemove property value. The tagsToRemove property
        Returns: Optional[List[tag.Tag]]
        """
        return self._tags_to_remove
    
    @tags_to_remove.setter
    def tags_to_remove(self,value: Optional[List[tag.Tag]] = None) -> None:
        """
        Sets the tagsToRemove property value. The tagsToRemove property
        Args:
            value: Value to set for the tagsToRemove property.
        """
        self._tags_to_remove = value
    


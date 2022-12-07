from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

additional_data_options = lazy_import('msgraph.generated.models.ediscovery.additional_data_options')
source_collection = lazy_import('msgraph.generated.models.ediscovery.source_collection')

class AddToReviewSetPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the addToReviewSet method.
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
    
    @property
    def additional_data_options(self,) -> Optional[additional_data_options.AdditionalDataOptions]:
        """
        Gets the additionalDataOptions property value. The additionalDataOptions property
        Returns: Optional[additional_data_options.AdditionalDataOptions]
        """
        return self._additional_data_options
    
    @additional_data_options.setter
    def additional_data_options(self,value: Optional[additional_data_options.AdditionalDataOptions] = None) -> None:
        """
        Sets the additionalDataOptions property value. The additionalDataOptions property
        Args:
            value: Value to set for the additionalDataOptions property.
        """
        self._additional_data_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new addToReviewSetPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The additionalDataOptions property
        self._additional_data_options: Optional[additional_data_options.AdditionalDataOptions] = None
        # The sourceCollection property
        self._source_collection: Optional[source_collection.SourceCollection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddToReviewSetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddToReviewSetPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_data_options": lambda n : setattr(self, 'additional_data_options', n.get_enum_value(additional_data_options.AdditionalDataOptions)),
            "source_collection": lambda n : setattr(self, 'source_collection', n.get_object_value(source_collection.SourceCollection)),
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
        writer.write_enum_value("additionalDataOptions", self.additional_data_options)
        writer.write_object_value("sourceCollection", self.source_collection)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_collection(self,) -> Optional[source_collection.SourceCollection]:
        """
        Gets the sourceCollection property value. The sourceCollection property
        Returns: Optional[source_collection.SourceCollection]
        """
        return self._source_collection
    
    @source_collection.setter
    def source_collection(self,value: Optional[source_collection.SourceCollection] = None) -> None:
        """
        Sets the sourceCollection property value. The sourceCollection property
        Args:
            value: Value to set for the sourceCollection property.
        """
        self._source_collection = value
    


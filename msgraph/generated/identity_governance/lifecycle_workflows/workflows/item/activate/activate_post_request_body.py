from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user = lazy_import('msgraph.generated.models.user')

class ActivatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the activate method.
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
        Instantiates a new activatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The subjects property
        self._subjects: Optional[List[user.User]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(user.User)),
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
        writer.write_collection_of_object_values("subjects", self.subjects)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subjects(self,) -> Optional[List[user.User]]:
        """
        Gets the subjects property value. The subjects property
        Returns: Optional[List[user.User]]
        """
        return self._subjects
    
    @subjects.setter
    def subjects(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the subjects property value. The subjects property
        Args:
            value: Value to set for the subjects property.
        """
        self._subjects = value
    


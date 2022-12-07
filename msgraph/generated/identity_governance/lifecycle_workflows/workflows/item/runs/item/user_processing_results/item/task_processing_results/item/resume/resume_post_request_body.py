from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_task_extension_callback_data = lazy_import('msgraph.generated.models.identity_governance.custom_task_extension_callback_data')

class ResumePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the resume method.
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
        Instantiates a new resumePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The data property
        self._data: Optional[custom_task_extension_callback_data.CustomTaskExtensionCallbackData] = None
        # The source property
        self._source: Optional[str] = None
        # The type property
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResumePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResumePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResumePostRequestBody()
    
    @property
    def data(self,) -> Optional[custom_task_extension_callback_data.CustomTaskExtensionCallbackData]:
        """
        Gets the data property value. The data property
        Returns: Optional[custom_task_extension_callback_data.CustomTaskExtensionCallbackData]
        """
        return self._data
    
    @data.setter
    def data(self,value: Optional[custom_task_extension_callback_data.CustomTaskExtensionCallbackData] = None) -> None:
        """
        Sets the data property value. The data property
        Args:
            value: Value to set for the data property.
        """
        self._data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(custom_task_extension_callback_data.CustomTaskExtensionCallbackData)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_str_value("source", self.source)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source(self,) -> Optional[str]:
        """
        Gets the source property value. The source property
        Returns: Optional[str]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[str] = None) -> None:
        """
        Sets the source property value. The source property
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    


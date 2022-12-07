from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ImportResourceActionsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the importResourceActions method.
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
        Instantiates a new importResourceActionsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The format property
        self._format: Optional[str] = None
        # The overwriteResourceNamespace property
        self._overwrite_resource_namespace: Optional[bool] = None
        # The value property
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportResourceActionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportResourceActionsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportResourceActionsPostRequestBody()
    
    @property
    def format(self,) -> Optional[str]:
        """
        Gets the format property value. The format property
        Returns: Optional[str]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[str] = None) -> None:
        """
        Sets the format property value. The format property
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "overwrite_resource_namespace": lambda n : setattr(self, 'overwrite_resource_namespace', n.get_bool_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        return fields
    
    @property
    def overwrite_resource_namespace(self,) -> Optional[bool]:
        """
        Gets the overwriteResourceNamespace property value. The overwriteResourceNamespace property
        Returns: Optional[bool]
        """
        return self._overwrite_resource_namespace
    
    @overwrite_resource_namespace.setter
    def overwrite_resource_namespace(self,value: Optional[bool] = None) -> None:
        """
        Sets the overwriteResourceNamespace property value. The overwriteResourceNamespace property
        Args:
            value: Value to set for the overwriteResourceNamespace property.
        """
        self._overwrite_resource_namespace = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("format", self.format)
        writer.write_bool_value("overwriteResourceNamespace", self.overwrite_resource_namespace)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. The value property
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    


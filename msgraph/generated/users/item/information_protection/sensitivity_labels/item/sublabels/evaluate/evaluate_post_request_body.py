from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

current_label = lazy_import('msgraph.generated.models.current_label')
discovered_sensitive_type = lazy_import('msgraph.generated.models.discovered_sensitive_type')

class EvaluatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the evaluate method.
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
        Instantiates a new evaluatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The currentLabel property
        self._current_label: Optional[current_label.CurrentLabel] = None
        # The discoveredSensitiveTypes property
        self._discovered_sensitive_types: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluatePostRequestBody()
    
    @property
    def current_label(self,) -> Optional[current_label.CurrentLabel]:
        """
        Gets the currentLabel property value. The currentLabel property
        Returns: Optional[current_label.CurrentLabel]
        """
        return self._current_label
    
    @current_label.setter
    def current_label(self,value: Optional[current_label.CurrentLabel] = None) -> None:
        """
        Sets the currentLabel property value. The currentLabel property
        Args:
            value: Value to set for the currentLabel property.
        """
        self._current_label = value
    
    @property
    def discovered_sensitive_types(self,) -> Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]]:
        """
        Gets the discoveredSensitiveTypes property value. The discoveredSensitiveTypes property
        Returns: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]]
        """
        return self._discovered_sensitive_types
    
    @discovered_sensitive_types.setter
    def discovered_sensitive_types(self,value: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]] = None) -> None:
        """
        Sets the discoveredSensitiveTypes property value. The discoveredSensitiveTypes property
        Args:
            value: Value to set for the discoveredSensitiveTypes property.
        """
        self._discovered_sensitive_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "current_label": lambda n : setattr(self, 'current_label', n.get_object_value(current_label.CurrentLabel)),
            "discovered_sensitive_types": lambda n : setattr(self, 'discovered_sensitive_types', n.get_collection_of_object_values(discovered_sensitive_type.DiscoveredSensitiveType)),
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
        writer.write_object_value("currentLabel", self.current_label)
        writer.write_collection_of_object_values("discoveredSensitiveTypes", self.discovered_sensitive_types)
        writer.write_additional_data_value(self.additional_data)
    


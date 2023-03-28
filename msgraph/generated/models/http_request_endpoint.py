from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_extension_endpoint_configuration

from . import custom_extension_endpoint_configuration

class HttpRequestEndpoint(custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new HttpRequestEndpoint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.httpRequestEndpoint"
        # The targetUrl property
        self._target_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HttpRequestEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HttpRequestEndpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HttpRequestEndpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_extension_endpoint_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "targetUrl": lambda n : setattr(self, 'target_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("targetUrl", self.target_url)
    
    @property
    def target_url(self,) -> Optional[str]:
        """
        Gets the targetUrl property value. The targetUrl property
        Returns: Optional[str]
        """
        return self._target_url
    
    @target_url.setter
    def target_url(self,value: Optional[str] = None) -> None:
        """
        Sets the targetUrl property value. The targetUrl property
        Args:
            value: Value to set for the target_url property.
        """
        self._target_url = value
    


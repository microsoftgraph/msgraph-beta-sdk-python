from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

on_token_issuance_start_custom_extension = lazy_import('msgraph.generated.models.on_token_issuance_start_custom_extension')
on_token_issuance_start_handler = lazy_import('msgraph.generated.models.on_token_issuance_start_handler')

class OnTokenIssuanceStartCustomExtensionHandler(on_token_issuance_start_handler.OnTokenIssuanceStartHandler):
    def __init__(self,) -> None:
        """
        Instantiates a new OnTokenIssuanceStartCustomExtensionHandler and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onTokenIssuanceStartCustomExtensionHandler"
        # The customExtension property
        self._custom_extension: Optional[on_token_issuance_start_custom_extension.OnTokenIssuanceStartCustomExtension] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnTokenIssuanceStartCustomExtensionHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnTokenIssuanceStartCustomExtensionHandler
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnTokenIssuanceStartCustomExtensionHandler()
    
    @property
    def custom_extension(self,) -> Optional[on_token_issuance_start_custom_extension.OnTokenIssuanceStartCustomExtension]:
        """
        Gets the customExtension property value. The customExtension property
        Returns: Optional[on_token_issuance_start_custom_extension.OnTokenIssuanceStartCustomExtension]
        """
        return self._custom_extension
    
    @custom_extension.setter
    def custom_extension(self,value: Optional[on_token_issuance_start_custom_extension.OnTokenIssuanceStartCustomExtension] = None) -> None:
        """
        Sets the customExtension property value. The customExtension property
        Args:
            value: Value to set for the customExtension property.
        """
        self._custom_extension = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_extension": lambda n : setattr(self, 'custom_extension', n.get_object_value(on_token_issuance_start_custom_extension.OnTokenIssuanceStartCustomExtension)),
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
        writer.write_object_value("customExtension", self.custom_extension)
    


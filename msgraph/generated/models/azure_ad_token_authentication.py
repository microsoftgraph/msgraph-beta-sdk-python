from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_extension_authentication_configuration = lazy_import('msgraph.generated.models.custom_extension_authentication_configuration')

class AzureAdTokenAuthentication(custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AzureAdTokenAuthentication and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.azureAdTokenAuthentication"
        # The appID of the Azure AD application to use to authenticate a logic app with a custom access package workflow extension.
        self._resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureAdTokenAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AzureAdTokenAuthentication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AzureAdTokenAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The appID of the Azure AD application to use to authenticate a logic app with a custom access package workflow extension.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The appID of the Azure AD application to use to authenticate a logic app with a custom access package workflow extension.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("resourceId", self.resource_id)
    


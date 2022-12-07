from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class TeamsAppSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamsAppSettings and sets the default values.
        """
        super().__init__()
        # Indicates whether resource-specific consent for chats/meetings has been enabled for the tenant. If true, Teams apps that are allowed in the tenant and require resource-specific permissions can be installed inside chats and meetings. If false, the installation of any Teams app that requires resource-specific permissions in a chat or a meeting will be blocked.
        self._is_chat_resource_specific_consent_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_chat_resource_specific_consent_enabled": lambda n : setattr(self, 'is_chat_resource_specific_consent_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_chat_resource_specific_consent_enabled(self,) -> Optional[bool]:
        """
        Gets the isChatResourceSpecificConsentEnabled property value. Indicates whether resource-specific consent for chats/meetings has been enabled for the tenant. If true, Teams apps that are allowed in the tenant and require resource-specific permissions can be installed inside chats and meetings. If false, the installation of any Teams app that requires resource-specific permissions in a chat or a meeting will be blocked.
        Returns: Optional[bool]
        """
        return self._is_chat_resource_specific_consent_enabled
    
    @is_chat_resource_specific_consent_enabled.setter
    def is_chat_resource_specific_consent_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isChatResourceSpecificConsentEnabled property value. Indicates whether resource-specific consent for chats/meetings has been enabled for the tenant. If true, Teams apps that are allowed in the tenant and require resource-specific permissions can be installed inside chats and meetings. If false, the installation of any Teams app that requires resource-specific permissions in a chat or a meeting will be blocked.
        Args:
            value: Value to set for the isChatResourceSpecificConsentEnabled property.
        """
        self._is_chat_resource_specific_consent_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isChatResourceSpecificConsentEnabled", self.is_chat_resource_specific_consent_enabled)
    


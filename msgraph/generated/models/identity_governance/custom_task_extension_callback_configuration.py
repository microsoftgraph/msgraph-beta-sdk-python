from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import application, custom_extension_callback_configuration

from .. import custom_extension_callback_configuration

class CustomTaskExtensionCallbackConfiguration(custom_extension_callback_configuration.CustomExtensionCallbackConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomTaskExtensionCallbackConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.customTaskExtensionCallbackConfiguration"
        # The authorizedApps property
        self._authorized_apps: Optional[List[application.Application]] = None
    
    @property
    def authorized_apps(self,) -> Optional[List[application.Application]]:
        """
        Gets the authorizedApps property value. The authorizedApps property
        Returns: Optional[List[application.Application]]
        """
        return self._authorized_apps
    
    @authorized_apps.setter
    def authorized_apps(self,value: Optional[List[application.Application]] = None) -> None:
        """
        Sets the authorizedApps property value. The authorizedApps property
        Args:
            value: Value to set for the authorized_apps property.
        """
        self._authorized_apps = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtensionCallbackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCallbackConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomTaskExtensionCallbackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import application, custom_extension_callback_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "authorizedApps": lambda n : setattr(self, 'authorized_apps', n.get_collection_of_object_values(application.Application)),
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
        writer.write_collection_of_object_values("authorizedApps", self.authorized_apps)
    


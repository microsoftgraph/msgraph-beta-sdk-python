from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_identifier = lazy_import('msgraph.generated.models.mobile_app_identifier')

class WindowsAppIdentifier(mobile_app_identifier.MobileAppIdentifier):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsAppIdentifier and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsAppIdentifier"
        # The identifier for an app, as specified in the app store.
        self._windows_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAppIdentifier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAppIdentifier
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsAppIdentifier()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "windows_app_id": lambda n : setattr(self, 'windows_app_id', n.get_str_value()),
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
        writer.write_str_value("windowsAppId", self.windows_app_id)
    
    @property
    def windows_app_id(self,) -> Optional[str]:
        """
        Gets the windowsAppId property value. The identifier for an app, as specified in the app store.
        Returns: Optional[str]
        """
        return self._windows_app_id
    
    @windows_app_id.setter
    def windows_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the windowsAppId property value. The identifier for an app, as specified in the app store.
        Args:
            value: Value to set for the windowsAppId property.
        """
        self._windows_app_id = value
    


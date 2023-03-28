from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import managed_app_registration

from . import managed_app_registration

class AndroidManagedAppRegistration(managed_app_registration.ManagedAppRegistration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidManagedAppRegistration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidManagedAppRegistration"
        # The patch version for the current android app registration
        self._patch_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedAppRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedAppRegistration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedAppRegistration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import managed_app_registration

        fields: Dict[str, Callable[[Any], None]] = {
            "patchVersion": lambda n : setattr(self, 'patch_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def patch_version(self,) -> Optional[str]:
        """
        Gets the patchVersion property value. The patch version for the current android app registration
        Returns: Optional[str]
        """
        return self._patch_version
    
    @patch_version.setter
    def patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the patchVersion property value. The patch version for the current android app registration
        Args:
            value: Value to set for the patch_version property.
        """
        self._patch_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("patchVersion", self.patch_version)
    


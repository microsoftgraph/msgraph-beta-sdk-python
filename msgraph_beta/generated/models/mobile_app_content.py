from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_content_file import MobileAppContentFile
    from .mobile_app_content_script import MobileAppContentScript
    from .mobile_contained_app import MobileContainedApp

from .entity import Entity

@dataclass
class MobileAppContent(Entity, Parsable):
    """
    Contains content properties for a specific app version. Each mobileAppContent can have multiple mobileAppContentFile.
    """
    # The collection of contained apps in a MobileLobApp acting as a package.
    contained_apps: Optional[list[MobileContainedApp]] = None
    # The list of files for this app content version.
    files: Optional[list[MobileAppContentFile]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of scripts for this app content version.
    scripts: Optional[list[MobileAppContentScript]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_content_file import MobileAppContentFile
        from .mobile_app_content_script import MobileAppContentScript
        from .mobile_contained_app import MobileContainedApp

        from .entity import Entity
        from .mobile_app_content_file import MobileAppContentFile
        from .mobile_app_content_script import MobileAppContentScript
        from .mobile_contained_app import MobileContainedApp

        fields: dict[str, Callable[[Any], None]] = {
            "containedApps": lambda n : setattr(self, 'contained_apps', n.get_collection_of_object_values(MobileContainedApp)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(MobileAppContentFile)),
            "scripts": lambda n : setattr(self, 'scripts', n.get_collection_of_object_values(MobileAppContentScript)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("containedApps", self.contained_apps)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_collection_of_object_values("scripts", self.scripts)
    


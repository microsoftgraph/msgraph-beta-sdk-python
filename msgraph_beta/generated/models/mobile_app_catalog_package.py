from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

from .entity import Entity

@dataclass
class MobileAppCatalogPackage(Entity, Parsable):
    """
    mobileAppCatalogPackage is an abstract type that application catalog package entities derive from. A mobileAppCatalogPackage entity contains information about an application catalog package that can be deployed to Intune-managed devices.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppCatalogPackage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppCatalogPackage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32MobileAppCatalogPackage".casefold():
            from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

            return Win32MobileAppCatalogPackage()
        return MobileAppCatalogPackage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

        from .entity import Entity
        from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

        fields: dict[str, Callable[[Any], None]] = {
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
    


from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class WindowsAutoUpdateCatalogApp(MobileApp, Parsable):
    """
    A mobileApp that is based on a referenced branch in a Win32CatalogApp repository
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsAutoUpdateCatalogApp"
    # The identifier of a specific branch in a product, which is a specific subset of product functionality as defined by the publisher . This is run-time resolved to be the latest MobileAppCatalogPackage in the branch. (example:'31a4c766-f23d-8d41-4803-35e155be7389'). Read-Only
    mobile_app_catalog_package_branch_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAutoUpdateCatalogApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutoUpdateCatalogApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsAutoUpdateCatalogApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app import MobileApp

        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "mobileAppCatalogPackageBranchId": lambda n : setattr(self, 'mobile_app_catalog_package_branch_id', n.get_str_value()),
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
        writer.write_str_value("mobileAppCatalogPackageBranchId", self.mobile_app_catalog_package_branch_id)
    


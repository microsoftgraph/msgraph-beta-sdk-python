from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_package_information, windows_phone81_app_x

from . import windows_phone81_app_x

@dataclass
class WindowsPhone81AppXBundle(windows_phone81_app_x.WindowsPhone81AppX):
    odata_type = "#microsoft.graph.windowsPhone81AppXBundle"
    # The list of AppX Package Information.
    app_x_package_information_list: Optional[List[windows_package_information.WindowsPackageInformation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81AppXBundle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81AppXBundle
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhone81AppXBundle()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_package_information, windows_phone81_app_x

        from . import windows_package_information, windows_phone81_app_x

        fields: Dict[str, Callable[[Any], None]] = {
            "appXPackageInformationList": lambda n : setattr(self, 'app_x_package_information_list', n.get_collection_of_object_values(windows_package_information.WindowsPackageInformation)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("appXPackageInformationList", self.app_x_package_information_list)
    


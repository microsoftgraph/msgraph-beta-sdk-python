from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_package_information = lazy_import('msgraph.generated.models.windows_package_information')
windows_phone81_app_x = lazy_import('msgraph.generated.models.windows_phone81_app_x')

class WindowsPhone81AppXBundle(windows_phone81_app_x.WindowsPhone81AppX):
    @property
    def app_x_package_information_list(self,) -> Optional[List[windows_package_information.WindowsPackageInformation]]:
        """
        Gets the appXPackageInformationList property value. The list of AppX Package Information.
        Returns: Optional[List[windows_package_information.WindowsPackageInformation]]
        """
        return self._app_x_package_information_list
    
    @app_x_package_information_list.setter
    def app_x_package_information_list(self,value: Optional[List[windows_package_information.WindowsPackageInformation]] = None) -> None:
        """
        Sets the appXPackageInformationList property value. The list of AppX Package Information.
        Args:
            value: Value to set for the appXPackageInformationList property.
        """
        self._app_x_package_information_list = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsPhone81AppXBundle and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81AppXBundle"
        # The list of AppX Package Information.
        self._app_x_package_information_list: Optional[List[windows_package_information.WindowsPackageInformation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81AppXBundle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81AppXBundle
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81AppXBundle()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_x_package_information_list": lambda n : setattr(self, 'app_x_package_information_list', n.get_collection_of_object_values(windows_package_information.WindowsPackageInformation)),
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
        writer.write_collection_of_object_values("appXPackageInformationList", self.app_x_package_information_list)
    


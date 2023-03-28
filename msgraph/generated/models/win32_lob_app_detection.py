from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import win32_lob_app_file_system_detection, win32_lob_app_power_shell_script_detection, win32_lob_app_product_code_detection, win32_lob_app_registry_detection

class Win32LobAppDetection(AdditionalDataHolder, Parsable):
    """
    Base class to detect a Win32 App
    """
    def __init__(self,) -> None:
        """
        Instantiates a new win32LobAppDetection and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppDetection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.win32LobAppFileSystemDetection":
                from . import win32_lob_app_file_system_detection

                return win32_lob_app_file_system_detection.Win32LobAppFileSystemDetection()
            if mapping_value == "#microsoft.graph.win32LobAppPowerShellScriptDetection":
                from . import win32_lob_app_power_shell_script_detection

                return win32_lob_app_power_shell_script_detection.Win32LobAppPowerShellScriptDetection()
            if mapping_value == "#microsoft.graph.win32LobAppProductCodeDetection":
                from . import win32_lob_app_product_code_detection

                return win32_lob_app_product_code_detection.Win32LobAppProductCodeDetection()
            if mapping_value == "#microsoft.graph.win32LobAppRegistryDetection":
                from . import win32_lob_app_registry_detection

                return win32_lob_app_registry_detection.Win32LobAppRegistryDetection()
        return Win32LobAppDetection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import win32_lob_app_file_system_detection, win32_lob_app_power_shell_script_detection, win32_lob_app_product_code_detection, win32_lob_app_registry_detection

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


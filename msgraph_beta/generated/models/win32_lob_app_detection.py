from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection
    from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection
    from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection
    from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection

@dataclass
class Win32LobAppDetection(AdditionalDataHolder, BackedModel, Parsable):
    """
    Base class to detect a Win32 App
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppDetection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppFileSystemDetection".casefold():
            from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection

            return Win32LobAppFileSystemDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppPowerShellScriptDetection".casefold():
            from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection

            return Win32LobAppPowerShellScriptDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppProductCodeDetection".casefold():
            from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection

            return Win32LobAppProductCodeDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppRegistryDetection".casefold():
            from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection

            return Win32LobAppRegistryDetection()
        return Win32LobAppDetection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection
        from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection
        from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection
        from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection

        from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection
        from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection
        from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection
        from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


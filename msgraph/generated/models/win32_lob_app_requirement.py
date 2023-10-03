from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
    from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement
    from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement
    from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement

@dataclass
class Win32LobAppRequirement(AdditionalDataHolder, BackedModel, Parsable):
    """
    Base class to detect a Win32 App
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The detection value
    detection_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains properties for detection operator.
    operator: Optional[Win32LobAppDetectionOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRequirement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppFileSystemRequirement".casefold():
            from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement

            return Win32LobAppFileSystemRequirement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppPowerShellScriptRequirement".casefold():
            from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement

            return Win32LobAppPowerShellScriptRequirement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppRegistryRequirement".casefold():
            from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement

            return Win32LobAppRegistryRequirement()
        return Win32LobAppRequirement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
        from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement
        from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement
        from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement

        from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
        from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement
        from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement
        from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement

        fields: Dict[str, Callable[[Any], None]] = {
            "detectionValue": lambda n : setattr(self, 'detection_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_collection_of_enum_values(Win32LobAppDetectionOperator)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("detectionValue", self.detection_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_additional_data_value(self.additional_data)
    


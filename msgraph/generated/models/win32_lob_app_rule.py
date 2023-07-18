from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule
    from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule
    from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule
    from .win32_lob_app_registry_rule import Win32LobAppRegistryRule
    from .win32_lob_app_rule_type import Win32LobAppRuleType

@dataclass
class Win32LobAppRule(AdditionalDataHolder, Parsable):
    """
    A base complex type to store the detection or requirement rule data for a Win32 LOB app.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Contains rule types for Win32 LOB apps.
    rule_type: Optional[Win32LobAppRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppFileSystemRule".casefold():
            from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule

            return Win32LobAppFileSystemRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppPowerShellScriptRule".casefold():
            from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule

            return Win32LobAppPowerShellScriptRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppProductCodeRule".casefold():
            from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule

            return Win32LobAppProductCodeRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppRegistryRule".casefold():
            from .win32_lob_app_registry_rule import Win32LobAppRegistryRule

            return Win32LobAppRegistryRule()
        return Win32LobAppRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule
        from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule
        from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule
        from .win32_lob_app_registry_rule import Win32LobAppRegistryRule
        from .win32_lob_app_rule_type import Win32LobAppRuleType

        from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule
        from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule
        from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule
        from .win32_lob_app_registry_rule import Win32LobAppRegistryRule
        from .win32_lob_app_rule_type import Win32LobAppRuleType

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(Win32LobAppRuleType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleType", self.rule_type)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_setting_scope

from . import entity

@dataclass
class UnsupportedGroupPolicyExtension(entity.Entity):
    """
    Unsupported Group Policy Extension.
    """
    # ExtensionType of the unsupported extension.
    extension_type: Optional[str] = None
    # Namespace Url of the unsupported extension.
    namespace_url: Optional[str] = None
    # Node name of the unsupported extension.
    node_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Scope of the group policy setting.
    setting_scope: Optional[group_policy_setting_scope.GroupPolicySettingScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnsupportedGroupPolicyExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnsupportedGroupPolicyExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnsupportedGroupPolicyExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_setting_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "extensionType": lambda n : setattr(self, 'extension_type', n.get_str_value()),
            "namespaceUrl": lambda n : setattr(self, 'namespace_url', n.get_str_value()),
            "nodeName": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "settingScope": lambda n : setattr(self, 'setting_scope', n.get_enum_value(group_policy_setting_scope.GroupPolicySettingScope)),
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
        writer.write_str_value("extensionType", self.extension_type)
        writer.write_str_value("namespaceUrl", self.namespace_url)
        writer.write_str_value("nodeName", self.node_name)
        writer.write_enum_value("settingScope", self.setting_scope)
    


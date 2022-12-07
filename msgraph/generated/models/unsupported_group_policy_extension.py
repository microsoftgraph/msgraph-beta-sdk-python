from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_setting_scope = lazy_import('msgraph.generated.models.group_policy_setting_scope')

class UnsupportedGroupPolicyExtension(entity.Entity):
    """
    Unsupported Group Policy Extension.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new unsupportedGroupPolicyExtension and sets the default values.
        """
        super().__init__()
        # ExtensionType of the unsupported extension.
        self._extension_type: Optional[str] = None
        # Namespace Url of the unsupported extension.
        self._namespace_url: Optional[str] = None
        # Node name of the unsupported extension.
        self._node_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Scope of the group policy setting.
        self._setting_scope: Optional[group_policy_setting_scope.GroupPolicySettingScope] = None
    
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
    
    @property
    def extension_type(self,) -> Optional[str]:
        """
        Gets the extensionType property value. ExtensionType of the unsupported extension.
        Returns: Optional[str]
        """
        return self._extension_type
    
    @extension_type.setter
    def extension_type(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionType property value. ExtensionType of the unsupported extension.
        Args:
            value: Value to set for the extensionType property.
        """
        self._extension_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "extension_type": lambda n : setattr(self, 'extension_type', n.get_str_value()),
            "namespace_url": lambda n : setattr(self, 'namespace_url', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "setting_scope": lambda n : setattr(self, 'setting_scope', n.get_enum_value(group_policy_setting_scope.GroupPolicySettingScope)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def namespace_url(self,) -> Optional[str]:
        """
        Gets the namespaceUrl property value. Namespace Url of the unsupported extension.
        Returns: Optional[str]
        """
        return self._namespace_url
    
    @namespace_url.setter
    def namespace_url(self,value: Optional[str] = None) -> None:
        """
        Sets the namespaceUrl property value. Namespace Url of the unsupported extension.
        Args:
            value: Value to set for the namespaceUrl property.
        """
        self._namespace_url = value
    
    @property
    def node_name(self,) -> Optional[str]:
        """
        Gets the nodeName property value. Node name of the unsupported extension.
        Returns: Optional[str]
        """
        return self._node_name
    
    @node_name.setter
    def node_name(self,value: Optional[str] = None) -> None:
        """
        Sets the nodeName property value. Node name of the unsupported extension.
        Args:
            value: Value to set for the nodeName property.
        """
        self._node_name = value
    
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
    
    @property
    def setting_scope(self,) -> Optional[group_policy_setting_scope.GroupPolicySettingScope]:
        """
        Gets the settingScope property value. Scope of the group policy setting.
        Returns: Optional[group_policy_setting_scope.GroupPolicySettingScope]
        """
        return self._setting_scope
    
    @setting_scope.setter
    def setting_scope(self,value: Optional[group_policy_setting_scope.GroupPolicySettingScope] = None) -> None:
        """
        Sets the settingScope property value. Scope of the group policy setting.
        Args:
            value: Value to set for the settingScope property.
        """
        self._setting_scope = value
    


from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_single_sign_on_extension = lazy_import('msgraph.generated.models.ios_single_sign_on_extension')
key_typed_value_pair = lazy_import('msgraph.generated.models.key_typed_value_pair')

class IosAzureAdSingleSignOnExtension(ios_single_sign_on_extension.IosSingleSignOnExtension):
    @property
    def bundle_id_access_control_list(self,) -> Optional[List[str]]:
        """
        Gets the bundleIdAccessControlList property value. An optional list of additional bundle IDs allowed to use the AAD extension for single sign-on.
        Returns: Optional[List[str]]
        """
        return self._bundle_id_access_control_list
    
    @bundle_id_access_control_list.setter
    def bundle_id_access_control_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the bundleIdAccessControlList property value. An optional list of additional bundle IDs allowed to use the AAD extension for single sign-on.
        Args:
            value: Value to set for the bundleIdAccessControlList property.
        """
        self._bundle_id_access_control_list = value
    
    @property
    def configurations(self,) -> Optional[List[key_typed_value_pair.KeyTypedValuePair]]:
        """
        Gets the configurations property value. Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[key_typed_value_pair.KeyTypedValuePair]]
        """
        return self._configurations
    
    @configurations.setter
    def configurations(self,value: Optional[List[key_typed_value_pair.KeyTypedValuePair]] = None) -> None:
        """
        Sets the configurations property value. Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the configurations property.
        """
        self._configurations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosAzureAdSingleSignOnExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosAzureAdSingleSignOnExtension"
        # An optional list of additional bundle IDs allowed to use the AAD extension for single sign-on.
        self._bundle_id_access_control_list: Optional[List[str]] = None
        # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
        self._configurations: Optional[List[key_typed_value_pair.KeyTypedValuePair]] = None
        # Enables or disables shared device mode.
        self._enable_shared_device_mode: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosAzureAdSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosAzureAdSingleSignOnExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosAzureAdSingleSignOnExtension()
    
    @property
    def enable_shared_device_mode(self,) -> Optional[bool]:
        """
        Gets the enableSharedDeviceMode property value. Enables or disables shared device mode.
        Returns: Optional[bool]
        """
        return self._enable_shared_device_mode
    
    @enable_shared_device_mode.setter
    def enable_shared_device_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSharedDeviceMode property value. Enables or disables shared device mode.
        Args:
            value: Value to set for the enableSharedDeviceMode property.
        """
        self._enable_shared_device_mode = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bundle_id_access_control_list": lambda n : setattr(self, 'bundle_id_access_control_list', n.get_collection_of_primitive_values(str)),
            "configurations": lambda n : setattr(self, 'configurations', n.get_collection_of_object_values(key_typed_value_pair.KeyTypedValuePair)),
            "enable_shared_device_mode": lambda n : setattr(self, 'enable_shared_device_mode', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("bundleIdAccessControlList", self.bundle_id_access_control_list)
        writer.write_collection_of_object_values("configurations", self.configurations)
        writer.write_bool_value("enableSharedDeviceMode", self.enable_shared_device_mode)
    


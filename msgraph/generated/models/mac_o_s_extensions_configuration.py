from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
mac_o_s_kernel_extension = lazy_import('msgraph.generated.models.mac_o_s_kernel_extension')
mac_o_s_system_extension = lazy_import('msgraph.generated.models.mac_o_s_system_extension')
mac_o_s_system_extension_type_mapping = lazy_import('msgraph.generated.models.mac_o_s_system_extension_type_mapping')

class MacOSExtensionsConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSExtensionsConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSExtensionsConfiguration"
        # All kernel extensions validly signed by the team identifiers in this list will be allowed to load.
        self._kernel_extension_allowed_team_identifiers: Optional[List[str]] = None
        # If set to true, users can approve additional kernel extensions not explicitly allowed by configurations profiles.
        self._kernel_extension_overrides_allowed: Optional[bool] = None
        # A list of kernel extensions that will be allowed to load. . This collection can contain a maximum of 500 elements.
        self._kernel_extensions_allowed: Optional[List[mac_o_s_kernel_extension.MacOSKernelExtension]] = None
        # Gets or sets a list of allowed macOS system extensions. This collection can contain a maximum of 500 elements.
        self._system_extensions_allowed: Optional[List[mac_o_s_system_extension.MacOSSystemExtension]] = None
        # Gets or sets a list of allowed team identifiers. Any system extension signed with any of the specified team identifiers will be approved.
        self._system_extensions_allowed_team_identifiers: Optional[List[str]] = None
        # Gets or sets a list of allowed macOS system extension types. This collection can contain a maximum of 500 elements.
        self._system_extensions_allowed_types: Optional[List[mac_o_s_system_extension_type_mapping.MacOSSystemExtensionTypeMapping]] = None
        # Gets or sets whether to allow the user to approve additional system extensions not explicitly allowed by configuration profiles.
        self._system_extensions_block_override: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSExtensionsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSExtensionsConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSExtensionsConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "kernel_extension_allowed_team_identifiers": lambda n : setattr(self, 'kernel_extension_allowed_team_identifiers', n.get_collection_of_primitive_values(str)),
            "kernel_extension_overrides_allowed": lambda n : setattr(self, 'kernel_extension_overrides_allowed', n.get_bool_value()),
            "kernel_extensions_allowed": lambda n : setattr(self, 'kernel_extensions_allowed', n.get_collection_of_object_values(mac_o_s_kernel_extension.MacOSKernelExtension)),
            "system_extensions_allowed": lambda n : setattr(self, 'system_extensions_allowed', n.get_collection_of_object_values(mac_o_s_system_extension.MacOSSystemExtension)),
            "system_extensions_allowed_team_identifiers": lambda n : setattr(self, 'system_extensions_allowed_team_identifiers', n.get_collection_of_primitive_values(str)),
            "system_extensions_allowed_types": lambda n : setattr(self, 'system_extensions_allowed_types', n.get_collection_of_object_values(mac_o_s_system_extension_type_mapping.MacOSSystemExtensionTypeMapping)),
            "system_extensions_block_override": lambda n : setattr(self, 'system_extensions_block_override', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def kernel_extension_allowed_team_identifiers(self,) -> Optional[List[str]]:
        """
        Gets the kernelExtensionAllowedTeamIdentifiers property value. All kernel extensions validly signed by the team identifiers in this list will be allowed to load.
        Returns: Optional[List[str]]
        """
        return self._kernel_extension_allowed_team_identifiers
    
    @kernel_extension_allowed_team_identifiers.setter
    def kernel_extension_allowed_team_identifiers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the kernelExtensionAllowedTeamIdentifiers property value. All kernel extensions validly signed by the team identifiers in this list will be allowed to load.
        Args:
            value: Value to set for the kernelExtensionAllowedTeamIdentifiers property.
        """
        self._kernel_extension_allowed_team_identifiers = value
    
    @property
    def kernel_extension_overrides_allowed(self,) -> Optional[bool]:
        """
        Gets the kernelExtensionOverridesAllowed property value. If set to true, users can approve additional kernel extensions not explicitly allowed by configurations profiles.
        Returns: Optional[bool]
        """
        return self._kernel_extension_overrides_allowed
    
    @kernel_extension_overrides_allowed.setter
    def kernel_extension_overrides_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the kernelExtensionOverridesAllowed property value. If set to true, users can approve additional kernel extensions not explicitly allowed by configurations profiles.
        Args:
            value: Value to set for the kernelExtensionOverridesAllowed property.
        """
        self._kernel_extension_overrides_allowed = value
    
    @property
    def kernel_extensions_allowed(self,) -> Optional[List[mac_o_s_kernel_extension.MacOSKernelExtension]]:
        """
        Gets the kernelExtensionsAllowed property value. A list of kernel extensions that will be allowed to load. . This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_kernel_extension.MacOSKernelExtension]]
        """
        return self._kernel_extensions_allowed
    
    @kernel_extensions_allowed.setter
    def kernel_extensions_allowed(self,value: Optional[List[mac_o_s_kernel_extension.MacOSKernelExtension]] = None) -> None:
        """
        Sets the kernelExtensionsAllowed property value. A list of kernel extensions that will be allowed to load. . This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the kernelExtensionsAllowed property.
        """
        self._kernel_extensions_allowed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("kernelExtensionAllowedTeamIdentifiers", self.kernel_extension_allowed_team_identifiers)
        writer.write_bool_value("kernelExtensionOverridesAllowed", self.kernel_extension_overrides_allowed)
        writer.write_collection_of_object_values("kernelExtensionsAllowed", self.kernel_extensions_allowed)
        writer.write_collection_of_object_values("systemExtensionsAllowed", self.system_extensions_allowed)
        writer.write_collection_of_primitive_values("systemExtensionsAllowedTeamIdentifiers", self.system_extensions_allowed_team_identifiers)
        writer.write_collection_of_object_values("systemExtensionsAllowedTypes", self.system_extensions_allowed_types)
        writer.write_bool_value("systemExtensionsBlockOverride", self.system_extensions_block_override)
    
    @property
    def system_extensions_allowed(self,) -> Optional[List[mac_o_s_system_extension.MacOSSystemExtension]]:
        """
        Gets the systemExtensionsAllowed property value. Gets or sets a list of allowed macOS system extensions. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_system_extension.MacOSSystemExtension]]
        """
        return self._system_extensions_allowed
    
    @system_extensions_allowed.setter
    def system_extensions_allowed(self,value: Optional[List[mac_o_s_system_extension.MacOSSystemExtension]] = None) -> None:
        """
        Sets the systemExtensionsAllowed property value. Gets or sets a list of allowed macOS system extensions. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the systemExtensionsAllowed property.
        """
        self._system_extensions_allowed = value
    
    @property
    def system_extensions_allowed_team_identifiers(self,) -> Optional[List[str]]:
        """
        Gets the systemExtensionsAllowedTeamIdentifiers property value. Gets or sets a list of allowed team identifiers. Any system extension signed with any of the specified team identifiers will be approved.
        Returns: Optional[List[str]]
        """
        return self._system_extensions_allowed_team_identifiers
    
    @system_extensions_allowed_team_identifiers.setter
    def system_extensions_allowed_team_identifiers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the systemExtensionsAllowedTeamIdentifiers property value. Gets or sets a list of allowed team identifiers. Any system extension signed with any of the specified team identifiers will be approved.
        Args:
            value: Value to set for the systemExtensionsAllowedTeamIdentifiers property.
        """
        self._system_extensions_allowed_team_identifiers = value
    
    @property
    def system_extensions_allowed_types(self,) -> Optional[List[mac_o_s_system_extension_type_mapping.MacOSSystemExtensionTypeMapping]]:
        """
        Gets the systemExtensionsAllowedTypes property value. Gets or sets a list of allowed macOS system extension types. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_system_extension_type_mapping.MacOSSystemExtensionTypeMapping]]
        """
        return self._system_extensions_allowed_types
    
    @system_extensions_allowed_types.setter
    def system_extensions_allowed_types(self,value: Optional[List[mac_o_s_system_extension_type_mapping.MacOSSystemExtensionTypeMapping]] = None) -> None:
        """
        Sets the systemExtensionsAllowedTypes property value. Gets or sets a list of allowed macOS system extension types. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the systemExtensionsAllowedTypes property.
        """
        self._system_extensions_allowed_types = value
    
    @property
    def system_extensions_block_override(self,) -> Optional[bool]:
        """
        Gets the systemExtensionsBlockOverride property value. Gets or sets whether to allow the user to approve additional system extensions not explicitly allowed by configuration profiles.
        Returns: Optional[bool]
        """
        return self._system_extensions_block_override
    
    @system_extensions_block_override.setter
    def system_extensions_block_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the systemExtensionsBlockOverride property value. Gets or sets whether to allow the user to approve additional system extensions not explicitly allowed by configuration profiles.
        Args:
            value: Value to set for the systemExtensionsBlockOverride property.
        """
        self._system_extensions_block_override = value
    


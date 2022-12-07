from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
key_storage_provider_option = lazy_import('msgraph.generated.models.key_storage_provider_option')

class Windows10PFXImportCertificateProfile(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10PFXImportCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10PFXImportCertificateProfile"
        # Key Storage Provider (KSP) Import Options.
        self._key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10PFXImportCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10PFXImportCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10PFXImportCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "key_storage_provider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(key_storage_provider_option.KeyStorageProviderOption)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_storage_provider(self,) -> Optional[key_storage_provider_option.KeyStorageProviderOption]:
        """
        Gets the keyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Returns: Optional[key_storage_provider_option.KeyStorageProviderOption]
        """
        return self._key_storage_provider
    
    @key_storage_provider.setter
    def key_storage_provider(self,value: Optional[key_storage_provider_option.KeyStorageProviderOption] = None) -> None:
        """
        Sets the keyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Args:
            value: Value to set for the keyStorageProvider property.
        """
        self._key_storage_provider = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
    


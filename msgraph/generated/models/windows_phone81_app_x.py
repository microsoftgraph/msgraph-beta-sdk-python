from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')
windows_architecture = lazy_import('msgraph.generated.models.windows_architecture')
windows_minimum_operating_system = lazy_import('msgraph.generated.models.windows_minimum_operating_system')

class WindowsPhone81AppX(mobile_lob_app.MobileLobApp):
    @property
    def applicable_architectures(self,) -> Optional[windows_architecture.WindowsArchitecture]:
        """
        Gets the applicableArchitectures property value. Contains properties for Windows architecture.
        Returns: Optional[windows_architecture.WindowsArchitecture]
        """
        return self._applicable_architectures
    
    @applicable_architectures.setter
    def applicable_architectures(self,value: Optional[windows_architecture.WindowsArchitecture] = None) -> None:
        """
        Sets the applicableArchitectures property value. Contains properties for Windows architecture.
        Args:
            value: Value to set for the applicableArchitectures property.
        """
        self._applicable_architectures = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsPhone81AppX and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81AppX"
        # Contains properties for Windows architecture.
        self._applicable_architectures: Optional[windows_architecture.WindowsArchitecture] = None
        # The Identity Name.
        self._identity_name: Optional[str] = None
        # The Identity Publisher Hash.
        self._identity_publisher_hash: Optional[str] = None
        # The Identity Resource Identifier.
        self._identity_resource_identifier: Optional[str] = None
        # The identity version.
        self._identity_version: Optional[str] = None
        # The minimum operating system required for a Windows mobile app.
        self._minimum_supported_operating_system: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None
        # The Phone Product Identifier.
        self._phone_product_identifier: Optional[str] = None
        # The Phone Publisher Id.
        self._phone_publisher_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81AppX:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81AppX
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81AppX()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_architectures": lambda n : setattr(self, 'applicable_architectures', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "identity_name": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identity_publisher_hash": lambda n : setattr(self, 'identity_publisher_hash', n.get_str_value()),
            "identity_resource_identifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identity_version": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(windows_minimum_operating_system.WindowsMinimumOperatingSystem)),
            "phone_product_identifier": lambda n : setattr(self, 'phone_product_identifier', n.get_str_value()),
            "phone_publisher_id": lambda n : setattr(self, 'phone_publisher_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_name(self,) -> Optional[str]:
        """
        Gets the identityName property value. The Identity Name.
        Returns: Optional[str]
        """
        return self._identity_name
    
    @identity_name.setter
    def identity_name(self,value: Optional[str] = None) -> None:
        """
        Sets the identityName property value. The Identity Name.
        Args:
            value: Value to set for the identityName property.
        """
        self._identity_name = value
    
    @property
    def identity_publisher_hash(self,) -> Optional[str]:
        """
        Gets the identityPublisherHash property value. The Identity Publisher Hash.
        Returns: Optional[str]
        """
        return self._identity_publisher_hash
    
    @identity_publisher_hash.setter
    def identity_publisher_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the identityPublisherHash property value. The Identity Publisher Hash.
        Args:
            value: Value to set for the identityPublisherHash property.
        """
        self._identity_publisher_hash = value
    
    @property
    def identity_resource_identifier(self,) -> Optional[str]:
        """
        Gets the identityResourceIdentifier property value. The Identity Resource Identifier.
        Returns: Optional[str]
        """
        return self._identity_resource_identifier
    
    @identity_resource_identifier.setter
    def identity_resource_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identityResourceIdentifier property value. The Identity Resource Identifier.
        Args:
            value: Value to set for the identityResourceIdentifier property.
        """
        self._identity_resource_identifier = value
    
    @property
    def identity_version(self,) -> Optional[str]:
        """
        Gets the identityVersion property value. The identity version.
        Returns: Optional[str]
        """
        return self._identity_version
    
    @identity_version.setter
    def identity_version(self,value: Optional[str] = None) -> None:
        """
        Sets the identityVersion property value. The identity version.
        Args:
            value: Value to set for the identityVersion property.
        """
        self._identity_version = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The minimum operating system required for a Windows mobile app.
        Returns: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The minimum operating system required for a Windows mobile app.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def phone_product_identifier(self,) -> Optional[str]:
        """
        Gets the phoneProductIdentifier property value. The Phone Product Identifier.
        Returns: Optional[str]
        """
        return self._phone_product_identifier
    
    @phone_product_identifier.setter
    def phone_product_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneProductIdentifier property value. The Phone Product Identifier.
        Args:
            value: Value to set for the phoneProductIdentifier property.
        """
        self._phone_product_identifier = value
    
    @property
    def phone_publisher_id(self,) -> Optional[str]:
        """
        Gets the phonePublisherId property value. The Phone Publisher Id.
        Returns: Optional[str]
        """
        return self._phone_publisher_id
    
    @phone_publisher_id.setter
    def phone_publisher_id(self,value: Optional[str] = None) -> None:
        """
        Sets the phonePublisherId property value. The Phone Publisher Id.
        Args:
            value: Value to set for the phonePublisherId property.
        """
        self._phone_publisher_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisherHash", self.identity_publisher_hash)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("phoneProductIdentifier", self.phone_product_identifier)
        writer.write_str_value("phonePublisherId", self.phone_publisher_id)
    


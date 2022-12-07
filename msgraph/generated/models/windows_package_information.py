from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_architecture = lazy_import('msgraph.generated.models.windows_architecture')
windows_minimum_operating_system = lazy_import('msgraph.generated.models.windows_minimum_operating_system')

class WindowsPackageInformation(AdditionalDataHolder, Parsable):
    """
    Contains properties for the package information for a Windows line of business app.
    """
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
    
    @property
    def applicable_architecture(self,) -> Optional[windows_architecture.WindowsArchitecture]:
        """
        Gets the applicableArchitecture property value. Contains properties for Windows architecture.
        Returns: Optional[windows_architecture.WindowsArchitecture]
        """
        return self._applicable_architecture
    
    @applicable_architecture.setter
    def applicable_architecture(self,value: Optional[windows_architecture.WindowsArchitecture] = None) -> None:
        """
        Sets the applicableArchitecture property value. Contains properties for Windows architecture.
        Args:
            value: Value to set for the applicableArchitecture property.
        """
        self._applicable_architecture = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsPackageInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Contains properties for Windows architecture.
        self._applicable_architecture: Optional[windows_architecture.WindowsArchitecture] = None
        # The Display Name.
        self._display_name: Optional[str] = None
        # The Identity Name.
        self._identity_name: Optional[str] = None
        # The Identity Publisher.
        self._identity_publisher: Optional[str] = None
        # The Identity Resource Identifier.
        self._identity_resource_identifier: Optional[str] = None
        # The Identity Version.
        self._identity_version: Optional[str] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPackageInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPackageInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPackageInformation()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The Display Name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The Display Name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_architecture": lambda n : setattr(self, 'applicable_architecture', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "identity_name": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identity_publisher": lambda n : setattr(self, 'identity_publisher', n.get_str_value()),
            "identity_resource_identifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identity_version": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(windows_minimum_operating_system.WindowsMinimumOperatingSystem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
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
    def identity_publisher(self,) -> Optional[str]:
        """
        Gets the identityPublisher property value. The Identity Publisher.
        Returns: Optional[str]
        """
        return self._identity_publisher
    
    @identity_publisher.setter
    def identity_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the identityPublisher property value. The Identity Publisher.
        Args:
            value: Value to set for the identityPublisher property.
        """
        self._identity_publisher = value
    
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
        Gets the identityVersion property value. The Identity Version.
        Returns: Optional[str]
        """
        return self._identity_version
    
    @identity_version.setter
    def identity_version(self,value: Optional[str] = None) -> None:
        """
        Sets the identityVersion property value. The Identity Version.
        Args:
            value: Value to set for the identityVersion property.
        """
        self._identity_version = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
        """
        self._minimum_supported_operating_system = value
    
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
            value: Value to set for the OdataType property.
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
        writer.write_enum_value("applicableArchitecture", self.applicable_architecture)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisher", self.identity_publisher)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


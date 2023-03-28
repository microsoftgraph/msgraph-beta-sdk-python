from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_lob_app

from . import mobile_lob_app

class WindowsMobileMSI(mobile_lob_app.MobileLobApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsMobileMSI and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsMobileMSI"
        # The command line.
        self._command_line: Optional[str] = None
        # The identity version.
        self._identity_version: Optional[str] = None
        # A boolean to control whether the app's version will be used to detect the app after it is installed on a device. Set this to true for Windows Mobile MSI Line of Business (LoB) apps that use a self update feature.
        self._ignore_version_detection: Optional[bool] = None
        # The product code.
        self._product_code: Optional[str] = None
        # The product version of Windows Mobile MSI Line of Business (LoB) app.
        self._product_version: Optional[str] = None
        # Indicates whether to install a dual-mode MSI in the device context. If true, app will be installed for all users. If false, app will be installed per-user. If null, service will use the MSI package's default install context. In case of dual-mode MSI, this default will be per-user.  Cannot be set for non-dual-mode apps.  Cannot be changed after initial creation of the application.
        self._use_device_context: Optional[bool] = None
    
    @property
    def command_line(self,) -> Optional[str]:
        """
        Gets the commandLine property value. The command line.
        Returns: Optional[str]
        """
        return self._command_line
    
    @command_line.setter
    def command_line(self,value: Optional[str] = None) -> None:
        """
        Sets the commandLine property value. The command line.
        Args:
            value: Value to set for the command_line property.
        """
        self._command_line = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsMobileMSI:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMobileMSI
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsMobileMSI()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_lob_app

        fields: Dict[str, Callable[[Any], None]] = {
            "commandLine": lambda n : setattr(self, 'command_line', n.get_str_value()),
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "ignoreVersionDetection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "productCode": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "useDeviceContext": lambda n : setattr(self, 'use_device_context', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
            value: Value to set for the identity_version property.
        """
        self._identity_version = value
    
    @property
    def ignore_version_detection(self,) -> Optional[bool]:
        """
        Gets the ignoreVersionDetection property value. A boolean to control whether the app's version will be used to detect the app after it is installed on a device. Set this to true for Windows Mobile MSI Line of Business (LoB) apps that use a self update feature.
        Returns: Optional[bool]
        """
        return self._ignore_version_detection
    
    @ignore_version_detection.setter
    def ignore_version_detection(self,value: Optional[bool] = None) -> None:
        """
        Sets the ignoreVersionDetection property value. A boolean to control whether the app's version will be used to detect the app after it is installed on a device. Set this to true for Windows Mobile MSI Line of Business (LoB) apps that use a self update feature.
        Args:
            value: Value to set for the ignore_version_detection property.
        """
        self._ignore_version_detection = value
    
    @property
    def product_code(self,) -> Optional[str]:
        """
        Gets the productCode property value. The product code.
        Returns: Optional[str]
        """
        return self._product_code
    
    @product_code.setter
    def product_code(self,value: Optional[str] = None) -> None:
        """
        Sets the productCode property value. The product code.
        Args:
            value: Value to set for the product_code property.
        """
        self._product_code = value
    
    @property
    def product_version(self,) -> Optional[str]:
        """
        Gets the productVersion property value. The product version of Windows Mobile MSI Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._product_version
    
    @product_version.setter
    def product_version(self,value: Optional[str] = None) -> None:
        """
        Sets the productVersion property value. The product version of Windows Mobile MSI Line of Business (LoB) app.
        Args:
            value: Value to set for the product_version property.
        """
        self._product_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("commandLine", self.command_line)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_bool_value("useDeviceContext", self.use_device_context)
    
    @property
    def use_device_context(self,) -> Optional[bool]:
        """
        Gets the useDeviceContext property value. Indicates whether to install a dual-mode MSI in the device context. If true, app will be installed for all users. If false, app will be installed per-user. If null, service will use the MSI package's default install context. In case of dual-mode MSI, this default will be per-user.  Cannot be set for non-dual-mode apps.  Cannot be changed after initial creation of the application.
        Returns: Optional[bool]
        """
        return self._use_device_context
    
    @use_device_context.setter
    def use_device_context(self,value: Optional[bool] = None) -> None:
        """
        Sets the useDeviceContext property value. Indicates whether to install a dual-mode MSI in the device context. If true, app will be installed for all users. If false, app will be installed per-user. If null, service will use the MSI package's default install context. In case of dual-mode MSI, this default will be per-user.  Cannot be set for non-dual-mode apps.  Cannot be changed after initial creation of the application.
        Args:
            value: Value to set for the use_device_context property.
        """
        self._use_device_context = value
    


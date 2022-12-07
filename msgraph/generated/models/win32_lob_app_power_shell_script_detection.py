from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_detection = lazy_import('msgraph.generated.models.win32_lob_app_detection')

class Win32LobAppPowerShellScriptDetection(win32_lob_app_detection.Win32LobAppDetection):
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppPowerShellScriptDetection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppPowerShellScriptDetection"
        # A value indicating whether signature check is enforced
        self._enforce_signature_check: Optional[bool] = None
        # A value indicating whether this script should run as 32-bit
        self._run_as32_bit: Optional[bool] = None
        # The base64 encoded script content to detect Win32 Line of Business (LoB) app
        self._script_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppPowerShellScriptDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppPowerShellScriptDetection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppPowerShellScriptDetection()
    
    @property
    def enforce_signature_check(self,) -> Optional[bool]:
        """
        Gets the enforceSignatureCheck property value. A value indicating whether signature check is enforced
        Returns: Optional[bool]
        """
        return self._enforce_signature_check
    
    @enforce_signature_check.setter
    def enforce_signature_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the enforceSignatureCheck property value. A value indicating whether signature check is enforced
        Args:
            value: Value to set for the enforceSignatureCheck property.
        """
        self._enforce_signature_check = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enforce_signature_check": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "run_as32_bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "script_content": lambda n : setattr(self, 'script_content', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def run_as32_bit(self,) -> Optional[bool]:
        """
        Gets the runAs32Bit property value. A value indicating whether this script should run as 32-bit
        Returns: Optional[bool]
        """
        return self._run_as32_bit
    
    @run_as32_bit.setter
    def run_as32_bit(self,value: Optional[bool] = None) -> None:
        """
        Sets the runAs32Bit property value. A value indicating whether this script should run as 32-bit
        Args:
            value: Value to set for the runAs32Bit property.
        """
        self._run_as32_bit = value
    
    @property
    def script_content(self,) -> Optional[str]:
        """
        Gets the scriptContent property value. The base64 encoded script content to detect Win32 Line of Business (LoB) app
        Returns: Optional[str]
        """
        return self._script_content
    
    @script_content.setter
    def script_content(self,value: Optional[str] = None) -> None:
        """
        Sets the scriptContent property value. The base64 encoded script content to detect Win32 Line of Business (LoB) app
        Args:
            value: Value to set for the scriptContent property.
        """
        self._script_content = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_str_value("scriptContent", self.script_content)
    


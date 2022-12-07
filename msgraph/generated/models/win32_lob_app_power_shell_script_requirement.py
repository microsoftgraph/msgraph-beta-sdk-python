from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

run_as_account_type = lazy_import('msgraph.generated.models.run_as_account_type')
win32_lob_app_power_shell_script_detection_type = lazy_import('msgraph.generated.models.win32_lob_app_power_shell_script_detection_type')
win32_lob_app_requirement = lazy_import('msgraph.generated.models.win32_lob_app_requirement')

class Win32LobAppPowerShellScriptRequirement(win32_lob_app_requirement.Win32LobAppRequirement):
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppPowerShellScriptRequirement and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppPowerShellScriptRequirement"
        # Contains all supported Powershell Script output detection type.
        self._detection_type: Optional[win32_lob_app_power_shell_script_detection_type.Win32LobAppPowerShellScriptDetectionType] = None
        # The unique display name for this rule
        self._display_name: Optional[str] = None
        # A value indicating whether signature check is enforced
        self._enforce_signature_check: Optional[bool] = None
        # A value indicating whether this script should run as 32-bit
        self._run_as32_bit: Optional[bool] = None
        # Indicates the type of execution context the app runs in.
        self._run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
        # The base64 encoded script content to detect Win32 Line of Business (LoB) app
        self._script_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppPowerShellScriptRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppPowerShellScriptRequirement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppPowerShellScriptRequirement()
    
    @property
    def detection_type(self,) -> Optional[win32_lob_app_power_shell_script_detection_type.Win32LobAppPowerShellScriptDetectionType]:
        """
        Gets the detectionType property value. Contains all supported Powershell Script output detection type.
        Returns: Optional[win32_lob_app_power_shell_script_detection_type.Win32LobAppPowerShellScriptDetectionType]
        """
        return self._detection_type
    
    @detection_type.setter
    def detection_type(self,value: Optional[win32_lob_app_power_shell_script_detection_type.Win32LobAppPowerShellScriptDetectionType] = None) -> None:
        """
        Sets the detectionType property value. Contains all supported Powershell Script output detection type.
        Args:
            value: Value to set for the detectionType property.
        """
        self._detection_type = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The unique display name for this rule
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The unique display name for this rule
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
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
            "detection_type": lambda n : setattr(self, 'detection_type', n.get_enum_value(win32_lob_app_power_shell_script_detection_type.Win32LobAppPowerShellScriptDetectionType)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforce_signature_check": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "run_as32_bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "run_as_account": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
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
    def run_as_account(self,) -> Optional[run_as_account_type.RunAsAccountType]:
        """
        Gets the runAsAccount property value. Indicates the type of execution context the app runs in.
        Returns: Optional[run_as_account_type.RunAsAccountType]
        """
        return self._run_as_account
    
    @run_as_account.setter
    def run_as_account(self,value: Optional[run_as_account_type.RunAsAccountType] = None) -> None:
        """
        Sets the runAsAccount property value. Indicates the type of execution context the app runs in.
        Args:
            value: Value to set for the runAsAccount property.
        """
        self._run_as_account = value
    
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
        writer.write_enum_value("detectionType", self.detection_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_str_value("scriptContent", self.script_content)
    


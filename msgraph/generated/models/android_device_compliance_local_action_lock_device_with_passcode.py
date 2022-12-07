from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_compliance_local_action_base = lazy_import('msgraph.generated.models.android_device_compliance_local_action_base')

class AndroidDeviceComplianceLocalActionLockDeviceWithPasscode(android_device_compliance_local_action_base.AndroidDeviceComplianceLocalActionBase):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceComplianceLocalActionLockDeviceWithPasscode and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode"
        # Passcode to reset to Android device. This property is read-only.
        self._passcode: Optional[str] = None
        # Number of sign in failures before wiping device, the value can be 4-11. Valid values 4 to 11
        self._passcode_sign_in_failure_count_before_wipe: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceComplianceLocalActionLockDeviceWithPasscode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceComplianceLocalActionLockDeviceWithPasscode
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceComplianceLocalActionLockDeviceWithPasscode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
            "passcode_sign_in_failure_count_before_wipe": lambda n : setattr(self, 'passcode_sign_in_failure_count_before_wipe', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def passcode(self,) -> Optional[str]:
        """
        Gets the passcode property value. Passcode to reset to Android device. This property is read-only.
        Returns: Optional[str]
        """
        return self._passcode
    
    @passcode.setter
    def passcode(self,value: Optional[str] = None) -> None:
        """
        Sets the passcode property value. Passcode to reset to Android device. This property is read-only.
        Args:
            value: Value to set for the passcode property.
        """
        self._passcode = value
    
    @property
    def passcode_sign_in_failure_count_before_wipe(self,) -> Optional[int]:
        """
        Gets the passcodeSignInFailureCountBeforeWipe property value. Number of sign in failures before wiping device, the value can be 4-11. Valid values 4 to 11
        Returns: Optional[int]
        """
        return self._passcode_sign_in_failure_count_before_wipe
    
    @passcode_sign_in_failure_count_before_wipe.setter
    def passcode_sign_in_failure_count_before_wipe(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeSignInFailureCountBeforeWipe property value. Number of sign in failures before wiping device, the value can be 4-11. Valid values 4 to 11
        Args:
            value: Value to set for the passcodeSignInFailureCountBeforeWipe property.
        """
        self._passcode_sign_in_failure_count_before_wipe = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("passcodeSignInFailureCountBeforeWipe", self.passcode_sign_in_failure_count_before_wipe)
    


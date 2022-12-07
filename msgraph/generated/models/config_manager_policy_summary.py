from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ConfigManagerPolicySummary(AdditionalDataHolder, Parsable):
    """
    A ConfigManager policy summary.
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
    def compliant_device_count(self,) -> Optional[int]:
        """
        Gets the compliantDeviceCount property value. The number of devices evaluated to be compliant by the policy.
        Returns: Optional[int]
        """
        return self._compliant_device_count
    
    @compliant_device_count.setter
    def compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantDeviceCount property value. The number of devices evaluated to be compliant by the policy.
        Args:
            value: Value to set for the compliantDeviceCount property.
        """
        self._compliant_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new configManagerPolicySummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of devices evaluated to be compliant by the policy.
        self._compliant_device_count: Optional[int] = None
        # The number of devices that have have been remediated by the policy.
        self._enforced_device_count: Optional[int] = None
        # The number of devices that failed to be evaluated by the policy.
        self._failed_device_count: Optional[int] = None
        # The number of devices evaluated to be noncompliant by the policy.
        self._non_compliant_device_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of devices that have acknowledged the policy but are pending evaluation.
        self._pending_device_count: Optional[int] = None
        # The number of devices targeted by the policy.
        self._targeted_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigManagerPolicySummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigManagerPolicySummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigManagerPolicySummary()
    
    @property
    def enforced_device_count(self,) -> Optional[int]:
        """
        Gets the enforcedDeviceCount property value. The number of devices that have have been remediated by the policy.
        Returns: Optional[int]
        """
        return self._enforced_device_count
    
    @enforced_device_count.setter
    def enforced_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the enforcedDeviceCount property value. The number of devices that have have been remediated by the policy.
        Args:
            value: Value to set for the enforcedDeviceCount property.
        """
        self._enforced_device_count = value
    
    @property
    def failed_device_count(self,) -> Optional[int]:
        """
        Gets the failedDeviceCount property value. The number of devices that failed to be evaluated by the policy.
        Returns: Optional[int]
        """
        return self._failed_device_count
    
    @failed_device_count.setter
    def failed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedDeviceCount property value. The number of devices that failed to be evaluated by the policy.
        Args:
            value: Value to set for the failedDeviceCount property.
        """
        self._failed_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "enforced_device_count": lambda n : setattr(self, 'enforced_device_count', n.get_int_value()),
            "failed_device_count": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "non_compliant_device_count": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pending_device_count": lambda n : setattr(self, 'pending_device_count', n.get_int_value()),
            "targeted_device_count": lambda n : setattr(self, 'targeted_device_count', n.get_int_value()),
        }
        return fields
    
    @property
    def non_compliant_device_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantDeviceCount property value. The number of devices evaluated to be noncompliant by the policy.
        Returns: Optional[int]
        """
        return self._non_compliant_device_count
    
    @non_compliant_device_count.setter
    def non_compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantDeviceCount property value. The number of devices evaluated to be noncompliant by the policy.
        Args:
            value: Value to set for the nonCompliantDeviceCount property.
        """
        self._non_compliant_device_count = value
    
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
    
    @property
    def pending_device_count(self,) -> Optional[int]:
        """
        Gets the pendingDeviceCount property value. The number of devices that have acknowledged the policy but are pending evaluation.
        Returns: Optional[int]
        """
        return self._pending_device_count
    
    @pending_device_count.setter
    def pending_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingDeviceCount property value. The number of devices that have acknowledged the policy but are pending evaluation.
        Args:
            value: Value to set for the pendingDeviceCount property.
        """
        self._pending_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("enforcedDeviceCount", self.enforced_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingDeviceCount", self.pending_device_count)
        writer.write_int_value("targetedDeviceCount", self.targeted_device_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def targeted_device_count(self,) -> Optional[int]:
        """
        Gets the targetedDeviceCount property value. The number of devices targeted by the policy.
        Returns: Optional[int]
        """
        return self._targeted_device_count
    
    @targeted_device_count.setter
    def targeted_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the targetedDeviceCount property value. The number of devices targeted by the policy.
        Args:
            value: Value to set for the targetedDeviceCount property.
        """
        self._targeted_device_count = value
    


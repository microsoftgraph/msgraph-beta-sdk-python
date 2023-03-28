from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class CloudPcLaunchInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcLaunchInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier of the Cloud PC.
        self._cloud_pc_id: Optional[str] = None
        # The connect URL of the Cloud PC.
        self._cloud_pc_launch_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates whether the Cloud PC supports switch functionality. If the value is true, it supports switch functionality; otherwise,  false.
        self._windows365_switch_compatible: Optional[bool] = None
        # Indicates the reason the Cloud PC doesn't support switch. CPCOsVersionNotMeetRequirement indicates that the user needs to update their Cloud PC operation system version. CPCHardwareNotMeetRequirement indicates that the Cloud PC needs more CPU or RAM to support the functionality.
        self._windows365_switch_not_compatible_reason: Optional[str] = None
    
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
    def cloud_pc_id(self,) -> Optional[str]:
        """
        Gets the cloudPcId property value. The unique identifier of the Cloud PC.
        Returns: Optional[str]
        """
        return self._cloud_pc_id
    
    @cloud_pc_id.setter
    def cloud_pc_id(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcId property value. The unique identifier of the Cloud PC.
        Args:
            value: Value to set for the cloud_pc_id property.
        """
        self._cloud_pc_id = value
    
    @property
    def cloud_pc_launch_url(self,) -> Optional[str]:
        """
        Gets the cloudPcLaunchUrl property value. The connect URL of the Cloud PC.
        Returns: Optional[str]
        """
        return self._cloud_pc_launch_url
    
    @cloud_pc_launch_url.setter
    def cloud_pc_launch_url(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcLaunchUrl property value. The connect URL of the Cloud PC.
        Args:
            value: Value to set for the cloud_pc_launch_url property.
        """
        self._cloud_pc_launch_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcLaunchInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcLaunchInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcLaunchInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "cloudPcLaunchUrl": lambda n : setattr(self, 'cloud_pc_launch_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "windows365SwitchCompatible": lambda n : setattr(self, 'windows365_switch_compatible', n.get_bool_value()),
            "windows365SwitchNotCompatibleReason": lambda n : setattr(self, 'windows365_switch_not_compatible_reason', n.get_str_value()),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_str_value("cloudPcLaunchUrl", self.cloud_pc_launch_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("windows365SwitchCompatible", self.windows365_switch_compatible)
        writer.write_str_value("windows365SwitchNotCompatibleReason", self.windows365_switch_not_compatible_reason)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def windows365_switch_compatible(self,) -> Optional[bool]:
        """
        Gets the windows365SwitchCompatible property value. Indicates whether the Cloud PC supports switch functionality. If the value is true, it supports switch functionality; otherwise,  false.
        Returns: Optional[bool]
        """
        return self._windows365_switch_compatible
    
    @windows365_switch_compatible.setter
    def windows365_switch_compatible(self,value: Optional[bool] = None) -> None:
        """
        Sets the windows365SwitchCompatible property value. Indicates whether the Cloud PC supports switch functionality. If the value is true, it supports switch functionality; otherwise,  false.
        Args:
            value: Value to set for the windows365_switch_compatible property.
        """
        self._windows365_switch_compatible = value
    
    @property
    def windows365_switch_not_compatible_reason(self,) -> Optional[str]:
        """
        Gets the windows365SwitchNotCompatibleReason property value. Indicates the reason the Cloud PC doesn't support switch. CPCOsVersionNotMeetRequirement indicates that the user needs to update their Cloud PC operation system version. CPCHardwareNotMeetRequirement indicates that the Cloud PC needs more CPU or RAM to support the functionality.
        Returns: Optional[str]
        """
        return self._windows365_switch_not_compatible_reason
    
    @windows365_switch_not_compatible_reason.setter
    def windows365_switch_not_compatible_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the windows365SwitchNotCompatibleReason property value. Indicates the reason the Cloud PC doesn't support switch. CPCOsVersionNotMeetRequirement indicates that the user needs to update their Cloud PC operation system version. CPCHardwareNotMeetRequirement indicates that the Cloud PC needs more CPU or RAM to support the functionality.
        Args:
            value: Value to set for the windows365_switch_not_compatible_reason property.
        """
        self._windows365_switch_not_compatible_reason = value
    


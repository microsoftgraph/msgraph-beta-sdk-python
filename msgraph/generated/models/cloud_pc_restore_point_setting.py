from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CloudPcRestorePointSetting(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcRestorePointSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The time interval in hours to take snapshots (restore points) of a Cloud PC automatically. Possible values are 4, 6, 12, 16, and 24. The default frequency is 12 hours.
        self._frequency_in_hours: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If true, the user has the ability to use snapshots to restore Cloud PCs. If false, non-admin users cannot use snapshots to restore the Cloud PC.
        self._user_restore_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcRestorePointSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRestorePointSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcRestorePointSetting()
    
    @property
    def frequency_in_hours(self,) -> Optional[int]:
        """
        Gets the frequencyInHours property value. The time interval in hours to take snapshots (restore points) of a Cloud PC automatically. Possible values are 4, 6, 12, 16, and 24. The default frequency is 12 hours.
        Returns: Optional[int]
        """
        return self._frequency_in_hours
    
    @frequency_in_hours.setter
    def frequency_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the frequencyInHours property value. The time interval in hours to take snapshots (restore points) of a Cloud PC automatically. Possible values are 4, 6, 12, 16, and 24. The default frequency is 12 hours.
        Args:
            value: Value to set for the frequencyInHours property.
        """
        self._frequency_in_hours = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "frequency_in_hours": lambda n : setattr(self, 'frequency_in_hours', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_restore_enabled": lambda n : setattr(self, 'user_restore_enabled', n.get_bool_value()),
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
        writer.write_int_value("frequencyInHours", self.frequency_in_hours)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("userRestoreEnabled", self.user_restore_enabled)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_restore_enabled(self,) -> Optional[bool]:
        """
        Gets the userRestoreEnabled property value. If true, the user has the ability to use snapshots to restore Cloud PCs. If false, non-admin users cannot use snapshots to restore the Cloud PC.
        Returns: Optional[bool]
        """
        return self._user_restore_enabled
    
    @user_restore_enabled.setter
    def user_restore_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userRestoreEnabled property value. If true, the user has the ability to use snapshots to restore Cloud PCs. If false, non-admin users cannot use snapshots to restore the Cloud PC.
        Args:
            value: Value to set for the userRestoreEnabled property.
        """
        self._user_restore_enabled = value
    


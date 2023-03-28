from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class CloudPcBulkRemoteActionResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcBulkRemoteActionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of all the Intune managed device IDs that completed the bulk action with a failure.
        self._failed_device_ids: Optional[List[str]] = None
        # A list of all the Intune managed device IDs that were not found when the bulk action was attempted.
        self._not_found_device_ids: Optional[List[str]] = None
        # A list of all the Intune managed device IDs that were identified as unsupported for the bulk action.
        self._not_supported_device_ids: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A list of all the Intune managed device IDs that completed the bulk action successfully.
        self._successful_device_ids: Optional[List[str]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcBulkRemoteActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkRemoteActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcBulkRemoteActionResult()
    
    @property
    def failed_device_ids(self,) -> Optional[List[str]]:
        """
        Gets the failedDeviceIds property value. A list of all the Intune managed device IDs that completed the bulk action with a failure.
        Returns: Optional[List[str]]
        """
        return self._failed_device_ids
    
    @failed_device_ids.setter
    def failed_device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the failedDeviceIds property value. A list of all the Intune managed device IDs that completed the bulk action with a failure.
        Args:
            value: Value to set for the failed_device_ids property.
        """
        self._failed_device_ids = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedDeviceIds": lambda n : setattr(self, 'failed_device_ids', n.get_collection_of_primitive_values(str)),
            "notFoundDeviceIds": lambda n : setattr(self, 'not_found_device_ids', n.get_collection_of_primitive_values(str)),
            "notSupportedDeviceIds": lambda n : setattr(self, 'not_supported_device_ids', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulDeviceIds": lambda n : setattr(self, 'successful_device_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def not_found_device_ids(self,) -> Optional[List[str]]:
        """
        Gets the notFoundDeviceIds property value. A list of all the Intune managed device IDs that were not found when the bulk action was attempted.
        Returns: Optional[List[str]]
        """
        return self._not_found_device_ids
    
    @not_found_device_ids.setter
    def not_found_device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notFoundDeviceIds property value. A list of all the Intune managed device IDs that were not found when the bulk action was attempted.
        Args:
            value: Value to set for the not_found_device_ids property.
        """
        self._not_found_device_ids = value
    
    @property
    def not_supported_device_ids(self,) -> Optional[List[str]]:
        """
        Gets the notSupportedDeviceIds property value. A list of all the Intune managed device IDs that were identified as unsupported for the bulk action.
        Returns: Optional[List[str]]
        """
        return self._not_supported_device_ids
    
    @not_supported_device_ids.setter
    def not_supported_device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notSupportedDeviceIds property value. A list of all the Intune managed device IDs that were identified as unsupported for the bulk action.
        Args:
            value: Value to set for the not_supported_device_ids property.
        """
        self._not_supported_device_ids = value
    
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
        writer.write_collection_of_primitive_values("failedDeviceIds", self.failed_device_ids)
        writer.write_collection_of_primitive_values("notFoundDeviceIds", self.not_found_device_ids)
        writer.write_collection_of_primitive_values("notSupportedDeviceIds", self.not_supported_device_ids)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("successfulDeviceIds", self.successful_device_ids)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def successful_device_ids(self,) -> Optional[List[str]]:
        """
        Gets the successfulDeviceIds property value. A list of all the Intune managed device IDs that completed the bulk action successfully.
        Returns: Optional[List[str]]
        """
        return self._successful_device_ids
    
    @successful_device_ids.setter
    def successful_device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the successfulDeviceIds property value. A list of all the Intune managed device IDs that completed the bulk action successfully.
        Args:
            value: Value to set for the successful_device_ids property.
        """
        self._successful_device_ids = value
    


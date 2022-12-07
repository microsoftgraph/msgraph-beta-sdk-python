from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_connectivity_status = lazy_import('msgraph.generated.models.cloud_pc_connectivity_status')
cloud_pc_health_check_item = lazy_import('msgraph.generated.models.cloud_pc_health_check_item')

class CloudPcConnectivityResult(AdditionalDataHolder, Parsable):
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
        Instantiates a new cloudPcConnectivityResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of failed health check items. If the status property is available, this property will be empty.
        self._failed_health_check_items: Optional[List[cloud_pc_health_check_item.CloudPcHealthCheckItem]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status property
        self._status: Optional[cloud_pc_connectivity_status.CloudPcConnectivityStatus] = None
        # Datetime when the status was updated. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        self._updated_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcConnectivityResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnectivityResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcConnectivityResult()
    
    @property
    def failed_health_check_items(self,) -> Optional[List[cloud_pc_health_check_item.CloudPcHealthCheckItem]]:
        """
        Gets the failedHealthCheckItems property value. A list of failed health check items. If the status property is available, this property will be empty.
        Returns: Optional[List[cloud_pc_health_check_item.CloudPcHealthCheckItem]]
        """
        return self._failed_health_check_items
    
    @failed_health_check_items.setter
    def failed_health_check_items(self,value: Optional[List[cloud_pc_health_check_item.CloudPcHealthCheckItem]] = None) -> None:
        """
        Sets the failedHealthCheckItems property value. A list of failed health check items. If the status property is available, this property will be empty.
        Args:
            value: Value to set for the failedHealthCheckItems property.
        """
        self._failed_health_check_items = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "failed_health_check_items": lambda n : setattr(self, 'failed_health_check_items', n.get_collection_of_object_values(cloud_pc_health_check_item.CloudPcHealthCheckItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_connectivity_status.CloudPcConnectivityStatus)),
            "updated_date_time": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("failedHealthCheckItems", self.failed_health_check_items)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[cloud_pc_connectivity_status.CloudPcConnectivityStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[cloud_pc_connectivity_status.CloudPcConnectivityStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_connectivity_status.CloudPcConnectivityStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the updatedDateTime property value. Datetime when the status was updated. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._updated_date_time
    
    @updated_date_time.setter
    def updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the updatedDateTime property value. Datetime when the status was updated. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the updatedDateTime property.
        """
        self._updated_date_time = value
    


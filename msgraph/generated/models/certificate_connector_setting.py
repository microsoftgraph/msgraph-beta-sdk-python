from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CertificateConnectorSetting(AdditionalDataHolder, Parsable):
    """
    Certificate connector settings.
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
    def cert_expiry_time(self,) -> Optional[datetime]:
        """
        Gets the certExpiryTime property value. Certificate expire time
        Returns: Optional[datetime]
        """
        return self._cert_expiry_time
    
    @cert_expiry_time.setter
    def cert_expiry_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certExpiryTime property value. Certificate expire time
        Args:
            value: Value to set for the certExpiryTime property.
        """
        self._cert_expiry_time = value
    
    @property
    def connector_version(self,) -> Optional[str]:
        """
        Gets the connectorVersion property value. Version of certificate connector
        Returns: Optional[str]
        """
        return self._connector_version
    
    @connector_version.setter
    def connector_version(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorVersion property value. Version of certificate connector
        Args:
            value: Value to set for the connectorVersion property.
        """
        self._connector_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new certificateConnectorSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Certificate expire time
        self._cert_expiry_time: Optional[datetime] = None
        # Version of certificate connector
        self._connector_version: Optional[str] = None
        # Certificate connector enrollment error
        self._enrollment_error: Optional[str] = None
        # Last time certificate connector connected
        self._last_connector_connection_time: Optional[datetime] = None
        # Version of last uploaded certificate connector
        self._last_upload_version: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Certificate connector status
        self._status: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CertificateConnectorSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CertificateConnectorSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CertificateConnectorSetting()
    
    @property
    def enrollment_error(self,) -> Optional[str]:
        """
        Gets the enrollmentError property value. Certificate connector enrollment error
        Returns: Optional[str]
        """
        return self._enrollment_error
    
    @enrollment_error.setter
    def enrollment_error(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentError property value. Certificate connector enrollment error
        Args:
            value: Value to set for the enrollmentError property.
        """
        self._enrollment_error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cert_expiry_time": lambda n : setattr(self, 'cert_expiry_time', n.get_datetime_value()),
            "connector_version": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "enrollment_error": lambda n : setattr(self, 'enrollment_error', n.get_str_value()),
            "last_connector_connection_time": lambda n : setattr(self, 'last_connector_connection_time', n.get_datetime_value()),
            "last_upload_version": lambda n : setattr(self, 'last_upload_version', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
        }
        return fields
    
    @property
    def last_connector_connection_time(self,) -> Optional[datetime]:
        """
        Gets the lastConnectorConnectionTime property value. Last time certificate connector connected
        Returns: Optional[datetime]
        """
        return self._last_connector_connection_time
    
    @last_connector_connection_time.setter
    def last_connector_connection_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastConnectorConnectionTime property value. Last time certificate connector connected
        Args:
            value: Value to set for the lastConnectorConnectionTime property.
        """
        self._last_connector_connection_time = value
    
    @property
    def last_upload_version(self,) -> Optional[int]:
        """
        Gets the lastUploadVersion property value. Version of last uploaded certificate connector
        Returns: Optional[int]
        """
        return self._last_upload_version
    
    @last_upload_version.setter
    def last_upload_version(self,value: Optional[int] = None) -> None:
        """
        Sets the lastUploadVersion property value. Version of last uploaded certificate connector
        Args:
            value: Value to set for the lastUploadVersion property.
        """
        self._last_upload_version = value
    
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
        writer.write_datetime_value("certExpiryTime", self.cert_expiry_time)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_str_value("enrollmentError", self.enrollment_error)
        writer.write_datetime_value("lastConnectorConnectionTime", self.last_connector_connection_time)
        writer.write_int_value("lastUploadVersion", self.last_upload_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[int]:
        """
        Gets the status property value. Certificate connector status
        Returns: Optional[int]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[int] = None) -> None:
        """
        Sets the status property value. Certificate connector status
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    


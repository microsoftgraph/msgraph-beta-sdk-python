from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, service_now_authentication_method, service_now_connection_status

from . import entity

class ServiceNowConnection(entity.Entity):
    """
    ServiceNow properties including the ServiceNow instanceUrl, connection credentials and other metadata.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new serviceNowConnection and sets the default values.
        """
        super().__init__()
        # Indicates the method used by Intune to authenticate with ServiceNow. Currently supports only web authentication with ServiceNow using the specified app id.
        self._authentication_method: Optional[service_now_authentication_method.ServiceNowAuthenticationMethod] = None
        # Date Time when connection properties were created. The value cannot be modified and is automatically populated when the connection properties were entered.
        self._created_date_time: Optional[datetime] = None
        # Indicates the ServiceNow incident API URL that Intune will use the fetch incidents. Saved in the format of /api/now/table/incident
        self._incident_api_url: Optional[str] = None
        # Indicates the ServiceNow instance URL that Intune will connect to. Saved in the format of https://<instance>.service-now.com
        self._instance_url: Optional[str] = None
        # Date Time when connection properties were last updated. The value cannot be modified and is automatically populated when the connection properties were updated.
        self._last_modified_date_time: Optional[datetime] = None
        # Date Time when incidents from ServiceNow were last queried
        self._last_queried_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Status of ServiceNow Connection
        self._service_now_connection_status: Optional[service_now_connection_status.ServiceNowConnectionStatus] = None
    
    @property
    def authentication_method(self,) -> Optional[service_now_authentication_method.ServiceNowAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Indicates the method used by Intune to authenticate with ServiceNow. Currently supports only web authentication with ServiceNow using the specified app id.
        Returns: Optional[service_now_authentication_method.ServiceNowAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[service_now_authentication_method.ServiceNowAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Indicates the method used by Intune to authenticate with ServiceNow. Currently supports only web authentication with ServiceNow using the specified app id.
        Args:
            value: Value to set for the authentication_method property.
        """
        self._authentication_method = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date Time when connection properties were created. The value cannot be modified and is automatically populated when the connection properties were entered.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date Time when connection properties were created. The value cannot be modified and is automatically populated when the connection properties were entered.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceNowConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceNowConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceNowConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, service_now_authentication_method, service_now_connection_status

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_object_value(service_now_authentication_method.ServiceNowAuthenticationMethod)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "incidentApiUrl": lambda n : setattr(self, 'incident_api_url', n.get_str_value()),
            "instanceUrl": lambda n : setattr(self, 'instance_url', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastQueriedDateTime": lambda n : setattr(self, 'last_queried_date_time', n.get_datetime_value()),
            "serviceNowConnectionStatus": lambda n : setattr(self, 'service_now_connection_status', n.get_enum_value(service_now_connection_status.ServiceNowConnectionStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incident_api_url(self,) -> Optional[str]:
        """
        Gets the incidentApiUrl property value. Indicates the ServiceNow incident API URL that Intune will use the fetch incidents. Saved in the format of /api/now/table/incident
        Returns: Optional[str]
        """
        return self._incident_api_url
    
    @incident_api_url.setter
    def incident_api_url(self,value: Optional[str] = None) -> None:
        """
        Sets the incidentApiUrl property value. Indicates the ServiceNow incident API URL that Intune will use the fetch incidents. Saved in the format of /api/now/table/incident
        Args:
            value: Value to set for the incident_api_url property.
        """
        self._incident_api_url = value
    
    @property
    def instance_url(self,) -> Optional[str]:
        """
        Gets the instanceUrl property value. Indicates the ServiceNow instance URL that Intune will connect to. Saved in the format of https://<instance>.service-now.com
        Returns: Optional[str]
        """
        return self._instance_url
    
    @instance_url.setter
    def instance_url(self,value: Optional[str] = None) -> None:
        """
        Sets the instanceUrl property value. Indicates the ServiceNow instance URL that Intune will connect to. Saved in the format of https://<instance>.service-now.com
        Args:
            value: Value to set for the instance_url property.
        """
        self._instance_url = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date Time when connection properties were last updated. The value cannot be modified and is automatically populated when the connection properties were updated.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date Time when connection properties were last updated. The value cannot be modified and is automatically populated when the connection properties were updated.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_queried_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastQueriedDateTime property value. Date Time when incidents from ServiceNow were last queried
        Returns: Optional[datetime]
        """
        return self._last_queried_date_time
    
    @last_queried_date_time.setter
    def last_queried_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastQueriedDateTime property value. Date Time when incidents from ServiceNow were last queried
        Args:
            value: Value to set for the last_queried_date_time property.
        """
        self._last_queried_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("authenticationMethod", self.authentication_method)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("incidentApiUrl", self.incident_api_url)
        writer.write_str_value("instanceUrl", self.instance_url)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastQueriedDateTime", self.last_queried_date_time)
        writer.write_enum_value("serviceNowConnectionStatus", self.service_now_connection_status)
    
    @property
    def service_now_connection_status(self,) -> Optional[service_now_connection_status.ServiceNowConnectionStatus]:
        """
        Gets the serviceNowConnectionStatus property value. Status of ServiceNow Connection
        Returns: Optional[service_now_connection_status.ServiceNowConnectionStatus]
        """
        return self._service_now_connection_status
    
    @service_now_connection_status.setter
    def service_now_connection_status(self,value: Optional[service_now_connection_status.ServiceNowConnectionStatus] = None) -> None:
        """
        Sets the serviceNowConnectionStatus property value. Status of ServiceNow Connection
        Args:
            value: Value to set for the service_now_connection_status property.
        """
        self._service_now_connection_status = value
    


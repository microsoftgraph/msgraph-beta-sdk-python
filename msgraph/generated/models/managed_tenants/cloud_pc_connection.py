from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CloudPcConnection(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcConnection and sets the default values.
        """
        super().__init__()
        # The display name of the cloud PC connection. Required. Read-only.
        self._display_name: Optional[str] = None
        # The health status of the cloud PC connection. Possible values are: pending, running, passed, failed, unknownFutureValue.  Required. Read-only.
        self._health_check_status: Optional[str] = None
        # Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The display name for the managed tenant. Required. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcConnection()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the cloud PC connection. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the cloud PC connection. Required. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "health_check_status": lambda n : setattr(self, 'health_check_status', n.get_str_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_check_status(self,) -> Optional[str]:
        """
        Gets the healthCheckStatus property value. The health status of the cloud PC connection. Possible values are: pending, running, passed, failed, unknownFutureValue.  Required. Read-only.
        Returns: Optional[str]
        """
        return self._health_check_status
    
    @health_check_status.setter
    def health_check_status(self,value: Optional[str] = None) -> None:
        """
        Sets the healthCheckStatus property value. The health status of the cloud PC connection. Possible values are: pending, running, passed, failed, unknownFutureValue.  Required. Read-only.
        Args:
            value: Value to set for the healthCheckStatus property.
        """
        self._health_check_status = value
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
        Args:
            value: Value to set for the lastRefreshedDateTime property.
        """
        self._last_refreshed_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("healthCheckStatus", self.health_check_status)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantDisplayName property.
        """
        self._tenant_display_name = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    


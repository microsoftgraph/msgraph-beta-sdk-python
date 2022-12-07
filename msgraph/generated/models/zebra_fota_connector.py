from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
zebra_fota_connector_state = lazy_import('msgraph.generated.models.zebra_fota_connector_state')

class ZebraFotaConnector(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new zebraFotaConnector and sets the default values.
        """
        super().__init__()
        # Complete account enrollment authorization URL. This corresponds to verification_uri_complete in the Zebra API documentations.
        self._enrollment_authorization_url: Optional[str] = None
        # Tenant enrollment token from Zebra. The token is used to enroll Zebra devices in the FOTA Service via app config.
        self._enrollment_token: Optional[str] = None
        # Flag indicating if required Firmware Over-the-Air (FOTA) Apps have been approved.
        self._fota_apps_approved: Optional[bool] = None
        # Date and time when the account was last synched with Zebra
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents various states for Zebra FOTA connector.
        self._state: Optional[zebra_fota_connector_state.ZebraFotaConnectorState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ZebraFotaConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ZebraFotaConnector()
    
    @property
    def enrollment_authorization_url(self,) -> Optional[str]:
        """
        Gets the enrollmentAuthorizationUrl property value. Complete account enrollment authorization URL. This corresponds to verification_uri_complete in the Zebra API documentations.
        Returns: Optional[str]
        """
        return self._enrollment_authorization_url
    
    @enrollment_authorization_url.setter
    def enrollment_authorization_url(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentAuthorizationUrl property value. Complete account enrollment authorization URL. This corresponds to verification_uri_complete in the Zebra API documentations.
        Args:
            value: Value to set for the enrollmentAuthorizationUrl property.
        """
        self._enrollment_authorization_url = value
    
    @property
    def enrollment_token(self,) -> Optional[str]:
        """
        Gets the enrollmentToken property value. Tenant enrollment token from Zebra. The token is used to enroll Zebra devices in the FOTA Service via app config.
        Returns: Optional[str]
        """
        return self._enrollment_token
    
    @enrollment_token.setter
    def enrollment_token(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentToken property value. Tenant enrollment token from Zebra. The token is used to enroll Zebra devices in the FOTA Service via app config.
        Args:
            value: Value to set for the enrollmentToken property.
        """
        self._enrollment_token = value
    
    @property
    def fota_apps_approved(self,) -> Optional[bool]:
        """
        Gets the fotaAppsApproved property value. Flag indicating if required Firmware Over-the-Air (FOTA) Apps have been approved.
        Returns: Optional[bool]
        """
        return self._fota_apps_approved
    
    @fota_apps_approved.setter
    def fota_apps_approved(self,value: Optional[bool] = None) -> None:
        """
        Sets the fotaAppsApproved property value. Flag indicating if required Firmware Over-the-Air (FOTA) Apps have been approved.
        Args:
            value: Value to set for the fotaAppsApproved property.
        """
        self._fota_apps_approved = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enrollment_authorization_url": lambda n : setattr(self, 'enrollment_authorization_url', n.get_str_value()),
            "enrollment_token": lambda n : setattr(self, 'enrollment_token', n.get_str_value()),
            "fota_apps_approved": lambda n : setattr(self, 'fota_apps_approved', n.get_bool_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(zebra_fota_connector_state.ZebraFotaConnectorState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Date and time when the account was last synched with Zebra
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Date and time when the account was last synched with Zebra
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("enrollmentAuthorizationUrl", self.enrollment_authorization_url)
        writer.write_str_value("enrollmentToken", self.enrollment_token)
        writer.write_bool_value("fotaAppsApproved", self.fota_apps_approved)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[zebra_fota_connector_state.ZebraFotaConnectorState]:
        """
        Gets the state property value. Represents various states for Zebra FOTA connector.
        Returns: Optional[zebra_fota_connector_state.ZebraFotaConnectorState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[zebra_fota_connector_state.ZebraFotaConnectorState] = None) -> None:
        """
        Sets the state property value. Represents various states for Zebra FOTA connector.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    


from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DataSharingConsent(entity.Entity):
    """
    Data sharing consent information.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new dataSharingConsent and sets the default values.
        """
        super().__init__()
        # The time consent was granted for this account
        self._grant_date_time: Optional[datetime] = None
        # The granted state for the data sharing consent
        self._granted: Optional[bool] = None
        # The Upn of the user that granted consent for this account
        self._granted_by_upn: Optional[str] = None
        # The UserId of the user that granted consent for this account
        self._granted_by_user_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The display name of the service work flow
        self._service_display_name: Optional[str] = None
        # The TermsUrl for the data sharing consent
        self._terms_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataSharingConsent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataSharingConsent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataSharingConsent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "grant_date_time": lambda n : setattr(self, 'grant_date_time', n.get_datetime_value()),
            "granted": lambda n : setattr(self, 'granted', n.get_bool_value()),
            "granted_by_upn": lambda n : setattr(self, 'granted_by_upn', n.get_str_value()),
            "granted_by_user_id": lambda n : setattr(self, 'granted_by_user_id', n.get_str_value()),
            "service_display_name": lambda n : setattr(self, 'service_display_name', n.get_str_value()),
            "terms_url": lambda n : setattr(self, 'terms_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grant_date_time(self,) -> Optional[datetime]:
        """
        Gets the grantDateTime property value. The time consent was granted for this account
        Returns: Optional[datetime]
        """
        return self._grant_date_time
    
    @grant_date_time.setter
    def grant_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the grantDateTime property value. The time consent was granted for this account
        Args:
            value: Value to set for the grantDateTime property.
        """
        self._grant_date_time = value
    
    @property
    def granted(self,) -> Optional[bool]:
        """
        Gets the granted property value. The granted state for the data sharing consent
        Returns: Optional[bool]
        """
        return self._granted
    
    @granted.setter
    def granted(self,value: Optional[bool] = None) -> None:
        """
        Sets the granted property value. The granted state for the data sharing consent
        Args:
            value: Value to set for the granted property.
        """
        self._granted = value
    
    @property
    def granted_by_upn(self,) -> Optional[str]:
        """
        Gets the grantedByUpn property value. The Upn of the user that granted consent for this account
        Returns: Optional[str]
        """
        return self._granted_by_upn
    
    @granted_by_upn.setter
    def granted_by_upn(self,value: Optional[str] = None) -> None:
        """
        Sets the grantedByUpn property value. The Upn of the user that granted consent for this account
        Args:
            value: Value to set for the grantedByUpn property.
        """
        self._granted_by_upn = value
    
    @property
    def granted_by_user_id(self,) -> Optional[str]:
        """
        Gets the grantedByUserId property value. The UserId of the user that granted consent for this account
        Returns: Optional[str]
        """
        return self._granted_by_user_id
    
    @granted_by_user_id.setter
    def granted_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the grantedByUserId property value. The UserId of the user that granted consent for this account
        Args:
            value: Value to set for the grantedByUserId property.
        """
        self._granted_by_user_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("grantDateTime", self.grant_date_time)
        writer.write_bool_value("granted", self.granted)
        writer.write_str_value("grantedByUpn", self.granted_by_upn)
        writer.write_str_value("grantedByUserId", self.granted_by_user_id)
        writer.write_str_value("serviceDisplayName", self.service_display_name)
        writer.write_str_value("termsUrl", self.terms_url)
    
    @property
    def service_display_name(self,) -> Optional[str]:
        """
        Gets the serviceDisplayName property value. The display name of the service work flow
        Returns: Optional[str]
        """
        return self._service_display_name
    
    @service_display_name.setter
    def service_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceDisplayName property value. The display name of the service work flow
        Args:
            value: Value to set for the serviceDisplayName property.
        """
        self._service_display_name = value
    
    @property
    def terms_url(self,) -> Optional[str]:
        """
        Gets the termsUrl property value. The TermsUrl for the data sharing consent
        Returns: Optional[str]
        """
        return self._terms_url
    
    @terms_url.setter
    def terms_url(self,value: Optional[str] = None) -> None:
        """
        Sets the termsUrl property value. The TermsUrl for the data sharing consent
        Args:
            value: Value to set for the termsUrl property.
        """
        self._terms_url = value
    


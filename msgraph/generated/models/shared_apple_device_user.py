from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SharedAppleDeviceUser(AdditionalDataHolder, Parsable):
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
        Instantiates a new sharedAppleDeviceUser and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Data quota
        self._data_quota: Optional[int] = None
        # Data to sync
        self._data_to_sync: Optional[bool] = None
        # Data quota
        self._data_used: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # User name
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedAppleDeviceUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedAppleDeviceUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedAppleDeviceUser()
    
    @property
    def data_quota(self,) -> Optional[int]:
        """
        Gets the dataQuota property value. Data quota
        Returns: Optional[int]
        """
        return self._data_quota
    
    @data_quota.setter
    def data_quota(self,value: Optional[int] = None) -> None:
        """
        Sets the dataQuota property value. Data quota
        Args:
            value: Value to set for the dataQuota property.
        """
        self._data_quota = value
    
    @property
    def data_to_sync(self,) -> Optional[bool]:
        """
        Gets the dataToSync property value. Data to sync
        Returns: Optional[bool]
        """
        return self._data_to_sync
    
    @data_to_sync.setter
    def data_to_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the dataToSync property value. Data to sync
        Args:
            value: Value to set for the dataToSync property.
        """
        self._data_to_sync = value
    
    @property
    def data_used(self,) -> Optional[int]:
        """
        Gets the dataUsed property value. Data quota
        Returns: Optional[int]
        """
        return self._data_used
    
    @data_used.setter
    def data_used(self,value: Optional[int] = None) -> None:
        """
        Sets the dataUsed property value. Data quota
        Args:
            value: Value to set for the dataUsed property.
        """
        self._data_used = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_quota": lambda n : setattr(self, 'data_quota', n.get_int_value()),
            "data_to_sync": lambda n : setattr(self, 'data_to_sync', n.get_bool_value()),
            "data_used": lambda n : setattr(self, 'data_used', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_int_value("dataQuota", self.data_quota)
        writer.write_bool_value("dataToSync", self.data_to_sync)
        writer.write_int_value("dataUsed", self.data_used)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User name
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    


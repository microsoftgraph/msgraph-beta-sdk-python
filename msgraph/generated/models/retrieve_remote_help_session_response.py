from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class RetrieveRemoteHelpSessionResponse(AdditionalDataHolder, Parsable):
    """
    Remote help - response we provide back to the helper on retrieve session API call
    """
    def __init__(self,) -> None:
        """
        Instantiates a new retrieveRemoteHelpSessionResponse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # ACS Group Id
        self._acs_group_id: Optional[str] = None
        # Helper ACS User Id
        self._acs_helper_user_id: Optional[str] = None
        # Helper ACS User Token
        self._acs_helper_user_token: Optional[str] = None
        # Sharer ACS User Id
        self._acs_sharer_user_id: Optional[str] = None
        # Android Device Name
        self._device_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Azure Pubsub Group Id
        self._pub_sub_group_id: Optional[str] = None
        # Azure Pubsub Group Id
        self._pub_sub_helper_access_uri: Optional[str] = None
        # Azure Pubsub Session Expiration Date Time.
        self._session_expiration_date_time: Optional[datetime] = None
        # The unique identifier for a session
        self._session_key: Optional[str] = None
    
    @property
    def acs_group_id(self,) -> Optional[str]:
        """
        Gets the acsGroupId property value. ACS Group Id
        Returns: Optional[str]
        """
        return self._acs_group_id
    
    @acs_group_id.setter
    def acs_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the acsGroupId property value. ACS Group Id
        Args:
            value: Value to set for the acs_group_id property.
        """
        self._acs_group_id = value
    
    @property
    def acs_helper_user_id(self,) -> Optional[str]:
        """
        Gets the acsHelperUserId property value. Helper ACS User Id
        Returns: Optional[str]
        """
        return self._acs_helper_user_id
    
    @acs_helper_user_id.setter
    def acs_helper_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the acsHelperUserId property value. Helper ACS User Id
        Args:
            value: Value to set for the acs_helper_user_id property.
        """
        self._acs_helper_user_id = value
    
    @property
    def acs_helper_user_token(self,) -> Optional[str]:
        """
        Gets the acsHelperUserToken property value. Helper ACS User Token
        Returns: Optional[str]
        """
        return self._acs_helper_user_token
    
    @acs_helper_user_token.setter
    def acs_helper_user_token(self,value: Optional[str] = None) -> None:
        """
        Sets the acsHelperUserToken property value. Helper ACS User Token
        Args:
            value: Value to set for the acs_helper_user_token property.
        """
        self._acs_helper_user_token = value
    
    @property
    def acs_sharer_user_id(self,) -> Optional[str]:
        """
        Gets the acsSharerUserId property value. Sharer ACS User Id
        Returns: Optional[str]
        """
        return self._acs_sharer_user_id
    
    @acs_sharer_user_id.setter
    def acs_sharer_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the acsSharerUserId property value. Sharer ACS User Id
        Args:
            value: Value to set for the acs_sharer_user_id property.
        """
        self._acs_sharer_user_id = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetrieveRemoteHelpSessionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetrieveRemoteHelpSessionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetrieveRemoteHelpSessionResponse()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Android Device Name
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Android Device Name
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "acsGroupId": lambda n : setattr(self, 'acs_group_id', n.get_str_value()),
            "acsHelperUserId": lambda n : setattr(self, 'acs_helper_user_id', n.get_str_value()),
            "acsHelperUserToken": lambda n : setattr(self, 'acs_helper_user_token', n.get_str_value()),
            "acsSharerUserId": lambda n : setattr(self, 'acs_sharer_user_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pubSubGroupId": lambda n : setattr(self, 'pub_sub_group_id', n.get_str_value()),
            "pubSubHelperAccessUri": lambda n : setattr(self, 'pub_sub_helper_access_uri', n.get_str_value()),
            "sessionExpirationDateTime": lambda n : setattr(self, 'session_expiration_date_time', n.get_datetime_value()),
            "sessionKey": lambda n : setattr(self, 'session_key', n.get_str_value()),
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
    
    @property
    def pub_sub_group_id(self,) -> Optional[str]:
        """
        Gets the pubSubGroupId property value. Azure Pubsub Group Id
        Returns: Optional[str]
        """
        return self._pub_sub_group_id
    
    @pub_sub_group_id.setter
    def pub_sub_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the pubSubGroupId property value. Azure Pubsub Group Id
        Args:
            value: Value to set for the pub_sub_group_id property.
        """
        self._pub_sub_group_id = value
    
    @property
    def pub_sub_helper_access_uri(self,) -> Optional[str]:
        """
        Gets the pubSubHelperAccessUri property value. Azure Pubsub Group Id
        Returns: Optional[str]
        """
        return self._pub_sub_helper_access_uri
    
    @pub_sub_helper_access_uri.setter
    def pub_sub_helper_access_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the pubSubHelperAccessUri property value. Azure Pubsub Group Id
        Args:
            value: Value to set for the pub_sub_helper_access_uri property.
        """
        self._pub_sub_helper_access_uri = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("acsGroupId", self.acs_group_id)
        writer.write_str_value("acsHelperUserId", self.acs_helper_user_id)
        writer.write_str_value("acsHelperUserToken", self.acs_helper_user_token)
        writer.write_str_value("acsSharerUserId", self.acs_sharer_user_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("pubSubGroupId", self.pub_sub_group_id)
        writer.write_str_value("pubSubHelperAccessUri", self.pub_sub_helper_access_uri)
        writer.write_datetime_value("sessionExpirationDateTime", self.session_expiration_date_time)
        writer.write_str_value("sessionKey", self.session_key)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def session_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the sessionExpirationDateTime property value. Azure Pubsub Session Expiration Date Time.
        Returns: Optional[datetime]
        """
        return self._session_expiration_date_time
    
    @session_expiration_date_time.setter
    def session_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sessionExpirationDateTime property value. Azure Pubsub Session Expiration Date Time.
        Args:
            value: Value to set for the session_expiration_date_time property.
        """
        self._session_expiration_date_time = value
    
    @property
    def session_key(self,) -> Optional[str]:
        """
        Gets the sessionKey property value. The unique identifier for a session
        Returns: Optional[str]
        """
        return self._session_key
    
    @session_key.setter
    def session_key(self,value: Optional[str] = None) -> None:
        """
        Sets the sessionKey property value. The unique identifier for a session
        Args:
            value: Value to set for the session_key property.
        """
        self._session_key = value
    


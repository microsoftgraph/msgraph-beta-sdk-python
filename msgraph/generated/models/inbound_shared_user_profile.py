from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class InboundSharedUserProfile(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new inboundSharedUserProfile and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name displayed in the address book for teh user at the time when the sharing record was created. Read-only.
        self._display_name: Optional[str] = None
        # The home tenant id of the external user. Read-only.
        self._home_tenant_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The object id of the external user. Read-only.
        self._user_id: Optional[str] = None
        # The user principal name (UPN) of the external user. Read-only.
        self._user_principal_name: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InboundSharedUserProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InboundSharedUserProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InboundSharedUserProfile()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name displayed in the address book for teh user at the time when the sharing record was created. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name displayed in the address book for teh user at the time when the sharing record was created. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "homeTenantId": lambda n : setattr(self, 'home_tenant_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def home_tenant_id(self,) -> Optional[str]:
        """
        Gets the homeTenantId property value. The home tenant id of the external user. Read-only.
        Returns: Optional[str]
        """
        return self._home_tenant_id
    
    @home_tenant_id.setter
    def home_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the homeTenantId property value. The home tenant id of the external user. Read-only.
        Args:
            value: Value to set for the home_tenant_id property.
        """
        self._home_tenant_id = value
    
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("homeTenantId", self.home_tenant_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The object id of the external user. Read-only.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The object id of the external user. Read-only.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the external user. Read-only.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the external user. Read-only.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    


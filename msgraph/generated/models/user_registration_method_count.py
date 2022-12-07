from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserRegistrationMethodCount(AdditionalDataHolder, Parsable):
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
    def authentication_method(self,) -> Optional[str]:
        """
        Gets the authenticationMethod property value. Name of authentication method.
        Returns: Optional[str]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationMethod property value. Name of authentication method.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userRegistrationMethodCount and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of authentication method.
        self._authentication_method: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of users registered.
        self._user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserRegistrationMethodCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationMethodCount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserRegistrationMethodCount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_count": lambda n : setattr(self, 'user_count', n.get_int_value()),
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
        writer.write_str_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_count(self,) -> Optional[int]:
        """
        Gets the userCount property value. Number of users registered.
        Returns: Optional[int]
        """
        return self._user_count
    
    @user_count.setter
    def user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the userCount property value. Number of users registered.
        Args:
            value: Value to set for the userCount property.
        """
        self._user_count = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ConnectPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the connect method.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new connectPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ownerAccessToken property
        self._owner_access_token: Optional[str] = None
        # The ownerUserPrincipalName property
        self._owner_user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "owner_access_token": lambda n : setattr(self, 'owner_access_token', n.get_str_value()),
            "owner_user_principal_name": lambda n : setattr(self, 'owner_user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def owner_access_token(self,) -> Optional[str]:
        """
        Gets the ownerAccessToken property value. The ownerAccessToken property
        Returns: Optional[str]
        """
        return self._owner_access_token
    
    @owner_access_token.setter
    def owner_access_token(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerAccessToken property value. The ownerAccessToken property
        Args:
            value: Value to set for the ownerAccessToken property.
        """
        self._owner_access_token = value
    
    @property
    def owner_user_principal_name(self,) -> Optional[str]:
        """
        Gets the ownerUserPrincipalName property value. The ownerUserPrincipalName property
        Returns: Optional[str]
        """
        return self._owner_user_principal_name
    
    @owner_user_principal_name.setter
    def owner_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerUserPrincipalName property value. The ownerUserPrincipalName property
        Args:
            value: Value to set for the ownerUserPrincipalName property.
        """
        self._owner_user_principal_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("ownerAccessToken", self.owner_access_token)
        writer.write_str_value("ownerUserPrincipalName", self.owner_user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    


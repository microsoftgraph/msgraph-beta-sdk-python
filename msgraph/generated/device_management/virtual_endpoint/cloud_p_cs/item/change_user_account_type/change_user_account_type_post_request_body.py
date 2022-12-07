from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_user_account_type = lazy_import('msgraph.generated.models.cloud_pc_user_account_type')

class ChangeUserAccountTypePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the changeUserAccountType method.
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
        Instantiates a new changeUserAccountTypePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The userAccountType property
        self._user_account_type: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChangeUserAccountTypePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChangeUserAccountTypePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChangeUserAccountTypePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_account_type": lambda n : setattr(self, 'user_account_type', n.get_enum_value(cloud_pc_user_account_type.CloudPcUserAccountType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_account_type(self,) -> Optional[cloud_pc_user_account_type.CloudPcUserAccountType]:
        """
        Gets the userAccountType property value. The userAccountType property
        Returns: Optional[cloud_pc_user_account_type.CloudPcUserAccountType]
        """
        return self._user_account_type
    
    @user_account_type.setter
    def user_account_type(self,value: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None) -> None:
        """
        Sets the userAccountType property value. The userAccountType property
        Args:
            value: Value to set for the userAccountType property.
        """
        self._user_account_type = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import cloud_pc_operating_system, cloud_pc_user_account_type

class ReprovisionPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new reprovisionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The osVersion property
        self._os_version: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None
        # The userAccountType property
        self._user_account_type: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReprovisionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReprovisionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReprovisionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import cloud_pc_operating_system, cloud_pc_user_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "osVersion": lambda n : setattr(self, 'os_version', n.get_enum_value(cloud_pc_operating_system.CloudPcOperatingSystem)),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(cloud_pc_user_account_type.CloudPcUserAccountType)),
        }
        return fields
    
    @property
    def os_version(self,) -> Optional[cloud_pc_operating_system.CloudPcOperatingSystem]:
        """
        Gets the osVersion property value. The osVersion property
        Returns: Optional[cloud_pc_operating_system.CloudPcOperatingSystem]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None) -> None:
        """
        Sets the osVersion property value. The osVersion property
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("osVersion", self.os_version)
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
            value: Value to set for the user_account_type property.
        """
        self._user_account_type = value
    


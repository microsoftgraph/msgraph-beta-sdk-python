from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class OnPremisesWritebackConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesWritebackConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The distinguished name of the on-premises container that the customer is using to store unified groups which are created in the cloud.
        self._unified_group_container: Optional[str] = None
        # The distinguished name of the on-premises container that the customer is using to store users which are created in the cloud.
        self._user_container: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesWritebackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesWritebackConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesWritebackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unifiedGroupContainer": lambda n : setattr(self, 'unified_group_container', n.get_str_value()),
            "userContainer": lambda n : setattr(self, 'user_container', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("unifiedGroupContainer", self.unified_group_container)
        writer.write_str_value("userContainer", self.user_container)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def unified_group_container(self,) -> Optional[str]:
        """
        Gets the unifiedGroupContainer property value. The distinguished name of the on-premises container that the customer is using to store unified groups which are created in the cloud.
        Returns: Optional[str]
        """
        return self._unified_group_container
    
    @unified_group_container.setter
    def unified_group_container(self,value: Optional[str] = None) -> None:
        """
        Sets the unifiedGroupContainer property value. The distinguished name of the on-premises container that the customer is using to store unified groups which are created in the cloud.
        Args:
            value: Value to set for the unified_group_container property.
        """
        self._unified_group_container = value
    
    @property
    def user_container(self,) -> Optional[str]:
        """
        Gets the userContainer property value. The distinguished name of the on-premises container that the customer is using to store users which are created in the cloud.
        Returns: Optional[str]
        """
        return self._user_container
    
    @user_container.setter
    def user_container(self,value: Optional[str] = None) -> None:
        """
        Sets the userContainer property value. The distinguished name of the on-premises container that the customer is using to store users which are created in the cloud.
        Args:
            value: Value to set for the user_container property.
        """
        self._user_container = value
    

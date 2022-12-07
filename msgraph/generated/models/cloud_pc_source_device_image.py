from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CloudPcSourceDeviceImage(AdditionalDataHolder, Parsable):
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
        Instantiates a new cloudPcSourceDeviceImage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name for the source image.
        self._display_name: Optional[str] = None
        # The ID of the source image.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The display name of subscription that hosts the source image.
        self._subscription_display_name: Optional[str] = None
        # The ID of subscription that hosts the source image.
        self._subscription_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcSourceDeviceImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSourceDeviceImage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcSourceDeviceImage()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the source image.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the source image.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subscription_display_name": lambda n : setattr(self, 'subscription_display_name', n.get_str_value()),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The ID of the source image.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The ID of the source image.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("subscriptionDisplayName", self.subscription_display_name)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subscription_display_name(self,) -> Optional[str]:
        """
        Gets the subscriptionDisplayName property value. The display name of subscription that hosts the source image.
        Returns: Optional[str]
        """
        return self._subscription_display_name
    
    @subscription_display_name.setter
    def subscription_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionDisplayName property value. The display name of subscription that hosts the source image.
        Args:
            value: Value to set for the subscriptionDisplayName property.
        """
        self._subscription_display_name = value
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. The ID of subscription that hosts the source image.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. The ID of subscription that hosts the source image.
        Args:
            value: Value to set for the subscriptionId property.
        """
        self._subscription_id = value
    


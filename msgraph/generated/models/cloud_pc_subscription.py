from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class CloudPcSubscription(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcSubscription and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ID of the subscription.
        self._subscription_id: Optional[str] = None
        # The name of the subscription.
        self._subscription_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcSubscription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSubscription
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcSubscription()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "subscriptionName": lambda n : setattr(self, 'subscription_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("subscriptionName", self.subscription_name)
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. The ID of the subscription.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. The ID of the subscription.
        Args:
            value: Value to set for the subscription_id property.
        """
        self._subscription_id = value
    
    @property
    def subscription_name(self,) -> Optional[str]:
        """
        Gets the subscriptionName property value. The name of the subscription.
        Returns: Optional[str]
        """
        return self._subscription_name
    
    @subscription_name.setter
    def subscription_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionName property value. The name of the subscription.
        Args:
            value: Value to set for the subscription_name property.
        """
        self._subscription_name = value
    


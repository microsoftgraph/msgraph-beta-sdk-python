from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_collection_pagination_count_response = lazy_import('msgraph.generated.models.base_collection_pagination_count_response')
portal_notification = lazy_import('msgraph.generated.models.device_management.portal_notification')

class GetPortalNotificationsResponse(base_collection_pagination_count_response.BaseCollectionPaginationCountResponse):
    """
    Provides operations to call the getPortalNotifications method.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new getPortalNotificationsResponse and sets the default values.
        """
        super().__init__()
        # The value property
        self._value: Optional[List[portal_notification.PortalNotification]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetPortalNotificationsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetPortalNotificationsResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetPortalNotificationsResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(portal_notification.PortalNotification)),
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
        writer.write_collection_of_object_values("value", self.value)
    
    @property
    def value(self,) -> Optional[List[portal_notification.PortalNotification]]:
        """
        Gets the value property value. The value property
        Returns: Optional[List[portal_notification.PortalNotification]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[portal_notification.PortalNotification]] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    


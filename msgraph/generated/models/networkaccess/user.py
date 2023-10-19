from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .traffic_type import TrafficType
    from .user_type import UserType

@dataclass
class User(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The displayName property
    display_name: Optional[str] = None
    # The lastAccessDateTime property
    last_access_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # The userId property
    user_id: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    # The userType property
    user_type: Optional[UserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> User:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return User()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .traffic_type import TrafficType
        from .user_type import UserType

        from .traffic_type import TrafficType
        from .user_type import UserType

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(UserType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
        writer.write_additional_data_value(self.additional_data)
    

